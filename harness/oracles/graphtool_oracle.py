#!/usr/bin/env python3
# oracle-env: graph-tool
# oracle-entries: graphtool
"""Golden values from graph-tool (Peixoto 2014, `peixoto2014graphtool`), the
reference implementation of the nonparametric stochastic block model
(`peixoto2017nonparametric`), run as a black box for the description length
of a partition and the change of it under a node move
(manifest/sbm.yaml, variants with a `graphtool` oracle).

    $NETORACLES_ORACLE_ENVS/graph-tool/bin/python oracles/graphtool_oracle.py

Runs on the heavy runner pool (graph-tool installs only through conda). Every
fixture is read as a multigraph (weights ignored, parallel edges kept) with
the partitions of derived/models.py. The pieces come from
state.entropy() with its terms switched on one at a time, in nats: the
adjacency term, the partition prior, the edge-count prior, and (degree
corrected) the degree prior with the uniform kind, which is the engine's.
A move's change is the entropy of the state after the move minus before,
each built afresh from the partition.
"""

from __future__ import annotations

import graph_tool.all as gt

from tool_common import run  # noqa: I001  (puts  on the path)
from derived.models import blocks, move_target  # noqa: E402

ORACLE = "graphtool"


def compact(labels):
    ids = {}
    return [ids.setdefault(x, len(ids)) for x in labels]


def pieces(fx, labels, dc):
    g = gt.Graph(directed=fx.directed)
    g.add_vertex(fx.n)
    g.add_edge_list(list(zip(fx.src, fx.tgt)))
    b = g.new_vp("int", vals=compact(labels))
    st = gt.BlockState(g, b=b, deg_corr=dc)
    off = dict(adjacency=False, dl=True, partition_dl=False, degree_dl=False, edges_dl=False)
    total = st.entropy(degree_dl_kind="uniform")
    adj = st.entropy(adjacency=True, dl=False)
    part = st.entropy(**{**off, "partition_dl": True})
    edges = st.entropy(**{**off, "edges_dl": True})
    deg = st.entropy(**{**off, "degree_dl": True, "degree_dl_kind": "uniform"}) if dc else 0.0
    return [total, adj, part, edges, deg]


FIT_RUNS = 10


def fit_length(fx, dc):
    """The least description length (uniform degree prior, as the engine's)
    over FIT_RUNS seeded runs of graph-tool's agglomerative minimization,
    each refined by greedy sweeps under the same entropy."""
    import numpy as np
    g = gt.Graph(directed=fx.directed)
    g.add_vertex(fx.n)
    g.add_edge_list(list(zip(fx.src, fx.tgt)))
    ea = dict(degree_dl_kind="uniform")
    best = None
    for run_id in range(FIT_RUNS):
        gt.seed_rng(1000 + run_id)
        gt.openmp_set_num_threads(1)
        found = gt.minimize_blockmodel_dl(g, state_args=dict(deg_corr=dc))
        st = gt.BlockState(g, b=found.get_blocks(), deg_corr=dc)
        prev = st.entropy(**ea)
        for _ in range(100):
            st.mcmc_sweep(beta=np.inf, niter=5, entropy_args=ea)
            now = st.entropy(**ea)
            if prev - now < 1e-9:
                break
            prev = now
        best = min(best, min(prev, now)) if best is not None else min(prev, now)
    return best


def compute(variant, spec, fx):
    e = spec["params"]
    if fx.n < 2 or not fx.src:
        return None
    if e["fn"] == "sbm_fit":
        return [fit_length(fx, e.get("degree_corrected", False))]
    k, dc = e["blocks"], e.get("degree_corrected", False)
    labels = blocks(fx.n, k)
    if e["fn"] == "sbm_description_length":
        return pieces(fx, labels, dc)
    moved = list(labels)
    moved[0] = move_target(labels, k)
    return [pieces(fx, moved, dc)[0] - pieces(fx, labels, dc)[0]]


if __name__ == "__main__":
    run(ORACLE, f"graph-tool {gt.__version__}", compute)
