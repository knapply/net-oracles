#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for
manifest/construct.yaml (encodings in bindings/construct.py, derived
inputs in derived/construct.py).

    python3 oracles/construct_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)
from derived import construct as D  # noqa: E402

ORACLE = "networkx"


def pack(g, directed, relabel=None):
    """[node count] and the sorted edge list, nodes mapped by `relabel`."""
    m = relabel or (lambda v: v)
    edges = D.normalize(((m(a), m(b)) for a, b in g.edges()), directed)
    return [g.number_of_nodes()] + [list(e) for e in edges]


def build(shape, n):
    directed = shape.endswith("_dir")
    base = shape[:-4] if directed else shape
    using = nx.DiGraph if directed else nx.Graph
    relabel = None
    if base == "empty":
        g = nx.empty_graph(n)
    elif base == "complete":
        g = nx.complete_graph(n, create_using=using)
    elif base == "complete_bipartite":
        g = nx.complete_bipartite_graph(n // 2, n - n // 2)
    elif base == "star":
        g = nx.star_graph(n - 1, create_using=using) if n > 0 else nx.empty_graph(0, create_using=using)
    elif base == "path":
        g = nx.path_graph(n, create_using=using)
    elif base == "cycle":
        g = nx.cycle_graph(n, create_using=using)
    elif base == "wheel":
        g = nx.wheel_graph(n)
    elif base == "lattice":
        g = nx.grid_2d_graph(3, n)
        relabel = lambda v: v[0] * n + v[1]  # noqa: E731
    elif base == "tree_binary":
        g = nx.balanced_tree(2, min(n, 5))
    elif base == "tree_ternary":
        g = nx.balanced_tree(3, min(n, 4))
    elif base == "hypercube":
        d = min(n, 8)
        g = nx.hypercube_graph(d)
        relabel = lambda v: v if isinstance(v, int) else sum(bit << (d - 1 - i) for i, bit in enumerate(v))  # noqa: E731
    elif base == "ladder":
        g = nx.ladder_graph(n)
    else:
        raise ValueError(shape)
    return pack(g, directed, relabel)


def graph_of(edges, fx):
    g = (nx.DiGraph if fx.directed else nx.Graph)()
    g.add_nodes_from(range(fx.n))
    g.add_edges_from(edges)
    return g


def line_graph(fx):
    edges = D.loop_free(D.first(fx))
    rank = {e: i for i, e in enumerate(edges)}
    lg = nx.line_graph(graph_of(edges, fx))

    def key(e):
        return rank[e if fx.directed else (min(e), max(e))]

    out = sorted((key(a), key(b)) if fx.directed else tuple(sorted((key(a), key(b))))
                 for a, b in lg.edges())
    return [len(edges)] + [list(e) for e in out]


def compute(engine, fx):
    fn = engine["fn"]
    if fn == "deterministic_generators":
        return build(engine["shape"], fx.n)
    if fn == "line_graph":
        return line_graph(fx)
    if fn == "paths_simple":
        if fx.n < 2:
            return []
        g = graph_of(D.loop_free(D.first(fx)), fx)
        return sorted(nx.all_simple_paths(g, 0, fx.n - 1, cutoff=engine["cutoff"]))
    g, h = graph_of(D.first(fx), fx), graph_of(D.second(fx), fx)
    if fn == "op_union":
        r = nx.compose(g, h)
    elif fn == "op_intersection":
        r = nx.intersection(g, h)
    elif fn == "op_difference":
        r = nx.difference(g, h)
    else:
        raise ValueError(fn)
    return pack(r, fx.directed)


def main() -> None:
    spec = load_area("construct")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, compute(v["params"], fx))
            count += 1
    write_version(ORACLE, f"networkx {nx.__version__}")
    print(f"networkx (construct): wrote {count} golden files")


if __name__ == "__main__":
    main()
