#!/usr/bin/env python3
"""Regenerate golden values from the oracles whose inputs changed.

Runs each Python oracle script in oracles/ (files ending in
`_oracle.py`) and, unless --python-only is given, each R oracle script
(files ending in `.R`). Scripts that need a package that is not installed
report it and are skipped, so a partial environment still produces every
golden file it can.

Incremental by default: a script runs only when its inputs changed since
the golden files were last written. Its inputs are the script itself,
common.py (Python), the fixtures and derived data, its area's
manifest file (or every manifest file for a script not named after an
area), and the installed versions of the packages the script imports
(read in the interpreter that runs it), so an upgraded tool reruns too. The hash of those inputs and the oracles the
script wrote are kept in golden/.hashes/<script>.json (one
small committed file per script). A script whose hash is unchanged is
skipped only if the golden files of every oracle it wrote are present.

Each Python oracle that needs its own environment says so in its first
lines with `# oracle-env: <name>`; it then runs with
$NETORACLES_ORACLE_ENVS/<name>/bin/python (default ~/oracle-envs), built
from oracles/envs/<name>.txt by tools/oracle_envs.sh. When that
environment is missing the script is skipped.

    python3 run_oracles.py                 # changed scripts only
    python3 run_oracles.py --all           # every script
    python3 run_oracles.py --python-only
    python3 run_oracles.py --jobs 4 core   # scripts matching a word
    python3 run_oracles.py --rehash        # see below

--rehash records the current input hash of every script that has a record,
without running anything and without touching the golden files. Use it only
after a pure move (the files changed place or wording, not what the scripts
compute), when the goldens are known to be unchanged, in the environment that
wrote them: a script whose interpreter is missing is left alone, and the
installed tool versions enter the hash.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE
ORACLES = HERE / "oracles"
GOLDEN = HERE / "golden"
HASHES = GOLDEN / ".hashes"
ENVS = Path(os.environ.get("NETORACLES_ORACLE_ENVS", Path.home() / "oracle-envs"))

# A script that computes only the manifest entries listing one oracle says
# so with `# oracle-entries: <oracle>` in its first lines.
ENTRIES_RE = re.compile(r"^#\s*oracle-entries:\s*([A-Za-z0-9_.-]+)\s*$", re.M)
ENV_RE = re.compile(r"^#\s*oracle-env:\s*([A-Za-z0-9_.-]+)\s*$", re.M)

# Versions of the packages a script uses, read in the interpreter that runs
# it: an upgraded tool reruns its scripts, an unrelated upgrade does not.
PY_VERSIONS = ("import importlib.metadata as m, sys\n"
               "dists = m.packages_distributions()\n"
               "for mod in sys.argv[1:]:\n"
               "    for d in sorted(set(dists.get(mod, []))):\n"
               "        print(f'{d}=={m.version(d)}')\n")
R_VERSIONS = ('for (p in commandArgs(TRUE)) cat(p, "==", tryCatch(format(utils::packageVersion(p)), '
              'error = function(e) "missing"), "\\n", sep = "")')
PY_IMPORT_RE = re.compile(r"^\s*(?:import|from)\s+([A-Za-z_]\w*)", re.M)
R_PKG_RE = re.compile(r"([A-Za-z][\w.]*)::|library\(([\w.]+)\)|requireNamespace\(\"([\w.]+)\"")
LOCAL_MODULES = {"common", "engine", "fixtures"}


def interpreter(script: Path) -> tuple[list[str] | None, str]:
    """The command that runs a script, or None and the reason it cannot."""
    if script.suffix == ".R":
        rscript = shutil.which("Rscript")
        return ([rscript], "") if rscript else (None, "Rscript not found")
    head = "\n".join(script.read_text().splitlines()[:10])
    m = ENV_RE.search(head)
    if not m:
        return [sys.executable, "-X", "faulthandler"], ""
    py = ENVS / m.group(1) / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    if not py.exists():
        return None, f"environment {m.group(1)} not installed ({py})"
    return [str(py), "-X", "faulthandler"], ""


def tool_versions(script: Path, cmd: list[str]) -> str:
    """name==version of every package the script uses."""
    text = script.read_text()
    if script.suffix == ".R":
        pkgs = sorted({a or b or c for a, b, c in R_PKG_RE.findall(text)} - {"utils", "base"})
        code = ["-e", R_VERSIONS, "--args"]
    else:
        pkgs = sorted({m for m in PY_IMPORT_RE.findall(text)}
                      - set(sys.stdlib_module_names) - LOCAL_MODULES)
        code = ["-c", PY_VERSIONS]
    if not pkgs:
        return ""
    out = subprocess.run(cmd + code + pkgs, capture_output=True, text=True, cwd=ROOT)
    return out.stdout


def area_of(script: Path, areas: list[str]) -> str | None:
    stem = script.stem.removeprefix("r_")
    for area in sorted(areas, key=len, reverse=True):
        if stem == area or stem.startswith(area + "_"):
            return area
    return None


def input_hash(script: Path, cmd: list[str]) -> str:
    h = hashlib.sha256()

    def add(path: Path) -> None:
        h.update(path.relative_to(ROOT).as_posix().encode() + b"\0")
        h.update(path.read_bytes().replace(b"\r\n", b"\n") + b"\0")

    add(script)
    if script.suffix == ".py":
        add(HERE / "common.py")
        if "tool_common" in script.read_text():
            add(ORACLES / "tool_common.py")
    # Driver sources of a system-tool oracle (oracles/system/<tool>/).
    drivers = ORACLES / "system" / script.stem.removesuffix("_oracle")
    for p in sorted(drivers.rglob("*")) if drivers.is_dir() else []:
        if p.is_file():
            add(p)
    if script.suffix == ".py" and "system_run" in script.read_text():
        add(ORACLES / "system_run.py")
    for d in (HERE / "fixtures", HERE / "derived"):
        for p in sorted(d.rglob("*")):
            if p.is_file():
                add(p)
    # presets.yaml holds engine-side convention checks only (no oracle
    # computes them), so it never reruns a script.
    manifests = sorted(p for p in (HERE / "manifest").glob("*.yaml")
                       if p.stem != "presets")
    head = "\n".join(script.read_text().splitlines()[:30])
    entries = ENTRIES_RE.search(head)
    if entries:
        # The script computes only the entries that list its oracle, so only
        # those (engine options and that oracle's block) enter the hash, and
        # editing other entries does not rerun it.
        import yaml
        name = entries.group(1)
        for p in manifests:
            for key, spec in (yaml.safe_load(p.read_text()) or {}).items():
                if name in spec.get("oracles", {}):
                    part = {k: spec.get(k) for k in ("params", "applies_to", "requires_weights")}
                    part["oracle"] = spec["oracles"][name]
                    h.update(json.dumps([key, part], sort_keys=True).encode() + b"\0")
    else:
        area = area_of(script, [p.stem for p in manifests])
        for p in manifests:
            if area is None or p.stem == area:
                add(p)
    h.update(tool_versions(script, cmd).encode())
    return h.hexdigest()


def versions() -> dict[str, float]:
    return {p.parent.name: p.stat().st_mtime for p in GOLDEN.glob("*/VERSION")}


def record_path(script: Path) -> Path:
    return HASHES / f"{script.name}.json"


def up_to_date(script: Path, digest: str) -> bool:
    try:
        rec = json.loads(record_path(script).read_text())
    except (OSError, ValueError):
        return False
    return (rec.get("inputs") == digest
            and all((GOLDEN / o / "VERSION").exists() for o in rec.get("oracles", [])))


def run(script: Path, force: bool) -> tuple[str, str, str]:
    """Runs one script; returns (name, status, output)."""
    cmd, why = interpreter(script)
    if cmd is None:
        return script.name, "skipped", why
    digest = input_hash(script, cmd)
    if not force and up_to_date(script, digest):
        return script.name, "unchanged", ""
    before = versions()
    t0 = time.monotonic()
    p = subprocess.run(cmd + [str(script)], cwd=ROOT, capture_output=True, text=True)
    secs = time.monotonic() - t0
    out = (p.stdout + p.stderr).rstrip()
    if p.returncode < 0:
        out += f"\n(killed by signal {-p.returncode})"
    if p.returncode == 3:
        # The script's tool is not installed here: nothing was written, and
        # nothing is recorded, so the committed goldens stay and it retries.
        return script.name, "skipped", out
    if p.returncode:
        return script.name, f"FAILED ({secs:.0f}s)", out
    after = versions()
    # Oracles whose VERSION this script (or one running alongside it) wrote.
    # Counting a neighbour's oracle too only makes the check stricter.
    wrote = sorted(o for o, t in after.items() if before.get(o) != t)
    HASHES.mkdir(parents=True, exist_ok=True)
    record_path(script).write_text(
        json.dumps({"inputs": digest, "oracles": wrote}, indent=1) + "\n", newline="")
    return script.name, f"ran ({secs:.0f}s)", out


def rehash(scripts: list[Path]) -> int:
    """Records the current input hash next to the oracles each script wrote,
    keeping the oracle list of its existing record; runs nothing."""
    counts = {"rehashed": 0, "unchanged": 0, "skipped": 0}
    for script in scripts:
        cmd, why = interpreter(script)
        try:
            old = json.loads(record_path(script).read_text())
        except (OSError, ValueError):
            old = None
        if cmd is None or old is None:
            counts["skipped"] += 1
            print(f"== {script.name}: skipped ({why or 'no record'})")
            continue
        digest = input_hash(script, cmd)
        if old.get("inputs") == digest:
            counts["unchanged"] += 1
            continue
        record_path(script).write_text(
            json.dumps({"inputs": digest, "oracles": old.get("oracles", [])}, indent=1) + "\n",
            newline="")
        counts["rehashed"] += 1
    print(f"oracle scripts: {counts['rehashed']} rehashed, {counts['unchanged']} unchanged, "
          f"{counts['skipped']} skipped (nothing was run)")
    return 0


def main(argv: list[str]) -> int:
    python_only = "--python-only" in argv
    force = "--all" in argv
    jobs = os.cpu_count() or 2
    words = []
    it = iter(argv)
    for a in it:
        if a == "--jobs":
            jobs = int(next(it))
        elif not a.startswith("--"):
            words.append(a)
    scripts = sorted(ORACLES.glob("*_oracle.py"))
    if not python_only:
        scripts += sorted(ORACLES.glob("*.R"))
    if words:
        scripts = [s for s in scripts if any(w in s.name for w in words)]
    if "--rehash" in argv:
        return rehash(scripts)
    # Slowest first (by the size of the script, a rough proxy), so the long
    # ones do not start last.
    scripts.sort(key=lambda s: -s.stat().st_size)
    t0 = time.monotonic()
    failed = []
    counts: dict[str, int] = {}
    with ThreadPoolExecutor(max_workers=max(1, jobs)) as pool:
        # Reported as each script finishes, so a slow or hung one is visible.
        futures = [pool.submit(run, s, force) for s in scripts]
        for fut in as_completed(futures):
            name, status, out = fut.result()
            counts[status.split()[0]] = counts.get(status.split()[0], 0) + 1
            if status == "unchanged":
                continue
            print(f"== {name}: {status}", flush=True)
            if out:
                print("   " + out.replace("\n", "\n   "))
            if status.startswith("FAILED"):
                failed.append(name)
    print(f"oracle scripts: {counts.get('ran', 0)} ran, {counts.get('unchanged', 0)} unchanged, "
          f"{counts.get('skipped', 0)} skipped, {counts.get('FAILED', 0)} failed "
          f"in {time.monotonic() - t0:.0f}s")
    if failed:
        print("Oracle scripts failed: " + ", ".join(failed))
        return 1
    return 0


if __name__ == "__main__":
    if {"-h", "--help"} & set(sys.argv[1:]):
        print(__doc__.strip())
        sys.exit(0)
    sys.exit(main(sys.argv[1:]))
