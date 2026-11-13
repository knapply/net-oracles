#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for the
planarity measures: is_planar, check_planarity (its embedding, as the
reference rotation system), get_counterexample (Kuratowski subgraph) and
combinatorial_embedding_to_pos (the de Fraysseix, Pach and Pollack drawing
on an integer grid). NetworkX has no outerplanarity test; the apex graph
(Chartrand and Harary 1967) goes through its is_planar. The validity checks
(../planarity_check.py) are applied to NetworkX's own embeddings,
certificates and drawings, which tests the checkers too. Inputs and
encodings: ../bindings/planarity.py.

    python3 oracles/planarity_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import planarity_check as C  # noqa: E402
from common import (applies, fixture_names, load_area, load_fixture, write_values,  # noqa: E402
                    write_version)

ORACLE = "networkx"
AREA = "planarity"
MEASURES = {}


def measure(name):
    def wrap(f):
        MEASURES[name] = f
        return f
    return wrap


def sorted_graph(fx):
    g = nx.Graph()
    g.add_nodes_from(range(fx.n))
    g.add_edges_from(C.simple_pairs(fx.src, fx.tgt))
    return g


def input_graph(fx):
    """The simple graph built edge by edge in the fixture's order (NetworkX's
    embedding and Kuratowski subgraph depend on the adjacency order)."""
    g = nx.Graph()
    g.add_nodes_from(range(fx.n))
    g.add_edges_from((a, b) for a, b in zip(fx.src, fx.tgt) if a != b)
    return g


def rings_of(fx):
    """NetworkX's rotation system (clockwise from the leftmost neighbour), or None."""
    ok, emb = nx.check_planarity(input_graph(fx))
    if not ok:
        return None
    data = emb.get_data()
    return [list(data.get(v, [])) for v in range(fx.n)]


def counterexample(fx):
    try:
        return nx.algorithms.planarity.get_counterexample(input_graph(fx))
    except nx.NetworkXException:
        return None


def apex_planar(n, pairs):
    g = nx.Graph()
    g.add_nodes_from(range(n + 1))
    g.add_edges_from(pairs)
    g.add_edges_from((v, n) for v in range(n))
    return nx.is_planar(g)


@measure("pl_planar")
def _planar(fx, e):
    return [int(nx.is_planar(sorted_graph(fx)))]


@measure("pl_embedding")
def _embedding(fx, e):
    rings = rings_of(fx)
    return [-1] if rings is None else [x for r in rings for x in [len(r)] + r]


def rotate_to_smallest(ring):
    if not ring:
        return ring
    k = ring.index(min(ring))
    return ring[k:] + ring[:k]


@measure("pl_embedding_smallest")
def _smallest(fx, e):
    rings = rings_of(fx)
    if rings is None:
        return [-1]
    return [x for r in rings for x in [len(r)] + rotate_to_smallest(r)]


@measure("pl_embedding_valid")
def _valid(fx, e):
    rings = rings_of(fx)
    return [-1] if rings is None else [C.check_simple_embedding(fx.n, C.simple_pairs(fx.src, fx.tgt), rings)]


def dart_rows(fx, rings):
    """The dart rotation of the multigraph from a simple rotation, by the
    documented rule: the darts of the edges between u and v sit together
    where the lowest-numbered of them would (in edge order at the smaller
    node of the pair, the reverse order at the larger), and a loop's darts
    (2e, 2e + 1) come right after u's first neighbour's group."""
    groups, loops = {}, {}
    for e, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        if a == b:
            loops.setdefault(a, []).append(e)
        else:
            groups.setdefault((min(a, b), max(a, b)), []).append(e)
    rows = []
    for v, ring in enumerate(rings):
        row = []
        for i, w in enumerate(ring):
            es = groups[(min(v, w), max(v, w))]
            if v < w:  # parallel edges in id order at the smaller end
                row += [2 * e + (0 if fx.src[e] == v else 1) for e in es]
            else:
                row += [2 * e + (0 if fx.src[e] == v else 1) for e in reversed(es)]
            if i == 0:
                row += [d for e in loops.get(v, []) for d in (2 * e, 2 * e + 1)]
        if not ring:
            row = [d for e in loops.get(v, []) for d in (2 * e, 2 * e + 1)]
        rows.append(row)
    return rows


@measure("pl_embedding_darts")
def _darts(fx, e):
    rings = rings_of(fx)
    return [-1] if rings is None else C.check_dart_embedding(fx.n, fx.src, fx.tgt, dart_rows(fx, rings))


@measure("pl_kuratowski_valid")
def _kuratowski(fx, e):
    k = counterexample(fx)
    if k is None:
        return [-1]
    return [int(C.certificate_kind(list(k.edges())) in (5, 33)), 1]


@measure("pl_kuratowski_nx")
def _kuratowski_nx(fx, e):
    k = counterexample(fx)
    if k is None:
        return [-1]
    return [x for p in sorted((min(u, v), max(u, v)) for u, v in k.edges()) for x in p]


@measure("pl_outerplanar")
def _outerplanar(fx, e):
    return [int(apex_planar(fx.n, C.simple_pairs(fx.src, fx.tgt)))]


@measure("pl_outerplanar_valid")
def _outer_valid(fx, e):
    pairs = C.simple_pairs(fx.src, fx.tgt)
    if apex_planar(fx.n, pairs):
        return [-1]
    # Shrink first with NetworkX's Kuratowski subgraph of the apex graph
    # (its edges at the apex dropped), then delete edges one at a time.
    g = nx.Graph()
    g.add_nodes_from(range(fx.n + 1))
    g.add_edges_from(pairs)
    g.add_edges_from((v, fx.n) for v in range(fx.n))
    sub = nx.algorithms.planarity.get_counterexample(g)
    keep = sorted((min(u, v), max(u, v)) for u, v in sub.edges() if fx.n not in (u, v))
    for p in list(keep):
        rest = [q for q in keep if q != p]
        if not apex_planar(fx.n, rest):
            keep = rest
    return [int(C.outer_certificate_kind(keep) != 0)]


@measure("pl_layout_valid")
def _layout(fx, e):
    ok, emb = nx.check_planarity(input_graph(fx))
    if not ok:
        return [-1]
    rings = rings_of(fx)
    if fx.n < 3:
        pos = {v: (v, 0) for v in range(fx.n)}
    else:
        pos = nx.combinatorial_embedding_to_pos(emb)
    pts = [tuple(int(c) for c in pos[v]) for v in range(fx.n)]
    return C.check_drawing(fx.n, pts, C.simple_pairs(fx.src, fx.tgt), rings)


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
