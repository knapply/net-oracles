#!/usr/bin/env python3
"""Definition oracle for layouts: the stress sum of a fixed probe layout by
Floyd-Warshall distances in exact rational arithmetic (weights as given
decimals), and the statement of the properties every layout must have.
Shares no code with the engine.

    python3 oracles/layout_definition_oracle.py
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"


def stress_value(fx, weighted):
    n = fx.n
    d = [[None] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = Fraction(0)
    for e, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        if a == b:
            continue
        w = Fraction(repr(fx.weights[e])) if weighted else Fraction(1)
        if d[a][b] is None or w < d[a][b]:
            d[a][b] = d[b][a] = w
    for k in range(n):
        for i in range(n):
            if d[i][k] is None:
                continue
            for j in range(n):
                if d[k][j] is None:
                    continue
                s = d[i][k] + d[k][j]
                if d[i][j] is None or s < d[i][j]:
                    d[i][j] = s
    xs = [Fraction((7 * i) % 13, 4) for i in range(n)]
    ys = [Fraction((5 * i * i + 3 * i) % 11, 3) for i in range(n)]
    total = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            if d[i][j] is None:
                continue
            dist = float(d[i][j])
            e = float((xs[i] - xs[j]) ** 2 + (ys[i] - ys[j]) ** 2) ** 0.5
            total += ((e - dist) / dist) ** 2
    return total


def compute(fx, e):
    fn = e["fn"]
    if fn == "layout_stress_value":
        return [stress_value(fx, bool(e.get("weighted")))]
    if fn == "layout_properties":
        return [(1, 1, 1, 1)]
    return None


def main() -> None:
    spec = load_area("layout")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            values = compute(fx, v["params"])
            if values is not None:
                write_values(ORACLE, name, variant, values)
                count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (layout): wrote {count} golden files")


if __name__ == "__main__":
    main()
