#!/usr/bin/env python3
"""Definition oracle for traversals and order-exact shortest paths.

Independent of the engine and of NetworkX's code: each search is written
from its textbook definition (Moore's breadth-first search, Tarjan's
depth-first search, Dijkstra's algorithm with a queue ordered by distance
and then insertion, the bidirectional and A* variants, and the
Bellman-Ford-Moore FIFO queue), visiting each node's neighbours in the
adjacency order of a graph built from the fixture as NetworkX builds it
(nodes 0..n - 1, then edges in file order). Distances are
as floating-point sums, as NetworkX compares them. Encodings follow bindings/traversal.py.

    python3 oracles/traversal_definition_oracle.py
"""

from __future__ import annotations

import heapq
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"


def rows(fx, direction=1):
    """[(neighbour, [edge positions])] per node in insertion order."""
    r = [dict() for _ in range(fx.n)]
    for e, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        if fx.directed:
            u, v = (a, b) if direction == 1 else (b, a)
            r[u].setdefault(v, []).append(e)
        else:
            r[a].setdefault(b, []).append(e)
            if a != b:
                r[b].setdefault(a, []).append(e)
    return [list(x.items()) for x in r]


def lengths(fx, weighted, direction=1):
    """Per node, [(neighbour, length)] with the least parallel weight."""
    out = []
    for row in rows(fx, direction):
        if weighted and fx.weighted:
            out.append([(v, min(fx.weights[e] for e in es)) for v, es in row])
        else:
            out.append([(v, 1) for v, es in row])
    return out


def bfs_edges(adj, s, n, width=None, value=None):
    seen = {s}
    out = []
    queue = [s]
    i = 0
    while i < len(queue) and len(seen) < n:
        v = queue[i]
        i += 1
        nbrs = [w for w, _ in adj[v]]
        if value is not None:
            nbrs = sorted(nbrs, key=value, reverse=True)[:width]
        for w in nbrs:
            if w not in seen:
                seen.add(w)
                queue.append(w)
                out.append((v, w))
    return out


def layers(adj, s):
    seen = {s}
    cur = [s]
    out = []
    while cur:
        out.append(cur)
        nxt = []
        for v in cur:
            for w, _ in adj[v]:
                if w not in seen:
                    seen.add(w)
                    nxt.append(w)
        cur = nxt
    return out


def labeled(adj, s, directed):
    depth = {s: 0}
    queue = [s]
    done = set()
    out = []
    i = 0
    while i < len(queue):
        u = queue[i]
        i += 1
        for v, _ in adj[u]:
            if v not in depth:
                depth[v] = depth[u] + 1
                queue.append(v)
                out.append((u, v, 0))
            elif depth[v] == depth[u]:
                if v not in done:
                    out.append((u, v, 1))
            elif depth[v] > depth[u]:
                out.append((u, v, 2))
            elif directed:
                out.append((u, v, 3))
        if not directed:
            done.add(u)
    return out


def dfs_events(adj, n):
    visited = set()
    out = []

    for s in range(n):
        if s in visited:
            continue
        out.append((s, s, 0))
        visited.add(s)
        stack = [(s, 0)]
        while stack:
            v, i = stack[-1]
            if i < len(adj[v]):
                stack[-1] = (v, i + 1)
                w = adj[v][i][0]
                if w in visited:
                    out.append((v, w, 1))
                else:
                    out.append((v, w, 0))
                    visited.add(w)
                    stack.append((w, 0))
            else:
                stack.pop()
                if stack:
                    out.append((stack[-1][0], v, 2))
        out.append((s, s, 2))
    return out


def edge_offers(fx, orientation):
    """Per node, the edges it offers: (source, target, position, reverse)."""
    out_rows = rows(fx, 1)
    in_rows = rows(fx, 2) if fx.directed else None
    offers = []
    for v in range(fx.n):
        lst = []
        if not (fx.directed and orientation == "reverse"):
            lst += [(v, w, e, 0) for w, es in out_rows[v] for e in es]
        if fx.directed and orientation in ("reverse", "ignore"):
            lst += [(w, v, e, 1) for w, es in in_rows[v] for e in es]
        offers.append(lst)
    return offers


def edge_bfs(fx, orientation):
    offers = edge_offers(fx, orientation)
    seen_nodes = set(range(fx.n))
    seen_edges = set()
    out = []
    for v in range(fx.n):  # every node starts in the queue
        for t, h, e, r in offers[v]:
            if e not in seen_edges:
                seen_edges.add(e)
                out.append((t, h, e, r))
    del seen_nodes
    return out


def edge_dfs(fx, orientation):
    offers = edge_offers(fx, orientation)
    pos = [0] * fx.n
    seen = set()
    out = []
    for s in range(fx.n):
        stack = [s]
        while stack:
            v = stack[-1]
            if pos[v] >= len(offers[v]):
                stack.pop()
                continue
            t, h, e, r = offers[v][pos[v]]
            pos[v] += 1
            if e not in seen:
                seen.add(e)
                stack.append(t if r else h)
                out.append((t, h, e, r))
    return out


def dijkstra(adj, s, want_preds=False):
    dist, seen, parent, preds, reached = {}, {s: 0}, {}, {s: []}, [s]
    heap = [(0, 0, s)]
    c = 1
    order = []
    while heap:
        d, _, v = heapq.heappop(heap)
        if v in dist:
            continue
        dist[v] = d
        order.append(v)
        for u, w in adj[v]:
            nd = d + w
            if u in dist:
                if nd == dist[u]:
                    preds[u].append(v)
            elif u not in seen or nd < seen[u]:
                if u not in seen:
                    reached.append(u)
                seen[u] = nd
                heapq.heappush(heap, (nd, c, u))
                c += 1
                parent[u] = v
                preds[u] = [v]
            elif nd == seen[u]:
                preds[u].append(v)
    if want_preds:
        return [tuple([v] + preds[v]) for v in reached]
    return [(v, dist[v], parent.get(v, -1)) for v in order]


def bellman_ford(adj, s, n):
    dist, preds, order = {s: 0}, {s: []}, [s]
    queue, in_q, count = [s], {s}, {}
    i = 0
    while i < len(queue):
        u = queue[i]
        i += 1
        in_q.discard(u)
        if any(p in in_q for p in preds[u]):
            continue
        for v, w in adj[u]:
            nd = dist[u] + w
            if v not in dist or nd < dist[v]:
                if v not in in_q:
                    queue.append(v)
                    in_q.add(v)
                    count[v] = count.get(v, 0) + 1
                if v not in dist:
                    order.append(v)
                dist[v] = nd
                preds[v] = [u]
            elif nd == dist[v]:
                preds[v].append(u)
    return [tuple([v, dist[v]] + preds[v]) for v in order]


def bidir_bfs(out_adj, in_adj, s, t):
    if s == t:
        return [s]
    pred, succ = {s: None}, {t: None}
    ff, rf = [s], [t]
    while ff and rf:
        if len(ff) <= len(rf):
            this, ff = ff, []
            for v in this:
                for w, _ in out_adj[v]:
                    if w not in pred:
                        ff.append(w)
                        pred[w] = v
                    if w in succ:
                        return walk(pred, succ, w)
        else:
            this, rf = rf, []
            for v in this:
                for w, _ in in_adj[v]:
                    if w not in succ:
                        succ[w] = v
                        rf.append(w)
                    if w in pred:
                        return walk(pred, succ, w)
    return []


def walk(pred, succ, w):
    path = []
    x = w
    while x is not None:
        path.append(x)
        x = pred[x]
    path.reverse()
    x = succ[w]
    while x is not None:
        path.append(x)
        x = succ[x]
    return path


def bidir_dijkstra(out_adj, in_adj, s, t):
    if s == t:
        return [s, 0]
    adj = [out_adj, in_adj]
    dists, seen = [{}, {}], [{s: 0}, {t: 0}]
    preds = [{s: None}, {t: None}]
    heaps = [[(0, 0, s)], [(0, 1, t)]]
    c = 2
    final, meet, d_ = None, None, 1
    while heaps[0] and heaps[1]:
        d_ = 1 - d_
        dist, _, v = heapq.heappop(heaps[d_])
        if v in dists[d_]:
            continue
        dists[d_][v] = dist
        if v in dists[1 - d_]:
            path = []
            x = meet
            while x is not None:
                path.append(x)
                x = preds[0][x]
            path.reverse()
            x = preds[1][meet]
            while x is not None:
                path.append(x)
                x = preds[1][x]
            return path + [final]
        for w, l in adj[d_][v]:
            nd = dist + l
            if w in dists[d_]:
                continue
            if w not in seen[d_] or nd < seen[d_][w]:
                seen[d_][w] = nd
                heapq.heappush(heaps[d_], (nd, c, w))
                c += 1
                preds[d_][w] = v
                if w in seen[1 - d_]:
                    fw = nd + seen[1 - d_][w]
                    if final is None or final > fw:
                        final, meet = fw, w
    return []


def astar(adj, s, t):
    heap = [(0, 0, s, 0, None)]
    c = 1
    enq, explored = {}, {}
    while heap:
        _, _, cur, dist, par = heapq.heappop(heap)
        if cur == t:
            path = [cur]
            x = par
            while x is not None:
                path.append(x)
                x = explored[x]
            return path[::-1]
        if cur in explored:
            if explored[cur] is None or enq[cur] < dist:
                continue
        explored[cur] = par
        for w, l in adj[cur]:
            nd = dist + l
            if w in enq and enq[w] <= nd:
                continue
            enq[w] = nd
            heapq.heappush(heap, (nd, c, w, nd, cur))
            c += 1
    return []


def compute(spec, fx):
    e = spec["params"]
    fn = e["fn"]
    if fx.n == 0:
        return []
    adj = lengths(fx, e.get("weighted", fn in ("ord_bidir_dijkstra", "ord_astar")))
    inv = lengths(fx, e.get("weighted", fn in ("ord_bidir_dijkstra", "ord_astar")), 2) \
        if fx.directed else adj
    f = float
    if fn == "trav_bfs_edges":
        return [(f(a), f(b)) for a, b in bfs_edges(adj, 0, fx.n)]
    if fn == "trav_beam":
        return [(f(a), f(b)) for a, b in bfs_edges(adj, 0, fx.n, e.get("width", 2),
                                                   lambda v: (v * 7) % 5)]
    if fn == "trav_bfs_layers":
        return [tuple(f(v) for v in layer) for layer in layers(adj, 0)]
    if fn == "trav_bfs_labeled":
        return [tuple(f(x) for x in t) for t in labeled(adj, 0, fx.directed)]
    if fn == "trav_dfs_events":
        return [tuple(f(x) for x in t) for t in dfs_events(adj, fx.n)]
    if fn == "trav_edge_bfs":
        return [tuple(f(x) for x in t) for t in edge_bfs(fx, e.get("orientation", "none"))]
    if fn == "trav_edge_dfs":
        return [tuple(f(x) for x in t) for t in edge_dfs(fx, e.get("orientation", "none"))]
    if fn == "ord_dijkstra":
        return [tuple(f(x) for x in t) for t in dijkstra(adj, 0, e.get("preds", False))]
    if fn == "ord_bellman_ford":
        return [tuple(f(x) for x in t) for t in bellman_ford(adj, 0, fx.n)]
    if fn == "ord_bidir_bfs":
        return [f(v) for v in bidir_bfs(adj, inv, 0, fx.n - 1)]
    if fn == "ord_bidir_dijkstra":
        return [f(v) for v in bidir_dijkstra(adj, inv, 0, fx.n - 1)]
    if fn == "ord_astar":
        return [f(v) for v in astar(adj, 0, fx.n - 1)]
    raise ValueError(fn)


def main() -> int:
    manifest = load_area("traversal")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        tags = set(fx.tags) | {"directed" if fx.directed else "undirected"}
        for variant, spec in manifest.items():
            ospec = spec["oracles"].get(ORACLE)
            if (ospec is None or not applies(spec, fx) or name in ospec.get("undefined_on", [])
                    or tags & set(ospec.get("undefined_when", []))):
                continue
            write_values(ORACLE, name, variant, compute(spec, fx))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (traversal): wrote {count} golden files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
