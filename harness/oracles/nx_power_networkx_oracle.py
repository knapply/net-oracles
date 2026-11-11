#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for its
power iterations and the Google matrix (see ../bindings/nx_power.py).
Fixtures with parallel edges are read as multigraphs; eigenvector and Katz
centrality are not implemented for multigraphs (declared undefined).

    python3 oracles/nx_power_networkx_oracle.py
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
    fn = e["fn"]
    w = "weight" if e.get("weighted") else None
    order = list(range(fx.n))
    try:
        if fn == "nxp_eigenvector":
            r = nx.eigenvector_centrality(G, max_iter=e.get("max_iter", 100),
                                          tol=e.get("tol", 1e-6), weight=w)
            return [r[v] for v in order]
        if fn == "nxp_katz":
            r = nx.katz_centrality(G, alpha=e.get("alpha", 0.1), max_iter=e.get("max_iter", 1000),
                                   tol=e.get("tol", 1e-6), normalized=e.get("normalized", True),
                                   weight=w)
            return [r[v] for v in order]
        if fn == "nxp_pagerank":
            pers = {v: v % 3 for v in order} if e.get("personalization") == "mod3" else None
            r = nx.pagerank(G, alpha=e.get("alpha", 0.85), personalization=pers,
                            max_iter=e.get("max_iter", 100), tol=e.get("tol", 1e-6), weight=w)
            return [r[v] for v in order]
        if fn == "nxp_hits":
            H = G if e.get("weighted") else nx.relabel_nodes(G, {}, copy=True)
            if not e.get("weighted"):
                for *_, d in H.edges(data=True):
                    d.pop("weight", None)
            h, a = nx.hits(H, max_iter=e.get("max_iter", 100), tol=e.get("tol", 1e-8),
                           normalized=e.get("normalized", True))
            return [h[v] for v in order] + [a[v] for v in order]
        if fn == "nxp_google":
            return list(nx.google_matrix(G, alpha=e.get("alpha", 0.85), weight=w).ravel())
    except nx.PowerIterationFailedConvergence:
        return [-999.0]
    except ZeroDivisionError:
        return [-999.0]
    raise ValueError(fn)


def main() -> None:
    spec = load_area("nx_power")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        if fx.n == 0:
            continue
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            if "multi_edges" in fx.tags and v["params"]["fn"] in ("nxp_eigenvector", "nxp_katz"):
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, f"networkx {nx.__version__}")
    print(f"networkx (nx_power): wrote {count} golden files")


if __name__ == "__main__":
    main()
