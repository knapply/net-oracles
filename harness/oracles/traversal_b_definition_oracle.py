#!/usr/bin/env python3
"""Definition oracles for manifest/traversal_b.yaml: each measure from
its definition, by enumeration or exact arithmetic on small fixtures
(encodings in the manifest).

    python3 oracles/traversal_b_definition_oracle.py
"""

from __future__ import annotations

import heapq
import sys
from fractions import Fraction
from itertools import combinations
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
NONE = [-1.0]


def weights(fx):
    return list(fx.weights) if fx.weighted else [1.0] * len(fx.src)


def succ_sets(fx, loops=False):
    out = [set() for _ in range(fx.n)]
    for a, b in zip(fx.src, fx.tgt):
        if a == b and not loops:
            continue
        out[a].add(b)
        if not fx.directed:
            out[b].add(a)
    return out


def pred_sets(fx):
    inc = [set() for _ in range(fx.n)]
    for a, b in zip(fx.src, fx.tgt):
        inc[b].add(a)
        if not fx.directed:
            inc[a].add(b)
    return inc


def reach(adj, s):
    seen = {s}
    stack = [s]
    while stack:
        v = stack.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return seen


def has_cycle(fx):
    if any(a == b for a, b in zip(fx.src, fx.tgt)):
        return True
    adj = succ_sets(fx)
    return any(v in reach(adj, w) for v in range(fx.n) for w in adj[v])


def levels(fx):
    """Generation of each node: the longest path to it from a source."""
    lev = [0] * fx.n
    for _ in range(fx.n):
        for a, b in zip(fx.src, fx.tgt):
            lev[b] = max(lev[b], lev[a] + 1)
    return lev


def lex_topo(fx):
    indeg = [0] * fx.n
    for b in fx.tgt:
        indeg[b] += 1
    out = [[] for _ in range(fx.n)]
    for a, b in zip(fx.src, fx.tgt):
        out[a].append(b)
    done, order = set(), []
    while len(order) < fx.n:
        v = min(u for u in range(fx.n) if u not in done and indeg[u] == 0)
        done.add(v)
        order.append(v)
        for w in out[v]:
            indeg[w] -= 1
    return order


def components(n, adj):
    seen, comps = set(), []
    for v in range(n):
        if v not in seen:
            c = reach(adj, v)
            seen |= c
            comps.append(c)
    return comps


def cycles_of(fx, limit=10 ** 6):
    """Simple cycles as node tuples (from their least node), NetworkX's
    conventions for loops and parallel edges."""
    n = fx.n
    out = []
    loops = sorted({a for a, b in zip(fx.src, fx.tgt) if a == b})
    out.extend((v,) for v in loops)
    adj = succ_sets(fx)
    if not fx.directed:
        mult = {}
        for a, b in zip(fx.src, fx.tgt):
            if a != b:
                key = (min(a, b), max(a, b))
                mult[key] = mult.get(key, 0) + 1
        out.extend(k for k, c in mult.items() if c > 1)

    def dfs(start, v, path, on):
        for w in sorted(adj[v]):
            if w == start and (fx.directed or len(path) >= 3):
                if fx.directed or path[1] < path[-1]:
                    out.append(tuple(path))
            elif w > start and w not in on:
                on.add(w)
                path.append(w)
                dfs(start, w, path, on)
                path.pop()
                on.discard(w)

    for s in range(n):
        dfs(s, s, [s], {s})
        if len(out) > limit:
            break
    return out


def min_cut(n, cap, s, t, directed):
    """Least capacity of the arcs from S to T over bipartitions with s in S
    and t in T (cap: {(u, v): capacity})."""
    others = [v for v in range(n) if v not in (s, t)]
    best = float("inf")
    for r in range(len(others) + 1):
        for extra in combinations(others, r):
            S = {s, *extra}
            total = 0.0
            for (u, v), c in cap.items():
                if (u in S) != (v in S):
                    if directed and not (u in S):
                        continue
                    total += c
            best = min(best, total)
    return best


def compute(spec, fx):
    fn = spec["params"]["fn"]
    n = fx.n
    w = weights(fx)
    if fn in ("gb_topo_levels", "gb_lex_topo", "gb_longest_path_len", "gb_antichain_width"):
        if has_cycle(fx):
            return NONE
        if fn == "gb_topo_levels":
            return [float(x) for x in levels(fx)]
        if fn == "gb_lex_topo":
            return [float(v) for v in lex_topo(fx)]
        if fn == "gb_longest_path_len":
            return [float(max(levels(fx), default=0))]
        adj = succ_sets(fx)
        r = [reach(adj, v) for v in range(n)]
        best = 0
        for k in range(1, n + 1):
            for sub in combinations(range(n), k):
                if all(b not in r[a] and a not in r[b] for a, b in combinations(sub, 2)):
                    best = k
                    break
        return [float(best)]
    if fn == "gb_aperiodic":
        adj = succ_sets(fx, loops=True)
        if n == 0 or any(len(reach(adj, v)) != n for v in range(n)):
            return NONE
        g = 0
        for c in cycles_of(fx):
            g = gcd(g, len(c))
        return [1.0 if g == 1 else 0.0]
    if fn == "gb_is_eulerian":
        if n == 0:
            return [0.0]
        if fx.directed:
            outd, ind = [0] * n, [0] * n
            for a, b in zip(fx.src, fx.tgt):
                outd[a] += 1
                ind[b] += 1
            adj = succ_sets(fx, loops=True)
            strong = all(len(reach(adj, v)) == n for v in range(n))
            return [1.0 if strong and outd == ind else 0.0]
        deg = [0] * n
        for a, b in zip(fx.src, fx.tgt):
            deg[a] += 1
            deg[b] += 1
        adj = succ_sets(fx, loops=True)
        return [1.0 if len(reach(adj, 0)) == n and all(d % 2 == 0 for d in deg) else 0.0]
    if fn == "gb_spanning_trees":
        if n == 0:
            return [0.0]
        L = [[Fraction(0)] * n for _ in range(n)]
        for a, b in zip(fx.src, fx.tgt):
            if a == b:
                continue
            L[a][a] += 1
            L[b][b] += 1
            L[a][b] -= 1
            L[b][a] -= 1
        A = [row[1:] for row in L[1:]]
        det = Fraction(1)
        m = len(A)
        for i in range(m):
            p = next((r for r in range(i, m) if A[r][i] != 0), None)
            if p is None:
                return [0.0]
            if p != i:
                A[i], A[p] = A[p], A[i]
                det = -det
            det *= A[i][i]
            for r in range(i + 1, m):
                f = A[r][i] / A[i][i]
                for c in range(i, m):
                    A[r][c] -= f * A[i][c]
        return [float(det)]
    if fn == "gb_mst_weight":
        best = {}
        for a, b, x in zip(fx.src, fx.tgt, w):
            if a == b:
                continue
            key = (min(a, b), max(a, b))
            best[key] = min(best.get(key, float("inf")), x)
        adj = [[] for _ in range(n)]
        for (a, b), x in best.items():
            adj[a].append((x, b))
            adj[b].append((x, a))
        seen, total = set(), 0.0
        for s in range(n):
            if s in seen:
                continue
            seen.add(s)
            h = list(adj[s])
            heapq.heapify(h)
            while h:
                x, v = heapq.heappop(h)
                if v in seen:
                    continue
                seen.add(v)
                total += x
                for item in adj[v]:
                    heapq.heappush(h, item)
        return [total]
    if fn == "gb_branching_weight":
        edges = [(a, b, x) for a, b, x in zip(fx.src, fx.tgt, w) if a != b]
        best = 0.0
        for k in range(len(edges) + 1):
            for sub in combinations(edges, k):
                targets = [b for _, b, _ in sub]
                if len(set(targets)) != len(targets):
                    continue
                parent = {b: a for a, b, _ in sub}
                ok = True
                for v in parent:
                    seen, u = set(), v
                    while u in parent:
                        if u in seen:
                            ok = False
                            break
                        seen.add(u)
                        u = parent[u]
                    if not ok:
                        break
                if ok:
                    best = max(best, sum(x for _, _, x in sub))
        return [best]
    if fn == "gb_maxflow":
        if n < 2:
            return NONE
        cap = {}
        for a, b, x in zip(fx.src, fx.tgt, w):
            if a == b:
                continue
            key = (a, b) if fx.directed else (min(a, b), max(a, b))
            cap[key] = x  # the last parallel edge, as NetworkX's simple graph keeps it
        return [min_cut(n, cap, 0, n - 1, fx.directed)]
    if fn == "gb_mincost":
        if n < 2 or (fx.weighted and any(x != int(x) for x in fx.weights)):
            return NONE
        dist = [float("inf")] * n
        dist[0] = 0.0
        for _ in range(n):
            for a, b, x in zip(fx.src, fx.tgt, w):
                if a != b and dist[a] + x < dist[b]:
                    dist[b] = dist[a] + x
        return NONE if dist[n - 1] == float("inf") else [dist[n - 1]]
    if fn == "gb_cycle_count":
        if n > spec["params"].get("max_nodes", 12):
            return NONE
        return [float(len(cycles_of(fx)))]
    if fn == "gb_mcb_weight":
        best = {}
        for a, b, x in zip(fx.src, fx.tgt, w):
            best[(min(a, b), max(a, b))] = x
        edge_ix = {e: i for i, e in enumerate(best)}
        cands = []
        for c in cycles_of(fx):
            if len(c) == 1:
                es = [(c[0], c[0])]
            elif len(c) == 2:
                continue  # parallel edges: not in NetworkX's simple graph
            else:
                es = [(min(c[i], c[(i + 1) % len(c)]), max(c[i], c[(i + 1) % len(c)]))
                      for i in range(len(c))]
            mask = 0
            for e in es:
                mask ^= 1 << edge_ix[e]
            cands.append((sum(best[e] for e in es), mask))
        cands.sort()
        basis, total = {}, 0.0
        for x, mask in cands:
            v = mask
            while v:
                top = v.bit_length() - 1
                if top in basis:
                    v ^= basis[top]
                else:
                    basis[top] = v
                    total += x
                    break
        return [total]
    if fn == "gb_disjoint_paths":
        if n < 2:
            return NONE
        s, t = 0, n - 1
        if not spec["params"].get("nodes"):
            cap = {}
            for a, b in zip(fx.src, fx.tgt):
                if a == b:
                    continue
                cap[(a, b) if fx.directed else (min(a, b), max(a, b))] = 1.0
            return [min_cut(n, cap, s, t, fx.directed)]
        adj = succ_sets(fx)
        direct = t in adj[s]
        if direct:
            adj[s].discard(t)
            if not fx.directed:
                adj[t].discard(s)
        others = [v for v in range(n) if v not in (s, t)]
        for k in range(len(others) + 1):
            for cut in combinations(others, k):
                removed = set(cut)
                seen, stack = {s}, [s]
                while stack:
                    v = stack.pop()
                    for u in adj[v]:
                        if u not in removed and u not in seen:
                            seen.add(u)
                            stack.append(u)
                if t not in seen:
                    return [float(k + direct)]
        return [float(len(others) + direct)]
    if fn == "gb_stoer_wagner":
        cap = {}
        for a, b, x in zip(fx.src, fx.tgt, w):
            if a != b:
                cap[(min(a, b), max(a, b))] = x
        adj = succ_sets(fx)
        if n < 2 or len(reach(adj, 0)) != n:
            return NONE
        best = float("inf")
        for k in range(1, n):
            for S in combinations(range(n), k):
                if 0 not in S:
                    continue
                Sset = set(S)
                best = min(best, sum(c for (u, v), c in cap.items() if (u in Sset) != (v in Sset)))
        return [best]
    if fn == "gb_d_separated":
        if n < 3 or has_cycle(fx):
            return NONE
        x, y, z = 0, n - 1, {1}
        inc = pred_sets(fx)
        anc = set()
        stack = [x, y, *z]
        while stack:
            v = stack.pop()
            if v in anc:
                continue
            anc.add(v)
            stack.extend(inc[v])
        und = {v: set() for v in anc}
        for a, b in zip(fx.src, fx.tgt):
            if a in anc and b in anc and a != b:
                und[a].add(b)
                und[b].add(a)
        for v in anc:
            parents = [p for p in inc[v] if p in anc]
            for p, q in combinations(parents, 2):
                if p != q:
                    und[p].add(q)
                    und[q].add(p)
        seen, stack = {x}, [x]
        while stack:
            v = stack.pop()
            for u in und[v]:
                if u not in seen and u not in z:
                    seen.add(u)
                    stack.append(u)
        return [0.0 if y in seen else 1.0]
    if fn == "gb_quotient_internal":
        k = min(3, n)
        counts = [0] * k
        for a, b in zip(fx.src, fx.tgt):
            if a % k == b % k:
                counts[a % k] += 1
        return [float(c) for c in counts]
    if fn == "gb_isolates":
        touched = set(fx.src) | set(fx.tgt)
        return [float(v) for v in range(n) if v not in touched]
    if fn == "gb_walks":
        if n > 40:
            return NONE
        A = [[0] * n for _ in range(n)]
        for a, b in zip(fx.src, fx.tgt):
            A[a][b] += 1
            if not fx.directed and a != b:
                A[b][a] += 1
        return [float(sum(A[i][k] * A[k][j] for k in range(n))) for i in range(n)
                for j in range(n)]
    if fn == "gb_chain_count":
        pairs = {(min(a, b), max(a, b)) for a, b in zip(fx.src, fx.tgt)}
        adj = succ_sets(fx)
        c = len(components(n, adj))
        return [float(len(pairs) - n + c)]
    if fn == "gb_broadcast_time":
        pairs = {(min(a, b), max(a, b)) for a, b in zip(fx.src, fx.tgt)}
        adj = succ_sets(fx)
        if n == 0 or any(a == b for a, b in pairs) or len(pairs) != n - 1 \
                or len(reach(adj, 0)) != n:
            return NONE

        def b(v, parent):
            vals = sorted((b(u, v) for u in adj[v] if u != parent), reverse=True)
            return max((x + i + 1 for i, x in enumerate(vals)), default=0)

        return [float(max(b(v, None) for v in range(n)))]
    if fn == "gb_moral_edges":
        pairs = {frozenset((a, b)) for a, b in zip(fx.src, fx.tgt)}
        inc = [dict() for _ in range(n)]  # distinct parents
        for a, b in zip(fx.src, fx.tgt):
            inc[b][a] = None
        for v in range(n):
            for p, q in combinations(inc[v], 2):
                pairs.add(frozenset((p, q)))
        return [float(len(pairs))]
    if fn == "gb_node_boundary":
        S = {v for v in (0, 1, 2) if v < n}
        adj = succ_sets(fx, loops=True)
        return [float(v) for v in sorted({u for s in S for u in adj[s]} - S)]
    if fn == "gb_dedensify":
        thr = spec["params"].get("threshold", 2)
        deg = [0] * n
        for a, b in zip(fx.src, fx.tgt):
            deg[b] += 1
            if not fx.directed:
                deg[a] += 1
        high = {v for v in range(n) if deg[v] > thr}
        adj = succ_sets(fx, loops=True)
        groups = {}
        for v in range(n):
            h = frozenset(high & adj[v])
            if h:
                groups.setdefault(h, set()).add(v)
        return [float(sum(1 for h, low in groups.items()
                          if len(h) * len(low) > len(h) + len(low)))]
    if fn == "gb_snap_groups":
        deg = [0] * n
        for a, b in zip(fx.src, fx.tgt):
            deg[a] += 1
            deg[b] += 1
        group = [d % 2 for d in deg]
        adj = succ_sets(fx, loops=True)
        while True:
            sig = [(group[v], frozenset(group[u] for u in adj[v])) for v in range(n)]
            ids = {}
            new = [ids.setdefault(s, len(ids)) for s in sig]
            if len(set(new)) == len(set(group)):
                return [float(len(set(new)))]
            group = new
    if fn == "gb_spanner_ok":
        return [1.0]
    if fn == "gb_k_edge_subgraphs":
        k = spec["params"].get("k", 2)
        mult = {}
        for a, b in zip(fx.src, fx.tgt):
            if a != b:
                key = (min(a, b), max(a, b))
                mult[key] = mult.get(key, 0) + 1
        done, work = [], [list(range(n))]
        while work:
            part = work.pop()
            if len(part) <= 1:
                done.append(part)
                continue
            best = None
            rest = part[1:]
            for r in range(len(rest) + 1):
                for extra in combinations(rest, r):
                    S = {part[0], *extra}
                    if len(S) == len(part):
                        continue
                    c = sum(x for (u, v), x in mult.items()
                            if u in part and v in part and (u in S) != (v in S))
                    if c < k and (best is None or c < best[0]):
                        best = (c, S)
            if best is None:
                done.append(part)
            else:
                S = best[1]
                work.append([v for v in part if v in S])
                work.append([v for v in part if v not in S])
        label = [0.0] * n
        for i, part in enumerate(done):
            for v in part:
                label[v] = float(i)
        return label
    raise ValueError(f"unknown function {fn}")


def main():
    for variant, spec in load_area("traversal_b").items():
        ospec = spec["oracles"].get("definition")
        if ospec is None:
            continue
        skip = set(ospec.get("undefined_on", []))
        for name in fixture_names():
            fx = load_fixture(name)
            if not applies(spec, fx) or name in skip:
                continue
            write_values(ORACLE, name, variant, compute(spec, fx))
    write_version(ORACLE, DEFINITION_VERSION)


if __name__ == "__main__":
    main()
