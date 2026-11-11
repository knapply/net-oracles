#!/usr/bin/env python3
"""Definition oracle for graph matrices and the Fiedler vector (see
../bindings/graph_matrices.py for the encodings).

Matrices are built entry by entry from the edge list with exact fractions:
A[u][v] adds w for every edge (and A[v][u] for undirected edges between
distinct nodes; an undirected self-loop is one diagonal entry w), the
Laplacian D - A with D the row sums, the normalized Laplacian
D^-1/2 (D - A) D^-1/2 (0 for zero degrees), the incidence matrix with a
column per edge (w at both ends, or -w at the source when oriented;
self-loops empty), the Bethe Hessian (r^2 - 1) I - r A + D with
r = sum d^2 / sum d - 1 (degrees counting a self-loop twice), and the
modularity matrix A - k k'/2m (A - k_out k_in'/m for directed graphs).
The Fiedler pair comes from NumPy's dense symmetric eigensolver applied to
the Laplacian of the graph with absolute weights summed over parallel edges
and both directions, self-loops dropped.

    python3 oracles/graph_matrices_definition_oracle.py
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
GAP = 1e-6


def weights(fx, weighted):
    return [Fraction(fx.weights[i]) if weighted else Fraction(1) for i in range(len(fx.src))]


def adjacency(fx, weighted):
    n = fx.n
    A = [[Fraction(0)] * n for _ in range(n)]
    for (a, b), w in zip(zip(fx.src, fx.tgt), weights(fx, weighted)):
        A[a][b] += w
        if not fx.directed and a != b:
            A[b][a] += w
    return A


def flat(M):
    return [float(x) for row in M for x in row]


def laplacian(fx, weighted, normalized):
    A = adjacency(fx, weighted)
    n = fx.n
    d = [sum(row) for row in A]
    L = [[(d[i] if i == j else 0) - A[i][j] for j in range(n)] for i in range(n)]
    if not normalized:
        return flat(L)
    h = [0.0 if d[i] == 0 else 1.0 / math.sqrt(d[i]) for i in range(n)]
    return [h[i] * float(L[i][j]) * h[j] for i in range(n) for j in range(n)]


def incidence(fx, weighted, oriented):
    m = len(fx.src)
    B = [[Fraction(0)] * m for _ in range(fx.n)]
    for e, ((a, b), w) in enumerate(zip(zip(fx.src, fx.tgt), weights(fx, weighted))):
        if a == b:
            continue
        B[a][e] = -w if oriented else w
        B[b][e] = w
    return flat(B)


def bethe(fx, weighted):
    if not fx.src:
        return [-999.0]
    deg = [0] * fx.n
    for a, b in zip(fx.src, fx.tgt):
        deg[a] += 1
        deg[b] += 1
    r = Fraction(sum(x * x for x in deg), sum(deg)) - 1
    A = adjacency(fx, weighted)
    d = [sum(row) for row in A]
    n = fx.n
    return flat([[((r * r - 1) + d[i] if i == j else 0) - r * A[i][j] for j in range(n)]
                 for i in range(n)])


def modularity(fx, weighted):
    A = adjacency(fx, weighted)
    n = fx.n
    kout = [sum(row) for row in A]
    kin = [sum(A[i][j] for i in range(n)) for j in range(n)]
    if fx.directed:
        m = sum(kin)
        left, right, den = kout, kin, m
    else:
        left, right, den = kout, kout, sum(kout)
    out = []
    for i in range(n):
        for j in range(n):
            out.append(-999.0 if den == 0 else float(A[i][j] - left[i] * right[j] / den))
    return out


def fiedler(fx, weighted, normalized, output):
    n = fx.n
    if n < 2:
        return [-999.0]
    W = np.zeros((n, n))
    for (a, b), w in zip(zip(fx.src, fx.tgt), weights(fx, weighted)):
        if a != b:
            W[a, b] += abs(float(w))
            W[b, a] += abs(float(w))
    d = W.sum(axis=1)
    # Connected?
    seen, stack = {0}, [0]
    while stack:
        v = stack.pop()
        for u in np.nonzero(W[v])[0]:
            if int(u) not in seen:
                seen.add(int(u))
                stack.append(int(u))
    if len(seen) < n:
        return [0.0] if output == "value" else [-999.0]
    L = np.diag(d) - W
    if normalized:
        h = 1 / np.sqrt(d)
        L = h[:, None] * L * h[None, :]
    vals, vecs = np.linalg.eigh(L)
    if output == "value":
        return [vals[1]]
    if n > 2 and not vals[2] - vals[1] > GAP * max(1.0, abs(vals[2])):
        return [-999.0]
    return list(signed(vecs[:, 1]))


# Entries at most this fraction of the largest |entry| count as zero when
# the Fiedler vector's sign is chosen (the engine's SIGN_TIE).
SIGN_TIE = 1e-9


def signed(v):
    """Unit vector whose first entry above SIGN_TIE times the largest
    |entry| is negative: NetworkX's sign (first entry negative) unless that
    entry is zero, whose computed value is a rounding residue."""
    x = v / np.linalg.norm(v)
    top = np.abs(x).max()
    first = next((e for e in x if abs(e) > SIGN_TIE * top), 0.0)
    return -x if first > 0 else x


def aperiodic(fx):
    n = fx.n
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    for a, b in zip(fx.src, fx.tgt):
        adj[a].append(b)
        radj[b].append(a)

    def levels(nbrs):
        lev = {0: 0}
        queue = [0]
        for v in queue:
            for w in nbrs[v]:
                if w not in lev:
                    lev[w] = lev[v] + 1
                    queue.append(w)
        return lev

    if n == 0 or len(levels(adj)) < n or len(levels(radj)) < n:
        return [-999.0]
    # Aperiodic iff some power of the adjacency matrix is positive
    # (primitive); Wielandt's bound n^2 - 2n + 2 on the exponent.
    A = np.zeros((n, n), dtype=bool)
    for a, b in zip(fx.src, fx.tgt):
        A[a, b] = True
    P = A.copy()
    for _ in range(n * n - 2 * n + 2):
        if P.all():
            return [1.0]
        P = (P.astype(np.int64) @ A.astype(np.int64)) > 0
    return [1.0 if P.all() else 0.0]


def compute(fx, e):
    fn = e["fn"]
    w = bool(e.get("weighted"))
    if fn == "gm_adjacency":
        return flat(adjacency(fx, w))
    if fn == "gm_laplacian":
        return laplacian(fx, w, bool(e.get("normalized")))
    if fn == "gm_incidence":
        return incidence(fx, w, bool(e.get("oriented")))
    if fn == "gm_bethe_hessian":
        return bethe(fx, w)
    if fn == "gm_modularity":
        return modularity(fx, w)
    if fn == "gm_fiedler":
        return fiedler(fx, w, bool(e.get("normalized")), e.get("output", "value"))
    if fn == "gm_aperiodic":
        return aperiodic(fx)
    if fn == "gm_class_matrix":
        M = [[Fraction(0)] * 3 for _ in range(3)]
        for (a, b), x in zip(zip(fx.src, fx.tgt), weights(fx, w)):
            M[a % 3][b % 3] += x
            if not fx.directed and a % 3 != b % 3:
                M[b % 3][a % 3] += x
        return flat(M)
    raise ValueError(fn)


def main() -> None:
    spec = load_area("graph_matrices")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (graph_matrices): wrote {count} golden files")


if __name__ == "__main__":
    main()
