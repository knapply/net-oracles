#!/usr/bin/env python3
"""igraph through its Python interface (tool id pyigraph), one thread."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# An adapter named like its tool (networkx.py) must not shadow the tool itself.
sys.path[:] = [p for p in sys.path if os.path.abspath(p or ".") != HERE]
sys.path.insert(0, os.path.join(HERE, ".."))
from common import Adapter, main, sig, vec  # noqa: E402


def _mean(xs):
    return sum(xs) / max(len(xs), 1)


class PyIgraph(Adapter):
    tool = "pyigraph"

    def __init__(self):
        import igraph as ig
        self.ig = ig
        self.calls = {
            "bfs": lambda G, c: {"reached": len(G.bfs(c.sources[0])[0])},
            "components": lambda G, c: {"components": len(G.connected_components(mode="weak"))},
            "pagerank": lambda G, c: vec(G.pagerank(damping=0.85)),
            "triangles": lambda G, c: {"clustering_mean": sig(_mean(G.transitivity_local_undirected(mode="zero")))},
            "betweenness": lambda G, c: {"sum": sig(sum(G.betweenness(sources=c.sources, directed=c.directed)))},
            "closeness": lambda G, c: vec(G.closeness()),
        }

    def version(self):
        return self.ig.__version__

    def load(self, ctx):
        return self.ig.Graph(n=ctx.n, edges=ctx.edges, directed=ctx.directed)


if __name__ == "__main__":
    main(PyIgraph)
