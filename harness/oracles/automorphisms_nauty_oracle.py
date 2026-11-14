#!/usr/bin/env python3
# oracle-env: pynauty
# oracle-entries: nauty
"""Golden values from nauty 2.8.8 (McKay and Piperno 2014) through pynauty for
the automorphism measures: group order, orbits, and canonical-form
self-consistency.

nauty takes simple coloured graphs, so each fixture is reduced as in
aut_reduce.py: self-loops become part of the node colour, and under
`multiplicity` each pair is subdivided by a node coloured by the number of
parallel edges (the group order and the orbits of the original nodes are
those of the multigraph). pynauty reports the group size as a double
(mantissa and exponent), so the exact order comes from the generators
by orbit-stabilizer: nauty's orbits of the graph, then of the graph with the
first node of the first non-trivial orbit given its own colour, and so on; the
order is the product of the orbit sizes met. The orbits are those of `pynauty.autgrp`, restricted
to the original nodes.

Canonical forms: for each of 8 seeded relabelings, and for rev(fixture) and
perturbed(fixture), whether the certificate of `pynauty.certificate` and the
colours in the order of `pynauty.canon_label` equal those of the fixture.

    python3 oracles/automorphisms_nauty_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import pynauty

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from aut_reduce import (color_ids, first_appearance, limbs16, perturbed_pairs,  # noqa: E402
                        reduce_graph, relabeled, rev_pairs, user_colors)
from common import (applies, fixture_names, load_area, load_fixture, write_values,  # noqa: E402
                    write_version)

ORACLE = "nauty"
RELABELINGS = 8
FACTS: dict = {}


def nauty_graph(n_nodes, edges, directed, colors):
    adjacency = {v: [] for v in range(n_nodes)}
    for a, b in edges:
        adjacency[a].append(b)
        if not directed:
            adjacency[b].append(a)
    cells = [{v for v in range(n_nodes) if colors[v] == c} for c in sorted(set(colors))]
    return pynauty.Graph(n_nodes, directed=directed, adjacency_dict=adjacency,
                         vertex_coloring=cells)


def group_facts(n_nodes, edges, directed, colors, n_original):
    graph = nauty_graph(n_nodes, edges, directed, colors)
    _, _, _, orbits, _ = pynauty.autgrp(graph)
    first = first_appearance(orbits[:n_original])
    order, colors = 1, list(colors)
    while True:
        sizes: dict = {}
        for rep in orbits:
            sizes[rep] = sizes.get(rep, 0) + 1
        pending = [v for v in range(n_nodes) if sizes[orbits[v]] > 1]
        if not pending:
            return order, first
        node = pending[0]
        order *= sizes[orbits[node]]
        colors[node] = max(colors) + 1
        _, _, _, orbits, _ = pynauty.autgrp(nauty_graph(n_nodes, edges, directed, colors))


def canonical_key(n_nodes, edges, directed, colors):
    graph = nauty_graph(n_nodes, edges, directed, colors)
    return (n_nodes, pynauty.certificate(graph),
            tuple(colors[v] for v in pynauty.canon_label(graph)))


def compute(fx, spec):
    e = spec["params"]
    pairs = list(zip(fx.src, fx.tgt))
    kind, mode = e.get("colors", "none"), e.get("edges", "simple")
    base = user_colors(fx.n, kind)
    n_nodes, edges, tuples, n_original = reduce_graph(fx.n, pairs, fx.directed, base, mode)
    if e["fn"] == "automorphism":
        cache = (fx.name, kind, mode)
        if cache not in FACTS:
            (colors,) = color_ids(tuples)
            FACTS[cache] = group_facts(n_nodes, edges, fx.directed, colors, n_original)
        order, labels = FACTS[cache]
        return labels if e["output"] == "orbits" else limbs16(order)

    def same(perm, other_pairs):
        moved = [0] * fx.n
        for v in range(fx.n):
            moved[perm[v]] = base[v]
        o_nodes, o_edges, o_tuples, _ = reduce_graph(fx.n, other_pairs, fx.directed, moved, mode)
        mine, theirs = color_ids(tuples, o_tuples)
        return (canonical_key(n_nodes, edges, fx.directed, mine)
                == canonical_key(o_nodes, o_edges, fx.directed, theirs))
    if e["check"] == "relabelings":
        return [sum(same(*relabeled(fx.n, pairs, fx.directed, f"nauty-{fx.name}-{s}"))
                    for s in range(RELABELINGS))]
    return [int(same(*rev_pairs(fx.n, pairs))), int(same(*perturbed_pairs(fx.n, pairs)))]


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
            if fx.directed and spec["params"].get("edges") == "multiplicity":
                continue  # pynauty does not return on these (undefined_when: directed)
            write_values(ORACLE, name, variant, compute(fx, spec))
            count += 1
    write_version(ORACLE, f"nauty via pynauty {pynauty.__version__} (nauty "
                  f"{getattr(pynauty, 'nauty_version', None) or getattr(pynauty, '_nauty_version', '?')})")
    print(f"nauty (pynauty {pynauty.__version__}): wrote {count} golden files")


if __name__ == "__main__":
    main()
