#!/usr/bin/env python3
"""Definition oracle for random walks and random-walk sampling
(manifest/random_walks.yaml; statistics as in
../bindings/random_walks.py).

The exact values come from the Markov chain the engine samples: from node v
a walker follows arc (v, x) with probability w(v, x) / sum of w(v, .) (1 per
arc when unweighted; parallel arcs add; an undirected self-loop is one arc),
and stays put at a node with no arc of positive weight.

  end     the distribution of the position after 4 moves from node 0:
          e_0 P^4 with the stuck rows made absorbing
  visits  the stationary distribution of the walk that returns to node 0
          with probability 0.2 before each move and at a stuck node:
          pi = 0.2 (I - 0.8 P')^-1 e_0, P' the stuck rows replaced by e_0
          (personalized PageRank, Page et al. 1998; Tong et al. 2006)
  valid, nodes  the invariants hold: [1, 1, 1, 1], and [1, min(5, reach)]
          with reach the nodes reachable from node 0 along arcs of positive
          weight (breadth-first search)

    python3 oracles/random_walks_definition_oracle.py
"""

from __future__ import annotations

import sys
from collections import deque
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "bindings"))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
END_STEPS = 4
RESTART = 0.2
TARGET = 5


def unusable(fx, spec):
    if fx.n == 0:
        return True
    return bool(spec.get("weighted") and fx.weighted and any(w < 0 for w in fx.weights))


def adjacency(fx, weighted):
    a = np.zeros((fx.n, fx.n))
    for e, (s, t) in enumerate(zip(fx.src, fx.tgt)):
        w = fx.weights[e] if weighted and fx.weighted else 1.0
        a[s, t] += w
        if not fx.directed and s != t:
            a[t, s] += w
    return a


def transition(fx, weighted):
    """Row-stochastic P (stuck rows zero) and the stuck mask."""
    a = adjacency(fx, weighted)
    total = a.sum(axis=1)
    stuck = ~(total > 0)
    p = np.divide(a, total[:, None], out=np.zeros_like(a), where=~stuck[:, None])
    return p, stuck


def end_distribution(fx, weighted):
    p, stuck = transition(fx, weighted)
    p[stuck, :] = 0.0
    p[stuck, np.flatnonzero(stuck)] = 1.0
    v = np.zeros(fx.n)
    v[0] = 1.0
    for _ in range(END_STEPS):
        v = v @ p
    return v


def visits(fx, weighted):
    p, stuck = transition(fx, weighted)
    p[stuck, :] = 0.0
    p[stuck, 0] = 1.0
    e0 = np.zeros(fx.n)
    e0[0] = 1.0
    # pi = alpha e0 (I - (1 - alpha) P)^-1, a row vector
    return RESTART * np.linalg.solve((np.eye(fx.n) - (1 - RESTART) * p).T, e0)


def reach(fx, weighted):
    a = adjacency(fx, weighted) > 0
    seen, queue = {0}, deque([0])
    while queue:
        v = queue.popleft()
        for x in np.flatnonzero(a[v]):
            if int(x) not in seen:
                seen.add(int(x))
                queue.append(int(x))
    return len(seen)


def compute(fx, spec):
    if unusable(fx, spec):
        return []
    weighted = bool(spec.get("weighted"))
    fn, stat = spec["fn"], spec["stat"]
    if fn == "random_walk":
        return [1, 1, 1, 1] if stat == "valid" else list(end_distribution(fx, weighted))
    if stat == "visits":
        return list(visits(fx, weighted))
    return [1, min(TARGET, reach(fx, weighted))]


def main() -> None:
    spec = load_area("random_walks")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (random walks): wrote {count} golden files")


if __name__ == "__main__":
    main()
