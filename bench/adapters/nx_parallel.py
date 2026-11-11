#!/usr/bin/env python3
"""NetworkX with the nx-parallel backend (joblib); every CPU offered unless --threads is set."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# An adapter named like its tool (networkx.py) must not shadow the tool itself.
sys.path[:] = [p for p in sys.path if os.path.abspath(p or ".") != HERE]
sys.path.insert(0, os.path.join(HERE, ".."))
from common import main  # noqa: E402
from nxbase import NetworkXBase  # noqa: E402


class NxParallel(NetworkXBase):
    tool = "nx-parallel"
    package = "nx-parallel"
    backend = 'parallel'

    def threads(self, requested):
        import os
        n = requested or len(os.sched_getaffinity(0))
        os.environ["NX_PARALLEL_N_JOBS"] = str(n)
        import networkx as nx
        try:
            nx.config.backends.parallel.active = True
            nx.config.backends.parallel.n_jobs = n
        except AttributeError:
            pass
        return n


if __name__ == "__main__":
    main(NxParallel)
