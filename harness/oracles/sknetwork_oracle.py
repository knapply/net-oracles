#!/usr/bin/env python3
# oracle-env: sknetwork
# oracle-entries: sknetwork
"""Golden values from scikit-network (Bonald et al. 2020), whose measures
are written as sparse-matrix computations on the adjacency matrix.

The adjacency matrix is built from the fixture with parallel edges summed
and a self-loop counted once on the diagonal (rows are sources). Calls
are recorded in the manifest's `call` entries.

    ~/oracle-envs/sknetwork/bin/python oracles/sknetwork_oracle.py
"""

from __future__ import annotations

import numpy as np
import sknetwork
from scipy import sparse
from sknetwork.clustering import get_modularity
from sknetwork.path import get_distances
import sknetwork.ranking as ranking
from sknetwork.ranking import HITS, PageRank
from sknetwork.topology import get_connected_components, get_core_decomposition

from tool_common import adjacency, node_rule, run

ORACLE = "sknetwork"


def matrix(fx, *, weighted=False, loops="once", simple=False):
    return sparse.csr_matrix(np.array(adjacency(fx, weighted=weighted, loops=loops,
                                                simple=simple), dtype=float))


def compute(variant: str, spec: dict, fx):
    e = spec["params"]
    fn = e["fn"]
    n = fx.n
    wt = bool(e.get("weighted"))
    if n == 0:
        return None
    if fn == "pagerank" and e.get("directed", True) \
            and not e.get("dangling"):
        a = matrix(fx, weighted=wt)
        pr = PageRank(damping_factor=e["damping"], solver="piteration", n_iter=100000,
                      tol=1e-15)
        kwargs = {}
        if e.get("personalization"):
            w = np.array(node_rule(e["personalization"], n))
            kwargs["weights"] = w / w.sum()
        return [float(x) for x in pr.fit_predict(a, **kwargs)]
    if fn == "hits" and e.get("scale") == "sum":
        a = matrix(fx, weighted=wt)
        h = HITS()
        h.fit(a)
        x = h.scores_row_ if e["which"] == "hubs" else h.scores_col_
        x = np.abs(np.asarray(x, dtype=float))
        return [float(v) for v in x / x.sum()]
    if fn == "closeness" and not wt and e.get("mode") == "out" \
            and e.get("unreachable") == "ignore" and e.get("normalized"):
        a = matrix(fx, simple=True, loops="ignore")
        return [float(v) for v in ranking.Closeness(method="exact").fit_predict(a)]
    if fn == "modularity" and e.get("partition") == "blocks3":
        a = matrix(fx, weighted=wt)
        labels = np.array(node_rule("blocks3", n), dtype=int)
        return [float(get_modularity(a, labels, resolution=e.get("resolution", 1.0)))]
    if fn == "coreness" and e["mode"] == "all":
        a = matrix(fx, loops="ignore")
        return [float(v) for v in get_core_decomposition(a)]
    if fn == "components":
        a = matrix(fx)
        kind = "strong" if fx.directed and e["kind"] == "strong" else "weak"
        lab = get_connected_components(a, connection=kind)
        first: dict = {}
        for v, c in enumerate(lab):
            first.setdefault(int(c), v)
        return [float(first[int(c)]) for c in lab]
    if fn == "distances" and not wt and e["mode"] in ("out", "all"):
        a = matrix(fx, simple=True, loops="ignore")
        if e["mode"] == "all":
            a = a.maximum(a.T)
        out = []
        for s_ in range(n):
            d = np.asarray(get_distances(a, source=s_), dtype=float)
            out.append(tuple(float("inf") if x < 0 else float(x) for x in d))
        return out
    return None


if __name__ == "__main__":
    run(ORACLE, f"scikit-network {sknetwork.__version__}", compute)
