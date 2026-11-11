#!/usr/bin/env python3
"""graph-tool (https://graph-tool.skewed.de), C++ core with OpenMP. Set GRAPH_TOOL_PY to run it
under another interpreter (for example the one of a container image); the runner does that."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# An adapter named like its tool (networkx.py) must not shadow the tool itself.
sys.path[:] = [p for p in sys.path if os.path.abspath(p or ".") != HERE]
sys.path.insert(0, os.path.join(HERE, ".."))
from common import Adapter, main, sig, vec  # noqa: E402


class GraphTool(Adapter):
    tool = "graphtool"

    def __init__(self):
        import graph_tool.all as gt
        self.gt = gt

        def components(G, c):
            _, hist = gt.label_components(G, directed=False)
            return {"components": len(hist)}

        self.calls = {
            "bfs": lambda G, c: {"reached": int(sum(1 for d in gt.shortest_distance(G, source=G.vertex(c.sources[0])).a if d < 2**31 - 1))},
            "components": components,
            "pagerank": lambda G, c: vec(gt.pagerank(G, damping=0.85, epsilon=1e-6, max_iter=100).a),
            "triangles": lambda G, c: {"clustering_mean": sig(float(gt.local_clustering(G, undirected=True).a.mean()))},
            "betweenness": lambda G, c: {"sum": sig(float(gt.betweenness(G, pivots=[G.vertex(s) for s in c.sources])[0].a.sum()))},
            "closeness": lambda G, c: vec(gt.closeness(G).a),
        }

    def version(self):
        return self.gt.__version__.split()[0]

    def threads(self, requested):
        if requested:
            self.gt.openmp_set_num_threads(requested)
        return self.gt.openmp_get_num_threads()

    def load(self, ctx):
        G = self.gt.Graph(directed=ctx.directed)
        G.add_vertex(ctx.n)
        G.add_edge_list(ctx.edges)
        return G


if __name__ == "__main__":
    main(GraphTool)
