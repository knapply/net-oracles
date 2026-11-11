#!/usr/bin/env python3
"""Definition oracle for graph matrices and spectra (manifest/
spectral_matrices.yaml; encodings as in ../bindings/spectral_matrices.py).

Matrices common with the capi entries (adjacency, Laplacians, incidence,
modularity) come from graph_matrices_definition_oracle.py (exact fractions).
New here, from the definitions:

  signless        Q = D + A, D the row sums of A (a loop once)
  transition      D^-1 A, a row without weight stays 0
  non_backtracking  the Hashimoto operator: arcs numbered by edge (an
                  undirected edge e gives arc 2e: source -> target and
                  2e + 1: target -> source), 1 from u -> v to v -> w, w != u
  ihara           the Ihara-Bass side: [1, log] of (1 - u^2)^(m - n)
                  det(I - u A + u^2 (D - I)) at u = 0.1, 0.2 (sign, log of
                  the absolute value), for simple undirected networks
  spectra         numpy's symmetric eigensolver (LAPACK) on the matrices
                  above, increasing

    python3 oracles/spectral_matrices_definition_oracle.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import graph_matrices_definition_oracle as gmd  # noqa: E402
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
U_VALUES = (0.1, 0.2)
CAPI = {"adjacency": ("gm_adjacency", {}), "laplacian": ("gm_laplacian", {}),
        "normalized_laplacian": ("gm_laplacian", {"normalized": True}),
        "incidence": ("gm_incidence", {}),
        "oriented_incidence": ("gm_incidence", {"oriented": True}),
        "modularity": ("gm_modularity", {})}


def simple_undirected(fx):
    if fx.directed or fx.n == 0:
        return False
    pairs = [frozenset((a, b)) for a, b in zip(fx.src, fx.tgt)]
    return all(len(p) == 2 for p in pairs) and len(set(pairs)) == len(pairs)


def dense(fx, kind, weighted):
    """The matrix as a numpy array, from the fraction-based builders."""
    n = fx.n
    A = gmd.adjacency(fx, weighted)
    d = [sum(row) for row in A]
    if kind in ("signless", "signless_laplacian"):
        return gmd.flat([[(d[i] if i == j else 0) + A[i][j] for j in range(n)] for i in range(n)])
    if kind == "transition":
        return gmd.flat([[(A[i][j] / d[i] if d[i] != 0 else 0) for j in range(n)]
                         for i in range(n)])
    fn, extra = CAPI[kind]
    return gmd.compute(fx, dict({"fn": fn, "weighted": weighted}, **extra))


def non_backtracking(fx):
    tail, head = [], []
    for a, b in zip(fx.src, fx.tgt):
        tail.append(a)
        head.append(b)
        if not fx.directed:
            tail.append(b)
            head.append(a)
    k = len(tail)
    out = [0.0] * (k * k)
    for i in range(k):
        for j in range(k):
            if tail[j] == head[i] and head[j] != tail[i]:
                out[i * k + j] = 1.0
    return out


def ihara(fx):
    if not simple_undirected(fx):
        return []
    n, m = fx.n, len(fx.src)
    A = np.zeros((n, n))
    for a, b in zip(fx.src, fx.tgt):
        A[a][b] = A[b][a] = 1.0
    D = np.diag(A.sum(axis=1))
    out = []
    for u in U_VALUES:
        sign, logabs = np.linalg.slogdet(np.eye(n) - u * A + u * u * (D - np.eye(n)))
        factor = 1.0 - u * u
        out += [float(sign * (1 if factor > 0 or (m - n) % 2 == 0 else -1)),
                float(logabs + (m - n) * math.log(abs(factor)))]
    return out


def spectrum(fx, kind, weighted):
    if fx.n == 0 or (kind == "modularity" and not fx.src):
        return []
    if kind == "normalized_laplacian" and weighted and fx.weighted and any(w < 0 for w in fx.weights):
        return []
    flat = np.array(dense(fx, kind, weighted), dtype=float).reshape(fx.n, fx.n)
    flat = (flat + flat.T) / 2
    return [float(x) for x in np.linalg.eigvalsh(flat)]


def compute(fx, spec):
    weighted = bool(spec.get("weighted"))
    if spec["fn"] == "graph_spectrum":
        return spectrum(fx, spec["kind"], weighted)
    if spec.get("stat") == "ihara":
        return ihara(fx)
    if spec["kind"] == "non_backtracking":
        return non_backtracking(fx)
    if spec["kind"] == "modularity" and fx.n == 0:
        return []
    return dense(fx, spec["kind"], weighted)


def main() -> None:
    spec = load_area("spectral_matrices")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            o = v["oracles"].get(ORACLE)
            if o is None or not applies(v, fx):
                continue
            if set(fx.tags) & set(o.get("undefined_when", [])):
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (spectral matrices): wrote {count} golden files")


if __name__ == "__main__":
    main()
