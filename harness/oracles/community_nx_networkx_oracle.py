#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for its
community package (inputs and encodings: ../bindings/community_nx.py).

    python3 oracles/community_nx_networkx_oracle.py
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

import networkx as nx
from networkx.algorithms.community import quality

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture, write_values,  # noqa: E402
                    write_version)

ORACLE = "networkx"
AREA = "community_nx"
MEASURES = {}


def measure(name):
    def wrap(f):
        MEASURES[name] = f
        return f
    return wrap


def simple(fx, directed=None):
    d = fx.directed if directed is None else directed
    g = nx.DiGraph() if d else nx.Graph()
    g.add_nodes_from(range(fx.n))
    g.add_edges_from((a, b) for a, b in zip(fx.src, fx.tgt) if a != b)
    return g


def natural(fx):
    pairs = list(zip(fx.src, fx.tgt))
    keys = {p if fx.directed else frozenset(p) for p in pairs}
    multi = len(keys) < len(pairs)
    cls = {(True, True): nx.MultiDiGraph, (True, False): nx.DiGraph,
           (False, True): nx.MultiGraph, (False, False): nx.Graph}[(fx.directed, multi)]
    g = cls()
    g.add_nodes_from(range(fx.n))
    for i, (a, b) in enumerate(pairs):
        if fx.weighted:
            g.add_edge(a, b, weight=fx.weights[i])
        else:
            g.add_edge(a, b)
    return g


def blocks(fx):
    out = [{v for v in range(fx.n) if 3 * v // fx.n == k} for k in range(3)]
    return [b for b in out if b]


def labels_of(fx, groups):
    lab = [0] * fx.n
    for i, grp in enumerate(groups):
        for v in grp:
            lab[v] = i
    return lab


@measure("cnx_girvan_newman")
def _gn(fx, e):
    g = simple(fx)
    if g.number_of_edges() == 0:
        return [()] * fx.n
    levels = list(itertools.islice(nx.community.girvan_newman(g), e["level"]))
    out = []
    for comps in levels:
        out.append(labels_of(fx, comps))
    return [tuple(lv[v] for lv in out) for v in range(fx.n)]


@measure("cnx_edge_betweenness")
def _ebp(fx, e):
    if e["k"] > fx.n:
        return [-1] * fx.n
    return labels_of(fx, nx.community.edge_betweenness_partition(simple(fx, False), e["k"]))


@measure("cnx_k_clique")
def _kc(fx, e):
    return [tuple(sorted(c)) for c in nx.community.k_clique_communities(simple(fx, False), e["k"])]


@measure("cnx_kernighan_lin")
def _kl(fx, e):
    if fx.n < 2:
        return [-1] * fx.n
    pairs = sorted({(min(a, b), max(a, b)) for a, b in zip(fx.src, fx.tgt) if a != b})
    w = {}
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        if a != b:
            w[(min(a, b), max(a, b))] = fx.weights[i] if fx.weighted else 1.0
    g = nx.Graph()
    g.add_nodes_from(range(fx.n))
    for p in pairs:
        g.add_edge(*p, weight=w[p])
    half = set(range(fx.n // 2))
    p1, p2 = nx.community.kernighan_lin_bisection(g, (half, set(g) - half), max_iter=10,
                                                  weight="weight" if fx.weighted else None)
    return [1 if v in p2 else 0 for v in range(fx.n)]


@measure("cnx_label_propagation")
def _lp(fx, e):
    return labels_of(fx, nx.community.label_propagation_communities(simple(fx, False)))


@measure("cnx_greedy_modularity")
def _gm(fx, e):
    g = simple(fx, False)
    return labels_of(fx, nx.community.greedy_modularity_communities(g, resolution=e["resolution"]))


@measure("cnx_modularity_nx")
def _mod(fx, e):
    g = natural(fx)
    if g.number_of_edges() == 0:
        return [0.0]
    return [nx.community.modularity(g, blocks(fx), weight="weight" if fx.weighted else None)]


@measure("cnx_overlapping")
def _om(fx, e):
    g = simple(fx, False)
    cover = blocks(fx) + [set(range(min(3, fx.n)))]
    return [nx.community.overlapping_modularity(g, cover)]


@measure("cnx_partition_counts")
def _pc(fx, e):
    g = natural(fx)
    b = blocks(fx)
    i = quality.intra_community_edges(g, b)
    o = quality.inter_community_edges(g, b)
    x = quality.inter_community_non_edges(g, b) if not g.is_multigraph() else -1
    return [(i, o, x)]


@measure("cnx_naive_greedy")
def _ng(fx, e):
    return labels_of(fx, nx.community.naive_greedy_modularity_communities(simple(fx, False)))


@measure("cnx_naive_greedy_nx")
def _ng_nx(fx, e):
    g = simple(fx, False)
    if g.number_of_edges() == 0:
        return [-1] * fx.n
    return labels_of(fx, nx.community.naive_greedy_modularity_communities(g))


@measure("cnx_lukes")
def _lukes(fx, e):
    g = simple(fx, False)
    if g.number_of_nodes() == 0 or not nx.is_tree(g):
        return [-1]
    try:
        parts = nx.community.lukes_partitioning(g, e["max_size"])
    except KeyError:
        return None  # NetworkX fails on a one-node tree
    where = {v: i for i, p in enumerate(parts) for v in p}
    inside = sum(1 for a, b in g.edges() if where[a] == where[b])
    return [(inside, int(all(len(p) <= e["max_size"] for p in parts)))]


@measure("cnx_current_flow")
def _cf(fx, e):
    if e["k"] > fx.n:
        return [-1] * fx.n
    g = simple(fx, False)
    return labels_of(fx, nx.community.edge_current_flow_betweenness_partition(g, e["k"]))



def _seeded_runs(fx):
    import random

    g = simple(fx)
    a = list(nx.community.asyn_lpa_communities(g, seed=random.Random(7)))
    f = list(nx.community.fast_label_propagation_communities(g, seed=random.Random(7)))
    u = simple(fx, directed=False)
    fl = None
    if fx.n and nx.is_connected(u):
        fl = labels_of(fx, list(nx.community.asyn_fluidc(u, min(3, fx.n), seed=random.Random(7))))
    return labels_of(fx, a), labels_of(fx, f), fl


@measure("cnx_seeded_labels")
def _seeded(fx, e):
    a, f, fl = _seeded_runs(fx)
    return [(a[v], f[v], -1 if fl is None else fl[v]) for v in range(fx.n)]


@measure("cnx_seeded_labels_valid")
def _seeded_valid(fx, e):
    a, f, fl = _seeded_runs(fx)
    g = simple(fx)

    def stable(labels, nbrs_of):
        for v in g:
            nbrs = nbrs_of(v)
            if not nbrs:
                continue
            c = {}
            for x in nbrs:
                c[labels[x]] = c.get(labels[x], 0) + 1
            if c.get(labels[v], 0) != max(c.values()):
                return 0
        return 1

    out = [stable(a, lambda v: list(g[v])), stable(f, lambda v: list(nx.all_neighbors(g, v)))]
    out.append(-1 if fl is None else int(sorted(set(fl)) == list(range(min(3, fx.n)))))
    return out



def _louvain_labels(fx):
    import random

    g = simple(fx)
    if g.number_of_edges() == 0:
        return None
    return labels_of(fx, nx.community.louvain_communities(g, seed=random.Random(7)))


@measure("cnx_louvain_seeded")
def _louvain_seeded(fx, e):
    lab = _louvain_labels(fx)
    return [-1] * fx.n if lab is None else lab


@measure("cnx_louvain_seeded_valid")
def _louvain_seeded_valid(fx, e):
    lab = _louvain_labels(fx)
    if lab is None:
        return [-1, -1]
    g = simple(fx)
    parts = {}
    for v, c in enumerate(lab):
        parts.setdefault(c, set()).add(v)
    parts = list(parts.values())
    q = nx.community.modularity(g, parts)
    q0 = nx.community.modularity(g, [{v} for v in g])
    return [int(nx.community.is_partition(g, parts)), int(q >= q0 - 1e-12)]



def _leiden_labels(fx, metric):
    import random

    g = simple(fx)
    if g.number_of_edges() == 0:
        return None
    return labels_of(fx, nx.community.leiden_communities(g, seed=random.Random(7), metric=metric))


@measure("cnx_leiden_seeded")
def _leiden_seeded(fx, e):
    if not hasattr(nx.community, "leiden_communities"):
        return None
    a, b = _leiden_labels(fx, "cpm"), _leiden_labels(fx, "modularity")
    if a is None:
        return [(-1, -1)] * fx.n
    return list(zip(a, b))


@measure("cnx_leiden_seeded_valid")
def _leiden_seeded_valid(fx, e):
    if not hasattr(nx.community, "leiden_communities"):
        return None
    out = []
    u = simple(fx, directed=False)
    for metric in ("cpm", "modularity"):
        lab = _leiden_labels(fx, metric)
        if lab is None:
            out += [-1, -1]
            continue
        parts = {}
        for v, c in enumerate(lab):
            parts.setdefault(c, set()).add(v)
        parts = list(parts.values())
        out += [int(nx.community.is_partition(u, parts)),
                int(all(nx.is_connected(u.subgraph(p)) for p in parts))]
    return out


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
