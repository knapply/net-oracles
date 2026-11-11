#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for its
bipartite package (inputs and encodings: ../bindings/bipartite_nx.py). Every
measure reads the simple Graph or DiGraph a fixture denotes (nodes 0..n - 1,
the edges in file order, self-loops dropped).

    python3 oracles/bipartite_nx_networkx_oracle.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (FIXTURES, applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)

ORACLE = "networkx"
AREA = "bipartite_nx"
MEASURES = {}


def measure(name):
    def wrap(f):
        MEASURES[name] = f
        return f
    return wrap


def simple(fx):
    g = nx.DiGraph() if fx.directed else nx.Graph()
    g.add_nodes_from(range(fx.n))
    g.add_edges_from((a, b) for a, b in zip(fx.src, fx.tgt) if a != b)
    return g


def top(fx):
    t = json.loads((FIXTURES / fx.name / "meta.json").read_text()).get("type")
    if t is not None:
        return [v for v in range(fx.n) if t[v] == 0]
    return list(range(0, fx.n, 2))


@measure("bipartite_color")
def _bc(fx, e):
    try:
        c = nx.bipartite.color(simple(fx))
    except nx.NetworkXError:
        return [-1] * fx.n
    return [c[v] for v in range(fx.n)]


PROJ = {"count": lambda g, t: nx.bipartite.weighted_projected_graph(g, t),
        "newman": lambda g, t: nx.bipartite.collaboration_weighted_projected_graph(g, t),
        "jaccard": lambda g, t: nx.bipartite.overlap_weighted_projected_graph(g, t),
        "min": lambda g, t: nx.bipartite.overlap_weighted_projected_graph(g, t, jaccard=False)}


@measure("projection")
def _proj(fx, e):
    g = simple(fx)
    t = top(fx)
    try:
        p = PROJ[e["weight"]](g, t)
    except nx.NetworkXAlgorithmError:
        return None  # no node outside `top` (single_node)
    out = []
    for u in t:
        nbrs = p.succ[u] if p.is_directed() else p[u]
        for v in sorted(nbrs):
            out.append((u, v, nbrs[v]["weight"]))
    return out


@measure("latapy_clustering")
def _lat(fx, e):
    g = simple(fx)
    try:
        c = nx.bipartite.latapy_clustering(g, mode=e["mode"])
    except nx.NetworkXError:
        return [-1] * fx.n
    return [c[v] for v in range(fx.n)]


@measure("butterflies")
def _bf(fx, e):
    b = nx.bipartite.butterflies(simple(fx))
    return [b[v] for v in range(fx.n)]


@measure("robins_alexander")
def _ra(fx, e):
    return [nx.bipartite.robins_alexander_clustering(simple(fx))]


@measure("node_redundancy")
def _nr(fx, e):
    g = simple(fx)
    good = [v for v in g if len(g[v]) >= 2]
    r = nx.bipartite.node_redundancy(g, good)
    return [r.get(v, -1.0) for v in range(fx.n)]


@measure("spectral_bipartivity")
def _sb(fx, e):
    g = simple(fx)
    per = nx.bipartite.spectral_bipartivity(g, nodes=list(g))
    return [per[v] for v in range(fx.n)] + [nx.bipartite.spectral_bipartivity(g)]


@measure("birank")
def _br(fx, e):
    g = simple(fx)
    t = top(fx)
    if len(t) in (0, fx.n):
        return [-1] * fx.n
    try:
        r = nx.bipartite.birank(g, t, max_iter=1000, tol=1e-10)
    except nx.PowerIterationFailedConvergence:
        return [-1] * fx.n
    return [r[v] for v in range(fx.n)]


@measure("bipartite_modularity")
def _bm(fx, e):
    g = simple(fx)
    comms = [{v for v in range(fx.n) if 3 * v // fx.n == k} for k in range(3)]
    comms = [c for c in comms if c]
    return [nx.bipartite.modularity(g, comms, top(fx))]


@measure("vertex_cover")
def _vc(fx, e):
    g = simple(fx)
    t = set(top(fx))
    if any((a in t) == (b in t) for a, b in g.edges()):
        return [-1]
    m = nx.bipartite.hopcroft_karp_matching(g, top_nodes=t)
    c = nx.bipartite.to_vertex_cover(g, m, top_nodes=t)
    return [(len(c), int(all(a in c or b in c for a, b in g.edges())))]


@measure("maximal_extendability")
def _me(fx, e):
    h = nx.Graph()
    h.add_nodes_from(range(2 * fx.n))
    for a, b in simple(fx).edges():
        h.add_edges_from([(2 * a, 2 * b + 1), (2 * b, 2 * a + 1)])
    try:
        return [nx.bipartite.maximal_extendability(h)]
    except nx.NetworkXError:
        return [-1]


def _bipartition(fx, g):
    t = set(top(fx))
    return None if any((a in t) == (b in t) for a, b in g.edges()) else t


@measure("hopcroft_karp")
def _hk(fx, e):
    g = simple(fx)
    t = _bipartition(fx, g)
    if t is None:
        return [-1]
    m = nx.bipartite.hopcroft_karp_matching(g, top_nodes=t)
    pairs = {frozenset(p) for p in m.items()}
    return [(len(pairs), int(nx.is_matching(g, {tuple(p) for p in pairs})))]


@measure("min_weight_full_matching")
def _mwfm(fx, e):
    g = simple(fx)
    t = _bipartition(fx, g)
    if t is None:
        return [-1]
    for a, b in g.edges():
        g[a][b]["weight"] = float((min(a, b) + 2 * max(a, b)) % 7 + 1)
    try:
        m = nx.bipartite.minimum_weight_full_matching(g, top_nodes=t)
    except ValueError:
        return [-1]
    pairs = {frozenset(p) for p in m.items()}
    small = min(len(t), fx.n - len(t))
    total = sum(g[a][b]["weight"] for a, b in (tuple(p) for p in pairs))
    return [(total, int(len(pairs) == small))]


@measure("nx_hk_mates")
def _hk_mates(fx, e):
    g = simple(fx)
    t = set(top(fx))
    if any((a in t) == (b in t) for a, b in g.edges()):
        return [-1]
    m = nx.bipartite.hopcroft_karp_matching(g, top_nodes=top(fx))
    return [m.get(v, -1) for v in range(fx.n)]



def _eppstein(fx):
    g = simple(fx)
    t = set(top(fx))
    if any((a in t) == (b in t) for a, b in g.edges()):
        return None
    return list(nx.bipartite.eppstein_matching(g, top_nodes=top(fx)).items())


@measure("nx_eppstein")
def _epp(fx, e):
    m = _eppstein(fx)
    return [-1] if m is None else (m or [(-2, -2)])


@measure("nx_eppstein_size")
def _epp_size(fx, e):
    m = _eppstein(fx)
    if m is None:
        return [-1]
    g = simple(fx)
    mate = dict(m)
    ok = all(g.has_edge(a, b) and mate.get(b) == a for a, b in m)
    return [(len(m) // 2, int(ok))]


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
