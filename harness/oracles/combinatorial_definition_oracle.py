#!/usr/bin/env python3
"""Definition oracle for the combinatorial measures: brute-force
enumeration from the published definitions (cliques grown one node at a
time in increasing order; maxima over every clique). Shares no code with
the engine. Inputs and encodings: ../bindings/combinatorial.py.

    python3 oracles/combinatorial_definition_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
AREA = "combinatorial"
MEASURES = {}


def measure(name):
    def wrap(f):
        MEASURES[name] = f
        return f
    return wrap


def arcs(fx, directed):
    """Adjacency sets of the simple graph (self-loops dropped)."""
    adj = {v: set() for v in range(fx.n)}
    for a, b in zip(fx.src, fx.tgt):
        if a == b:
            continue
        adj[a].add(b)
        if not directed:
            adj[b].add(a)
    return adj


def every_clique(n, adj):
    """Every clique (a set in which each node has an arc to every later
    node), as sorted tuples, by depth-first growth in increasing order."""
    out = []

    def grow(c):
        out.append(tuple(c))
        for w in range(c[-1] + 1, n):
            if all(w in adj[u] for u in c):
                grow(c + [w])

    for v in range(n):
        grow([v])
    return out


def node_weights(n):
    return [(7 * v) % 5 - 1 for v in range(n)]


@measure("node_clique_number")
def _ncn(fx, e):
    best = [0] * fx.n
    for c in every_clique(fx.n, arcs(fx, False)):
        for v in c:
            best[v] = max(best[v], len(c))
    return best


@measure("all_cliques")
def _all(fx, e):
    return sorted(every_clique(fx.n, arcs(fx, fx.directed)), key=lambda c: (len(c), c))


@measure("max_weight_clique")
def _mwc(fx, e):
    w = node_weights(fx.n)
    best = max([sum(w[v] for v in c) for c in every_clique(fx.n, arcs(fx, False))] + [0])
    return [(best, 1)]


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
