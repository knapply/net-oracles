#!/usr/bin/env python3
"""Definition oracle for NetworkX's community measures: edge betweenness in
exact rational arithmetic from shortest-path counts (Girvan-Newman and the
edge betweenness partition, removing a most central edge, the first in
edge order on exact ties), clique percolation from every clique enumerated
by growth, and modularity, overlapping modularity, and the partition counts
from their formulas. Kernighan-Lin, label propagation, and greedy
modularity are heuristics without a closed form and have no definition
oracle. Shares no code with the engine. Inputs and encodings:
../bindings/community_nx.py.

    python3 oracles/community_nx_definition_oracle.py
"""

from __future__ import annotations

import itertools
import sys
from collections import deque
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
AREA = "community_nx"
MEASURES = {}


def measure(name):
    def wrap(f):
        MEASURES[name] = f
        return f
    return wrap


def copy_rows(fx):
    """Undirected rows as NetworkX's to_undirected orders them (see
    community_nx.rs), from the edges in G.edges() order of the simple graph
    (directed fixtures: arcs in successor order)."""
    adj = {v: {} for v in range(fx.n)}
    for a, b in zip(fx.src, fx.tgt):
        if a == b:
            continue
        adj[a][b] = True
        if not fx.directed:
            adj[b][a] = True
    edges, seen = [], set()
    for u in range(fx.n):
        for v in adj[u]:
            if fx.directed or v not in seen:
                edges.append((u, v))
        seen.add(u)
    rows = {v: [] for v in range(fx.n)}
    for u, v in edges:
        if v not in rows[u]:
            rows[u].append(v)
        if u not in rows[v]:
            rows[v].append(u)
    return rows


def edge_order(rows):
    out, seen = [], set()
    for u in sorted(rows):
        for v in rows[u]:
            if v not in seen:
                out.append((u, v))
        seen.add(u)
    return out


def betweenness(rows):
    """Exact edge betweenness: for every ordered pair (s, t), the share of
    shortest s-t paths through each edge (each unordered pair counted in
    both directions, as Brandes' sum over all sources gives)."""
    n = len(rows)
    bet = {}
    for s in range(n):
        dist = {s: 0}
        sigma = {s: 1}
        order = [s]
        q = deque([s])
        while q:
            v = q.popleft()
            for w in rows[v]:
                if w not in dist:
                    dist[w] = dist[v] + 1
                    sigma[w] = 0
                    q.append(w)
                    order.append(w)
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
        # Paths from s through edge (v, w): sigma_s(v) * (paths w -> t
        # continuing downward), accumulated by dependency.
        delta = {v: Fraction(0) for v in order}
        for w in reversed(order):
            for v in rows[w]:
                if dist.get(v) == dist[w] - 1:
                    c = Fraction(sigma[v], sigma[w]) * (1 + delta[w])
                    key = frozenset((v, w))
                    bet[key] = bet.get(key, Fraction(0)) + c
                    delta[v] += c
    return bet


def components(rows):
    n = len(rows)
    label = [-1] * n
    k = 0
    for s in range(n):
        if label[s] >= 0:
            continue
        label[s] = k
        stack = [s]
        while stack:
            v = stack.pop()
            for w in rows[v]:
                if label[w] < 0:
                    label[w] = k
                    stack.append(w)
        k += 1
    return label, k


def remove_central(rows):
    bet = betweenness(rows)
    best = None
    for u, v in edge_order(rows):
        b = bet.get(frozenset((u, v)), Fraction(0))
        if best is None or b > best[0]:
            best = (b, u, v)
    _, u, v = best
    rows[u].remove(v)
    rows[v].remove(u)


@measure("cnx_girvan_newman")
def _gn(fx, e):
    rows = copy_rows(fx)
    if not edge_order(rows):
        return [()] * fx.n
    levels = []
    while len(levels) < e["level"] and edge_order(rows):
        _, before = components(rows)
        while True:
            remove_central(rows)
            label, k = components(rows)
            if k > before:
                break
        levels.append(label)
    return [tuple(lv[v] for lv in levels) for v in range(fx.n)]


@measure("cnx_edge_betweenness")
def _ebp(fx, e):
    if e["k"] > fx.n:
        return [-1] * fx.n
    rows = copy_rows(fx)
    while True:
        label, k = components(rows)
        if k >= e["k"]:
            return label
        remove_central(rows)


def every_clique(n, adj):
    out = []

    def grow(c):
        out.append(c)
        for w in range(c[-1] + 1, n):
            if all(w in adj[u] for u in c):
                grow(c + [w])

    for v in range(n):
        grow([v])
    return out


@measure("cnx_k_clique")
def _kc(fx, e):
    k = e["k"]
    adj = {v: set() for v in range(fx.n)}
    for a, b in zip(fx.src, fx.tgt):
        if a != b:
            adj[a].add(b)
            adj[b].add(a)
    cl = [frozenset(c) for c in every_clique(fx.n, adj)]
    maximal = [c for c in cl if len(c) >= k and not any(c < d for d in cl)]
    parent = list(range(len(maximal)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i, j in itertools.combinations(range(len(maximal)), 2):
        if len(maximal[i] & maximal[j]) >= k - 1:
            parent[find(i)] = find(j)
    groups = {}
    for i, c in enumerate(maximal):
        groups.setdefault(find(i), set()).update(c)
    return [tuple(sorted(g)) for g in groups.values()]


def blocks(fx):
    return [3 * v // fx.n for v in range(fx.n)]


@measure("cnx_modularity_nx")
def _mod(fx, e):
    w = [Fraction(x) for x in fx.weights] if fx.weighted else [Fraction(1)] * len(fx.src)
    lab = blocks(fx)
    outd = [Fraction(0)] * fx.n
    ind = [Fraction(0)] * fx.n
    inside = {}
    for (a, b), x in zip(zip(fx.src, fx.tgt), w):
        outd[a] += x
        ind[b] += x
        if lab[a] == lab[b]:
            inside[lab[a]] = inside.get(lab[a], Fraction(0)) + x
    total = sum(outd)
    if total == 0:
        return [0.0]
    q = Fraction(0)
    for c in set(lab):
        members = [v for v in range(fx.n) if lab[v] == c]
        if fx.directed:
            so = sum(outd[v] for v in members)
            si = sum(ind[v] for v in members)
            q += inside.get(c, 0) / total - so * si / total ** 2
        else:
            d = sum(outd[v] + ind[v] for v in members)
            q += inside.get(c, 0) / (total) - d * d / (2 * total) ** 2
    return [float(q)]


@measure("cnx_overlapping")
def _om(fx, e):
    lab = blocks(fx)
    cover = [{v for v in range(fx.n) if lab[v] == k} for k in range(3)]
    cover = [c for c in cover if c] + [set(range(min(3, fx.n)))]
    s = [sum(1 for c in cover if v in c) for v in range(fx.n)]
    edges = {frozenset((a, b)) for a, b in zip(fx.src, fx.tgt) if a != b}
    deg = [0] * fx.n
    for edge in edges:
        for v in edge:
            deg[v] += 1
    dsum = sum(deg)
    if dsum == 0:
        return [0.0]
    total = Fraction(0)
    for c in cover:
        lt = sum(Fraction(1, s[a] * s[b]) for a, b in (tuple(x) for x in edges)
                 if a in c and b in c)
        kt = sum(Fraction(deg[v], s[v]) for v in c)
        total += 2 * lt / dsum - (kt / dsum) ** 2
    return [float(total)]


@measure("cnx_partition_counts")
def _pc(fx, e):
    lab = blocks(fx)
    pairs = list(zip(fx.src, fx.tgt))
    intra = sum(1 for a, b in pairs if lab[a] == lab[b])
    cross = {(a, b) if fx.directed else frozenset((a, b)) for a, b in pairs if lab[a] != lab[b]}
    keys = {p if fx.directed else frozenset(p) for p in pairs}
    if len(keys) < len(pairs):
        non = -1
    else:
        non = 0
        for a in range(fx.n):
            for b in range(fx.n):
                if a == b or lab[a] == lab[b] or (not fx.directed and b < a):
                    continue
                key = (a, b) if fx.directed else frozenset((a, b))
                if key not in cross:
                    non += 1
    return [(intra, len(cross), non)]


@measure("cnx_lukes")
def _lukes(fx, e):
    edges = sorted({(min(a, b), max(a, b)) for a, b in zip(fx.src, fx.tgt) if a != b})
    n = fx.n
    if n == 0 or len(edges) != n - 1:
        return [-1]
    # Connected? (a forest with n - 1 edges is a tree)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        parent[find(a)] = find(b)
    if len({find(v) for v in range(n)}) != 1:
        return [-1]
    # Optimum: keep a set of edges whose components have at most max_size
    # nodes, as many as possible (unit weights), by enumeration for small
    # trees, else by the subtree-size recursion on the edge count.
    if len(edges) > 20:
        return None
    best = 0
    for mask in range(1 << len(edges)):
        kept = [edges[i] for i in range(len(edges)) if mask >> i & 1]
        if len(kept) <= best:
            continue
        parent = list(range(n))
        for a, b in kept:
            parent[find(a)] = find(b)
        sizes = {}
        for v in range(n):
            r = find(v)
            sizes[r] = sizes.get(r, 0) + 1
        if max(sizes.values()) <= e["max_size"]:
            best = len(kept)
    return [(best, 1)]



@measure("cnx_seeded_labels_valid")
def _seeded_valid(fx, e):
    # Asynchronous label propagation stops only when every node holds a most
    # frequent label among its neighbours (Raghavan et al. 2007); fast label
    # propagation keeps that invariant for every node out of its queue
    # (Traag and Subelj 2023); fluid communities keep k non-empty
    # communities on a connected graph (Pares et al. 2018).
    rows = copy_rows(fx)
    seen, stack = {0}, [0]
    while stack and fx.n:
        for y in rows[stack.pop()]:
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return [1, 1, 1 if fx.n and len(seen) == fx.n else -1]



@measure("cnx_louvain_seeded_valid")
def _louvain_seeded_valid(fx, e):
    # The Louvain method moves a node only for a positive modularity gain and
    # merges whole communities (Blondel et al. 2008), so it returns a
    # partition whose modularity is at least that of the singletons.
    has_edge = any(a != b for a, b in zip(fx.src, fx.tgt))
    return [1, 1] if has_edge else [-1, -1]



@measure("cnx_leiden_seeded_valid")
def _leiden_seeded_valid(fx, e):
    # Leiden's refinement merges a node only into a refined community it is
    # joined to, so every community it returns is a connected partition
    # class (Traag, Waltman and van Eck 2019), for either quality function.
    has_edge = any(a != b for a, b in zip(fx.src, fx.tgt))
    return [1, 1, 1, 1] if has_edge else [-1, -1, -1, -1]


def main() -> None:
    spec = load_area(AREA)
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            f = MEASURES.get(v["params"]["fn"])
            values = f(fx, v["params"]) if f else None
            if values is not None:
                write_values(ORACLE, name, variant, values)
                count += 1
    print(f"definition ({AREA}): wrote {count} golden files")
    write_version(ORACLE, DEFINITION_VERSION)


if __name__ == "__main__":
    main()
