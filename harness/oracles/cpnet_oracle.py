#!/usr/bin/env python3
# oracle-env: cpnet
# oracle-entries: cpnet
"""Core-periphery assignments from cpnet (Kojaku and Masuda 2017, 2018),
run as a black box, scored with the definition oracle's objectives.

cpnet's algorithms are heuristics, so each one gives a feasible solution,
not the optimum, and the engine must do at least as well on the engine's own
objective:

- `core_periphery*_vs_cpnet`: Borgatti and Everett's (2000) discrete
  model. cpnet's BE core set (computed on the undirected, unweighted,
  loop-free network) is scored by the correlation between the observed
  values and the ideal pattern, for the link convention of the entry
  (missing | ones | zeros) and the observed values it uses (weighted or
  not). The engine's best correlation must be at least that.
- `core_periphery_minres_vs_cpnet`: the least residual sum of squares
  sum (a_ij - c_i c_j)^2 over non-negative coreness vectors. The coreness
  vectors of cpnet's continuous algorithms (MINRES, Rombach, Rossa; those
  the installed version provides) are feasible, and the smallest residual
  among them is written. The engine's residual must be at most that.

A value of -1 means no defined correlation (fewer than two pairs, or an
observed or ideal pattern that does not vary), as the engine reports it.

    ~/oracle-envs/cpnet/bin/python oracles/cpnet_oracle.py
"""

from __future__ import annotations

import importlib.metadata

import cpnet
import networkx as nx
import numpy as np

import groups_definition_oracle as defn
from tool_common import run

ORACLE = "cpnet"


def plain_graph(fx):
    g = nx.Graph()
    g.add_nodes_from(range(fx.n))
    g.add_edges_from((a, b) for a, b in zip(fx.src, fx.tgt) if a != b)
    return g


def be_core(fx):
    alg = cpnet.BE()
    alg.detect(plain_graph(fx))
    x = alg.get_coreness()
    return np.array([x[v] >= 0.5 for v in range(fx.n)])


def correlation(fx, core, links, weighted):
    a, mask = defn.value_matrix(fx, weighted)
    if fx.n < 2 or np.var(a[mask]) == 0:
        return -1.0
    both = np.outer(core, core)
    neither = np.outer(~core, ~core)
    if links == "missing":
        keep = mask & (both | neither)
        d = both[keep].astype(float)
    elif links == "ones":
        keep = mask
        d = (~neither)[keep].astype(float)
    else:
        keep = mask
        d = both[keep].astype(float)
    x = a[keep]
    if len(x) < 2 or np.var(x) == 0 or np.var(d) == 0:
        return -1.0
    return float(np.corrcoef(x, d)[0, 1])


def coreness_vectors(fx):
    g = plain_graph(fx)
    out = []
    for name in ("MINRES", "Rombach", "Rossa"):
        cls = getattr(cpnet, name, None)
        if cls is None:
            continue
        try:
            alg = cls()
            alg.detect(g)
            x = alg.get_coreness()
            c = np.array([float(x[v]) for v in range(fx.n)])
            if np.all(np.isfinite(c)) and np.all(c >= 0):
                out.append(c)
        except Exception:  # an algorithm that rejects this network is skipped
            continue
    return out


def residual(fx, c, weighted):
    a, mask = defn.value_matrix(fx, weighted)
    r = a[mask] - np.outer(c, c)[mask]
    return float(r @ r)


def compute(variant: str, spec: dict, fx):
    e = spec["params"]
    weighted = bool(e.get("weighted", False))
    if fx.n < 2:
        return [-1.0]
    if e["fn"] == "core_periphery":
        if not any(a != b for a, b in zip(fx.src, fx.tgt)):
            return [-1.0]
        return [correlation(fx, be_core(fx), e.get("links", "missing"), weighted)]
    a, mask = defn.value_matrix(fx, weighted)
    if np.var(a[mask]) == 0:
        return [-1.0]
    best = [residual(fx, c, weighted) for c in coreness_vectors(fx)]
    return [min(best)] if best else None


if __name__ == "__main__":
    run(ORACLE, f"cpnet {importlib.metadata.version('cpnet')}", compute)
