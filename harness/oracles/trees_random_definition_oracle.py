# oracle-entries: definition
"""Golden values for the random spanning tree sampler
(manifest/trees_random.yaml): the exact distribution of a
random spanning tree, with probability proportional to the product of edge
weights (conductances; 1 for the unweighted reading).

  rst_valid        [1, 1] (checked in the binding)
  rst_edge_freq    P(e in T) = w_e b_e' L+ b_e, with L the weighted Laplacian
                   and L+ its pseudo-inverse (Kirchhoff: the effective
                   resistance of the edge times its conductance); parallel
                   edges add to L and are separate edges, loops never occur
  rst_pair_freq    P(e, f in T) = Y_ee Y_ff - Y_ef^2 for the transfer
                   current Y_ef = sqrt(w_e w_f) b_e' L+ b_f (Burton and
                   Pemantle 1993: the spanning tree is a determinantal
                   process)
  rst_chi_square   [1e-4]: the p-value of Pearson's goodness-of-fit test of
                   the drawn trees against the enumerated distribution
                   (computed in the binding with the enumeration below)
                   must be at least 1e-4, on networks with at most 3000
                   trees

    python3 oracles/trees_random_definition_oracle.py
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
MAX_TREES = 3000


def weights(fx, weighted):
    return list(fx.weights) if weighted and fx.weights is not None else [1.0] * len(fx.src)


def connected(fx):
    parent = list(range(fx.n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b in zip(fx.src, fx.tgt):
        parent[find(a)] = find(b)
    return len({find(v) for v in range(fx.n)}) == 1


def usable(fx):
    return fx.n >= 2 and not fx.directed and connected(fx)


def laplacian_pinv(fx, w):
    n = fx.n
    lap = np.zeros((n, n))
    for a, b, x in zip(fx.src, fx.tgt, w):
        if a != b:
            lap[a, a] += x
            lap[b, b] += x
            lap[a, b] -= x
            lap[b, a] -= x
    return np.linalg.pinv(lap)


def transfer_current(fx, w):
    """Y[e][f] = sqrt(w_e w_f) b_e' L+ b_f over the edges (zero rows for
    loops)."""
    lp = laplacian_pinv(fx, w)
    m = len(fx.src)
    b = np.zeros((m, fx.n))
    for e, (s, t) in enumerate(zip(fx.src, fx.tgt)):
        if s != t:
            b[e, s], b[e, t] = 1.0, -1.0
    sw = np.sqrt(np.array(w))
    return (b @ lp @ b.T) * np.outer(sw, sw)


def edge_probabilities(fx, weighted):
    return [float(x) for x in np.diag(transfer_current(fx, weights(fx, weighted)))]


def pair_probabilities(fx, weighted):
    y = transfer_current(fx, weights(fx, weighted))
    first = min(8, len(fx.src))
    return [float(y[i, i] * y[j, j] - y[i, j] ** 2)
            for i in range(first) for j in range(i + 1, first)]


def tree_count(fx):
    n = fx.n
    lap = np.zeros((n, n))
    for a, b in zip(fx.src, fx.tgt):
        if a != b:
            lap[a, a] += 1
            lap[b, b] += 1
            lap[a, b] -= 1
            lap[b, a] -= 1
    return round(np.linalg.det(lap[1:, 1:]))


def enumerable(fx):
    return usable(fx) and 2 <= tree_count(fx) <= MAX_TREES and len(fx.src) <= 22


def tree_probabilities(fx, weighted=False):
    """Every spanning tree (a sorted tuple of edge positions) with its
    probability, by testing each subset of n - 1 edges."""
    w = weights(fx, weighted)
    out = {}
    for subset in itertools.combinations(range(len(fx.src)), fx.n - 1):
        parent = list(range(fx.n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        ok = True
        for e in subset:
            a, b = find(fx.src[e]), find(fx.tgt[e])
            if a == b:
                ok = False
                break
            parent[a] = b
        if ok:
            out[subset] = float(np.prod([w[e] for e in subset]))
    total = sum(out.values())
    return {t: p / total for t, p in out.items()}


def compute(fx, spec):
    fn, weighted = "rst_" + spec["stat"], spec.get("weighted", False)
    if not usable(fx):
        return []
    if fn == "rst_valid":
        return [1, 1]
    if fn == "rst_edge_freq":
        return edge_probabilities(fx, weighted)
    if fn == "rst_pair_freq":
        return pair_probabilities(fx, weighted)
    if fn == "rst_chi_square":
        # The engine's draws must pass Pearson's test at level 1e-4: its
        # p-value at least this (compare: ge).
        return [1e-4] if enumerable(fx) else []
    raise ValueError(fn)


def main() -> None:
    spec = load_area("trees_random")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (random spanning trees): wrote {count} golden files")


if __name__ == "__main__":
    main()
