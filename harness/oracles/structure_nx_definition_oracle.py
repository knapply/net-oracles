#!/usr/bin/env python3
"""Definition oracle for NetworkX's structural tests: domination by
checking every node, regularity and the s-metric from degrees,
tournaments by every pair and reachability by search, distance
regularity from all distances, perfection by searching every node subset
for an induced odd cycle of length at least 5 in the graph or its
complement (n <= 16), AT-freeness from the definition of an asteroidal
triple, and chordality by repeatedly removing simplicial nodes (Fulkerson
and Gross 1965), the treewidth from the largest clique by enumeration,
planarity by the path-addition algorithm of Demoucron, Malgrange and
Pertuiset (1964) on each biconnected block.
Shares no code with the engine. Inputs and encodings:
../bindings/structure_nx.py.

    python3 oracles/structure_nx_definition_oracle.py
"""

from __future__ import annotations

import itertools
import sys
from collections import deque
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
AREA = "structure_nx"
MEASURES = {}
MAX_PERFECT = 16


def measure(name):
    def wrap(f):
        MEASURES[name] = f
        return f
    return wrap


def arcs(fx, directed):
    succ = {v: set() for v in range(fx.n)}
    pred = {v: set() for v in range(fx.n)}
    for a, b in zip(fx.src, fx.tgt):
        if a == b:
            continue
        succ[a].add(b)
        pred[b].add(a)
        if not directed:
            succ[b].add(a)
            pred[a].add(b)
    return succ, pred


@measure("st_dominating")
def _dom(fx, e):
    succ, _ = arcs(fx, fx.directed)

    def dominates(s):
        return all(v in s or any(v in succ[u] for u in s) for v in range(fx.n))

    return [int(dominates({v for v in range(fx.n) if v % 2 == 0})), int(dominates({0}))]


@measure("st_regular")
def _reg(fx, e):
    succ, pred = arcs(fx, fx.directed)
    if fx.directed:
        outs = [len(succ[v]) for v in range(fx.n)]
        ins = [len(pred[v]) for v in range(fx.n)]
        regular = len(set(outs)) <= 1 and len(set(ins)) <= 1
        deg = [outs[v] + ins[v] for v in range(fx.n)]
        edges = [(a, b) for a in range(fx.n) for b in succ[a]]
    else:
        deg = [len(succ[v]) for v in range(fx.n)]
        regular = len(set(deg)) <= 1
        edges = [(a, b) for a in range(fx.n) for b in succ[a] if a < b]
    return [int(regular), float(sum(deg[a] * deg[b] for a, b in edges))]


@measure("st_tournament")
def _tour(fx, e):
    succ, _ = arcs(fx, True)
    t = all((b in succ[a]) != (a in succ[b]) for a, b in itertools.combinations(range(fx.n), 2))
    if not t:
        return [0, -1]

    def reach(s):
        seen, stack = {s}, [s]
        while stack:
            for w in succ[stack.pop()]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        return seen

    return [1, int(all(len(reach(v)) == fx.n for v in range(fx.n)))]


def distances(fx):
    succ, _ = arcs(fx, False)
    d = []
    for s in range(fx.n):
        dist = {s: 0}
        q = deque([s])
        while q:
            v = q.popleft()
            for w in succ[v]:
                if w not in dist:
                    dist[w] = dist[v] + 1
                    q.append(w)
        d.append(dist)
    return succ, d


@measure("st_intersection")
def _ia(fx, e):
    succ, d = distances(fx)
    if fx.n == 0 or any(len(x) < fx.n for x in d) or len({len(succ[v]) for v in succ}) > 1:
        return [-1]
    diam = max(max(x.values()) for x in d)
    b, c = {}, {}
    for u in range(fx.n):
        for v in range(fx.n):
            i = d[u][v]
            bb = sum(1 for x in succ[v] if d[u][x] == i + 1)
            cc = sum(1 for x in succ[v] if d[u][x] == i - 1)
            if b.setdefault(i, bb) != bb or c.setdefault(i, cc) != cc:
                return [-1]
    return [b.get(j, 0) for j in range(diam)] + [c.get(j + 1, 0) for j in range(diam)]


def induced_odd_cycle(n, adj):
    for size in range(5, n + 1, 2):
        for sub in itertools.combinations(range(n), size):
            s = set(sub)
            if all(len(adj[v] & s) == 2 for v in sub):
                # 2-regular induced subgraph: a cycle if connected.
                seen, stack = {sub[0]}, [sub[0]]
                while stack:
                    for w in adj[stack.pop()] & s:
                        if w not in seen:
                            seen.add(w)
                            stack.append(w)
                if len(seen) == size:
                    return True
    return False


@measure("st_perfect")
def _perf(fx, e):
    if fx.n > MAX_PERFECT:
        return None
    succ, _ = arcs(fx, False)
    comp = {v: set(range(fx.n)) - succ[v] - {v} for v in range(fx.n)}
    return [int(not induced_odd_cycle(fx.n, succ) and not induced_odd_cycle(fx.n, comp))]


@measure("st_at_free")
def _at(fx, e):
    succ, _ = arcs(fx, False)

    def connected_avoiding(x, y, z):
        blocked = succ[z] | {z}
        if x in blocked or y in blocked:
            return False
        seen, stack = {x}, [x]
        while stack:
            for w in succ[stack.pop()]:
                if w not in seen and w not in blocked:
                    seen.add(w)
                    stack.append(w)
        return y in seen

    for a, b, c in itertools.combinations(range(fx.n), 3):
        if b in succ[a] or c in succ[a] or c in succ[b]:
            continue
        if connected_avoiding(a, b, c) and connected_avoiding(a, c, b) and connected_avoiding(b, c, a):
            return [0]
    return [1]


@measure("st_chordal")
def _ch(fx, e):
    succ, _ = arcs(fx, False)
    alive = set(range(fx.n))
    while alive:
        simplicial = next((v for v in sorted(alive)
                           if all(b in succ[a] for a, b in itertools.combinations(succ[v] & alive, 2))), None)
        if simplicial is None:
            return [0, -1]
        alive.remove(simplicial)
    best = 0

    def grow(c, cand):
        nonlocal best
        best = max(best, len(c))
        for w in sorted(cand):
            if not c or w > c[-1]:
                grow(c + [w], cand & succ[w])

    grow([], set(range(fx.n)))
    return [1, best - 1]


def blocks(n, adj):
    """Edge sets of the biconnected blocks (Hopcroft and Tarjan 1973)."""
    sys.setrecursionlimit(max(10000, 4 * n))
    disc, low, stack, out = {}, {}, [], []
    t = [0]

    def dfs(v, parent):
        disc[v] = low[v] = t[0]
        t[0] += 1
        for w in sorted(adj[v]):
            if w == parent:
                continue
            if w not in disc:
                stack.append((v, w))
                dfs(w, v)
                low[v] = min(low[v], low[w])
                if low[w] >= disc[v]:
                    block = []
                    while True:
                        e = stack.pop()
                        block.append(e)
                        if e == (v, w):
                            break
                    out.append(block)
            elif disc[w] < disc[v]:
                stack.append((v, w))
                low[v] = min(low[v], disc[w])

    for v in range(n):
        if v not in disc:
            dfs(v, None)
    return out


def block_planar(edges):
    adj = {}
    for u, v in edges:
        adj.setdefault(u, set()).add(v)
        adj.setdefault(v, set()).add(u)
    nv, ne = len(adj), len(edges)
    if ne <= 3:
        return True
    if ne > 3 * nv - 6:
        return False
    # A cycle: a path back to the start found by search from any edge.
    u0 = min(adj)
    v0 = min(adj[u0])
    prev = {v0: None}
    queue = deque([v0])
    while u0 not in prev:
        x = queue.popleft()
        for y in sorted(adj[x]):
            if y not in prev and not (x == v0 and y == u0):
                prev[y] = x
                queue.append(y)
    cycle = []
    x = u0
    while x is not None:
        cycle.append(x)
        x = prev[x]
    faces = [list(cycle), list(cycle)]
    hv = set(cycle)
    he = {frozenset(e) for e in zip(cycle, cycle[1:] + cycle[:1])}
    while len(he) < ne:
        frags = []
        for u, v in edges:
            if frozenset((u, v)) not in he and u in hv and v in hv:
                frags.append(({u, v}, [u, v]))
        seen = set()
        for s in sorted(adj):
            if s in hv or s in seen:
                continue
            comp, att, q = {s}, set(), [s]
            while q:
                x = q.pop()
                for y in adj[x]:
                    if y in hv:
                        att.add(y)
                    elif y not in comp:
                        comp.add(y)
                        q.append(y)
            seen |= comp
            frags.append((att, comp))
        choice = None
        for att, body in frags:
            ok = [i for i, f in enumerate(faces) if att <= set(f)]
            if not ok:
                return False
            if choice is None or len(ok) == 1:
                choice = (att, body, ok[0])
                if len(ok) == 1:
                    break
        att, body, fi = choice
        if isinstance(body, list):
            path = body
        else:
            a = min(att)
            prev = {a: None}
            q = deque([a])
            end = None
            while end is None:
                x = q.popleft()
                for y in sorted(adj[x]):
                    if x != a and y in att and y != a:
                        prev.setdefault(y, x)
                        end = y
                        break
                    if y in body and y not in prev:
                        prev[y] = x
                        q.append(y)
            path = []
            x = end
            while x is not None:
                path.append(x)
                x = prev[x]
            path.reverse()
        f = faces.pop(fi)
        a, b = path[0], path[-1]
        i = f.index(a)
        rot = f[i:] + f[:i]
        k = rot.index(b)
        arc1, arc2 = rot[:k + 1], rot[k:] + [a]
        inner = path[1:-1]
        faces.append(arc1 + inner[::-1])
        faces.append(arc2 + inner)
        hv |= set(path)
        he |= {frozenset(e) for e in zip(path, path[1:])}
    return True


@measure("st_planar")
def _planar(fx, e):
    succ, _ = arcs(fx, False)
    return [int(all(block_planar(b) for b in blocks(fx.n, succ)))]


@measure("st_kuratowski")
def _kur(fx, e):
    return [-1 if _planar(fx, e)[0] else 1]


@measure("st_embedding_euler")
def _euler(fx, e):
    return [1 if _planar(fx, e)[0] else -1]


def simple_weighted(fx):
    first = {}
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        if a != b:
            first.setdefault((min(a, b), max(a, b)), fx.weights[i] if fx.weights else 1.0)
    pairs = sorted(first)
    return pairs, [first[p] for p in pairs]


def edge_program(n, pairs, cost, node_lb, node_ub, total=None):
    """Integer program over edge indicators: minimize cost . x with each
    node's chosen degree in [node_lb, node_ub] (and the edge count fixed
    when total is given). None if infeasible."""
    import numpy as np
    from scipy.optimize import Bounds, LinearConstraint, milp

    if not pairs:
        ok = node_lb <= 0 and (total is None or total == 0)
        return (0.0, 0) if ok else None
    a = np.zeros((n, len(pairs)))
    for j, (u, v) in enumerate(pairs):
        a[u, j] = a[v, j] = 1
    cons = [LinearConstraint(a, lb=node_lb, ub=node_ub)]
    if total is not None:
        cons.append(LinearConstraint(np.ones((1, len(pairs))), lb=total, ub=total))
    res = milp(np.array(cost, dtype=float), constraints=cons, integrality=np.ones(len(pairs)),
               bounds=Bounds(0, 1))
    if res.status != 0:
        return None
    x = [round(v) for v in res.x]
    return sum(c * xi for c, xi in zip(cost, x)), sum(x)


@measure("st_mwm")
def _mwm(fx, e):
    pairs, w = simple_weighted(fx)
    # Maximum weight: edges of non-positive weight never help.
    best, size = edge_program(fx.n, pairs, [-x for x in w], 0, 1)
    best = -best
    # The size of a maximum-weight matching is not unique when zero-weight
    # edges or ties exist (edges 6-0 of weight 7 against 3-0 and 11-6 of
    # weights 2 and 5): report it only when every maximum-weight matching
    # has the same size, else NaN (not published; the entry is `partial`).
    card = edge_program(fx.n, pairs, [-1.0] * len(pairs), 0, 1)[1]
    sizes = []
    for k in range(card + 1):
        r = edge_program(fx.n, pairs, [-x for x in w], 0, 1, total=k)
        if r is not None and abs(-r[0] - best) <= 1e-9 * max(1.0, abs(best)):
            sizes.append(k)
    if len(sizes) > 1:
        size = float("nan")
    hi, _ = edge_program(fx.n, pairs, [-x for x in w], 0, 1, total=card)
    lo, _ = edge_program(fx.n, pairs, list(w), 0, 1, total=card)
    return [best, size, -hi, card, lo, card]


@measure("st_kfactor")
def _kfactor(fx, e):
    pairs, _ = simple_weighted(fx)
    out = []
    for k in (1, 2, 3):
        r = edge_program(fx.n, pairs, [0.0] * len(pairs), k, k)
        out.append(-1 if r is None else k * fx.n // 2)
    return out


@measure("st_edge_cover")
def _cover(fx, e):
    pairs, _ = simple_weighted(fx)
    if len({x for p in pairs for x in p}) < fx.n:
        return [-1]
    return [int(edge_program(fx.n, pairs, [1.0] * len(pairs), 1, len(pairs))[0])]


@measure("st_coloring_valid")
def _colouring_valid(fx, e):
    # Every colouring is proper by construction, and the equitable ones
    # equitable (Hajnal and Szemerédi 1970, `hajnal1970proof`): all checks
    # hold.
    return [1, 1, 1, 1, 1]


TRIADS = ("003", "012", "102", "021D", "021U", "021C", "111D", "111U", "030T",
          "030C", "201", "120D", "120U", "120C", "210", "300")


def triad_type(arc, a, b, c):
    """Holland and Leinhardt's type of the triad {a, b, c} from its dyads:
    M mutual, A asymmetric, N null, then the orientation of the asymmetric
    arcs (D: out of one node, U: into one node, C: a path or cycle, T:
    transitive)."""
    pairs = [(a, b), (a, c), (b, c)]
    mutual = [p for p in pairs if arc(*p) and arc(p[1], p[0])]
    asym = [(x, y) if arc(x, y) else (y, x) for x, y in pairs
            if arc(x, y) != arc(y, x)]
    m, s = len(mutual), len(asym)
    name = f"{m}{s}{3 - m - s}"
    if name in ("003", "012", "102", "201", "210", "300"):
        return name
    if name == "021":
        (x1, y1), (x2, y2) = asym
        if x1 == x2:
            return "021D"
        if y1 == y2:
            return "021U"
        return "021C"
    if name == "111":
        (x, y), = asym
        shared = set(mutual[0])
        return "111D" if y in shared else "111U"
    if name == "030":
        outs = [x for x, _ in asym]
        return "030C" if len(set(outs)) == 3 else "030T"
    # 120: one mutual dyad {p, q}, the third node r joined to both.
    (p, q), = mutual
    r = ({a, b, c} - {p, q}).pop()
    to_r = sum(1 for x, y in asym if y == r)
    if to_r == 0:
        return "120D"
    if to_r == 2:
        return "120U"
    return "120C"


@measure("st_triads")
def _triads(fx, e):
    arcs = {(a, b) for a, b in zip(fx.src, fx.tgt) if a != b}

    def arc(x, y):
        return (x, y) in arcs

    out = []
    for subset in (set(range(fx.n)), {v for v in range(fx.n) if v % 2 == 0}, {0} & set(range(fx.n))):
        counts = dict.fromkeys(TRIADS, 0)
        for t in itertools.combinations(range(fx.n), 3):
            if subset & set(t):
                counts[triad_type(arc, *t)] += 1
        out += [counts[t] for t in TRIADS]
    return out


def _rank(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    r = 0
    for u, v in edges:
        a, b = find(u), find(v)
        if a != b:
            parent[a] = b
            r += 1
    return r


@measure("st_polynomials")
def _polys(fx, e):
    from math import comb

    edges, _ = simple_weighted(fx)
    if len(edges) > 20:
        return [-1]
    n = fx.n
    # Chromatic: Whitney's expansion, the sum over edge subsets A of
    # (-1)^|A| x^c(A) with c(A) = n - r(A) components
    # (`whitney1932logical`).
    chrom = [0] * (n + 1)
    full = _rank(n, edges)
    ranks = []
    for mask in range(1 << len(edges)):
        sub = [edges[i] for i in range(len(edges)) if mask >> i & 1]
        ra = _rank(n, sub)
        ranks.append((len(sub), ra))
        chrom[n - ra] += (-1) ** len(sub)
    while len(chrom) > 1 and chrom[-1] == 0:
        chrom.pop()
    # Tutte: sum over edge subsets of (x - 1)^(r(E) - r(A)) (y - 1)^(|A| - r(A)).
    poly = {}
    for size, ra in ranks:
        p_, q_ = full - ra, size - ra
        for i in range(p_ + 1):
            for j in range(q_ + 1):
                poly[(i, j)] = poly.get((i, j), 0) + comb(p_, i) * comb(q_, j) * (-1) ** (p_ - i + q_ - j)
    terms = sorted((i, j, c) for (i, j), c in poly.items() if c)
    return [len(chrom)] + chrom + [len(terms)] + [v for t in terms for v in t]


@measure("st_tsp_valid")
def _tsp_valid(fx, e):
    edges, _ = simple_weighted(fx)
    seen, stack = {0}, [0]
    adj = {v: set() for v in range(fx.n)}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    while stack:
        v = stack.pop()
        for w in adj[v] - seen:
            seen.add(w)
            stack.append(w)
    if fx.n < 2 or len(seen) < fx.n:
        return [-1]
    # A connected graph always has such walks; every check holds.
    return [1, 1, 1]


@measure("st_asteroidal_valid")
def _asteroidal_valid(fx, e):
    # Whether an asteroidal triple exists, by brute force (the engine's
    # value is 1 when the returned triple is asteroidal, -1 when none is
    # returned).
    return [-1 if _at(fx, e)[0] else 1]



@measure("st_junction_valid")
def _junction_valid(fx, e):
    # A junction tree of a chordal completion is a clique tree: its cliques
    # are the completion's maximal cliques (covering every edge, none inside
    # another), each separator is the intersection of its two cliques, and
    # the cliques holding a node form a subtree (Lauritzen and Spiegelhalter
    # 1988; a maximum-weight spanning tree of the clique graph is one).
    return [1, 1, 1]


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
