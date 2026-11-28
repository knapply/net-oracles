#!/usr/bin/env python3
"""Golden values for the css area (cognitive social structures) computed
directly from the definitions in manifest/css.yaml: the
informant reports by rule, the consensus structures dyad by dyad, and each
informant's agreement, hit rate and false alarm rate with exact fractions.

This oracle shares no code or algorithmic idea with the engine. Each fixture
has a hard time limit of 300 seconds (signal.alarm).

    python3 oracles/css_definition_oracle.py
"""

from __future__ import annotations

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
NAN = float("nan")


class TimeLimit(Exception):
    pass


def _alarm(signum, frame):
    raise TimeLimit()


def reports(fx):
    n = fx.n
    a = [[0] * n for _ in range(n)]
    for u, v in zip(fx.src, fx.tgt):
        if u != v:
            a[u][v] = 1
            if not fx.directed:
                a[v][u] = 1
    out = []
    for k in range(n):
        s = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                key = (i + 2 * j + 3 * k) if fx.directed else (i + j + 3 * k)
                s[i][j] = a[i][j] ^ (1 if key % 5 == 0 else 0)
        out.append(s)
    return out


def consensus(rep, method):
    m = len(rep)
    n = m
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if method == "central_graph":
                c[i][j] = 1 if 2 * sum(rep[k][i][j] for k in range(m)) >= m else 0
            elif method == "las_intersection":
                c[i][j] = rep[i][i][j] & rep[j][i][j]
            elif method == "las_union":
                c[i][j] = rep[i][i][j] | rep[j][i][j]
            elif method == "or_row":
                c[i][j] = rep[i][i][j]
            elif method == "or_col":
                c[i][j] = rep[j][i][j]
    return c


def accuracy(rep, c):
    n = len(c)
    off = [(i, j) for i in range(n) for j in range(n) if i != j]
    ones = [(i, j) for i, j in off if c[i][j]]
    zeros = [(i, j) for i, j in off if not c[i][j]]
    out = []
    for s in rep:
        agree = Fraction(sum(1 for i, j in off if s[i][j] == c[i][j]), len(off)) if off else None
        hit = Fraction(sum(s[i][j] for i, j in ones), len(ones)) if ones else None
        fa = Fraction(sum(s[i][j] for i, j in zeros), len(zeros)) if zeros else None
        out.append(tuple(NAN if x is None else float(x) for x in (agree, hit, fa)))
    return out


def compute(fx, e):
    if e["fn"] != "css_accuracy" or fx.n == 0:
        return None
    rep = reports(fx)
    c = consensus(rep, e["method"])
    if e.get("part") == "accuracy":
        return accuracy(rep, c)
    return [tuple(float(x) for x in row) for row in c]


def main() -> None:
    spec = load_area("css")
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
    print(f"definition (css): wrote {count} golden files")


if __name__ == "__main__":
    main()
