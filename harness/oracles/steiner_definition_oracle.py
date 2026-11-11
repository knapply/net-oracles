#!/usr/bin/env python3
"""Definition oracle for approximate Steiner trees (manifest/
steiner.yaml; statistics as in ../bindings/steiner.py).

  bounds  [0, 2 (1 - 1/t) OPT, -OPT] for t terminals: OPT is the weight of
          a minimum Steiner tree, computed exactly by the Dreyfus-Wagner
          dynamic program over subsets of the terminals on all-pairs shortest
          paths (Floyd-Warshall); both methods return trees of weight at most
          2 (1 - 1/l) times the optimum for l the leaves of an optimal tree,
          and l <= t (Kou, Markowsky and Berman 1981; Mehlhorn 1988)

    python3 oracles/steiner_definition_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
INF = float("inf")


def terminal_list(fx, kind):
    terms = list(range(0, fx.n, 3))
    return {"few": terms[:5], "three": terms[:3]}.get(kind, terms)


def unusable(fx, weighted):
    if fx.n == 0:
        return True
    parent = list(range(fx.n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b in zip(fx.src, fx.tgt):
        parent[find(a)] = find(b)
    if len({find(v) for v in range(fx.n)}) > 1:
        return True
    pairs = [(min(a, b), max(a, b)) for a, b in zip(fx.src, fx.tgt) if a != b]
    if len(pairs) != len(set(pairs)):
        return True
    return bool(weighted and fx.weighted and any(w < 0 for w in fx.weights))


def optimum(fx, terms, weighted):
    n = fx.n
    d = [[INF] * n for _ in range(n)]
    for v in range(n):
        d[v][v] = 0.0
    for e, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        if a != b:
            w = fx.weights[e] if weighted and fx.weighted else 1.0
            d[a][b] = d[b][a] = min(d[a][b], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    t = len(terms)
    if t <= 1:
        return 0.0
    dp = [[INF] * n for _ in range(1 << t)]
    for i, x in enumerate(terms):
        dp[1 << i] = list(d[x])
    for mask in range(1, 1 << t):
        if mask & (mask - 1) == 0:
            continue
        row = dp[mask]
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:
                for v in range(n):
                    c = dp[sub][v] + dp[other][v]
                    if c < row[v]:
                        row[v] = c
            sub = (sub - 1) & mask
        best = list(row)
        for v in range(n):
            for u in range(n):
                c = row[u] + d[u][v]
                if c < best[v]:
                    best[v] = c
        dp[mask] = best
    return dp[(1 << t) - 1][terms[0]]


def compute(fx, spec):
    weighted = bool(spec.get("weighted"))
    if unusable(fx, weighted):
        return []
    terms = terminal_list(fx, spec.get("terminals", "third"))
    opt = optimum(fx, terms, weighted)
    t = len(terms)
    bound = 2.0 * (1.0 - 1.0 / t) * opt if t else 0.0
    return [0, bound, -opt]


def main() -> None:
    spec = load_area("steiner")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (Steiner trees): wrote {count} golden files")


if __name__ == "__main__":
    main()
