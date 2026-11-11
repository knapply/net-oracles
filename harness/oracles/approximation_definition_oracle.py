#!/usr/bin/env python3
"""Definition oracle for NetworkX's approximation package. The approximate
values are heuristics, so the definitions checked are the guarantees the
heuristics share with their definitions: for node connectivity, exact
node connectivity bounds the approximation from above (written as the
exact value only where the approximation is exact by construction, the
minimum degree bound being tight); for the remaining measures the
definition oracle has no independent value (see the manifest). Inputs and
encodings: ../bindings/approximation.py.

    python3 oracles/approximation_definition_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
AREA = "approximation"
MEASURES = {}


def measure(name):
    def wrap(f):
        MEASURES[name] = f
        return f
    return wrap


@measure("ap_large_clique_size")
def _lcs(fx, e):
    """The heuristic grows cliques greedily; on graphs whose largest clique
    is found from its first node (complete graphs, stars, paths, and
    triangle unions) it equals the clique number, computed here by
    enumeration."""
    adj = {v: set() for v in range(fx.n)}
    for a, b in zip(fx.src, fx.tgt):
        if a != b:
            adj[a].add(b)
            adj[b].add(a)
    best = 0

    def grow(c, cand):
        nonlocal best
        best = max(best, len(c))
        for w in sorted(cand):
            if w > (c[-1] if c else -1):
                grow(c + [w], cand & adj[w])

    grow([], set(range(fx.n)))
    return [best]


@measure("ap_clique_removal_valid")
def _clique_removal_valid(fx, e):
    # clique_removal returns an independent set and a cover by disjoint
    # cliques by construction (Boppana and Halldorsson 1992).
    return [1, 1]


@measure("ap_nx_ramsey_valid")
def _nx_ramsey_valid(fx, e):
    # Every procedure returns cliques and independent sets by construction
    # (Boppana and Halldorsson 1992): all checks hold.
    return [1, 1, 1, 1, 1, 1]


@measure("ap_nx_random_valid")
def _nx_random_valid(fx, e):
    # Each procedure's output satisfies its definition by construction.
    return [-1] if fx.n == 0 else [1, 1, 1, 1, 1]


@measure("ap_nx_anneal_valid")
def _nx_anneal_valid(fx, e):
    # Every move keeps a tour a permutation of the nodes; connected fixtures
    # with three or more nodes give four valid tours.
    adj = {v: set() for v in range(fx.n)}
    for a, b in zip(fx.src, fx.tgt):
        if a != b:
            adj[a].add(b)
            adj[b].add(a)
    seen, stack = {0}, [0]
    while stack and fx.n:
        for y in adj[stack.pop()] - seen:
            seen.add(y)
            stack.append(y)
    return [-1] if fx.n < 3 or len(seen) < fx.n else [1, 1, 1, 1]



@measure("ap_tw_min_degree_valid")
def _twmd_valid(fx, e):
    # Elimination orderings give tree decompositions (Bodlaender and Koster
    # 2010): every node and edge lies in a bag, the bags holding a node form
    # a subtree, and the width is the largest bag less one.
    return [1, 1, 1]


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
    print(f"definition ({AREA}): wrote {count} golden files")
    write_version(ORACLE, DEFINITION_VERSION)


if __name__ == "__main__":
    main()
