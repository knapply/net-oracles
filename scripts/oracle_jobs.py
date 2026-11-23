#!/usr/bin/env python3
"""Run the oracle scripts of harness/ in groups, one group per CI job, and
check the reference outputs they write against the committed ones.

    python3 scripts/oracle_jobs.py matrix               # JSON list of the groups (for the workflow matrix)
    python3 scripts/oracle_jobs.py scripts GROUP        # the scripts of one group
    python3 scripts/oracle_jobs.py rpkgs                # R packages the R scripts use
    python3 scripts/oracle_jobs.py run GROUP [--all] [--jobs N] [--report FILE]
    python3 scripts/oracle_jobs.py compare [--report FILE] [--summary FILE]

Groups follow what a script needs installed:
- base-1..base-4: Python scripts that run in the main interpreter
  (NetworkX, NumPy, SciPy and exact arithmetic), split in four by size;
- env-NAME: scripts that declare `# oracle-env: NAME` (their own environment,
  harness/oracles/envs/NAME.txt, or a conda environment for graph-tool);
- system: scripts driving native tools through oracles/system_run.py
  (Octave, Boost, nauty, JVM tools), bootstrapped by harness/tools/oracle_env.sh;
- r: the R scripts.

`run` calls harness/run_oracles.py's own runner for each script of the group
(the same hashing and records), so a group run here is what
`python3 run_oracles.py` would do for those scripts. `compare` reads
`git status` after a run and classifies every changed reference output
against the committed file: `identical` (byte for byte), `within 1e-9`
(every number within an absolute or relative 1e-9 of the committed one, every
other cell equal), `differs`, `new` or `removed`. A changed VERSION file is a
tool version that moved. Exit 1 when anything differs, so a scheduled run
that cannot reproduce the committed outputs shows up as a failure.

Standard library only.
"""
from __future__ import annotations

import csv
import gzip
import io
import json
import math
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HARNESS = ROOT / "harness"
ORACLES = HARNESS / "oracles"
ENV_RE = re.compile(r"^#\s*oracle-env:\s*([A-Za-z0-9_.-]+)\s*$", re.M)
R_PKG_RE = re.compile(r"([A-Za-z][\w.]*)::|library\(([\w.]+)\)|requireNamespace\(\"([\w.]+)\"")
BASE_SHARDS = 4
TOL = 1e-9


def groups() -> dict[str, list[Path]]:
    g: dict[str, list[Path]] = {}
    base = []
    for s in sorted(ORACLES.glob("*_oracle.py")):
        text = s.read_text()
        m = ENV_RE.search("\n".join(text.splitlines()[:10]))
        if m:
            g.setdefault("env-" + m.group(1), []).append(s)
        elif "system_run" in text:
            g.setdefault("system", []).append(s)
        else:
            base.append(s)
    # Round-robin by size (a rough proxy for time) so the shards take about as long.
    base.sort(key=lambda s: -s.stat().st_size)
    for i in range(BASE_SHARDS):
        g[f"base-{i + 1}"] = sorted(base[i::BASE_SHARDS])
    g["r"] = sorted(ORACLES.glob("*.R"))
    return dict(sorted(g.items()))


def r_packages() -> list[str]:
    pkgs: set[str] = set()
    for s in ORACLES.glob("*.R"):
        pkgs |= {a or b or c for a, b, c in R_PKG_RE.findall(s.read_text())}
    return sorted(pkgs - {"utils", "base", "stats", "methods", "graphics", "grDevices", "tools", "parallel"})


def cmd_run(group: str, force: bool, jobs: int, report: Path | None) -> int:
    sys.path.insert(0, str(HARNESS))
    import run_oracles  # noqa: E402  (the harness's own runner)

    scripts = groups().get(group)
    if scripts is None:
        print(f"unknown group {group!r}; groups: {', '.join(groups())}", file=sys.stderr)
        return 2
    scripts = sorted(scripts, key=lambda s: -s.stat().st_size)
    results = []
    with ThreadPoolExecutor(max_workers=max(1, jobs)) as pool:
        futs = [pool.submit(run_oracles.run, s, force) for s in scripts]
        for f in as_completed(futs):
            name, status, out = f.result()
            results.append({"script": name, "status": status, "output": out[-4000:]})
            if status != "unchanged":
                print(f"== {name}: {status}", flush=True)
                if out and not status.startswith("ran"):
                    print("   " + out[-2000:].replace("\n", "\n   "), flush=True)
    counts: dict[str, int] = {}
    for r in results:
        k = r["status"].split()[0]
        counts[k] = counts.get(k, 0) + 1
    print(f"{group}: " + ", ".join(f"{v} {k}" for k, v in sorted(counts.items())))
    if report:
        report.write_text(json.dumps({"group": group, "counts": counts,
                                      "results": sorted(results, key=lambda r: r["script"])}, indent=1))
    return 1 if counts.get("FAILED") else 0


def _rows(data: bytes, name: str) -> list[list[str]] | None:
    if name.endswith(".gz"):
        try:
            data = gzip.decompress(data)
        except OSError:
            return None
        name = name[:-3]
    text = data.decode("utf-8", "replace")
    if name.endswith(".json"):
        try:
            return [[json.dumps(json.loads(text), sort_keys=True)]]
        except ValueError:
            return None
    delim = "\t" if name.endswith(".tsv") else ","
    return list(csv.reader(io.StringIO(text), delimiter=delim))


def _close(a: str, b: str) -> bool:
    if a == b:
        return True
    try:
        x, y = float(a), float(b)
    except ValueError:
        return False
    if math.isnan(x) and math.isnan(y):
        return True
    return abs(x - y) <= TOL or abs(x - y) <= TOL * max(abs(x), abs(y))


def classify(path: str) -> str:
    p = ROOT / path
    old = subprocess.run(["git", "show", f"HEAD:{path}"], cwd=ROOT, capture_output=True)
    if old.returncode:
        return "new"
    if not p.exists():
        return "removed"
    new = p.read_bytes()
    if new == old.stdout:
        return "identical"
    a, b = _rows(old.stdout, path), _rows(new, path)
    if a is None or b is None or len(a) != len(b):
        return "differs"
    for ra, rb in zip(a, b):
        if len(ra) != len(rb) or not all(_close(x, y) for x, y in zip(ra, rb)):
            return "differs"
    return "within 1e-9"


def changed_outputs() -> list[str]:
    out = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all", "--",
                          "harness/golden", "harness/golden-sized"],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout
    paths = []
    for line in out.splitlines():
        path = line[3:].split(" -> ")[-1].strip('"')
        if "/.hashes/" not in path:
            paths.append(path)
    return sorted(paths)


def cmd_compare(report: Path | None, summary: Path | None) -> int:
    rows = [(p, classify(p)) for p in changed_outputs()]
    versions = [p for p, _ in rows if p.endswith("/VERSION")]
    data = [(p, c) for p, c in rows if not p.endswith("/VERSION")]
    counts: dict[str, int] = {}
    for _, c in data:
        counts[c] = counts.get(c, 0) + 1
    bad = [(p, c) for p, c in data if c in ("differs", "removed")]
    lines = ["| Outcome | Files |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in sorted(counts.items())] or ["| no change | 0 |"]
    if versions:
        lines += ["", "Tool versions that moved:", ""]
        for v in versions:
            old = subprocess.run(["git", "show", f"HEAD:{v}"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
            new = (ROOT / v).read_text().strip() if (ROOT / v).exists() else ""
            lines.append(f"- `{v}`: {old or '(none)'} -> {new or '(none)'}")
    if bad:
        lines += ["", f"Outputs that differ ({len(bad)}, first 50):", ""]
        lines += [f"- `{p}` ({c})" for p, c in bad[:50]]
    text = "\n".join(lines) + "\n"
    print(text)
    if summary:
        with summary.open("a") as f:
            f.write(text)
    if report:
        report.write_text(json.dumps({"counts": counts, "versions": versions,
                                      "files": [{"path": p, "outcome": c} for p, c in rows]}, indent=1))
    return 1 if bad else 0


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__.strip())
        return 0
    cmd, rest = argv[0], argv[1:]

    def opt(name: str) -> str | None:
        return rest[rest.index(name) + 1] if name in rest else None

    if cmd == "matrix":
        print(json.dumps(list(groups())))
        return 0
    if cmd == "scripts":
        for s in groups().get(rest[0], []):
            print(s.name)
        return 0
    if cmd == "rpkgs":
        print(" ".join(r_packages()))
        return 0
    if cmd == "run":
        rep = opt("--report")
        return cmd_run(rest[0], "--all" in rest, int(opt("--jobs") or 4), Path(rep) if rep else None)
    if cmd == "compare":
        rep, summ = opt("--report"), opt("--summary")
        return cmd_compare(Path(rep) if rep else None, Path(summ) if summ else None)
    print(f"unknown command {cmd!r}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
