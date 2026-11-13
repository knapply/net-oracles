#!/usr/bin/env python3
"""Definition oracle for the planarity measures: planarity by path addition
(Demoucron, Malgrange and Pertuiset 1964) on each biconnected block of the
simple undirected graph underlying the fixture (code shared with
structure_nx_definition_oracle.py, which has no code in common with the
engine), outerplanarity by the apex graph (Chartrand and Harary 1967: G is
outerplanar exactly when G plus a node joined to every node is planar), and
the properties every correct embedding, Kuratowski certificate and drawing
has (expected values of the validity entries; the checkers themselves are
in ../planarity_check.py and are run on NetworkX's and Boost's results by
the other oracles). Inputs and encodings: ../bindings/planarity.py.

    python3 oracles/planarity_definition_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)
from structure_nx_definition_oracle import block_planar, blocks  # noqa: E402

ORACLE = "definition"
AREA = "planarity"
MEASURES = {}


def measure(name):
    def wrap(f):
        MEASURES[name] = f
        return f
    return wrap


def simple_adjacency(n, pairs, apex=False):
    """Successor sets of the simple graph, plus an apex node n joined to
    every node when asked."""
    succ = {v: set() for v in range(n + (1 if apex else 0))}
    for a, b in pairs:
        succ[a].add(b)
        succ[b].add(a)
    if apex:
        for v in range(n):
            succ[v].add(n)
            succ[n].add(v)
    return succ


def planar(n, pairs, apex=False):
    succ = simple_adjacency(n, pairs, apex)
    return all(block_planar(b) for b in blocks(len(succ), succ))


def pairs_of(fx):
    return sorted({(min(a, b), max(a, b)) for a, b in zip(fx.src, fx.tgt) if a != b})


@measure("pl_planar")
def _planar(fx, e):
    return [int(planar(fx.n, pairs_of(fx)))]


@measure("pl_embedding_valid")
def _valid(fx, e):
    return [1 if planar(fx.n, pairs_of(fx)) else -1]


@measure("pl_embedding_darts")
def _darts(fx, e):
    return [1, 1, 1] if planar(fx.n, pairs_of(fx)) else [-1]


@measure("pl_kuratowski_valid")
def _kuratowski(fx, e):
    return [-1] if planar(fx.n, pairs_of(fx)) else [1, 1]


@measure("pl_outerplanar")
def _outerplanar(fx, e):
    return [int(planar(fx.n, pairs_of(fx), apex=True))]


@measure("pl_outerplanar_valid")
def _outer_valid(fx, e):
    return [-1] if planar(fx.n, pairs_of(fx), apex=True) else [1]


@measure("pl_layout_valid")
def _layout(fx, e):
    return [1, 1, 1, 1] if planar(fx.n, pairs_of(fx)) else [-1]


def main() -> None:
    spec = load_area(AREA)
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            f = MEASURES.get(v["params"]["fn"])
            if f is not None:
                write_values(ORACLE, name, variant, f(fx, v["params"]))
                count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition ({AREA}): wrote {count} golden files")


if __name__ == "__main__":
    main()
