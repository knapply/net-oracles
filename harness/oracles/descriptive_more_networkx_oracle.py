#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for dyad
census, degree distribution, Krackhardt dimensions, ego composition,
symmetrize (strong and weak), Simmelian ties, cocitation and coupling,
partition quality and the motif census (see ../bindings/descriptive_more.py
for the encodings). Where NetworkX has no function for the measure the value
is built from NetworkX graph operations and numpy/scipy, as the manifest
`call` of each entry says.

    python3 oracles/descriptive_more_networkx_oracle.py
"""

from __future__ import annotations

import math
import sys
from itertools import combinations
from pathlib import Path

import networkx as nx
import numpy as np
from scipy.stats import entropy

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture, write_values,  # noqa: E402
                    write_version)

ORACLE = "networkx"
UNDEF = -999.0
SIZE4_MAX_NODES = 40


def mark(x):
    return UNDEF if x is None or (isinstance(x, float) and math.isnan(x)) else float(x)


def simple_graph(fx):
    """Graph or DiGraph of the distinct pairs, loops removed."""
    g = nx.DiGraph() if fx.directed else nx.Graph()
    g.add_nodes_from(range(fx.n))
    g.add_edges_from((a, b) for a, b in zip(fx.src, fx.tgt) if a != b)
    return g


def multi_graph(fx, loops=True):
    g = nx.MultiDiGraph() if fx.directed else nx.MultiGraph()
    g.add_nodes_from(range(fx.n))
    g.add_edges_from((a, b) for a, b in zip(fx.src, fx.tgt) if loops or a != b)
    return g


def dyad_census(fx):
    g = simple_graph(fx)
    n = fx.n
    if not fx.directed:
        m = g.number_of_edges()
        return [float(m), 0.0, float(n * (n - 1) // 2 - m)]
    mutual = g.to_undirected(reciprocal=True).number_of_edges()
    union = g.to_undirected().number_of_edges()
    return [float(mutual), float(union - mutual), float(n * (n - 1) // 2 - union)]


def stats(deg):
    d = np.array(deg, dtype=float)
    n = len(d)
    s = np.sort(d)
    gini = (2 * np.sum(np.arange(1, n + 1) * s) / (n * s.sum()) - (n + 1) / n) if s.sum() > 0 else None
    return [d.mean(), d.var(), d.min(), d.max(), mark(gini)]


def degree_distribution(fx, e):
    mode, loops = e.get("mode", "all"), e.get("loops", True)
    g = multi_graph(fx, loops)
    if not fx.directed or mode == "all":
        deg = [d for _, d in g.degree()]
        hist = nx.degree_histogram(g)
    else:
        view = g.out_degree() if mode == "out" else g.in_degree()
        deg = [d for _, d in view]
        hist = list(np.bincount(deg))
    return [float(c) for c in hist] + [mark(x) for x in stats(deg)]


def krackhardt(fx):
    g = simple_graph(fx)
    n = fx.n
    d = g if fx.directed else g.to_directed()
    comps = [len(c) for c in nx.weakly_connected_components(d)]
    pairs = n * (n - 1) // 2
    conn = (sum(c * (c - 1) // 2 for c in comps) / pairs) if pairs else None
    reach = sum(len(nx.descendants(d, v)) for v in d)
    mutual = sum(len(c) * (len(c) - 1) for c in nx.strongly_connected_components(d))
    hier = (1 - mutual / reach) if reach else None
    minimum = n - len(comps)
    eff = None if n < 2 else 1 - (d.number_of_edges() - minimum) / (n * (n - 1) - minimum)
    violations, most = 0, 0
    for comp in nx.weakly_connected_components(d):
        c = len(comp)
        most += (c - 1) * (c - 2) // 2 if c >= 3 else 0
        above = {v: nx.ancestors(d, v) | {v} for v in comp}
        for i, j in combinations(sorted(comp), 2):
            upper = above[i] & above[j]
            if not any(upper <= above[u] for u in upper):
                violations += 1
    lub = None if most == 0 else 1 - violations / most
    return [mark(conn), mark(hier), mark(eff), mark(lub)]


def ego_composition(fx, e):
    mode = e.get("mode", "all")
    g = simple_graph(fx)
    code = [v % 3 for v in range(fx.n)]
    levels = sorted(set(code))
    k = len(levels)
    cols = {"alters": [], "blau": [], "shannon": [], "iqv": [], "same": []}
    shares = []
    for v in range(fx.n):
        if not fx.directed or mode == "all":
            nb = set(g.neighbors(v)) if not fx.directed else set(g.successors(v)) | set(g.predecessors(v))
        elif mode == "out":
            nb = set(g.successors(v))
        else:
            nb = set(g.predecessors(v))
        counts = np.array([sum(1 for u in nb if code[u] == lv) for lv in levels], dtype=float)
        total = counts.sum()
        cols["alters"].append(total)
        if total == 0:
            for name in ("blau", "shannon", "iqv", "same"):
                cols[name].append(UNDEF)
            shares.extend([UNDEF] * k)
            continue
        p = counts / total
        blau = 1 - np.sum(p * p)
        cols["blau"].append(blau)
        cols["shannon"].append(float(entropy(counts)))
        cols["iqv"].append(UNDEF if k == 1 else blau / (1 - 1 / k))
        cols["same"].append(counts[levels.index(code[v])] / total)
        shares.extend(p.tolist())
    return [float(x) for name in ("alters", "blau", "shannon", "iqv", "same")
            for x in cols[name]] + [float(x) for x in shares]


def symmetrize(fx, e):
    g = simple_graph(fx)
    u = g if not fx.directed else (g.to_undirected(reciprocal=True) if e["method"] == "strong"
                                   else g.to_undirected())
    return sorted((min(a, b), max(a, b), 1.0) for a, b in u.edges())


def simmelian(fx):
    g = simple_graph(fx)
    u = g.to_undirected(reciprocal=True) if fx.directed else g
    return sorted((min(a, b), max(a, b)) for a, b in u.edges()
                  if len(list(nx.common_neighbors(u, a, b))) > 0)


def cocitation(fx, e):
    a = nx.to_numpy_array(simple_graph(fx), nodelist=range(fx.n), weight=None)
    m = a.T @ a if e["kind"] == "cocitation" else a @ a.T
    return [(i, j, float(m[i, j])) for i, j in combinations(range(fx.n), 2) if m[i, j] > 0]


def partition_quality(fx):
    g = simple_graph(fx)
    blocks = {}
    for v in range(fx.n):
        blocks.setdefault(v % 3, set()).add(v)
    cov, perf = nx.community.partition_quality(g, list(blocks.values()))
    return [float(cov), float(perf)]


FOUR = {
    0: nx.star_graph(3),
    1: nx.path_graph(4),
    2: nx.cycle_graph(4),
    3: nx.Graph([(0, 1), (1, 2), (2, 0), (2, 3)]),
    4: nx.Graph([(0, 1), (1, 2), (2, 0), (1, 3), (2, 3)]),
    5: nx.complete_graph(4),
}


def motif_census(fx, e):
    g = simple_graph(fx)
    if fx.directed:
        census = nx.triadic_census(g)
        order = ["021D", "021U", "021C", "111D", "111U", "030T", "030C", "201", "120D", "120U",
                 "120C", "210", "300"]
        return [float(census[t]) for t in order]
    if e["size"] == 3:
        tri = sum(nx.triangles(g).values()) // 3
        paths = sum(d * (d - 1) // 2 for _, d in g.degree()) - 3 * tri
        return [float(paths), float(tri)]
    counts = [0] * 6
    for sub in combinations(range(fx.n), 4):
        h = g.subgraph(sub)
        if h.number_of_edges() < 3 or not nx.is_connected(h):
            continue
        for idx, motif in FOUR.items():
            if h.number_of_edges() == motif.number_of_edges() and nx.is_isomorphic(h, motif):
                counts[idx] += 1
                break
    return [float(c) for c in counts]


def compute(fx, e):
    fn = e["fn"]
    return {"dyad_census": lambda: dyad_census(fx),
            "degree_distribution": lambda: degree_distribution(fx, e),
            "krackhardt_dimensions": lambda: krackhardt(fx)[3:] if e.get("part") == "lubness" else krackhardt(fx)[:3],
            "ego_composition": lambda: ego_composition(fx, e),
            "symmetrize": lambda: symmetrize(fx, e),
            "simmelian_ties": lambda: simmelian(fx),
            "cocitation": lambda: cocitation(fx, e),
            "partition_quality": lambda: partition_quality(fx),
            "motif_census": lambda: motif_census(fx, e)}[fn]()


def main() -> None:
    spec = load_area("descriptive_more")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            e = v["params"]
            if e["fn"] == "partition_quality" and not fx.src:
                continue
            if e["fn"] == "motif_census" and e["size"] == 4 and fx.n > SIZE4_MAX_NODES:
                continue
            write_values(ORACLE, name, variant, compute(fx, e))
            count += 1
    print(f"networkx {nx.__version__} (descriptive_more): wrote {count} golden files")
    write_version(ORACLE, f"networkx {nx.__version__}")


if __name__ == "__main__":
    main()
