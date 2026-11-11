#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for the
DAG, tree, flow, cycle, connectivity and structure measures of
manifest/traversal_b.yaml (encodings there).

    python3 oracles/traversal_b_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx
from networkx.algorithms.flow import edmonds_karp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)

ORACLE = "networkx"
NONE = [-1.0]


def multigraph(fx):
    g = (nx.MultiDiGraph if fx.directed else nx.MultiGraph)()
    g.add_nodes_from(range(fx.n))
    for e, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        w = fx.weights[e] if fx.weighted else 1.0
        g.add_edge(a, b, key=e, weight=w)
    return g


def simple(M):
    return (nx.DiGraph if M.is_directed() else nx.Graph)(M)


def _try(f):
    try:
        return f()
    except (nx.NetworkXException, ValueError):
        return NONE


def compute(spec, fx):
    fn = spec["params"]["fn"]
    M = multigraph(fx)
    n = fx.n
    if fn == "gb_topo_levels":
        def levels():
            out = [0.0] * n
            for k, gen in enumerate(nx.topological_generations(M)):
                for v in gen:
                    out[v] = float(k)
            return out
        return _try(levels)
    if fn == "gb_lex_topo":
        return _try(lambda: [float(v) for v in nx.lexicographical_topological_sort(M)])
    if fn == "gb_longest_path_len":
        return _try(lambda: [float(max(len(nx.dag_longest_path(M, weight=None)) - 1, 0))])
    if fn == "gb_aperiodic":
        return _try(lambda: [float(nx.is_aperiodic(M))])
    if fn == "gb_antichain_width":
        def width():
            if not nx.is_directed_acyclic_graph(M):
                return NONE
            width = getattr(nx.algorithms.dag, "antichain_width", None)
            if width is None:  # older NetworkX
                return [float(max(len(a) for a in nx.antichains(M)))]
            return [float(width(M))]
        return _try(width)
    if fn == "gb_is_eulerian":
        return [float(nx.is_eulerian(M))]
    if fn == "gb_spanning_trees":
        return [float(nx.number_of_spanning_trees(M))]
    if fn == "gb_mst_weight":
        return [sum(d["weight"] for _, _, d in nx.minimum_spanning_edges(M, keys=False,
                                                                          data=True))]
    if fn == "gb_branching_weight":
        B = nx.maximum_branching(M, preserve_attrs=True)
        return [sum(d.get("weight", 1.0) for _, _, d in B.edges(data=True))]
    if fn == "gb_maxflow":
        if n < 2:
            return NONE
        D = simple(M)
        for _, _, d in D.edges(data=True):
            d["capacity"] = d["weight"]
        return _try(lambda: [float(nx.maximum_flow_value(D, 0, n - 1, flow_func=edmonds_karp))])
    if fn == "gb_mincost":
        if n < 2 or (fx.weighted and any(x != int(x) for x in fx.weights)):
            # NetworkX's network simplex does not stop on these (rounding).
            return NONE
        H = M.copy()
        nx.set_node_attributes(H, 0, "demand")
        H.nodes[0]["demand"] = -1
        H.nodes[n - 1]["demand"] = 1
        return _try(lambda: [float(nx.network_simplex(H)[0])])
    if fn == "gb_cycle_count":
        if n > spec["params"].get("max_nodes", 12):
            return NONE
        return [float(sum(1 for _ in nx.simple_cycles(M)))]
    if fn == "gb_mcb_weight":
        if M.is_multigraph() and any(len(d) > 1 for _, nbrs in M.adj.items()
                                     for d in nbrs.values()):
            return NONE
        G = nx.Graph(M)
        total = 0.0
        for cyc in nx.minimum_cycle_basis(G, weight="weight"):
            k = len(cyc)
            if k == 1:
                total += G[cyc[0]][cyc[0]]["weight"]
                continue
            total += sum(G[cyc[i]][cyc[(i + 1) % k]]["weight"] for i in range(k))
        return [total]
    if fn == "gb_disjoint_paths":
        if n < 2:
            return NONE
        f = nx.node_disjoint_paths if spec["params"].get("nodes") else nx.edge_disjoint_paths
        try:
            return [float(len(list(f(M, 0, n - 1))))]
        except nx.NetworkXNoPath:
            return [0.0]
    if fn == "gb_stoer_wagner":
        return _try(lambda: [float(nx.stoer_wagner(nx.Graph(M))[0])])
    if fn == "gb_d_separated":
        if n < 3:
            return NONE
        return _try(lambda: [float(nx.is_d_separator(M, 0, n - 1, {1}))])
    if fn == "gb_quotient_internal":
        k = min(3, n)
        if k == 0:
            return []
        parts = [[v for v in range(n) if v % k == i] for i in range(k)]
        Q = nx.quotient_graph(M, parts)
        return [float(Q.nodes[frozenset(p)]["nedges"]) for p in parts]
    if fn == "gb_isolates":
        return [float(v) for v in nx.isolates(M)]
    if fn == "gb_walks":
        if n > 40:
            return NONE
        w = nx.number_of_walks(M, spec["params"].get("k", 2))
        return [float(w[u][v]) for u in range(n) for v in range(n)]
    if fn == "gb_chain_count":
        return _try(lambda: [float(sum(1 for _ in nx.chain_decomposition(nx.Graph(M))))])
    if fn == "gb_broadcast_time":
        return _try(lambda: [float(nx.tree_broadcast_time(nx.Graph(M)))])
    if fn == "gb_moral_edges":
        H = nx.moral_graph(M)
        return [float(len({frozenset((u, v)) for u, v in H.edges()}))]
    if fn == "gb_node_boundary":
        return [float(v) for v in sorted(nx.node_boundary(M, {v for v in (0, 1, 2) if v < n}))]
    if fn == "gb_dedensify":
        return [float(len(nx.dedensify(M, spec["params"].get("threshold", 2))[1]))]
    if fn == "gb_snap_groups":
        H = M.copy()
        for v, d in H.degree():
            H.nodes[v]["parity"] = d % 2
        return [float(nx.snap_aggregation(H, node_attributes=("parity",)).number_of_nodes())]
    if fn == "gb_spanner_ok":
        if M.is_multigraph() and any(len(d) > 1 for _, nbrs in M.adj.items()
                                     for d in nbrs.values()):
            return NONE
        G = nx.Graph(M)
        k = spec["params"].get("stretch", 3)
        S = nx.spanner(G, k, weight="weight", seed=1)
        dist = dict(nx.all_pairs_dijkstra_path_length(S, weight="weight"))
        ok = all(u == v or dist[u].get(v, float("inf")) <= k * d["weight"] * (1 + 1e-12)
                 for u, v, d in G.edges(data=True))
        return [1.0 if ok else 0.0]
    if fn == "gb_k_edge_subgraphs":
        if any(len(d) > 1 for _, nbrs in M.adj.items() for d in nbrs.values()):
            return NONE
        label = [0.0] * n
        for i, part in enumerate(nx.k_edge_subgraphs(nx.Graph(M), spec["params"].get("k", 2))):
            for v in part:
                label[v] = float(i)
        return label
    raise ValueError(f"unknown function {fn}")


def main():
    for variant, spec in load_area("traversal_b").items():
        if "networkx" not in spec["oracles"]:
            continue
        for name in fixture_names():
            fx = load_fixture(name)
            if not applies(spec, fx):
                continue
            write_values(ORACLE, name, variant, compute(spec, fx))
    write_version(ORACLE, f"networkx {nx.__version__}")


if __name__ == "__main__":
    main()
