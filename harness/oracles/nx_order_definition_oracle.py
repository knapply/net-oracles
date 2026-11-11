#!/usr/bin/env python3
"""Definition oracle for group C's NetworkX-ordered results (see
../bindings/nx_order.py): triangles by enumerating node triples of the
simple undirected graph, and flow hierarchy from strongly connected
components found by mutual reachability. The ordered results (Kosaraju,
biconnected component edges, label spreading) are compared with NetworkX
only, whose order they reproduce.

    python3 oracles/nx_order_definition_oracle.py
"""

from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"


def prominent_undefined(fx, k):
    """Inputs on which NetworkX's prominent_group has no answer."""
    if fx.n < k + 2:
        return True
    if not fx.directed:
        return False
    fwd = [set() for _ in range(fx.n)]
    rev = [set() for _ in range(fx.n)]
    for a, b in zip(fx.src, fx.tgt):
        fwd[a].add(b)
        rev[b].add(a)
    for adj in (fwd, rev):
        seen, stack = {0}, [0]
        while stack:
            for w in adj[stack.pop()]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        if len(seen) < fx.n:
            return True
    return False


def triangles(fx):
    adj = [set() for _ in range(fx.n)]
    for a, b in zip(fx.src, fx.tgt):
        if a != b:
            adj[a].add(b)
            adj[b].add(a)
    t = [0] * fx.n
    for a, b, c in itertools.combinations(range(fx.n), 3):
        if b in adj[a] and c in adj[a] and c in adj[b]:
            t[a] += 1
            t[b] += 1
            t[c] += 1
    return t


def flow_hierarchy(fx, weighted):
    if not fx.src:
        return [-999.0]
    n = fx.n
    reach = [[False] * n for _ in range(n)]
    for i in range(n):
        reach[i][i] = True
    for a, b in zip(fx.src, fx.tgt):
        reach[a][b] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    if reach[k][j]:
                        reach[i][j] = True
    inner = total = Fraction(0)
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        w = Fraction(fx.weights[i]) if weighted else Fraction(1)
        total += w
        if reach[a][b] and reach[b][a]:
            inner += w
    return [float(1 - inner / total)]


def directed_clustering(fx, weighted):
    n = fx.n
    succ = [dict() for _ in range(n)]
    pred = [dict() for _ in range(n)]
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        w = fx.weights[i] if weighted else 1.0
        if a != b and b not in succ[a]:
            succ[a][b] = w
            pred[b][a] = w
    top = max(fx.weights) if weighted and fx.src else 1.0

    def wt(u, v):
        return succ[u][v] / top

    out = []
    for i in range(n):
        P, S = set(pred[i]), set(succ[i])
        t = 0.0
        # Every directed triangle i, j, k: each ordered choice of j (as a
        # predecessor and as a successor) and k (in P or S, and adjacent to
        # j either way).
        for j, jin in [(j, True) for j in P] + [(j, False) for j in S]:
            wij = wt(j, i) if jin else wt(i, j)
            for k, kin in [(k, True) for k in pred[j]] + [(k, False) for k in succ[j]]:
                wjk = wt(k, j) if kin else wt(j, k)
                for kk, ki in ((k in P, True), (k in S, False)):
                    if kk:
                        wik = wt(k, i) if ki else wt(i, k)
                        t += (wij * wik * wjk) ** (1 / 3) if weighted else 1.0
        dt, db = len(P) + len(S), len(P & S)
        out.append(0.0 if t == 0 else t / ((dt * (dt - 1) - 2 * db) * 2))
    return out


def successor_transitivity(fx):
    succ = [set() for _ in range(fx.n)]
    for a, b in zip(fx.src, fx.tgt):
        if a != b:
            succ[a].add(b)
    tri = sum(len(succ[v] & succ[w]) for v in range(fx.n) for w in succ[v])
    con = sum(len(s) * (len(s) - 1) for s in succ)
    return [0.0 if tri == 0 else tri / con]


def node_reciprocity(fx):
    succ = [set() for _ in range(fx.n)]
    pred = [set() for _ in range(fx.n)]
    for a, b in zip(fx.src, fx.tgt):
        succ[a].add(b)
        pred[b].add(a)
    out = []
    for v in range(fx.n):
        tot = len(succ[v]) + len(pred[v])
        out.append(-999.0 if tot == 0 else float(Fraction(2 * len(succ[v] & pred[v]), tot)))
    return out


def prominent_value(fx, k):
    """Largest normalized group betweenness over all k-node groups, from
    shortest-path counts (breadth-first; parallel arcs and loops do not
    change them) with exact fractions."""
    if prominent_undefined(fx, k):
        return [-999.0]
    n = fx.n
    adj = [[] for _ in range(n)]
    for a, b in zip(fx.src, fx.tgt):
        if a == b:
            continue
        adj[a].append(b)
        if not fx.directed:
            adj[b].append(a)
    adj = [sorted(set(r)) for r in adj]
    searches = []
    for s in range(n):
        dist = {s: 0}
        order = [s]
        for v in order:
            for w in adj[v]:
                if w not in dist:
                    dist[w] = dist[v] + 1
                    order.append(w)
        sigma = dict.fromkeys(order, 0)
        sigma[s] = 1
        for v in order:
            for w in adj[v]:
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
        searches.append((dist, order, sigma))
    best = Fraction(0)
    for group in itertools.combinations(range(n), k):
        inside = set(group)
        total = Fraction(0)
        for s in range(n):
            if s in inside:
                continue
            dist, order, sigma = searches[s]
            avoid = dict.fromkeys(order, 0)
            avoid[s] = 1
            for v in order:
                if v in inside:
                    continue
                for w in adj[v]:
                    if dist[w] == dist[v] + 1:
                        avoid[w] += avoid[v]
            for t in order:
                if t != s and t not in inside:
                    total += Fraction(sigma[t] - avoid[t], sigma[t])
        best = max(best, total)
    value = best / ((n - k) * (n - k - 1))
    return [float(f"{float(value):.2f}")]


def main() -> None:
    spec = load_area("nx_order")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            e = v["params"]
            if e["fn"] == "nxo_triangles":
                vals = triangles(fx)
            elif e["fn"] == "nxo_flow_hierarchy":
                vals = flow_hierarchy(fx, bool(e.get("weighted")))
            elif e["fn"] == "nxo_directed_clustering":
                vals = directed_clustering(fx, bool(e.get("weighted")))
            elif e["fn"] == "nxo_successor_transitivity":
                vals = successor_transitivity(fx)
            elif e["fn"] == "nxo_node_reciprocity":
                vals = node_reciprocity(fx)
            elif e["fn"] == "nxo_prominent":
                vals = prominent_value(fx, e.get("k", 2))
            else:
                continue
            write_values(ORACLE, name, variant, vals)
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (nx_order): wrote {count} golden files")


if __name__ == "__main__":
    main()
