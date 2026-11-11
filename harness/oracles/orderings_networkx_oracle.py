#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for vertex
orderings (manifest/orderings.yaml, entries with a `networkx`
oracle), on the simple undirected network underlying the fixture:

  degeneracy width  the largest core number, max(nx.core_number(G).values())
  chordal           nx.is_chordal(G)

    python3 oracles/orderings_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)

ORACLE = "networkx"


def compute(fx, spec):
    g = nx.Graph()
    g.add_nodes_from(range(fx.n))
    g.add_edges_from((a, b) for a, b in zip(fx.src, fx.tgt) if a != b)
    if spec["stat"] == "chordal":
        return [int(nx.is_chordal(g))]
    return [max(nx.core_number(g).values(), default=0)]


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
    write_version(ORACLE, f"networkx {nx.__version__}")
    print(f"networkx (vertex orderings): wrote {count} golden files")


if __name__ == "__main__":
    main()
