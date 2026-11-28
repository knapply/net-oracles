#!/usr/bin/env python3
"""Golden values for the signed area computed directly from the definitions.

PN centrality (Everett and Borgatti 2014): PN = (I - A / (2n - 2))^-1 1
with A = P - 2N, P and N the 0/1 matrices of positive and negative ties,
solved by Gauss-Jordan elimination in exact rational arithmetic. Balanced
triads (ergm's `balance` term): every node triple is classified by brute
force on the simple graph.

This oracle shares no code or algorithmic idea with the engine: it is
deliberately slow and simple (exact arithmetic, brute force), so it runs
only on fixtures of at most MAX_NODES nodes. Each fit has a hard time limit
of 300 seconds (signal.alarm).

    python3 oracles/signed_definition_oracle.py
"""

from __future__ import annotations

import itertools
import signal
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
MAX_NODES = 80
TIME_LIMIT = 300


class TimeLimit(Exception):
    pass


def _alarm(signum, frame):
    raise TimeLimit()


def edge_sign(u: int, v: int, w: float, signs: str) -> float:
    if signs == "rule":
        return -1.0 if (u + v) % 3 == 0 else 1.0
    return w


def sign_matrix(fx, signs: str) -> list[list[int]]:
    """Tie of each ordered pair: the sign of the summed weights of its
    parallel edges (both directions of an undirected edge); loops dropped."""
    n = fx.n
    total = [[0.0] * n for _ in range(n)]
    weights = fx.weights or [1.0] * len(fx.src)
    for u, v, w in zip(fx.src, fx.tgt, weights):
        if u == v:
            continue
        s = edge_sign(u, v, w, signs)
        total[u][v] += s
        if not fx.directed:
            total[v][u] += s
    return [[(x > 0) - (x < 0) for x in row] for row in total]


def pn_centrality(fx, e):
    n = fx.n
    if n < 2:
        return None
    s = sign_matrix(fx, e.get("signs", "weights"))
    if e.get("mode", "out") == "in":
        s = [[s[j][i] for j in range(n)] for i in range(n)]
    a = [[Fraction(1 if x > 0 else (-2 if x < 0 else 0)) for x in row] for row in s]
    c = Fraction(1, 2 * n - 2)
    # Augmented matrix [I - c A | 1].
    m = [[(Fraction(1) if i == j else Fraction(0)) - c * a[i][j] for j in range(n)] + [Fraction(1)]
         for i in range(n)]
    for col in range(n):
        piv = next((r for r in range(col, n) if m[r][col] != 0), None)
        if piv is None:
            return [float("nan")] * n
        m[col], m[piv] = m[piv], m[col]
        p = m[col][col]
        m[col] = [x / p for x in m[col]]
        for r in range(n):
            if r != col and m[r][col] != 0:
                f = m[r][col]
                m[r] = [x - f * y for x, y in zip(m[r], m[col])]
    return [float(m[i][n]) for i in range(n)]


def balanced_triads(fx, e):
    n = fx.n
    tie = set()
    for u, v in zip(fx.src, fx.tgt):
        if u == v:
            continue
        tie.add((u, v))
        if not fx.directed:
            tie.add((v, u))
    count = 0
    for i, j, k in itertools.combinations(range(n), 3):
        pairs = [(i, j), (i, k), (j, k)]
        if fx.directed:
            mutual = sum(1 for a, b in pairs if (a, b) in tie and (b, a) in tie)
            asym = sum(1 for a, b in pairs if ((a, b) in tie) != ((b, a) in tie))
            # MAN 102 (one mutual, two null) or 300 (three mutual).
            if (mutual, asym) in ((1, 0), (3, 0)):
                count += 1
        else:
            ties = sum(1 for a, b in pairs if (a, b) in tie)
            if ties in (1, 3):
                count += 1
    return [count]


def compute(fx, engine: dict):
    fn = engine["fn"]
    if fn == "pn_centrality":
        return pn_centrality(fx, engine)
    if fn == "balanced_triads":
        return balanced_triads(fx, engine)
    return None


def main() -> None:
    spec = load_area("signed")
    signal.signal(signal.SIGALRM, _alarm)
    count = 0
    for fixture in fixture_names():
        fx = load_fixture(fixture)
        if fx.n > MAX_NODES:
            continue
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            signal.alarm(TIME_LIMIT)
            try:
                values = compute(fx, v["params"])
            except TimeLimit:
                print(f"  {variant} on {fixture}: over {TIME_LIMIT} s, skipped")
                values = None
            finally:
                signal.alarm(0)
            if values is None:
                continue
            write_values(ORACLE, fixture, variant, values)
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (signed): wrote {count} golden files")


if __name__ == "__main__":
    main()
