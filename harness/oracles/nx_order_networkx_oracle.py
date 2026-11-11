#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for group
C's NetworkX-ordered results (see ../bindings/nx_order.py). Each fixture is
built by adding nodes 0..n and then its edges in order (a multigraph when
it has parallel edges), so NetworkX's adjacency order is the edge order.

    python3 oracles/nx_order_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture, write_values,  # noqa: E402
                    write_version)

ORACLE = "networkx"

try:
    import pandas  # noqa: F401  (NetworkX's prominent_group needs it)

    HAVE_PANDAS = True
except ImportError:
    HAVE_PANDAS = False


def spreading_ties(H, labelled, method, alpha, max_iter, rel=1e-9):
    """Nodes whose best class score is tied (within `rel` of it) with
    another class's, from the published iteration F <- P F + B evaluated in
    floating point. NetworkX's argmax decides those by platform rounding
    (fused multiply-add, vendor BLAS), so they are not comparable."""
    import numpy as np

    X = nx.to_scipy_sparse_array(H).toarray()
    n = X.shape[0]
    classes = sorted(set(labelled.values()))
    deg = X.sum(axis=0)
    deg[deg == 0] = 1
    B = np.zeros((n, len(classes)))
    if method == "consistency":
        P = alpha * (X / np.sqrt(deg)[:, None] / np.sqrt(deg)[None, :])
        for v, c in labelled.items():
            B[v, classes.index(c)] = 1 - alpha
    else:
        P = X / deg[:, None]
        for v, c in labelled.items():
            P[v] = 0
            B[v, classes.index(c)] = 1
    F = np.zeros((n, len(classes)))
    for _ in range(max_iter):
        F = P @ F + B
    top = F.max(axis=1)
    return [bool(top[v] > 0 and np.sum(np.abs(F[v] - top[v]) <= rel * top[v]) > 1)
            for v in range(n)]


def prominent_undefined(fx, k):
    """Inputs on which NetworkX's prominent_group has no answer."""
    if fx.n < k + 2:
        return True
    if not fx.directed:
        return False
    fwd = [set() for _ in range(fx.n)]
    rev = [set() for _ in range(fx.n)]
    for a, b in zip(fx.src, fx.tgt):
        fwd[a].add(b)
        rev[b].add(a)
    for adj in (fwd, rev):
        seen, stack = {0}, [0]
        while stack:
            for w in adj[stack.pop()]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        if len(seen) < fx.n:
            return True
    return False


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
    if fn == "nxo_triangles":
        t = nx.triangles(nx.Graph(G))
        return [t[v] for v in range(fx.n)]
    if fn == "nxo_kosaraju":
        return [tuple(sorted(c)) for c in nx.kosaraju_strongly_connected_components(G)]
    if fn == "nxo_biconnected":
        return [tuple(sorted(u * fx.n + v for u, v in c))
                for c in nx.biconnected_component_edges(G)]
    if fn == "nxo_flow_hierarchy":
        if G.number_of_edges() == 0:
            return [-999.0]
        return [nx.flow_hierarchy(G, weight="weight" if e.get("weighted") else None)]
    if fn == "nxo_directed_clustering":
        c = nx.clustering(nx.DiGraph(G), weight="weight" if e.get("weighted") else None)
        return [float(c[v]) for v in range(fx.n)]
    if fn == "nxo_successor_transitivity":
        return [float(nx.transitivity(nx.DiGraph(G)))]
    if fn == "nxo_node_reciprocity":
        r = nx.reciprocity(nx.DiGraph(G), nodes=list(range(fx.n)))
        return [-999.0 if r[v] is None else float(r[v]) for v in range(fx.n)]
    if fn == "nxo_prominent":
        k = e.get("k", 2)
        if prominent_undefined(fx, k):
            return [-999.0]
        H = G
        if not e.get("weighted"):
            H = G.copy()
            for *_, d in H.edges(data=True):
                d.pop("weight", None)
        value, group = nx.prominent_group(H, k, weight="weight" if e.get("weighted") else None,
                                          endpoints=e.get("endpoints", False),
                                          normalized=e.get("normalized", True),
                                          greedy=e.get("greedy", False))
        if e.get("value_only"):
            return [value]
        return [value, tuple(group)]
    if fn == "nxo_label_spreading":
        H = G.copy()
        if not e.get("weighted"):
            for *_, d in H.edges(data=True):
                d.pop("weight", None)
        labelled = {v: (v // 4) % 3 for v in range(0, fx.n, 4)}
        for v, c in labelled.items():
            H.nodes[v]["label"] = c
        method, alpha, max_iter = e.get("method"), e.get("alpha", 0.99), e.get("max_iter", 30)
        if method == "consistency":
            out = nx.node_classification.local_and_global_consistency(
                H, alpha=alpha, max_iter=max_iter)
        else:
            out = nx.node_classification.harmonic_function(H, max_iter=max_iter)
        # -1 where the best score is tied: NetworkX's argmax then depends on
        # the platform's rounding, and the engine reports the same -1.
        tied = spreading_ties(H, labelled, method, alpha, max_iter)
        return [-1.0 if t else float(x) for x, t in zip(out, tied)]
    raise ValueError(fn)


def main() -> None:
    spec = load_area("nx_order")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            if fx.n == 0:
                continue
            if v["params"]["fn"] == "nxo_prominent" and not HAVE_PANDAS:
                continue  # NetworkX's prominent_group needs pandas; keep the golden files
            if "multi_edges" in fx.tags and v["params"]["fn"] in ("nxo_kosaraju",
                                                                 "nxo_biconnected"):
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, f"networkx {nx.__version__}")
    print(f"networkx (nx_order): wrote {count} golden files")


if __name__ == "__main__":
    main()
