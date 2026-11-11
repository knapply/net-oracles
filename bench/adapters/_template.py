#!/usr/bin/env python3
"""TOOL NAME (homepage), implementation language, threading. Copy to adapters/<tool>.py."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# An adapter named like its tool must not shadow the tool itself.
sys.path[:] = [p for p in sys.path if os.path.abspath(p or ".") != HERE]
sys.path.insert(0, os.path.join(HERE, ".."))
from common import Adapter, main, sig, vec  # noqa: E402


class Template(Adapter):
    tool = "tool-id"  # as in data/tools.json

    def __init__(self):
        import yourtool as t  # imported here so that `--list` and the runner can tell it is missing
        self.t = t
        self.calls = {
            # "bfs": lambda G, c: {"reached": len(t.bfs(G, c.sources[0]))},
            # "components": lambda G, c: {"components": t.n_components(G)},
            # "pagerank": lambda G, c: vec(t.pagerank(G, damping=0.85, tol=1e-6, max_iter=100)),
        }

    def version(self):
        return self.t.__version__

    def threads(self, requested):
        return 1  # or set the tool's thread count (0 = every CPU offered) and return the number used

    def load(self, ctx):
        return self.t.Graph(ctx.n, ctx.edges, directed=ctx.directed)


if __name__ == "__main__":
    main(Template)
