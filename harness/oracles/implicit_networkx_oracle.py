#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for
manifest/implicit.yaml (encodings in bindings/implicit.py, case tables and
node numbering in derived/implicit.py). NetworkX has no de Bruijn or Kautz
generator: both are built as iterated line digraphs, the node of the line
digraph being an arc whose word is the tail's word plus the head's last
letter.

    python3 oracles/implicit_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)
from derived import implicit as D  # noqa: E402

ORACLE = "networkx"


def words_of(graph, base):
    """Word of every node of an iterated line digraph: `base` gives the words
    of the starting graph's nodes; an arc (u, v) is u's word plus v's last
    letter."""
    def word(node):
        if node in base:
            return base[node]
        u, v = node
        return word(u) + (word(v)[-1],)

    return {node: word(node) for node in graph.nodes}


def line_family(base_graph, base_words, steps):
    g, words = base_graph, dict(base_words)
    for _ in range(steps):
        g = nx.line_graph(g)
        words = words_of(g, words)
    return g, words


def build(family, directed, case):
    """(node count, sorted edges) from NetworkX."""
    relabel = None
    if family == "complete_bipartite":
        g = nx.complete_bipartite_graph(*case)
        # The first part holds the smaller ids: the arcs run from it.
        edges = [(min(u, v), max(u, v)) for u, v in g.edges()]
        return g.number_of_nodes(), D.normalize(edges, directed)
    if family == "complete_multipartite":
        g = nx.complete_multipartite_graph(*case[0])
    elif family == "star":
        g = nx.star_graph(case[0])
    elif family == "path":
        g = nx.path_graph(case[0], create_using=nx.DiGraph if directed else nx.Graph)
    elif family == "wheel":
        g = nx.wheel_graph(case[0])
    elif family == "hypercube":
        d = case[0]
        g = nx.hypercube_graph(d)
        relabel = lambda v: v if isinstance(v, int) else sum(  # noqa: E731
            bit << (d - 1 - i) for i, bit in enumerate(v))
    elif family == "circulant":
        g = nx.circulant_graph(case[0], case[1])
    elif family == "de_bruijn":
        k, order = case
        # B(k, 1) is the complete digraph with a loop at every node.
        base = nx.complete_graph(k, create_using=nx.DiGraph)
        base.add_edges_from((v, v) for v in range(k))
        g, words = line_family(base, {v: (v,) for v in range(k)}, order - 1)
        relabel = lambda node: D.debruijn_id(words[node], k)  # noqa: E731
    elif family == "kautz":
        m, order = case
        # K(m, 0) is the complete digraph on m + 1 nodes.
        base = nx.complete_graph(m + 1, create_using=nx.DiGraph)
        g, words = line_family(base, {v: (v,) for v in range(m + 1)}, order)
        relabel = lambda node: D.kautz_id(words[node], m)  # noqa: E731
    else:
        raise ValueError(family)
    mapping = relabel or (lambda v: v)
    edges = [(mapping(a), mapping(b)) for a, b in g.edges()]
    return g.number_of_nodes(), D.normalize(edges, g.is_directed())


def compute(engine):
    out = []
    for case in D.cases(engine["family"]):
        out += D.pack(*build(engine["family"], bool(engine.get("directed")), case))
    return out


def main() -> None:
    spec = load_area("implicit")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            if "only_on" in v["oracles"][ORACLE] and name not in v["oracles"][ORACLE]["only_on"]:
                continue
            write_values(ORACLE, name, variant, compute(v["params"]))
            count += 1
    write_version(ORACLE, f"networkx {nx.__version__}")
    print(f"networkx (implicit): wrote {count} golden files")


if __name__ == "__main__":
    main()
