#!/usr/bin/env python3
# oracle-env: rustworkx
# oracle-entries: rustworkx
"""Golden values from rustworkx (Treinish et al. 2022), an independent
Rust implementation built on petgraph.

Fixtures load into rx.PyGraph / rx.PyDiGraph with multigraph=True, so
parallel edges and self-loops are kept; edge payloads are the weights.
Iterative methods run to tight tolerances so that the result is the
converged value. Calls are recorded in the manifest's `call` entries.

    ~/oracle-envs/rustworkx/bin/python oracles/rustworkx_oracle.py
"""

from __future__ import annotations

import math

import numpy as np
import rustworkx as rx

from tool_common import adjacency, has_loops, node_rule, run, simple_edges, weights

ORACLE = "rustworkx"


def build(fx, *, directed=None, edges=None):
    directed = fx.directed if directed is None else directed
    g = rx.PyDiGraph(multigraph=True) if directed else rx.PyGraph(multigraph=True)
    g.add_nodes_from(list(range(fx.n)))
    if edges is None:
        edges = list(zip(fx.src, fx.tgt, weights(fx)))
    g.add_edges_from([(a, b, float(w)) for a, b, w in edges])
    return g


def wfn(weighted):
    return (lambda w: float(w)) if weighted else (lambda w: 1.0)


def ordered(d, n):
    return [float(d[v]) for v in range(n)]


def labels(groups, n):
    out = [0.0] * n
    for c in groups:
        first = float(min(c))
        for v in c:
            out[v] = first
    return out


def compute(variant: str, spec: dict, fx):
    e = spec["params"]
    fn = e["fn"]
    n = fx.n
    wt = bool(e.get("weighted"))
    if fn == "betweenness" and not wt:
        g = build(fx)
        return ordered(rx.betweenness_centrality(g, normalized=e["normalized"]), n)
    if fn == "edge_betweenness" and not wt and not e.get("normalized"):
        g = build(fx)
        eb = rx.edge_betweenness_centrality(g, normalized=False)
        return [float(eb[i]) for i in range(len(fx.src))]
    if fn == "closeness" and not wt and e.get("unreachable") == "wasserman_faust" \
            and e.get("mode") == "in" and e.get("normalized"):
        g = build(fx)
        return ordered(rx.closeness_centrality(g, wf_improved=True), n)
    if fn == "eigenvector" and e.get("scale") == "unit" \
            and e.get("mode", "in") == "in":
        g = build(fx)
        x = rx.eigenvector_centrality(g, weight_fn=wfn(wt), max_iter=100000, tol=1e-14)
        return ordered(x, n)
    if fn == "katz" and e.get("normalized") and n >= 1:
        a = np.array(adjacency(fx, weighted=wt, loops="once"))
        lam = max(abs(np.linalg.eigvals(a))) if n else 0.0
        alpha = e["alpha_fraction"] / lam if lam > 0 else e["alpha_fraction"]
        g = build(fx)
        x = rx.katz_centrality(g, alpha=float(alpha), beta=1.0, weight_fn=wfn(wt),
                               max_iter=100000, tol=1e-14)
        return ordered(x, n)
    if fn == "pagerank" and e.get("directed", True):
        g = build(fx, directed=True) if fx.directed else build(fx)
        kwargs = {}
        if e.get("personalization"):
            kwargs["personalization"] = dict(enumerate(node_rule(e["personalization"], n)))
        if e.get("dangling") == "uniform":
            kwargs["dangling"] = {v: 1.0 for v in range(n)}
        if not fx.directed:
            # rustworkx's pagerank takes a directed graph: each undirected
            # edge becomes a pair of arcs (a loop stays one arc).
            arcs = []
            for a, b, w in zip(fx.src, fx.tgt, weights(fx)):
                arcs.append((a, b, w))
                if a != b:
                    arcs.append((b, a, w))
            g = build(fx, directed=True, edges=arcs)
        x = rx.pagerank(g, alpha=e["damping"], weight_fn=wfn(wt), tol=1e-14,
                        max_iter=100000, **kwargs)
        return ordered(x, n)
    if fn == "hits" and e.get("scale") == "sum":
        arcs = list(zip(fx.src, fx.tgt, weights(fx)))
        if not fx.directed:
            arcs += [(b, a, w) for a, b, w in arcs if a != b]
        g = build(fx, directed=True, edges=arcs)
        h, a = rx.hits(g, weight_fn=wfn(wt), max_iter=1000000, tol=1e-13)
        return ordered(a if e["which"] == "authorities" else h, n)
    if fn == "distances" and not e.get("weights_as") and e["mode"] != "in":
        directed = fx.directed and e["mode"] == "out"
        g = build(fx, directed=directed)
        if wt:
            d = rx.floyd_warshall_numpy(g, weight_fn=float, default_weight=1.0)
        elif directed:
            d = rx.digraph_distance_matrix(g, null_value=math.inf)
        else:
            d = rx.graph_distance_matrix(g, null_value=math.inf)
        d = np.array(d, dtype=float)
        np.fill_diagonal(d, 0.0)
        return [tuple(float(x) for x in row) for row in d]
    if fn == "coreness" and e["mode"] == "all":
        # The fixture as given, parallel edges kept and loops dropped.
        g = build(fx, edges=[(a, b, w) for a, b, w in zip(fx.src, fx.tgt, weights(fx))
                             if a != b])
        return ordered(rx.core_number(g), n)
    if fn == "transitivity" and e.get("undefined") == "zero":
        # The undirected simple reading, as the engine reads a directed
        # network here.
        g = build(fx, edges=simple_edges(fx, undirected=True), directed=False)
        return [float(rx.transitivity(g))]
    if fn == "components":
        g = build(fx)
        if not fx.directed:
            groups = rx.connected_components(g)
        elif e["kind"] == "weak":
            groups = rx.weakly_connected_components(g)
        else:
            groups = rx.strongly_connected_components(g)
        return labels(groups, n)
    if fn == "cut_points" and not fx.directed:
        return sorted(float(v) for v in rx.articulation_points(build(fx)))
    if fn == "bridges" and not fx.directed:
        return [(float(min(a, b)), float(max(a, b))) for a, b in rx.bridges(build(fx))]
    if fn == "spanning_weight" and not fx.directed:
        g = build(fx)
        if e.get("maximum"):
            return None
        f = rx.minimum_spanning_edges
        return [float(sum(w if wt else 1.0 for _, _, w in f(g, weight_fn=wfn(wt))))]
    if fn == "is_dag":
        return [float(rx.is_directed_acyclic_graph(build(fx, directed=True)))] \
            if fx.directed else None
    return None


if __name__ == "__main__":
    run(ORACLE, f"rustworkx {rx.__version__}", compute)
