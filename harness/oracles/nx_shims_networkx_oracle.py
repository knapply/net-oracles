#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for the
routines of manifest/nx_shims.yaml that reproduce its results and order
(encodings in bindings/nx_shims.py, derived inputs in derived/nx_shims.py).

Graphs are built by adding nodes 0..n - 1 and then the edges in file order,
as a MultiGraph/MultiDiGraph where the function accepts one.

    python3 oracles/nx_shims_networkx_oracle.py
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)
from derived import nx_shims as D  # noqa: E402

ORACLE = "networkx"


def multigraph(fx):
    g = (nx.MultiDiGraph if fx.directed else nx.MultiGraph)()
    g.add_nodes_from(range(fx.n))
    g.add_edges_from(zip(fx.src, fx.tgt))
    return g


def simple(fx):
    g = (nx.DiGraph if fx.directed else nx.Graph)()
    g.add_nodes_from(range(fx.n))
    g.add_edges_from(zip(fx.src, fx.tgt))
    return g


def forest_flags(fx):
    g = multigraph(fx)
    if not fx.directed:
        return [nx.is_tree(g), nx.is_forest(g), -1, -1]
    return [nx.is_tree(g), nx.is_forest(g), nx.is_arborescence(g), nx.is_branching(g)]


def tree_centroid(fx):
    t = D.tree_fixture(fx)
    g = simple(t)
    centroid = getattr(nx, "centroid", None) or nx.barycenter
    return sorted(centroid(g))


def prufer(fx):
    t = D.tree_fixture(fx)
    if t.n < 3:
        return []
    return list(nx.to_prufer_sequence(simple(t)))


def from_prufer(fx, ordered):
    k, _ = D.bfs_tree(fx)
    if k < 3:
        return []
    t = nx.from_prufer_sequence(D.prufer_sequence(k))
    if ordered:
        return [tuple(t.adj[v]) for v in range(k)]
    return sorted((min(e), max(e)) for e in t.edges())


def tree_lca(fx):
    t = D.tree_fixture(fx, directed=True)
    return [(u, v, a) for (u, v), a in nx.tree_all_pairs_lowest_common_ancestor(simple(t), root=0)]


def greedy_branching(fx, kind):
    s = D.simple_digraph(fx)
    g = nx.DiGraph()
    g.add_nodes_from(range(s.n))
    for a, b, w in zip(s.src, s.tgt, s.weights):
        g.add_edge(a, b, weight=w)
    if not s.src:
        return []
    b = nx.algorithms.tree.branchings.greedy_branching(g, attr="weight", kind=kind)
    return sorted(b.edges())


def is_simple_path(fx):
    g = multigraph(fx)
    return [int(nx.is_simple_path(g, seq)) for seq in D.path_sequences(fx)]


def simple_nx(s):
    g = (nx.DiGraph if s.directed else nx.Graph)()
    g.add_nodes_from(range(s.n))
    g.add_edges_from(zip(s.src, s.tgt))
    return g


def recursive_cycles(fx):
    s = D.simple_graph(fx, loops=True)
    if not D.small(fx):
        return []
    return [tuple(c) for c in nx.recursive_simple_cycles(simple_nx(s))]


def cycle_basis(fx):
    s = D.simple_graph(fx)
    return [tuple(c) for c in nx.cycle_basis(simple_nx(s))]


ORIENT = {"none": None, "original": "original", "reverse": "reverse", "ignore": "ignore"}


def find_cycle(fx, orientation, source):
    s = D.simple_graph(fx, loops=True)
    try:
        edges = nx.find_cycle(simple_nx(s), source=None if source < 0 else s.n // 2,
                              orientation=ORIENT[orientation])
    except nx.NetworkXNoCycle:
        return [(-1, -1)]
    if s.directed and orientation in ("reverse", "ignore"):
        return [(e[0], e[1], int(e[2] == "reverse")) for e in edges]
    return [(e[0], e[1]) for e in edges]


def contracted(fx, self_loops, ordered=True):
    s = D.simple_graph(fx, loops=True)
    if s.n < 2:
        return []
    g = nx.contracted_nodes(simple_nx(s), 0, s.n - 1, self_loops=self_loops)
    edges = [tuple(e) for e in g.edges()]
    if ordered:
        return edges
    return sorted((a, b) if s.directed else (min(a, b), max(a, b)) for a, b in edges)


def cd_index(fx, delta, weighted):
    s = D.simple_graph(fx)
    g = simple_nx(s)
    times, weights = D.node_times(s.n), D.node_weights(s.n)
    for v in range(s.n):
        g.nodes[v]["time"] = times[v]
        g.nodes[v]["w"] = weights[v]
    out = []
    for v in range(s.n):
        try:
            val = nx.cd_index(g, v, time_delta=delta, weight="w" if weighted else None)
        except (ZeroDivisionError, nx.NetworkXError):
            val = -999.0
        out.append(float(val))
    return out


def triangle_list(fx):
    s = D.simple_graph(fx)
    return [tuple(t) for t in nx.all_triangles(simple_nx(s))]


def graphical(fx, test):
    und, dirs = D.sequence_cases(fx)
    if test == 4:
        return [int(nx.is_digraphical(i, o)) for i, o in dirs]
    check = {0: lambda q: nx.is_graphical(q, method="eg"),
             1: lambda q: nx.is_graphical(q, method="hh"),
             2: nx.is_multigraphical, 3: nx.is_pseudographical}[test]
    return [int(check(q)) for q in und]


def weighted_digraph(s):
    g = nx.DiGraph()
    g.add_nodes_from(range(s.n))
    g.add_weighted_edges_from(zip(s.src, s.tgt, s.weights))
    return g


def fw_tree(fx, negative, part):
    s = D.fw_graph(fx, negative)
    pred, dist = nx.floyd_warshall_tree(weighted_digraph(s))
    if part == "dist":
        return sorted((u, v, d) for u, row in dist.items() for v, d in row.items()
                      if d != float("inf"))
    return sorted((u, v, p) for u, row in pred.items() for v, p in row.items())


def johnson_lengths(fx):
    s = D.weighted_dag(fx)
    g = weighted_digraph(s)
    h = g.copy()
    h.add_node(-1)
    h.add_weighted_edges_from((-1, v, 0) for v in range(s.n))
    pot = nx.single_source_bellman_ford_path_length(h, -1)
    return [g[u][v]["weight"] + pot[u] - pot[v] for u in g for v in g[u]]


def dag_reach(fx):
    s = D.dag(fx)
    g = simple_nx(s)
    return sorted((u, v) for u in g for v in nx.descendants(g, u))


def topo_sorts(fx, limit):
    s = D.sort_graph(fx)
    if s is None:
        return []
    return [tuple(o) for o in itertools.islice(nx.all_topological_sorts(simple_nx(s)), limit)]


def colliders(fx, v_structures):
    s = D.simple_graph(fx)
    g = simple_nx(s)
    gen = nx.dag.v_structures(g) if v_structures else nx.dag.colliders(g)
    return [tuple(t) for t in gen]


def euler_circuit(fx):
    e = D.eulerian(fx)
    g = multigraph(e)
    return [tuple(t) for t in nx.eulerian_circuit(g, source=0, keys=True)]


def compute(spec, fx):
    fn = spec["fn"]
    if fn == "nxs_forest_flags":
        return [int(x) if x != -1 else -1 for x in forest_flags(fx)]
    if fn == "nxs_tree_centroid":
        return tree_centroid(fx)
    if fn == "nxs_prufer":
        return prufer(fx)
    if fn == "nxs_from_prufer":
        return from_prufer(fx, spec.get("ordered", True))
    if fn == "nxs_tree_lca":
        return tree_lca(fx)
    if fn == "nxs_greedy_branching":
        return greedy_branching(fx, spec["kind"])
    if fn == "nxs_is_simple_path":
        return is_simple_path(fx)
    if fn == "nxs_recursive_cycles":
        return recursive_cycles(fx)
    if fn == "nxs_cycle_basis":
        return cycle_basis(fx)
    if fn == "nxs_find_cycle":
        return find_cycle(fx, spec.get("orientation_name", "none"), spec.get("source", -1))
    if fn == "nxs_contracted_nodes":
        return contracted(fx, spec["self_loops"], spec.get("ordered", True))
    if fn == "nxs_cd_index":
        return cd_index(fx, spec["delta"], spec.get("weighted", False))
    if fn == "nxs_triangle_list":
        return triangle_list(fx)
    if fn == "nxs_degree_sequence_test":
        return graphical(fx, spec["test"])
    if fn == "nxs_fw_tree":
        return fw_tree(fx, spec.get("negative", False), spec["part"])
    if fn == "nxs_johnson_lengths":
        return johnson_lengths(fx)
    if fn == "nxs_dag_reachability":
        return dag_reach(fx)
    if fn == "nxs_topological_sorts":
        return topo_sorts(fx, spec.get("limit", 2000))
    if fn == "nxs_colliders":
        return colliders(fx, spec.get("v_structures", False))
    if fn == "nxs_euler_circuit":
        return euler_circuit(fx)
    raise ValueError(fn)


def main() -> None:
    spec = load_area("nx_shims")
    count = errors = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            try:
                values = compute(v["params"], fx)
            except Exception as exc:  # NetworkX rejects this input
                errors += 1
                print(f"  {variant} on {name}: {type(exc).__name__}: {str(exc)[:120]}")
                continue
            write_values(ORACLE, name, variant, values)
            count += 1
    write_version(ORACLE, f"networkx {nx.__version__}")
    print(f"networkx (nx shims): wrote {count} golden files, {errors} inputs rejected")


if __name__ == "__main__":
    main()
