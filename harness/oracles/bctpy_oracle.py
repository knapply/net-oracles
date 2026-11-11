#!/usr/bin/env python3
# oracle-env: bctpy
# oracle-entries: bctpy
"""Golden values from bctpy (the Python port of the Brain Connectivity
Toolbox, Rubinov and Sporns 2010), which works on dense connection
matrices.

BCT functions assume a matrix without self-connections, so the diagonal
is cleared. Binary measures get the 0/1 matrix (parallel edges collapsed);
weighted measures get summed weights (strength measures) or, for path
lengths, the shortest of any parallel edges as a length matrix. Calls are
recorded in the manifest's `call` entries.

    ~/oracle-envs/bctpy/bin/python oracles/bctpy_oracle.py
"""

from __future__ import annotations

import importlib.metadata
import math

import bct
import numpy as np

from tool_common import adjacency, run, simple_edges

ORACLE = "bctpy"


def binary(fx):
    a = np.array(adjacency(fx, loops="ignore", simple=True))
    return a


def symmetric(fx):
    """The undirected binary reading (the engine's reading of a directed
    network for clustering and transitivity)."""
    a = binary(fx)
    return np.maximum(a, a.T)


def summed(fx):
    return np.array(adjacency(fx, weighted=True, loops="ignore"))


def lengths(fx):
    n = fx.n
    a = np.zeros((n, n))
    for u, v, w in simple_edges(fx, keep="min"):
        a[u, v] = w
        if not fx.directed:
            a[v, u] = w
    return a


def vec(x):
    return [float(v) for v in np.asarray(x, dtype=float).reshape(-1)]


def compute(variant: str, spec: dict, fx):
    e = spec["params"]
    fn = e["fn"]
    n = fx.n
    wt = bool(e.get("weighted"))
    if n == 0:
        return None
    if fn == "clustering" and (not fx.directed or e.get("weighting") == "none"):
        if e.get("weighting") == "none" and e.get("undefined") == "zero":
            return vec(bct.clustering_coef_bu(symmetric(fx)))
        if e.get("weighting") == "onnela":
            w = summed(fx)
            top = w.max()
            return vec(bct.clustering_coef_wu(w / top if top else w))
        return None
    if fn == "average_clustering" and e.get("undefined") == "zero" \
            and (not fx.directed or e.get("weighting") == "none"):
        if e.get("weighting") == "none":
            return [float(np.mean(bct.clustering_coef_bu(symmetric(fx))))]
        if e.get("weighting") == "onnela":
            w = summed(fx)
            top = w.max()
            return [float(np.mean(bct.clustering_coef_wu(w / top if top else w)))]
        return None
    if fn == "nxo_directed_clustering" and fx.directed:
        if wt:
            w = summed(fx)
            top = w.max()
            return vec(bct.clustering_coef_wd(w / top if top else w))
        return vec(bct.clustering_coef_bd(binary(fx)))
    if fn == "transitivity" and e.get("undefined") == "zero":
        return [float(bct.transitivity_bu(symmetric(fx)))]
    if fn == "dm_index" and e["index"] == "global_efficiency":
        if wt:
            # BCT reads weights as strengths (length 1 / w); the engine's
            # weights are lengths, so BCT gets their reciprocals.
            ln = lengths(fx)
            inv = np.divide(1.0, ln, out=np.zeros_like(ln), where=ln > 0)
            return [float(bct.efficiency_wei(inv, local=False))]
        return [float(bct.efficiency_bin(binary(fx), local=False))]
    if fn == "dm_local_efficiency" and not fx.directed:
        return [float(np.mean(bct.efficiency_bin(binary(fx), local=True)))]
    if fn == "betweenness" and not e.get("weights_as") and not e.get("normalized"):
        b = bct.betweenness_wei(lengths(fx)) if wt else bct.betweenness_bin(binary(fx))
        # BCT counts ordered pairs, so each undirected pair twice.
        return vec(b) if fx.directed else vec(np.asarray(b) / 2)
    if fn == "distances" and e["mode"] == "out" and not e.get("weights_as"):
        d = bct.distance_wei(lengths(fx))[0] if wt else bct.distance_bin(binary(fx))
        d = np.asarray(d, dtype=float)
        np.fill_diagonal(d, 0.0)
        return [tuple(float(x) for x in row) for row in d]
    if fn in ("mean_distance", "diameter", "radius", "eccentricity") \
            and e.get("mode") in ("out", "all") and not (fx.directed and e["mode"] == "all"):
        d = bct.distance_wei(lengths(fx))[0] if wt else bct.distance_bin(binary(fx))
        d = np.asarray(d, dtype=float)
        lam, eff, ecc, radius, diameter = bct.charpath(d, include_diagonal=False,
                                                       include_infinite=False)
        if fn == "mean_distance" and e.get("unconnected"):
            return [float(lam)]
        if fn == "diameter" and e.get("unconnected"):
            return [float(diameter)]
        if fn == "radius":
            return [float(radius)]
        if fn == "eccentricity":
            return vec(ecc)
        return None
    if fn == "density" and not e.get("loops") and e.get("simple"):
        a = binary(fx)
        f = bct.density_dir if fx.directed else bct.density_und
        return [float(f(a)[0])]
    if fn == "coreness" and e["mode"] == "all":
        return vec(bct.kcoreness_centrality_bu(symmetric(fx))[0])
    if fn == "assort" and e.get("coefficient") == "degree" and not e.get("subset") \
            and not fx.directed and not e.get("x"):
        if wt:
            return [float(bct.assortativity_wei(summed(fx), flag=0))]
        return [float(bct.assortativity_bin(binary(fx), flag=0))]
    return None


if __name__ == "__main__":
    run(ORACLE, f"bctpy {importlib.metadata.version('bctpy')}", compute)
