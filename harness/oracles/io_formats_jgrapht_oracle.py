#!/usr/bin/env python3
"""Golden values from JGraphT 1.5.2 (Michail et al. 2020) for
manifest/io_formats.yaml: the CSV importer (edge list, adjacency list and
matrix formats) and the TSPLIB importer, run as a black box through a small Java
driver (system/io_formats_jgrapht/IoOracle.java) on the case texts of
io_formats_cases.py. The driver prints each graph's vertices in its own order and
its edges; positions are that order. Needs the private tool prefix
(tools/oracle_env.sh: OpenJDK) and downloads the pinned jars from Maven Central.
Without them the script is skipped and the committed goldens stay. Hard limits:
120 seconds per Java call and 600 seconds for the script.

    python3 oracles/io_formats_jgrapht_oracle.py
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import io_formats_cases as C  # noqa: E402
import system_run as sr  # noqa: E402
from derived import io_formats as D  # noqa: E402
from io_formats_common import run  # noqa: E402

JGRAPHT = "1.5.2"
ORACLE_INPUTS = ["oracles/system/io_formats_jgrapht", "oracles/system_run.py",
                 "oracles/io_formats_jgrapht_oracle.py", "oracles/io_formats_cases.py"]
CASES = {}   # entry -> [(kind, text, directed, weights, ids)], filled by cases()


def cases():
    """Every case the oracle reads, by manifest entry."""
    return {
        ("io_csv", None): [("csv_edges", t, d, w, False) for t, d, w in C.CSV_EDGES],
        ("io_csv", "adjlist"): [("csv_adjlist", t, d, False, False) for t, d in C.CSV_ADJLIST],
        ("io_csv", "matrix"): [("csv_matrix", t, d, w, ids) for t, d, w, ids in C.CSV_MATRIX],
        ("io_tsplib", None): [("tsplib", t, False, False, False) for t in C.TSPLIB],
    }


def parse(path):
    """The (kind-independent) graphs of the driver's output: a list of
    (vertex names, [(source, target, weight)])."""
    graphs = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        head, _, rest = line.partition(" ")
        if head == "case":
            graphs.append(([], []))
        elif head == "V":
            graphs[-1][0].append(rest)
        elif head == "E":
            source, target, weight = rest.split(" ")
            graphs[-1][1].append((source, target, float(weight)))
    return graphs


def packed(directed, weighted_value, vertices, edges):
    position = {name: i for i, name in enumerate(vertices)}
    rows = [(position[a], position[b], w if weighted_value else None) for a, b, w in edges]
    return D.pack(directed, len(vertices), rows)


def results():
    java, javac = sr.which("java"), sr.which("javac")
    if not (java and javac):
        sr.skip("java not found (run tools/oracle_env.sh)")
    src = sr.ROOT / "oracles" / "system" / "io_formats_jgrapht"
    cp = sr.run(["bash", str(src / "fetch_jars.sh")], timeout=600).stdout.strip()
    every = cases()
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        index, order = [], []
        for key, items in every.items():
            for kind, text, directed, weights, ids in items:
                name = f"case{len(index)}.txt"
                (tmp / name).write_bytes(text.encode("latin-1"))
                index.append(f"{kind} {name} {int(directed)} {int(weights)} {int(ids)}")
                order.append((key, kind, directed, weights))
        (tmp / "index.txt").write_text("\n".join(index) + "\n")
        classes = tmp / "classes"
        classes.mkdir()
        sr.run([javac, "-d", str(classes), "-cp", cp, str(src / "IoOracle.java")], timeout=120)
        sr.run([java, "-cp", f"{cp}:{classes}", "IoOracle", str(tmp), str(tmp / "out.txt")], timeout=120)
        graphs = parse(tmp / "out.txt")
    assert len(graphs) == len(order), (len(graphs), len(order))
    by_entry = {}
    for (key, kind, directed, weights), (vertices, edges) in zip(order, graphs):
        # CSV edge lists and adjacency lists have a value only when read with
        # weights; the matrix and TSPLIB graphs always have one.
        weighted_value = weights or kind in ("csv_matrix", "tsplib")
        by_entry.setdefault(key, []).extend(packed(directed, weighted_value, vertices, edges))
    return by_entry


def main() -> None:
    cache = {}

    def compute(engine):
        key = (engine["fn"], engine.get("cases"))
        if key not in cases():
            return None
        if not cache:
            cache.update(results())
        return cache[key]
    java = sr.which("java")
    jv = sr.run([java, "-version"]).stderr.splitlines()[0] if java else "java"
    run("jgrapht", compute, f"JGraphT {JGRAPHT} ({jv})")


if __name__ == "__main__":
    main()
