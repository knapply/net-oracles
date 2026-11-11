#!/usr/bin/env python3
"""Definition oracle for vertex orderings (manifest/
orderings.yaml; statistics as in ../bindings/orderings.py): the textbook
procedures by repeated selection over all nodes, O(n^2), on the simple
undirected network underlying the fixture.

  degeneracy       repeatedly remove the node of least degree in the remaining
                   network, ties to the smallest id (Matula and Beck 1983)
  max-cardinality  repeatedly visit the unvisited node with the most visited
                   neighbours, ties to the smallest id (Tarjan and Yannakakis
                   1984)
  chordal          whether repeatedly removing a simplicial node (one whose
                   remaining neighbours form a clique) empties the network:
                   a network is chordal exactly when it does (Fulkerson and
                   Gross 1965; an independent criterion, not the search)

    python3 oracles/orderings_definition_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"


def simple_sets(fx):
    nbr = {v: set() for v in range(fx.n)}
    for a, b in zip(fx.src, fx.tgt):
        if a != b:
            nbr[a].add(b)
            nbr[b].add(a)
    return nbr


def degeneracy(fx):
    nbr = simple_sets(fx)
    remaining, order, width = set(range(fx.n)), [], 0
    while remaining:
        v = min(remaining, key=lambda x: (len(nbr[x] & remaining), x))
        width = max(width, len(nbr[v] & remaining))
        order.append(v)
        remaining.discard(v)
    return order, width


def max_cardinality(fx):
    nbr = simple_sets(fx)
    unvisited, order, width = set(range(fx.n)), [], 0
    visited = set()
    while unvisited:
        v = min(unvisited, key=lambda x: (-len(nbr[x] & visited), x))
        width = max(width, len(nbr[v] & visited))
        order.append(v)
        visited.add(v)
        unvisited.discard(v)
    return order, width


def chordal(fx):
    nbr = simple_sets(fx)
    remaining = set(range(fx.n))
    while remaining:
        for v in sorted(remaining):
            around = nbr[v] & remaining
            if all(b in nbr[a] for a in around for b in around if a != b):
                remaining.discard(v)
                break
        else:
            return False
    return True


def compute(fx, spec):
    stat = spec["stat"]
    if stat == "chordal":
        return [int(chordal(fx))]
    order, width = (degeneracy if spec["kind"] == "degeneracy" else max_cardinality)(fx)
    return order if stat == "order" else [width]


def main() -> None:
    spec = load_area("orderings")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (vertex orderings): wrote {count} golden files")


if __name__ == "__main__":
    main()
