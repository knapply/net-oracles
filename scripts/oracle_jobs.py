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
against the committed file: `identical` (byte for byte), `within tolerance`
(every number within the manifest tolerance of its entry, the oracle's own
tolerance where it has one, and never tighter than 1e-9; every other cell
equal), `differs`, `new` or `removed`. Entries are compared the way the
manifest says: `compare: sets` and `sorted` ignore row order, `partition`
ignores group labels, and `ge` / `le` mark a heuristic whose value is only a
bound, so a rerun is reported as `bound` and need not reproduce. A differing
file on an input that the oracle's `differs_when` tags name, or on which an
oracle of the entry declares the value undefined (`undefined_on`: no unique
answer, such as a repeated leading eigenvalue), is reported as `documented
input`. Only `differs` and `removed`
fail. The bound is twice the manifest
tolerance: that tolerance bounds each run's distance from the reference
value, so two runs of an iterative or sampled oracle can be twice as far from
each other (both within it of the reference). A file harness/golden/ORACLE/FIXTURE/
ENTRY.csv takes the tolerance of manifest entry ENTRY. A changed VERSION file is a
tool version that moved. Exit 1 when anything differs, so a scheduled run
that cannot reproduce the committed outputs shows up as a failure.

Standard library only, plus PyYAML for the tolerances (without it every
file is compared at 1e-9).
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
_ENTRIES: dict[str, dict] | None = None
_TAGS: dict[str, set[str]] = {}


def entries() -> dict[str, dict]:
    """Manifest entries by key (empty without PyYAML)."""
    global _ENTRIES
    if _ENTRIES is None:
        _ENTRIES = {}
        try:
            import yaml
        except ImportError:
            return _ENTRIES
        for f in sorted((HARNESS / "manifest").glob("*.yaml")):
            for key, e in (yaml.safe_load(f.read_text()) or {}).items():
                if isinstance(e, dict):
                    _ENTRIES[key] = e
    return _ENTRIES


def fixture_tags(name: str) -> set[str]:
    if name not in _TAGS:
        tags: set[str] = set()
        for d in ("fixtures", "fixtures-extra"):
            meta = HARNESS / d / name / "meta.json"
            if meta.exists():
                m = json.loads(meta.read_text())
                tags = set(m.get("tags", [])) | {"directed" if m.get("directed") else "undirected"}
                break
        _TAGS[name] = tags
    return _TAGS[name]


def parse_path(path: str) -> tuple[str, str, str] | None:
    """(oracle, fixture, entry) of harness/golden*/ORACLE/FIXTURE/ENTRY.ext."""
    parts = path.split("/")
    if len(parts) == 5 and parts[1] in ("golden", "golden-sized"):
        return parts[2], parts[3], re.sub(r"\.(csv|tsv|json)(\.gz)?$", "", parts[4])
    return None


def entry_rules(path: str) -> tuple[tuple[float, float], str, set[str], set[str]]:
    """Doubled tolerance (abs, rel), compare mode, the oracle's differs_when
    tags, and the fixtures on which any oracle of the entry declares the
    value undefined (no unique answer, so any rerun may differ)."""
    where = parse_path(path)
    if not where:
        return (TOL, TOL), "", set(), set()
    oracle, _, key = where
    e = entries().get(key) or {}
    oe = (e.get("oracles") or {}).get(oracle) or {}
    oe = oe if isinstance(oe, dict) else {}
    t = oe.get("tolerance") or e.get("tolerance") or {}
    tol = (max(2 * float(t.get("abs", 0)), TOL), max(2 * float(t.get("rel", 0)), TOL))
    mode = str(oe.get("compare") or e.get("compare") or "")
    undefined = {f for o in (e.get("oracles") or {}).values() if isinstance(o, dict)
                 for f in (o.get("undefined_on") or [])}
    return tol, mode, set(oe.get("differs_when") or []), undefined


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


def _close(a: str, b: str, tol: tuple[float, float]) -> bool:
    if a == b:
        return True
    # A cell may hold a vector as space-separated numbers (a matrix row).
    if " " in a.strip() or " " in b.strip():
        xa, xb = a.split(), b.split()
        return len(xa) == len(xb) and all(_close(x, y, tol) for x, y in zip(xa, xb))
    try:
        x, y = float(a), float(b)
    except ValueError:
        return False
    if math.isnan(x) and math.isnan(y):
        return True
    return abs(x - y) <= tol[0] + tol[1] * max(abs(x), abs(y))


def _same(a: list[list[str]], b: list[list[str]], tol: tuple[float, float]) -> bool:
    return len(a) == len(b) and all(
        len(ra) == len(rb) and all(_close(x, y, tol) for x, y in zip(ra, rb)) for ra, rb in zip(a, b))


def _num_key(row: list[str]) -> tuple:
    out = []
    for c in row:
        try:
            out.append((0, float(c), ""))
        except ValueError:
            out.append((1, 0.0, c))
    return tuple(out)


def _canonical_partition(rows: list[list[str]]) -> list[list[str]]:
    seen: dict[str, str] = {}
    return [[seen.setdefault(c, str(len(seen))) for c in r] for r in rows]


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
    tol, mode, differs_when, undefined = entry_rules(path)
    if mode in ("ge", "le"):
        return "bound"
    a, b = _rows(old.stdout, path), _rows(new, path)
    if a is not None and b is not None and a[:1] == b[:1]:
        head, a, b = a[:1], a[1:], b[1:]
        if mode in ("sets", "sorted"):
            a, b = sorted(a, key=_num_key), sorted(b, key=_num_key)
        elif mode == "partition":
            a, b = _canonical_partition(a), _canonical_partition(b)
        if _same(a, b, tol):
            return "within tolerance"
    where = parse_path(path)
    if where and (differs_when & fixture_tags(where[1]) or where[1] in undefined):
        return "documented input"
    return "differs"


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
    notes = [(p, c) for p, c in data if c in ("bound", "documented input")]
    lines = ["| Outcome | Files |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in sorted(counts.items())] or ["| no change | 0 |"]
    if versions:
        lines += ["", "Tool versions that moved:", ""]
        for v in versions:
            old = subprocess.run(["git", "show", f"HEAD:{v}"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
            new = (ROOT / v).read_text().strip() if (ROOT / v).exists() else ""
            lines.append(f"- `{v}`: {old or '(none)'} -> {new or '(none)'}")
    if notes:
        lines += ["", f"Changed but allowed by the manifest ({len(notes)}, first 20):", ""]
        lines += [f"- `{p}` ({c})" for p, c in notes[:20]]
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
