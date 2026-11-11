#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for its
structural tests (inputs and encodings: ../bindings/structure_nx.py).

    python3 oracles/structure_nx_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture, write_values,  # noqa: E402
                    write_version)

ORACLE = "networkx"
AREA = "structure_nx"
MEASURES = {}


def measure(name):
    def wrap(f):
        MEASURES[name] = f
        return f
    return wrap


def sorted_graph(fx, directed=False):
    g = nx.DiGraph() if directed else nx.Graph()
    g.add_nodes_from(range(fx.n))
    if directed:
        g.add_edges_from(sorted({(a, b) for a, b in zip(fx.src, fx.tgt) if a != b}))
    else:
        g.add_edges_from(sorted({(min(a, b), max(a, b)) for a, b in zip(fx.src, fx.tgt) if a != b}))
    return g


@measure("st_dominating")
def _dom(fx, e):
    g = sorted_graph(fx, fx.directed)
    return [int(nx.is_dominating_set(g, [v for v in g if v % 2 == 0])),
            int(nx.is_dominating_set(g, [0]))]


@measure("st_cds")
def _cds(fx, e):
    g = sorted_graph(fx)
    if not nx.is_connected(g):
        return [-1]
    return sorted(nx.connected_dominating_set(g))


@measure("st_regular")
def _reg(fx, e):
    g = sorted_graph(fx, fx.directed)
    return [int(nx.is_regular(g)), nx.s_metric(g)]


@measure("st_kl")
def _kl(fx, e):
    g = sorted_graph(fx, fx.directed)
    if g.number_of_edges() > 300:
        return None
    subs = [nx.kl_connected_subgraph(g, 2, l) for l in (2, 3)]
    return [tuple(int(s.has_edge(u, v)) for s in subs) for u, v in g.edges()]


@measure("st_tournament")
def _tour(fx, e):
    g = sorted_graph(fx, True)
    t = nx.tournament.is_tournament(g)
    return [int(t), int(nx.tournament.is_strongly_connected(g)) if t else -1]


@measure("st_intersection")
def _ia(fx, e):
    g = sorted_graph(fx)
    try:
        b, c = nx.intersection_array(g)
    except nx.NetworkXError:
        return [-1]
    return list(b) + list(c)


@measure("st_perfect")
def _perf(fx, e):
    return [int(nx.is_perfect_graph(sorted_graph(fx)))]


@measure("st_at_free")
def _at(fx, e):
    return [int(nx.is_at_free(sorted_graph(fx)))]


@measure("st_chordal")
def _ch(fx, e):
    g = sorted_graph(fx)
    if not nx.is_chordal(g):
        return [0, -1]
    return [1, nx.chordal_graph_treewidth(g)]


@measure("st_fill")
def _fill(fx, e):
    g = sorted_graph(fx)
    h, alpha = nx.complete_to_chordal_graph(g)
    return [h.number_of_edges() - g.number_of_edges()] + [alpha[v] for v in range(fx.n)]


def smooths_to_kuratowski(g):
    """1 if g is a subdivision of K5 or K3,3."""
    h = nx.Graph(g)
    h.remove_nodes_from([v for v in list(h) if h.degree(v) == 0])
    for v in sorted(h):
        if h.degree(v) == 2:
            a, b = list(h[v])
            if h.has_edge(a, b):
                return 0
            h.remove_node(v)
            h.add_edge(a, b)
    if nx.is_isomorphic(h, nx.complete_graph(5)) or nx.is_isomorphic(h, nx.complete_bipartite_graph(3, 3)):
        return 1
    return 0


def _cex(fx):
    try:
        return nx.get_counterexample(sorted_graph(fx)) if hasattr(nx, "get_counterexample") \
            else nx.algorithms.planarity.get_counterexample(sorted_graph(fx))
    except nx.NetworkXException:
        return None


@measure("st_planar")
def _planar(fx, e):
    return [int(nx.is_planar(sorted_graph(fx)))]


@measure("st_counterexample")
def _counterexample(fx, e):
    k = _cex(fx)
    if k is None:
        return [-1]
    return [x for p in sorted((min(u, v), max(u, v)) for u, v in k.edges()) for x in p]


@measure("st_kuratowski")
def _kur(fx, e):
    k = _cex(fx)
    return [-1] if k is None else [smooths_to_kuratowski(k)]


@measure("st_embedding")
def _emb(fx, e):
    ok, emb = nx.check_planarity(sorted_graph(fx))
    if not ok:
        return [-1]
    data = emb.get_data()
    return [x for v in range(fx.n) for x in [len(data.get(v, []))] + list(data.get(v, []))]


@measure("st_embedding_euler")
def _euler(fx, e):
    g = sorted_graph(fx)
    ok, emb = nx.check_planarity(g)
    if not ok:
        return [-1]
    seen, faces = set(), 0
    for u, v in emb.edges():
        if (u, v) not in seen:
            emb.traverse_face(u, v, mark_half_edges=seen)
            faces += 1
    c = nx.number_connected_components(g)
    nontrivial = sum(1 for comp in nx.connected_components(g) if len(comp) > 1)
    return [int(g.number_of_nodes() - g.number_of_edges() + faces == c + nontrivial)]


def weighted_graph(fx):
    first = {}
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        if a != b:
            first.setdefault((min(a, b), max(a, b)), fx.weights[i] if fx.weights else 1.0)
    g = nx.Graph()
    g.add_nodes_from(range(fx.n))
    g.add_weighted_edges_from((a, b, first[(a, b)]) for a, b in sorted(first))
    return g


def _three(fx):
    g = weighted_graph(fx)
    return g, [nx.max_weight_matching(g), nx.max_weight_matching(g, True), nx.min_weight_matching(g)]


@measure("st_mwm")
def _mwm(fx, e):
    g, ms = _three(fx)
    return [x for m in ms for x in (sum(g[u][v]["weight"] for u, v in m), len(m))]


@measure("st_mwm_pairs")
def _mwm_pairs(fx, e):
    _, ms = _three(fx)
    return [x for m in ms for x in [len(m)] + [y for p in sorted(m) for y in p]]


def _kf(fx, k):
    try:
        return nx.k_factor(weighted_graph(fx), k)
    except nx.NetworkXUnfeasible:
        return None


@measure("st_kfactor")
def _kfactor(fx, e):
    return [-1 if (f := _kf(fx, k)) is None else f.number_of_edges() for k in (1, 2, 3)]


@measure("st_kfactor_edges")
def _kfactor_edges(fx, e):
    out = []
    for k in (1, 2):
        f = _kf(fx, k)
        out += [-1] if f is None else [f.number_of_edges()] + [y for p in f.edges() for y in p]
    return out


@measure("st_edge_cover")
def _cover(fx, e):
    g = weighted_graph(fx)
    try:
        c = nx.min_edge_cover(g)
    except nx.NetworkXException:
        return [-1]
    return [len({frozenset(p) for p in c})]


def _colourings(fx):
    g = sorted_graph(fx)
    big = max((d for _, d in g.degree), default=0)
    out = [nx.greedy_color(g, "largest_first"), nx.greedy_color(g, "largest_first", interchange=True),
           nx.greedy_color(g, "DSATUR"), nx.equitable_color(g, big + 1), nx.equitable_color(g, big + 3)]
    return g, big, [[c[v] for v in range(fx.n)] for c in out]


@measure("st_coloring")
def _colouring(fx, e):
    return [x for col in _colourings(fx)[2] for x in col]


@measure("st_coloring_valid")
def _colouring_valid(fx, e):
    g, big, cols = _colourings(fx)
    out = []
    for i, col in enumerate(cols):
        c = dict(enumerate(col))
        ok = nx.coloring.equitable_coloring.is_coloring(g, c)
        if i >= 3:
            ok = ok and nx.coloring.equitable_coloring.is_equitable(g, c, big + (1 if i == 3 else 3))
        out.append(int(ok))
    return out


@measure("st_triads")
def _triads(fx, e):
    g = nx.MultiDiGraph()
    g.add_nodes_from(range(fx.n))
    g.add_edges_from(zip(fx.src, fx.tgt))
    out = []
    for nl in (None, [v for v in range(fx.n) if v % 2 == 0], [0] if fx.n else []):
        c = nx.triadic_census(g, nl)
        out += [c[t] for t in ("003", "012", "102", "021D", "021U", "021C", "111D", "111U", "030T",
                               "030C", "201", "120D", "120U", "120C", "210", "300")]
    return out


@measure("st_polynomials")
def _polys(fx, e):
    g = sorted_graph(fx)
    if g.number_of_edges() > 20:
        return [-1]
    try:
        import sympy
    except ImportError:  # goldens come from a run with sympy installed
        return None
    x, y = sympy.Symbol("x"), sympy.Symbol("y")
    chrom = [int(c) for c in reversed(sympy.Poly(nx.chromatic_polynomial(g), x).all_coeffs())]
    while len(chrom) > 1 and chrom[-1] == 0:
        chrom.pop()
    t = sympy.Poly(sympy.expand(nx.tutte_polynomial(g)), x, y)
    terms = sorted((int(i), int(j), int(c)) for (i, j), c in t.terms() if c)
    return [len(chrom)] + chrom + [len(terms)] + [v for tt in terms for v in tt]


def _walks(fx):
    g = weighted_graph(fx)
    if len(g) < 2 or not nx.is_connected(g):
        return g, None
    ap = nx.algorithms.approximation
    return g, [ap.traveling_salesman_problem(g), ap.traveling_salesman_problem(g, method=ap.greedy_tsp),
               ap.traveling_salesman_problem(g, cycle=False)]


@measure("st_tsp")
def _tsp(fx, e):
    _, walks = _walks(fx)
    return [-1] if walks is None else [x for wk in walks for x in [len(wk)] + wk]


@measure("st_tsp_valid")
def _tsp_valid(fx, e):
    g, walks = _walks(fx)
    if walks is None:
        return [-1]
    out = []
    for i, wk in enumerate(walks):
        ok = all(g.has_edge(a, b) for a, b in zip(wk, wk[1:])) and set(wk) == set(g)
        if i < 2:
            ok = ok and wk[0] == wk[-1]
        out.append(int(ok))
    return out


@measure("st_asteroidal")
def _asteroidal(fx, e):
    t = nx.find_asteroidal_triple(sorted_graph(fx))
    return [-1] if t is None else list(t)


@measure("st_asteroidal_valid")
def _asteroidal_valid(fx, e):
    return [-1] if nx.find_asteroidal_triple(sorted_graph(fx)) is None else [1]


@measure("st_hampath")
def _hampath(fx, e):
    return list(nx.tournament.hamiltonian_path(sorted_graph(fx, True)))



def junction_encode(nodes, edges):
    """Lines: (0 clique / 1 sepset, members...) per node in order, then
    (-1, i, j) per edge in order (node positions)."""
    pos = {v: i for i, (v, _) in enumerate(nodes)}
    out = [(0 if d["type"] == "clique" else 1, *v) for v, d in nodes]
    return out + [(-1, pos[u], pos[v]) for u, v in edges]


def junction_valid(fx, nodes, edges):
    """[cliques cover every edge and none contains another, every
    sepset is the intersection of its two cliques, the cliques holding
    each node form a connected subtree (running intersection)]."""
    cl = [set(v) for v, d in nodes if d["type"] == "clique"]
    pairs = {(min(a, b), max(a, b)) for a, b in zip(fx.src, fx.tgt) if a != b}
    cover = int(all(any(a in c and b in c for c in cl) for a, b in pairs)
                and all(any(v in c for c in cl) for v in range(fx.n))
                and not any(i != j and cl[i] <= cl[j] for i in range(len(cl)) for j in range(len(cl))))
    adj = {}
    for u, v in edges:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    seps = int(all(len(adj.get(v, [])) >= 2 and set(v) == set(adj[v][0]) & set(adj[v][1])
                   for v, d in nodes if d["type"] == "sepset"))
    ok = 1
    for x in range(fx.n):
        holders = [v for v, d in nodes if d["type"] == "clique" and x in v]
        if not holders:
            continue
        seen, stack = {holders[0]}, [holders[0]]
        while stack:
            u = stack.pop()
            for w in adj.get(u, []):
                if x in w and w not in seen:
                    seen.add(w)
                    stack.append(w)
        ok &= int(set(holders) <= seen)
    return [cover, seps, ok]


@measure("st_chordal_order")
def _chordal_order(fx, e):
    h, _ = nx.complete_to_chordal_graph(sorted_graph(fx))
    return [tuple(sorted(c)) for c in nx.chordal_graph_cliques(h)]


def _jt(fx):
    t = nx.junction_tree(sorted_graph(fx))
    return list(t.nodes(data=True)), list(t.edges())


@measure("st_junction")
def _junction(fx, e):
    return junction_encode(*_jt(fx))


@measure("st_junction_valid")
def _junction_valid(fx, e):
    return junction_valid(fx, *_jt(fx))


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
