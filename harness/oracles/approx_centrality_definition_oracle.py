#!/usr/bin/env python3
"""Definition oracle for sampled and pruned centralities (
manifest/approx_centrality.yaml; statistics as in
../bindings/approx_centrality.py), from the definitions, in exact arithmetic
where sums of reciprocals are ranked.

  betweenness   sum over ordered pairs (s, t), s != v != t, of the share of
                the shortest s-t paths that pass through v (path counts by
                BFS from every source); halved when undirected
  closeness     nodes reached over the sum of their distances (distances into
                the node when directed), 0 when none is reached
  harmonic      the sum of 1 / distance over the nodes that reach the node
                (Fractions), the five largest, ties to the smallest id
  group         greedy: k times the node that minimizes the sum of the
                distances from the group to all nodes (undirected reading),
                ties to the smallest id

    python3 oracles/approx_centrality_definition_oracle.py
"""

from __future__ import annotations

import sys
from collections import deque
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
TOP = 5
BOUNDS = {"bcapprox_mean": [0.02, 0.05], "clapprox_mean": [0.03]}


def rows(fx, reverse=False, undirected=False, multiple=False):
    """Neighbour sets without loops (parallel edges collapse), or, with
    `multiple`, neighbour lists with one entry per edge."""
    out = [[] if multiple else set() for _ in range(fx.n)]
    add = (lambda row, w: row.append(w)) if multiple else (lambda row, w: row.add(w))
    for a, b in zip(fx.src, fx.tgt):
        if a == b:
            continue
        if undirected or not fx.directed:
            add(out[a], b)
            add(out[b], a)
        elif reverse:
            add(out[b], a)
        else:
            add(out[a], b)
    return out


def bfs(out, source):
    dist = {source: 0}
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for w in out[u]:
            if w not in dist:
                dist[w] = dist[u] + 1
                queue.append(w)
    return dist


def counts(out, source):
    """Distances and shortest-path counts from `source`; `out` lists a
    neighbour once per edge, so parallel edges give separate paths."""
    dist, sigma = {source: 0}, {source: 1}
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for w in out[u]:
            if w not in dist:
                dist[w] = dist[u] + 1
                sigma[w] = 0
                queue.append(w)
            if dist[w] == dist[u] + 1:
                sigma[w] += sigma[u]
    return dist, sigma


def betweenness(fx):
    out = rows(fx, multiple=True)
    info = [counts(out, s) for s in range(fx.n)]
    result = []
    for v in range(fx.n):
        total = Fraction(0)
        for s in range(fx.n):
            ds, ss = info[s]
            if v == s or v not in ds:
                continue
            for t in ds:
                if t == s or t == v:
                    continue
                dv, sv = info[v]
                if t in dv and ds[v] + dv[t] == ds[t]:
                    total += Fraction(ss[v] * sv[t], ss[t])
        result.append(float(total if fx.directed else total / 2))
    return result


def closeness(fx):
    out = rows(fx, reverse=True)
    result = []
    for v in range(fx.n):
        dist = bfs(out, v)
        total = sum(dist.values())
        result.append((len(dist) - 1) / total if total else 0.0)
    return result


def harmonic(fx):
    out = rows(fx, reverse=True)
    return [sum((Fraction(1, d) for d in bfs(out, v).values() if d), Fraction(0))
            for v in range(fx.n)]


def top(fx):
    value = harmonic(fx)
    order = sorted(range(fx.n), key=lambda v: (-value[v], v))[:TOP]
    return order, [float(value[v]) for v in order]


def group(fx):
    if fx.n < 2:
        return None
    out = rows(fx, undirected=True)
    dist = [bfs(out, v) for v in range(fx.n)]
    if len(dist[0]) != fx.n:
        return None
    k = min(3, fx.n - 1)
    chosen, held = [], [None] * fx.n
    for _ in range(k):
        best = None
        for c in range(fx.n):
            if c in chosen:
                continue
            total = sum(dist[c][v] if held[v] is None else min(held[v], dist[c][v])
                        for v in range(fx.n))
            if best is None or total < best[0]:
                best = (total, c)
        chosen.append(best[1])
        held = [dist[best[1]][v] if held[v] is None else min(held[v], dist[best[1]][v])
                for v in range(fx.n)]
    total = sum(held[v] for v in range(fx.n) if v not in chosen)
    return chosen, (fx.n - k) / total


def compute(fx, variant, spec):
    if fx.n == 0:
        return []
    stat = spec["stat"]
    if variant == "bcapprox_mean":
        return BOUNDS[variant] if sum(betweenness(fx)) > 0 else []
    if variant == "clapprox_mean":
        big = fx.n >= 20 and any(x > 0 for x in closeness(fx))
        return BOUNDS[variant] if big else []
    if spec["fn"] == "betweenness_approx":
        return [1, 1] if stat == "threads" else betweenness(fx)
    if spec["fn"] == "closeness_approx":
        return closeness(fx)
    if spec["fn"] == "closeness_top_k":
        order, value = top(fx)
        return value if stat == "values" else order
    result = group(fx)
    if result is None:
        return []
    return result[0] if stat == "nodes" else [result[1]]


def main() -> None:
    spec = load_area("approx_centrality")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            weights_bad = v["params"].get("weighted") and fx.weighted and any(w <= 0 for w in fx.weights)
            if weights_bad:
                continue
            write_values(ORACLE, name, variant, compute(fx, variant, v["params"]))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (approximate centralities): wrote {count} golden files")


if __name__ == "__main__":
    main()
