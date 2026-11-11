#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for the
random spanning tree sampler (manifest/trees_random.yaml,
entries with a `networkx` oracle): the fraction of 2000 draws of
nx.random_spanning_tree(G, weight, multiplicative = True, seed = k),
k = 0..1999, that contain each edge, in fixture edge order. The fixtures
used are simple graphs, so a tree edge identifies an edge position.

NetworkX samples by contraction and deletion with exact tree counts; the
engine uses Wilson's algorithm, so the two draw different trees and are
compared by distribution (tolerance of five standard errors).

    python3 oracles/trees_random_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)

ORACLE = "networkx"
DRAWS = 2000


def frequencies(fx, weighted):
    g = nx.Graph()
    g.add_nodes_from(range(fx.n))
    position = {}
    for e, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        assert a != b and (min(a, b), max(a, b)) not in position
        position[(min(a, b), max(a, b))] = e
        g.add_edge(a, b, weight=fx.weights[e] if weighted else 1.0)
    count = [0] * len(fx.src)
    for k in range(DRAWS):
        tree = nx.random_spanning_tree(g, weight="weight" if weighted else None, seed=k)
        for a, b in tree.edges():
            count[position[(min(a, b), max(a, b))]] += 1
    return [c / DRAWS for c in count]


def main() -> None:
    spec = load_area("trees_random")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            o = v["oracles"].get(ORACLE)
            if o is None or not applies(v, fx) or name not in o["only_on"]:
                continue
            write_values(ORACLE, name, variant,
                         frequencies(fx, v["params"].get("weighted", False)))
            count += 1
    write_version(ORACLE, f"networkx {nx.__version__}")
    print(f"networkx (random spanning trees): wrote {count} golden files")


if __name__ == "__main__":
    main()
