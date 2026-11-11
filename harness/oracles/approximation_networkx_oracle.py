#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for its
approximation package (inputs and encodings: ../bindings/approximation.py).

    python3 oracles/approximation_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx
from networkx.algorithms import approximation as apx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture, write_values,  # noqa: E402
                    write_version)

ORACLE = "networkx"
AREA = "approximation"
MEASURES = {}


def measure(name):
    def wrap(f):
        MEASURES[name] = f
        return f
    return wrap


def sorted_graph(fx):
    g = nx.Graph()
    g.add_nodes_from(range(fx.n))
    g.add_edges_from(sorted({(min(a, b), max(a, b)) for a, b in zip(fx.src, fx.tgt) if a != b}))
    return g


@measure("ap_node_connectivity")
def _nc(fx, e):
    return [apx.node_connectivity(sorted_graph(fx))]


@measure("ap_local_connectivity")
def _lc(fx, e):
    if fx.n < 3:
        return [-1, -1]
    g = sorted_graph(fx)
    return [apx.local_node_connectivity(g, 0, fx.n - 1),
            apx.local_node_connectivity(g, fx.n - 1, 1, cutoff=2)]


@measure("ap_dominating_set")
def _ds(fx, e):
    g = sorted_graph(fx)
    for v in g:
        g.nodes[v]["w"] = v % 3
    return sorted(apx.min_weighted_dominating_set(g, weight="w"))


@measure("ap_vertex_cover")
def _vc(fx, e):
    g = sorted_graph(fx)
    for v in g:
        g.nodes[v]["w"] = v % 4 + 1
    return sorted(apx.min_weighted_vertex_cover(g, weight="w"))


@measure("ap_treewidth")
def _tw(fx, e):
    w, d = apx.treewidth_min_fill_in(sorted_graph(fx))
    return [(w, d.number_of_nodes())]


@measure("ap_densest")
def _dn(fx, e):
    d, s = apx.densest_subgraph(sorted_graph(fx), 2, method="greedy++")
    return [(d, len(s))]


@measure("ap_clique_removal")
def _cr(fx, e):
    iset, cliques = apx.clique_removal(sorted_graph(fx))
    return [(len(iset), len(cliques))]


@measure("ap_large_clique_size")
def _lcs(fx, e):
    return [apx.large_clique_size(sorted_graph(fx))]


def _ramsey_all(fx):
    ap = nx.algorithms.approximation
    g = sorted_graph(fx)
    c, ind = ap.ramsey_R2(g)
    iset, cliques = ap.clique_removal(g)
    return (sorted(c), sorted(ind), sorted(iset), [sorted(s) for s in cliques], sorted(ap.max_clique(g)),
            sorted(ap.maximum_independent_set(g)), ap.large_clique_size(g))


@measure("ap_nx_ramsey")
def _nx_ramsey(fx, e):
    c, ind, iset, cliques, mc, mis, lcs = _ramsey_all(fx)
    out = []
    for s in (c, ind, iset):
        out += [len(s)] + s
    out.append(len(cliques))
    for s in cliques:
        out += [len(s)] + s
    for s in (mc, mis):
        out += [len(s)] + s
    return out + [lcs]


@measure("ap_nx_ramsey_valid")
def _nx_ramsey_valid(fx, e):
    c, ind, iset, cliques, mc, mis, _ = _ramsey_all(fx)
    g = sorted_graph(fx)

    def clique(s):
        return all(g.has_edge(a, b) for i, a in enumerate(s) for b in s[i + 1:])

    def independent(s):
        return not any(g.has_edge(a, b) for i, a in enumerate(s) for b in s[i + 1:])

    cover = sorted(x for s in cliques for x in s) == list(range(fx.n))
    return [int(clique(c)), int(independent(ind)), int(cover and all(clique(s) for s in cliques)),
            int(independent(iset)), int(clique(mc)), int(independent(mis))]


def _nx_random_all(fx):
    ap = nx.algorithms.approximation
    g = sorted_graph(fx)
    if fx.n == 0:
        return None
    mis = sorted(nx.maximal_independent_set(g, seed=7))
    closed = round(ap.average_clustering(g, trials=200, seed=7) * 200)
    try:
        d = ap.diameter(g, seed=7)
    except nx.NetworkXError:
        d = -1
    rs, (rc, _) = ap.randomized_partitioning(g, seed=7)
    os_, (oc, _) = ap.one_exchange(g, seed=7)
    return mis, closed, d, (int(rs), sorted(rc)), (int(os_), sorted(oc))


@measure("ap_nx_random")
def _nx_random(fx, e):
    r = _nx_random_all(fx)
    if r is None:
        return [-1]
    mis, closed, d, rp, oe = r
    return [len(mis)] + mis + [closed, d] + [rp[0], len(rp[1])] + rp[1] + [oe[0], len(oe[1])] + oe[1]


@measure("ap_nx_random_valid")
def _nx_random_valid(fx, e):
    r = _nx_random_all(fx)
    if r is None:
        return [-1]
    mis, closed, d, rp, oe = r
    g = sorted_graph(fx)
    s = set(mis)
    ok_mis = not any(g.has_edge(a, b) for a in s for b in s if a < b) and \
        all(v in s or set(g[v]) & s for v in g)
    connected = nx.is_connected(g)
    ok_d = (d == -1 and not connected) or (connected and d <= nx.diameter(g))
    return [int(ok_mis), int(0 <= closed <= 200), int(ok_d),
            int(nx.cut_size(g, set(rp[1])) == rp[0]), int(nx.cut_size(g, set(oe[1])) == oe[0])]


def _anneal_all(fx):
    g = sorted_graph(fx)
    if fx.n < 3 or not nx.is_connected(g):
        return None
    dist = dict(nx.all_pairs_shortest_path_length(g))
    k = nx.complete_graph(fx.n)
    for i, j in k.edges():
        k[i][j]["weight"] = float(dist[i][j])
    ap = nx.algorithms.approximation
    out = []
    for f in (ap.simulated_annealing_tsp, ap.threshold_accepting_tsp):
        for move in ("1-1", "1-0"):
            out.append(f(k, "greedy", move=move, seed=7))
    return out


@measure("ap_nx_anneal")
def _nx_anneal(fx, e):
    tours = _anneal_all(fx)
    if tours is None:
        return [-1]
    return [x for t in tours for x in [len(t)] + list(t)]


@measure("ap_nx_anneal_valid")
def _nx_anneal_valid(fx, e):
    tours = _anneal_all(fx)
    if tours is None:
        return [-1]
    return [int(t[0] == t[-1] and sorted(t[:-1]) == list(range(fx.n))) for t in tours]



def _twmd_parts(fx):
    w, d = apx.treewidth_min_degree(sorted_graph(fx))
    bags = [sorted(b) for b in d.nodes]
    pos = {b: i for i, b in enumerate(d.nodes)}
    return w, bags, [(pos[a], pos[b]) for a, b in d.edges]


@measure("ap_tw_min_degree")
def _twmd(fx, e):
    w, bags, edges = _twmd_parts(fx)
    return [(w,)] + [tuple(b) for b in bags] + [(-1, i, j) for i, j in edges]


@measure("ap_tw_min_degree_valid")
def _twmd_valid(fx, e):
    w, bags, edges = _twmd_parts(fx)
    pairs = {(min(a, b), max(a, b)) for a, b in zip(fx.src, fx.tgt) if a != b}
    cover = int(all(any(v in b for b in bags) for v in range(fx.n))
                and all(any(a in b and c in b for b in bags) for a, c in pairs))
    adj = {i: set() for i in range(len(bags))}
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)
    ok = 1
    for v in range(fx.n):
        hold = [i for i, b in enumerate(bags) if v in b]
        seen, stack = {hold[0]}, [hold[0]]
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in seen and v in bags[y]:
                    seen.add(y)
                    stack.append(y)
        ok &= int(len(seen) == len(hold))
    return [cover, ok, int(w == max(len(b) for b in bags) - 1)]


def main() -> None:
    spec = load_area(AREA)
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            f = MEASURES.get(v["params"]["fn"])
            values = f(fx, v["params"]) if f else None
            if values is not None:
                write_values(ORACLE, name, variant, values)
                count += 1
    print(f"networkx {nx.__version__} ({AREA}): wrote {count} golden files")
    write_version(ORACLE, f"networkx {nx.__version__}")


if __name__ == "__main__":
    main()
