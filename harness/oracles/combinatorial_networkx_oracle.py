#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for the
combinatorial measures (see ../bindings/combinatorial.py for the inputs and
encodings). Every measure reads the simple Graph or DiGraph a fixture
denotes: nodes 0..n - 1, then the edges in file order, self-loops dropped.

    python3 oracles/combinatorial_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture, write_values,  # noqa: E402
                    write_version)

ORACLE = "networkx"
AREA = "combinatorial"
MEASURES = {}


def measure(name):
    def wrap(f):
        MEASURES[name] = f
        return f
    return wrap


def simple(fx, directed=None):
    d = fx.directed if directed is None else directed
    g = nx.DiGraph() if d else nx.Graph()
    g.add_nodes_from(range(fx.n))
    g.add_edges_from((a, b) for a, b in zip(fx.src, fx.tgt) if a != b)
    return g


def node_weights(n):
    return [(7 * v) % 5 - 1 for v in range(n)]


@measure("node_clique_number")
def _ncn(fx, e):
    c = nx.node_clique_number(simple(fx, False))
    return [c[v] for v in range(fx.n)]


@measure("all_cliques")
def _all(fx, e):
    return [tuple(c) for c in nx.enumerate_all_cliques(simple(fx))]


def _mwc(fx):
    g = simple(fx, False)
    for v, w in enumerate(node_weights(fx.n)):
        g.nodes[v]["weight"] = w
    return nx.max_weight_clique(g)


@measure("max_weight_clique")
def _mwc_weight(fx, e):
    c, w = _mwc(fx)
    g = simple(fx, False)
    ok = all(g.has_edge(a, b) for i, a in enumerate(c) for b in c[i + 1:])
    return [(w, int(ok))]


@measure("max_weight_clique_nodes")
def _mwc_nodes(fx, e):
    return list(_mwc(fx)[0])


@measure("nx_cliques_order")
def _cliques_order(fx, e):
    g = simple(fx)
    return [list(c) for c in nx.find_cliques(g)] + [list(c) for c in nx.find_cliques_recursive(g)]


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
