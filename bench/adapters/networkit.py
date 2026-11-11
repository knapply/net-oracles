#!/usr/bin/env python3
"""NetworKit (https://networkit.github.io), C++ core with OpenMP; every CPU offered unless --threads is set."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# An adapter named like its tool (networkx.py) must not shadow the tool itself.
sys.path[:] = [p for p in sys.path if os.path.abspath(p or ".") != HERE]
sys.path.insert(0, os.path.join(HERE, ".."))
from common import Adapter, main, sig, vec  # noqa: E402


def _mean(xs):
    return sum(xs) / max(len(xs), 1)


class NetworKit(Adapter):
    tool = "networkit"
    note = ""

    def __init__(self):
        import networkit as nk
        self.nk = nk

        def components(G, c):
            cc = (nk.components.WeaklyConnectedComponents(G) if c.directed else nk.components.ConnectedComponents(G))
            cc.run()
            return {"components": cc.numberOfComponents()}

        def pagerank(G, c):
            pr = nk.centrality.PageRank(G, damp=0.85, tol=1e-6)
            if hasattr(pr, "maxIterations"):
                pr.maxIterations = 100
            pr.run()
            return vec(pr.scores())

        def closeness(G, c):
            cv = nk.centrality.ClosenessVariant
            cl = nk.centrality.Closeness(G, False, getattr(cv, "GENERALIZED", None) or cv.Generalized)
            cl.run()
            return vec(cl.scores())

        self.calls = {
            "bfs": self._bfs,
            "components": components,
            "pagerank": pagerank,
            "triangles": lambda G, c: {"clustering_mean": sig(_mean(nk.centrality.LocalClusteringCoefficient(G, turbo=True).run().scores()))},
            # random pivots: not the same sources as the exact tools
            "betweenness": lambda G, c: {"sum_sampled": sig(sum(nk.centrality.EstimateBetweenness(G, len(c.sources), False, True).run().scores()))},
            "closeness": closeness,
        }

    def _bfs(self, G, c):
        b = self.nk.distance.BFS(G, c.sources[0], storePaths=False)
        b.run()
        return {"ran": 1}

    def version(self):
        return self.nk.__version__

    def threads(self, requested):
        if requested:
            self.nk.setNumberOfThreads(requested)
        return self.nk.getMaxNumberOfThreads()

    def load(self, ctx):
        import numpy as np
        nk = self.nk
        G = nk.Graph(ctx.n, weighted=False, directed=ctx.directed)
        a = np.ascontiguousarray(ctx.edges[:, 0], dtype=np.uint64)
        b = np.ascontiguousarray(ctx.edges[:, 1], dtype=np.uint64)
        try:
            G.addEdges((a, b))
        except TypeError:
            G.addEdges((np.ones(len(a)), (a, b)))
        return G


if __name__ == "__main__":
    main(NetworKit)
