#!/usr/bin/env python3
"""Golden values for the blockmodels area computed directly from the
definitions (Doreian, Batagelj and Ferligoj 2005, the binary approach; the
block formulas are in manifest/blockmodels.yaml): the
criterion of the partition v % 3, and the smallest criterion over every
partition into exactly k non-empty clusters (enumerated as restricted
growth strings) on fixtures of at most 12 nodes.

This oracle shares no code or algorithmic idea with the engine: every
block is recounted from the matrix for every partition. Each fit has a hard
time limit of 300 seconds (signal.alarm).

    python3 oracles/blockmodels_definition_oracle.py
"""

from __future__ import annotations

import signal
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
MAX_NODES = 80
MAX_SEARCH = 12
TIME_LIMIT = 300

TYPES = {"structural": ("nul", "com"), "regular": ("nul", "reg"),
         "generalized": ("nul", "com", "reg", "rre", "cre")}


class TimeLimit(Exception):
    pass


def _alarm(signum, frame):
    raise TimeLimit()


def matrix(fx):
    n = fx.n
    m = [[0] * n for _ in range(n)]
    weights = fx.weights or [1.0] * len(fx.src)
    for u, v, w in zip(fx.src, fx.tgt, weights):
        if w > 0:
            m[u][v] = 1
            if not fx.directed:
                m[v][u] = 1
    return m


def block_error(m, rows, cols, kind, diagonal):
    nr, nc = len(rows), len(cols)
    st = sum(m[r][c] for r in rows for c in cols)
    pr = sum(1 for r in rows if any(m[r][c] for c in cols))
    pc = sum(1 for c in cols if any(m[r][c] for r in rows))
    if kind == "nul":
        if diagonal:
            sd = sum(m[r][r] for r in rows)
            return st - sd + min(sd, nr - sd)
        return st
    if kind == "com":
        if diagonal:
            sd = sum(m[r][r] for r in rows)
            return nr * nc - nr - (st - sd) + min(sd, nr - sd)
        return nr * nc - st
    if kind == "reg":
        return (nc - pc) * nr + (nr - pr) * pc
    if kind == "rre":
        return (nr - pr) * nc
    if kind == "cre":
        return (nc - pc) * nr
    raise ValueError(kind)


def criterion(m, labels, k, types):
    groups = [[v for v, g in enumerate(labels) if g == c] for c in range(k)]
    total = 0
    for a in range(k):
        for b in range(k):
            if not groups[a] or not groups[b]:
                continue
            total += min(block_error(m, groups[a], groups[b], t, a == b) for t in types)
    return total


def partitions(n, k):
    """Every partition of 0..n-1 into exactly k non-empty clusters."""
    labels = [0] * n

    def rec(v, used):
        if v == n:
            if used == k:
                yield labels
            return
        if k - used > n - v:
            return
        for g in range(min(used + 1, k)):
            labels[v] = g
            yield from rec(v + 1, max(used, g + 1))

    yield from rec(0, 0)


def compute(fx, e):
    types = TYPES[e["blocks"]]
    m = matrix(fx)
    if e["fn"] == "blockmodel_criterion":
        if fx.n == 0:
            return None
        labels = [v % 3 for v in range(fx.n)]
        return [criterion(m, labels, 3, types)]
    if e["fn"] == "blockmodel_search":
        k = int(e["k"])
        if fx.n < k or fx.n > MAX_SEARCH:
            return None
        return [min(criterion(m, p, k, types) for p in partitions(fx.n, k))]
    return None


def main() -> None:
    spec = load_area("blockmodels")
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
    print(f"definition (blockmodels): wrote {count} golden files")


if __name__ == "__main__":
    main()
