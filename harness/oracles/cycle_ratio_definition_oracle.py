#!/usr/bin/env python3
"""Definition oracle for cycle ratios (manifest/cycle_ratio.yaml;
synthetic costs and times as in ../bindings/cycle_ratio.py).

The minimum cycle ratio is the least lambda for which no cycle has negative
total of c_e - lambda t_e (Lawler 1967: a negative cycle exists exactly when
lambda exceeds the optimum). The oracle bisects lambda to 1e-13 and tests
for a negative cycle by Bellman-Ford with a slack of 1e-12: an algorithm
independent of Karp's table and of Dinkelbach's iteration, with a result
good to about 1e-9. The maximum is the negated minimum of the negated
costs. A network without a directed cycle (Kahn's test) gives -999.

    python3 oracles/cycle_ratio_definition_oracle.py
"""

from __future__ import annotations

import sys
from collections import deque
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
SLACK = 1e-12


def cost(e):
    return float(((7 * e + 3) % 11) - 3)


def time(e):
    return float(1 + e % 3)


def acyclic(fx):
    indeg = [0] * fx.n
    out = [[] for _ in range(fx.n)]
    for a, b in zip(fx.src, fx.tgt):
        out[a].append(b)
        indeg[b] += 1
    queue = deque(v for v in range(fx.n) if indeg[v] == 0)
    seen = 0
    while queue:
        v = queue.popleft()
        seen += 1
        for w in out[v]:
            indeg[w] -= 1
            if indeg[w] == 0:
                queue.append(w)
    return seen == fx.n


def negative_cycle(fx, c, t, lam):
    dist = [0.0] * fx.n
    for _ in range(fx.n):
        changed = False
        for e, (a, b) in enumerate(zip(fx.src, fx.tgt)):
            cand = dist[a] + c[e] - lam * t[e]
            if cand < dist[b] - SLACK:
                dist[b] = cand
                changed = True
        if not changed:
            return False
    return True


def minimum_ratio(fx, c, t):
    hi = max(abs(x) for x in c) / min(t) + 1.0
    lo = -hi
    for _ in range(200):
        mid = (lo + hi) / 2
        if negative_cycle(fx, c, t, mid):
            hi = mid
        else:
            lo = mid
        if hi - lo < 1e-13:
            break
    return (lo + hi) / 2


def compute(fx, spec):
    if not fx.directed:
        return []
    m = len(fx.src)
    if spec.get("stat", "ratio") == "valid":
        return [1]
    if acyclic(fx):
        return [-999.0]
    c = [cost(e) for e in range(m)] if spec.get("costs", "pattern") == "pattern" else list(fx.weights)
    t = [time(e) for e in range(m)] if spec.get("times", "none") == "pattern" else [1.0] * m
    if spec.get("extreme", "minimum") == "maximum":
        return [-minimum_ratio(fx, [-x for x in c], t)]
    return [minimum_ratio(fx, c, t)]


def main() -> None:
    spec = load_area("cycle_ratio")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (cycle ratio): wrote {count} golden files")


if __name__ == "__main__":
    main()
