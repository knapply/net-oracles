#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for the
graph theory and combinatorics measures (inputs and encodings:
../bindings/graph_theory.py): threshold graphs, the weight of a maximum
matching as a bound on approximate ones, travelling salesman tours of the
metric closure, and distances to the nearest of several centers.

    python3 oracles/graph_theory_networkx_oracle.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import networkx as nx
from networkx.algorithms import threshold as nx_threshold

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture, write_values,  # noqa: E402
                    write_version)

ORACLE = "networkx"
AREA = "graph_theory"
MEASURES = {}


def measure(*names):
    def wrap(f):
        for name in names:
            MEASURES[name] = f
        return f
    return wrap


def simple_undirected(fx):
    g = nx.Graph()
    g.add_nodes_from(range(fx.n))
    g.add_edges_from((a, b) for a, b in zip(fx.src, fx.tgt) if a != b)
    return g


@measure("gt_threshold_is")
def _threshold_is(fx, e):
    return [int(nx_threshold.is_threshold_graph(simple_undirected(fx)))]


@measure("gt_threshold_types")
def _threshold_types(fx, e):
    cs = nx_threshold.creation_sequence(dict(simple_undirected(fx).degree()))
    return [-1] if cs is None else [1 if c == "d" else 0 for c in cs]


@measure("gt_match_half_bound", "gt_match_upper_bound")
def _match_bound(fx, e):
    first = {}
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        if a != b:
            w = fx.weights[i] if fx.weights else 1.0
            key = (min(a, b), max(a, b))
            first[key] = max(first.get(key, w), w)
    g = nx.Graph()
    g.add_nodes_from(range(fx.n))
    g.add_weighted_edges_from((a, b, w) for (a, b), w in first.items())
    opt = sum(g[a][b]["weight"] for a, b in nx.max_weight_matching(g))
    return [opt, opt]


def weighted_graph(fx):
    first = {}
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        if a != b:
            first.setdefault((min(a, b), max(a, b)), fx.weights[i] if fx.weights else 1.0)
    g = nx.Graph()
    g.add_nodes_from(range(fx.n))
    g.add_weighted_edges_from((a, b, first[(a, b)]) for a, b in sorted(first))
    return g


def closure(fx):
    """The complete graph of shortest-path distances, built as
    traveling_salesman_problem builds it, or None."""
    if fx.directed or fx.n < 3:
        return None
    g = weighted_graph(fx)
    if not nx.is_connected(g):
        return None
    dist = {n: d for n, (d, _) in nx.all_pairs_dijkstra(g, weight="weight")}
    gg = nx.Graph()
    for u in g.nodes:
        for v in g.nodes:
            if u != v:
                gg.add_edge(u, v, weight=dist[u][v])
    return gg


def rotate(tour, start=0):
    body = tour[:-1]
    at = body.index(start)
    body = body[at:] + body[:at]
    return body + [body[0]]


def length(gg, tour):
    return sum(gg[a][b]["weight"] for a, b in zip(tour, tour[1:]))


@measure("gt_tsp_nn_tour")
def _tsp_nn(fx, e):
    gg = closure(fx)
    if gg is None:
        return [-1]
    tour = nx.approximation.greedy_tsp(gg, weight="weight", source=0)
    return [length(gg, tour)] + tour


@measure("gt_tsp_christofides_tour")
def _tsp_christofides(fx, e):
    gg = closure(fx)
    if gg is None:
        return [-1]
    tour = rotate(nx.approximation.christofides(gg, weight="weight"))
    return [length(gg, tour)] + tour


@measure("gt_voronoi_distance")
def _voronoi_distance(fx, e):
    g = nx.MultiDiGraph() if fx.directed else nx.MultiGraph()
    g.add_nodes_from(range(fx.n))
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        g.add_edge(a, b, weight=fx.weights[i] if fx.weighted else 1.0)
    centers = [0, fx.n // 2] if fx.n >= 2 else [0]
    cells = nx.voronoi_cells(g, centers, weight="weight")
    out = [-1.0] * fx.n
    for center, members in cells.items():
        if center == "unreachable":
            continue
        d = nx.single_source_dijkstra_path_length(g, center, weight="weight")
        for v in members:
            out[v] = d[v]
    return out


def main() -> None:
    spec = load_area(AREA)
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            f = MEASURES.get(variant)
            if f is None:
                continue
            values = f(fx, v["params"])
            write_values(ORACLE, name, variant, values)
            count += 1
    print(f"networkx {nx.__version__} ({AREA}): wrote {count} golden files")
    write_version(ORACLE, f"networkx {nx.__version__}")


if __name__ == "__main__":
    main()
