#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for the
automorphism measures, with its isomorphism test as a black box.

The group order and the orbits come from the orbit-stabilizer theorem with
`nx.vf2pp_is_isomorphic` deciding, for a node v and a candidate c, whether
an automorphism fixing some nodes sends v to c: both copies of the graph get
node labels, the nodes to fix get one unique label each in both copies, and v
(in the first copy) and c (in the second) get one more. The order is the product of the orbit sizes
along the nodes in index order; the orbits are the classes of the nodes that
some automorphism joins.

Multiplicities are edge labels for NetworkX's VF2 matcher (VF2++ takes no edge labels), and
a node's self-loops are part of its label.

Canonical-form entries: whether NetworkX finds each of 8 seeded relabelings
isomorphic to the fixture (a count), and whether the fixture is isomorphic to
rev(fixture) and perturbed(fixture).

    python3 oracles/automorphisms_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from aut_reduce import (first_appearance, limbs16, perturbed_pairs, relabeled,  # noqa: E402
                        rev_pairs, user_colors)
from common import (applies, fixture_names, load_area, load_fixture, write_values,  # noqa: E402
                    write_version)

ORACLE = "networkx"
RELABELINGS = 8
FACTS: dict = {}


def read_graph(n, pairs, directed, base, multi):
    """(node keys, weighted edges): a node's key is (user colour, loops) and an edge carries
    the number of parallel edges under `multiplicity` (1 otherwise); loops are not edges."""
    loops = [0] * n
    counts: dict = {}
    for a, b in pairs:
        if a == b:
            loops[a] += 1
        else:
            key = (a, b) if directed else (min(a, b), max(a, b))
            counts[key] = counts.get(key, 0) + 1
    keys = [(base[v], loops[v] if multi else int(loops[v] > 0)) for v in range(n)]
    return keys, {k: (c if multi else 1) for k, c in counts.items()}


def build(keys, edges, directed, tags):
    """A NetworkX graph whose node labels are (key, tag) and edges carry `mult`."""
    g = nx.DiGraph() if directed else nx.Graph()
    for v, key in enumerate(keys):
        g.add_node(v, label=(key, tags.get(v, 0)))
    for (a, b), count in edges.items():
        g.add_edge(a, b, mult=count)
    return g


def same_graph(g1, g2, multi):
    """NetworkX's isomorphism test: VF2++ on labelled nodes, or the VF2 matcher with
    edge multiplicities as edge labels."""
    # Without parallel edges every label is 1: VF2++ then decides it, much faster than VF2.
    if not multi or all(d["mult"] == 1 for g in (g1, g2) for *_, d in g.edges(data=True)):
        return nx.vf2pp_is_isomorphic(g1, g2, node_label="label")
    matcher = nx.isomorphism.DiGraphMatcher if g1.is_directed() else nx.isomorphism.GraphMatcher
    return matcher(
        g1, g2, node_match=nx.isomorphism.categorical_node_match("label", None),
        edge_match=nx.isomorphism.categorical_edge_match("mult", 1)).is_isomorphic()


def group_facts(keys, edges, directed, multi):
    """(order, orbit labels) by orbit-stabilizer, NetworkX deciding each existence."""
    n = len(keys)
    out_deg = [0] * n
    in_deg = [0] * n
    for (a, b), count in edges.items():
        out_deg[a] += count
        in_deg[b] += count
        if not directed:
            out_deg[b] += count
            in_deg[a] += count
    shape = [(keys[v], out_deg[v], in_deg[v]) for v in range(n)]

    def exists(fixed, v, c):
        tags1 = {u: k for k, u in enumerate(fixed, start=1)}
        tags2 = dict(tags1)
        tags1[v] = -1
        tags2[c] = -1
        return same_graph(build(keys, edges, directed, tags1), build(keys, edges, directed, tags2),
                          multi)

    order = 1
    for v in range(n):
        orbit = 1
        for c in range(n):
            if c != v and shape[c] == shape[v] and exists(list(range(v)), v, c):
                orbit += 1
        order *= orbit
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for v in range(n):
        for c in range(v):
            if find(v) != find(c) and shape[c] == shape[v] and exists([], v, c):
                parent[find(v)] = find(c)
    return order, first_appearance([find(v) for v in range(n)])


def compute(fx, spec):
    e = spec["params"]
    pairs = list(zip(fx.src, fx.tgt))
    kind, mode = e.get("colors", "none"), e.get("edges", "simple")
    multi = mode == "multiplicity"
    base = user_colors(fx.n, kind)
    keys, edges = read_graph(fx.n, pairs, fx.directed, base, multi)
    if e["fn"] == "automorphism":
        cache = (fx.name, kind, mode)
        if cache not in FACTS:
            FACTS[cache] = group_facts(keys, edges, fx.directed, multi)
        order, labels = FACTS[cache]
        return labels if e["output"] == "orbits" else limbs16(order)

    def isomorphic(perm, other_pairs):
        """Whether the fixture is isomorphic to the graph with nodes renamed by perm
        (colours follow the nodes) and the given edges."""
        moved = [0] * fx.n
        for v in range(fx.n):
            moved[perm[v]] = base[v]
        o_keys, o_edges = read_graph(fx.n, other_pairs, fx.directed, moved, multi)
        return same_graph(build(keys, edges, fx.directed, {}), build(o_keys, o_edges, fx.directed, {}),
                          multi)
    if e["check"] == "relabelings":
        return [sum(isomorphic(*relabeled(fx.n, pairs, fx.directed, f"nx-{fx.name}-{s}"))
                    for s in range(RELABELINGS))]
    return [int(isomorphic(*rev_pairs(fx.n, pairs))),
            int(isomorphic(*perturbed_pairs(fx.n, pairs)))]


def main() -> None:
    manifest = load_area("automorphisms")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        if fx.n == 0:
            continue
        for variant, spec in manifest.items():
            if ORACLE not in spec["oracles"] or not applies(spec, fx):
                continue
            write_values(ORACLE, name, variant, compute(fx, spec))
            count += 1
    write_version(ORACLE, f"networkx {nx.__version__} (vf2pp_is_isomorphic)")
    print(f"networkx: wrote {count} golden files")


if __name__ == "__main__":
    main()
