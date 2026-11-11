#!/usr/bin/env python3
# oracle-env: graphblas
# oracle-entries: graphblas
"""Golden values from graphblas-algorithms (python-graphblas over
SuiteSparse:GraphBLAS, Davis 2019), which computes each measure as sparse
linear algebra over semirings: an algorithmic family independent of the
traversal-based tools.

graphblas-algorithms is a NetworkX backend; NetworkX in this environment
only builds the graph and dispatches the call (`backend="graphblas"`), and
naming the backend explicitly makes NetworkX raise rather than fall back
to its own code when the backend lacks a function. It accepts Graph and
DiGraph only, so parallel edges collapse (the last weight wins) and the
manifest records where that matters.

    ~/oracle-envs/graphblas/bin/python oracles/graphblas_oracle.py
"""

from __future__ import annotations

import importlib.metadata

import networkx as nx
import numpy as np

from tool_common import adjacency, node_rule, run, weights

ORACLE = "graphblas"
B = {"backend": "graphblas"}


def simple(fx, *, loops=True):
    g = nx.DiGraph() if fx.directed else nx.Graph()
    g.add_nodes_from(range(fx.n))
    for a, b, w in zip(fx.src, fx.tgt, weights(fx)):
        if a == b and not loops:
            continue
        g.add_edge(a, b, weight=w)
    return g


def undirected(fx):
    """The undirected simple reading without loops (as the engine's
    clustering and transitivity read a directed network)."""
    g = simple(fx, loops=False)
    return g.to_undirected() if fx.directed else g


def ordered(d, n):
    # Results are sparse GraphBLAS vectors: a node without an entry holds
    # the implicit value 0.
    return [float(d.get(v, 0.0)) for v in range(n)]


def compute(variant: str, spec: dict, fx):
    e = spec["params"]
    fn = e["fn"]
    n = fx.n
    wt = bool(e.get("weighted"))
    w = "weight" if wt else None
    if n == 0:
        return None
    if fn == "pagerank" and e.get("directed", True):
        kwargs = {}
        if e.get("personalization"):
            kwargs["personalization"] = dict(enumerate(node_rule(e["personalization"], n)))
        if e.get("dangling") == "uniform":
            kwargs["dangling"] = {v: 1.0 for v in range(n)}
        x = nx.pagerank(simple(fx), alpha=e["damping"], weight=w, tol=1e-14, max_iter=100000,
                        **kwargs, **B)
        return ordered(x, n)
    if fn == "hits" and e.get("scale") == "sum":
        g = simple(fx)
        if not wt:
            for *_, d in g.edges(data=True):
                d.pop("weight")
        h, a = nx.hits(g, max_iter=1000000, tol=1e-13, normalized=True, **B)
        return ordered(a if e["which"] == "authorities" else h, n)
    if fn == "katz" and e.get("normalized"):
        a = np.array(adjacency(fx, weighted=wt, loops="once"))
        lam = max(abs(np.linalg.eigvals(a)))
        alpha = e["alpha_fraction"] / lam if lam > 0 else e["alpha_fraction"]
        x = nx.katz_centrality(simple(fx), alpha=float(alpha), beta=1.0, weight=w,
                               max_iter=100000, tol=1e-14, normalized=True, **B)
        return ordered(x, n)
    if fn == "eigenvector" and e.get("scale") == "unit":
        x = nx.eigenvector_centrality(simple(fx), weight=w, max_iter=100000, tol=1e-14, **B)
        return ordered(x, n)
    if fn == "clustering" and e.get("weighting") == "none" \
            and e.get("undefined") == "zero":
        return ordered(nx.clustering(undirected(fx), **B), n)
    if fn == "average_clustering" and e.get("weighting") == "none" \
            and e.get("undefined") == "zero":
        return [float(nx.average_clustering(undirected(fx), **B))]
    if fn == "transitivity" and e.get("undefined") == "zero":
        return [float(nx.transitivity(undirected(fx), **B))]
    if fn == "nxo_triangles":
        return ordered(nx.triangles(simple(fx, loops=False), **B), n)
    if fn == "nxo_directed_clustering" and fx.directed:
        return ordered(nx.clustering(simple(fx), weight=w, **B), n)
    if fn == "nxo_node_reciprocity" and fx.directed:
        r = nx.reciprocity(simple(fx), nodes=list(range(n)), **B)
        return [-999.0 if r.get(v) is None else float(r[v]) for v in range(n)]
    if fn == "reciprocity" and e.get("mode") == "default" and fx.directed:
        return [float(nx.overall_reciprocity(simple(fx, loops=False), **B))]
    if fn == "square_clustering":
        return ordered(nx.square_clustering(simple(fx), **B), n)
    if fn == "generalized_degree" and not fx.directed:
        gd = nx.generalized_degree(simple(fx), **B)
        return [tuple(x for k in sorted(gd.get(v, {})) for x in (k, gd[v][k])) for v in range(n)]
    if fn == "distances" and e["mode"] == "out" and not e.get("weights_as") and not wt:
        g = simple(fx)
        out = []
        for s in range(n):
            dd = nx.single_source_shortest_path_length(g, s, **B)
            out.append(tuple(float(dd.get(t, float("inf"))) for t in range(n)))
        return out
    return None


if __name__ == "__main__":
    run(ORACLE, f"graphblas-algorithms {importlib.metadata.version('graphblas-algorithms')} "
                f"(python-graphblas {importlib.metadata.version('python-graphblas')}, "
                f"SuiteSparse:GraphBLAS {importlib.metadata.version('suitesparse-graphblas')})",
        compute)
