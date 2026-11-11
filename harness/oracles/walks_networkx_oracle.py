#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for
personalized PageRank (see ../bindings/walks.py). Fixtures with parallel
edges are read as multigraphs, whose parallel edges add their weights.

    python3 oracles/walks_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture, write_values,  # noqa: E402
                    write_version)

ORACLE = "networkx"


def build(fx):
    pairs = list(zip(fx.src, fx.tgt))
    keys = {p if fx.directed else frozenset(p) for p in pairs}
    multi = len(keys) < len(pairs)
    cls = {(True, True): nx.MultiDiGraph, (True, False): nx.DiGraph,
           (False, True): nx.MultiGraph, (False, False): nx.Graph}[(fx.directed, multi)]
    g = cls()
    g.add_nodes_from(range(fx.n))
    for i, (a, b) in enumerate(pairs):
        g.add_edge(a, b, weight=fx.weights[i] if fx.weighted else 1.0)
    return g


def compute(fx, e):
    G = build(fx)
    pers = {0: 2.0} if fx.n == 1 else {0: 2.0, fx.n - 1: 1.0}
    w = "weight" if e.get("weighted") else None
    r = nx.pagerank(G, alpha=1.0 - e.get("alpha", 0.15), personalization=pers, tol=1e-14,
                    max_iter=100000, weight=w)
    return [r[v] for v in range(fx.n)]


def main() -> None:
    spec = load_area("walks")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        if fx.n == 0:
            continue
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            if "loops" in fx.tags:
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, f"networkx {nx.__version__}")
    print(f"networkx (walks): wrote {count} golden files")


if __name__ == "__main__":
    main()
