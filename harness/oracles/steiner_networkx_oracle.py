#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for
approximate Steiner trees (manifest/steiner.yaml, entries with
a `networkx` oracle): the edge positions of
nx.algorithms.approximation.steiner_tree(G, terminals, weight, method), with
the terminals every third node. NetworkX's `kou` takes its terminals in the
iteration order of a set; the engine is given that order.

    python3 oracles/steiner_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx
from networkx.algorithms.approximation import steiner_tree

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)
from steiner_definition_oracle import terminal_list, unusable  # noqa: E402

ORACLE = "networkx"


def compute(fx, spec):
    weighted = bool(spec.get("weighted"))
    if unusable(fx, weighted):
        return []
    g = nx.Graph()
    g.add_nodes_from(range(fx.n))
    position = {}
    for e, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        if a == b:
            continue
        position[frozenset((a, b))] = e
        g.add_edge(a, b, weight=fx.weights[e] if weighted and fx.weighted else 1.0)
    terms = terminal_list(fx, spec.get("terminals", "third"))
    tree = steiner_tree(g, terms, weight="weight", method=spec["method"])
    return sorted(position[frozenset(edge)] for edge in tree.edges())


def main() -> None:
    spec = load_area("steiner")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, f"networkx {nx.__version__}")
    print(f"networkx (Steiner trees): wrote {count} golden files")


if __name__ == "__main__":
    main()
