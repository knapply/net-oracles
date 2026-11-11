#!/usr/bin/env python3
"""Definition oracle for the b-matching measure: the optimum of the integer
program  maximize sum_e w_e x_e  subject to  sum over the edges at v of x_e
<= b(v),  x_e in {0, 1}  over the edges that are not self-loops (and, when
weighted, have weight above zero), solved exactly by HiGHS through
scipy.optimize.milp with a zero optimality gap; fixtures of at most 18
usable edges are also solved by exhaustive search and the two must agree.
Direction is ignored and parallel edges are separate variables. The
capacity of node v is b(v) = 1 + v % 3 (../bindings/bmatching.py).

    python3 oracles/bmatching_definition_oracle.py

Validity entries expect [1, 1, 1] and the bounds on the greedy matching
compare with the optimum weight (twice the greedy weight is at least it, the
greedy weight is at most it).
"""

from __future__ import annotations

import sys
from itertools import product
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
AREA = "bmatching"


def capacity(fx):
    return [1 + v % 3 for v in range(fx.n)]


def usable(fx, weighted):
    """(source, target, weight) of the edges that may join the matching."""
    out = []
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        w = fx.weights[i] if weighted else 1.0
        if a != b and w > 0:
            out.append((a, b, w))
    return out


def optimum(fx, weighted):
    edges = usable(fx, weighted)
    if not edges:
        return 0.0
    b = capacity(fx)
    a = lil_matrix((fx.n, len(edges)))
    for k, (u, v, _) in enumerate(edges):
        a[u, k] += 1
        a[v, k] += 1
    w = np.array([e[2] for e in edges])
    res = milp(-w, constraints=LinearConstraint(a.tocsr(), -np.inf, np.array(b, dtype=float)),
               integrality=np.ones(len(edges)), bounds=Bounds(0, 1),
               options={"mip_rel_gap": 0.0})
    assert res.status == 0, res.message
    value = float(sum(wi for wi, xi in zip(w, np.round(res.x)) if xi > 0.5))
    if len(edges) <= 18:
        best = 0.0
        for pick in product((0, 1), repeat=len(edges)):
            used = [0] * fx.n
            for take, (u, v, _) in zip(pick, edges):
                if take:
                    used[u] += 1
                    used[v] += 1
            if all(x <= c for x, c in zip(used, b)):
                best = max(best, sum(e[2] for t, e in zip(pick, edges) if t))
        assert abs(best - value) <= 1e-9 * max(1.0, abs(best)), (best, value)
    return value


def compute(fx, e):
    fn = e["fn"]
    if fn == "bmatching_cardinality":
        return [optimum(fx, False)]
    if fn == "bmatching_valid":
        return [1, 1, 1]
    return [optimum(fx, True)]


def main() -> None:
    spec = load_area(AREA)
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition ({AREA}): wrote {count} golden files")


if __name__ == "__main__":
    main()
