#!/usr/bin/env python3
"""Definition oracle for NetworkX's power iterations and the Google matrix
(see ../bindings/nx_power.py): each iteration written out from its
definition in plain Python over the edge list (no NetworkX), with the
start vector, update, stopping rule, and iteration cap that NetworkX
documents.

    python3 oracles/nx_power_definition_oracle.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"


def matrix(fx, weighted, collapse=False):
    """Dense adjacency: A[u][v] for arcs u -> v (both ways when undirected,
    a self-loop once); parallel edges add up, or count once with weight 1."""
    n = fx.n
    A = [[0.0] * n for _ in range(n)]
    seen = set()
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        w = fx.weights[i] if weighted and fx.weighted else 1.0
        pairs = [(a, b)] if fx.directed or a == b else [(a, b), (b, a)]
        for u, v in pairs:
            if collapse:
                if (u, v) not in seen:
                    seen.add((u, v))
                    A[u][v] = 1.0
            else:
                A[u][v] += w
    return A


def eigenvector(fx, e):
    n = fx.n
    A = matrix(fx, e.get("weighted"))
    x = [1.0 / n] * n
    for _ in range(e.get("max_iter", 100)):
        y = [x[v] + sum(x[u] * A[u][v] for u in range(n)) for v in range(n)]
        norm = math.sqrt(sum(t * t for t in y)) or 1.0
        y = [t / norm for t in y]
        if sum(abs(y[i] - x[i]) for i in range(n)) < n * e.get("tol", 1e-6):
            return y
        x = y
    return [-999.0]


def katz(fx, e):
    n = fx.n
    A = matrix(fx, e.get("weighted"))
    alpha = e.get("alpha", 0.1)
    x = [0.0] * n
    for _ in range(e.get("max_iter", 1000)):
        y = [alpha * sum(x[u] * A[u][v] for u in range(n)) + 1.0 for v in range(n)]
        if sum(abs(y[i] - x[i]) for i in range(n)) < n * e.get("tol", 1e-6):
            if e.get("normalized", True):
                norm = math.sqrt(sum(t * t for t in y))
                if norm:
                    y = [t / norm for t in y]
            return y
        x = y
    return [-999.0]


def pagerank(fx, e):
    n = fx.n
    if n == 0:
        return []
    A = matrix(fx, e.get("weighted"))
    alpha = e.get("alpha", 0.85)
    s = [sum(row) for row in A]
    if e.get("personalization") == "mod3":
        p = [v % 3 for v in range(n)]
        p = [t / sum(p) for t in p]
    else:
        p = [1.0 / n] * n
    x = [1.0 / n] * n
    for _ in range(e.get("max_iter", 100)):
        stuck = sum(x[i] for i in range(n) if s[i] == 0)
        y = [alpha * (sum(x[u] * A[u][v] / s[u] for u in range(n) if s[u]) + stuck * p[v])
             + (1 - alpha) * p[v] for v in range(n)]
        if sum(abs(y[i] - x[i]) for i in range(n)) < n * e.get("tol", 1e-6):
            return y
        x = y
    return [-999.0]


def hits(fx, e):
    n = fx.n
    A = matrix(fx, e.get("weighted"))
    h = [1.0 / n] * n
    for _ in range(e.get("max_iter", 100)):
        a = [sum(h[u] * A[u][v] for u in range(n)) for v in range(n)]
        hn = [sum(A[u][v] * a[v] for v in range(n)) for u in range(n)]
        top = max(hn)
        if top == 0:
            return [-999.0]
        hn = [t / top for t in hn]
        done = sum(abs(hn[i] - h[i]) for i in range(n)) < e.get("tol", 1e-8)
        h = hn
        if done:
            if e.get("normalized", True):
                sh, sa = sum(h), sum(a)
                return [t / sh for t in h] + [t / sa for t in a]
            ma = max(a)
            return h + [t / ma for t in a]
    return [-999.0]


def google(fx, e):
    n = fx.n
    A = matrix(fx, e.get("weighted"))
    alpha = e.get("alpha", 0.85)
    p = [1.0 / n] * n
    out = []
    for u in range(n):
        row = A[u] if sum(A[u]) else p[:]
        s = sum(row)
        out += [alpha * (row[v] / s) + (1 - alpha) * p[v] for v in range(n)]
    return out


FUNCS = {"nxp_eigenvector": eigenvector, "nxp_katz": katz, "nxp_pagerank": pagerank,
         "nxp_hits": hits, "nxp_google": google}


def main() -> None:
    spec = load_area("nx_power")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        if fx.n == 0:
            continue
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, FUNCS[v["params"]["fn"]](fx, v["params"]))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (nx_power): wrote {count} golden files")


if __name__ == "__main__":
    main()
