# oracle-entries: definition
"""Golden values for the microcanonical stochastic block model, computed
directly from the definitions of Peixoto (2017).

Every fixture is read as a multigraph (weights ignored, parallel edges with
multiplicity; an undirected loop adds 2 to A_ii and to the degree, a
directed loop 1 to A_ii and to both degrees) with the partitions of
derived/models.py. The oracle builds the dense adjacency matrix
A and the dense block matrix e_rs (e_rr twice the internal edges when
undirected) and evaluates

  -ln P(A|e,b)   = -sum_{r<s} ln e_rs! - sum_r ln e_rr!! + sum_r e_r ln n_r
                   + sum_{i<j} ln A_ij! + sum_i ln A_ii!!
  -ln P(A|k,e,b) = the same with sum_r ln e_r! - sum_i ln k_i! in place of
                   the n_r terms
  -ln P(e)       = ln ((B(B+1)/2, E))        (B^2 when directed)
  -ln P(b)       = ln C(N-1, B-1) + ln N! - sum_r ln n_r! + ln N
  -ln P(k|e,b)   = sum_r ln ((n_r, e_r))     (degree-corrected only)

(directed networks: ordered block pairs and all ordered node pairs,
n_r^(e_r+ + e_r-), e_r+! e_r-!, and both degree sums in the degree prior)
with math.lgamma. The engine instead keeps hash-map rows of e_rs and
evaluates sums over non-empty entries; its move deltas touch only the
changed entries, while the oracle recomputes the whole description length
after the move and subtracts.

    python3 oracles/sbm_definition_oracle.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)
from derived.models import blocks, move_target  # noqa: E402

ORACLE = "definition"


def lf(x):
    return math.lgamma(x + 1.0)


def lbinom(n, k):
    return lf(n) - lf(k) - lf(n - k)


def lmulti(n, k):
    return 0.0 if k == 0 else lbinom(n + k - 1, k)


def ldfact_even(x):
    """ln x!! for even x = 2m: m ln 2 + ln m!."""
    return x / 2 * math.log(2) + lf(x / 2)


def description_length(fx, labels, dc):
    n, d = fx.n, fx.directed
    if n == 0:
        return [0.0] * 5
    ids = {}
    b = np.array([ids.setdefault(x, len(ids)) for x in labels])
    nb = len(ids)
    A = np.zeros((n, n))
    for s, t in zip(fx.src, fx.tgt):
        A[s, t] += 1
        if not d:
            A[t, s] += 1  # a loop adds 2 to A_ii
    kout = A.sum(axis=1)
    kin = A.sum(axis=0) if d else np.zeros(n)
    Z = np.zeros((nb, n))
    Z[b, np.arange(n)] = 1
    E = Z @ A @ Z.T
    size = Z.sum(axis=1)
    er_out, er_in = Z @ kout, Z @ kin
    adj = 0.0
    for r in range(nb):
        for s in range(nb):
            if d or r < s:
                adj -= lf(E[r, s])
            elif r == s:
                adj -= ldfact_even(E[r, r])
    for i in range(n):
        for j in range(n):
            if d or i < j:
                adj += lf(A[i, j])
            elif i == j:
                adj += ldfact_even(A[i, i])
    deg = 0.0
    for r in range(nb):
        if dc:
            adj += lf(er_out[r]) + (lf(er_in[r]) if d else 0.0)
            deg += lmulti(size[r], er_out[r]) + (lmulti(size[r], er_in[r]) if d else 0.0)
        else:
            adj += (er_out[r] + er_in[r]) * math.log(size[r])
    if dc:
        adj -= sum(lf(k) for k in kout) + (sum(lf(k) for k in kin) if d else 0.0)
    m = len(fx.src)
    pairs = nb * nb if d else nb * (nb + 1) // 2
    edges = lmulti(pairs, m)
    part = lbinom(n - 1, nb - 1) + lf(n) + math.log(n) - sum(lf(x) for x in size)
    return [adj + part + edges + deg, adj, part, edges, deg]


def compute(fx, spec):
    k, dc = spec["blocks"], spec.get("degree_corrected", False)
    labels = blocks(fx.n, k)
    if spec["fn"] == "sbm_description_length":
        return description_length(fx, labels, dc)
    if fx.n == 0:
        return []
    moved = list(labels)
    moved[0] = move_target(labels, k)
    return [description_length(fx, moved, dc)[0] - description_length(fx, labels, dc)[0]]


def main() -> None:
    spec = load_area("sbm")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (sbm): wrote {count} golden files")


if __name__ == "__main__":
    main()
