#!/usr/bin/env python3
"""Definition oracle for the graph theory and combinatorics measures:
brute force from the definitions (forbidden subgraphs, subset enumeration,
all permutations, Floyd-Warshall, direct-sum zeta functions). Shares no code
with the engine. Inputs and encodings: ../bindings/graph_theory.py.

    python3 oracles/graph_theory_definition_oracle.py
"""

from __future__ import annotations

import itertools
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
AREA = "graph_theory"
MEASURES = {}
NAN = float("nan")


def measure(*names):
    def wrap(f):
        for name in names:
            MEASURES[name] = f
        return f
    return wrap


def pairs_of(fx, directed):
    out = set()
    for a, b in zip(fx.src, fx.tgt):
        if a != b:
            out.add((a, b) if directed else (min(a, b), max(a, b)))
    return out


def candidate(rule, n):
    return {"all": list(range(n)), "even": [v for v in range(n) if v % 2 == 0],
            "first3": list(range(min(3, n)))}[rule]


# ---- completeness, cliques ------------------------------------------------------
@measure("gt_is_complete")
def _complete(fx, e):
    p = pairs_of(fx, fx.directed)
    need = fx.n * (fx.n - 1) // (1 if fx.directed else 2)
    return [int(len(p) == need)]


@measure("gt_is_clique_all", "gt_is_clique_even", "gt_is_clique_first3", "gt_is_clique_even_mutual")
def _clique(fx, e):
    members = candidate(e["candidate"], fx.n)
    arcs = bool(e.get("directed")) and fx.directed
    p = pairs_of(fx, arcs)
    ok = True
    for a, b in itertools.combinations(members, 2):
        if arcs:
            ok &= (a, b) in p and (b, a) in p
        else:
            ok &= (a, b) in p
    return [int(ok)]


# ---- threshold graphs ------------------------------------------------------------
def is_threshold_by_subgraphs(fx):
    p = pairs_of(fx, False)
    adj = [[False] * fx.n for _ in range(fx.n)]
    for a, b in p:
        adj[a][b] = adj[b][a] = True
    for quad in itertools.combinations(range(fx.n), 4):
        edges = [(a, b) for a, b in itertools.combinations(quad, 2) if adj[a][b]]
        degree = sorted(sum(1 for e in edges if v in e) for v in quad)
        if (len(edges) == 3 and degree == [1, 1, 2, 2] or
                len(edges) == 4 and degree == [2, 2, 2, 2] or
                len(edges) == 2 and degree == [1, 1, 1, 1]):
            return False
    return True


@measure("gt_threshold_is")
def _threshold_is(fx, e):
    return [int(is_threshold_by_subgraphs(fx))]


@measure("gt_threshold_types")
def _threshold_types(fx, e):
    p = pairs_of(fx, False)
    left = set(range(fx.n))
    peeled = []
    while left:
        degree = {v: sum(1 for u in left if u != v and (min(u, v), max(u, v)) in p) for v in left}
        iso = [v for v in sorted(left) if degree[v] == 0]
        dom = [v for v in sorted(left) if degree[v] == len(left) - 1]
        if iso:
            v, kind = iso[0], 0
        elif dom:
            v, kind = dom[0], 1
        else:
            return [-1]
        left.discard(v)
        peeled.append(kind)
    if peeled:
        peeled[-1] = 1
    return peeled[::-1]


@measure("gt_threshold_valid")
def _threshold_valid(fx, e):
    return [1] if is_threshold_by_subgraphs(fx) else [-1]


# ---- feedback sets ------------------------------------------------------------------
def acyclic(n, edges, directed):
    """No cycle among the edges (a loop is a cycle; undirected parallel edges
    are a cycle)."""
    if any(a == b for a, b in edges):
        return False
    if directed:
        indeg = [0] * n
        out = [[] for _ in range(n)]
        for a, b in edges:
            indeg[b] += 1
            out[a].append(b)
        stack = [v for v in range(n) if indeg[v] == 0]
        seen = 0
        while stack:
            v = stack.pop()
            seen += 1
            for w in out[v]:
                indeg[w] -= 1
                if indeg[w] == 0:
                    stack.append(w)
        return seen == n
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb
    return True


def components(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for a, b in edges:
        parent[find(a)] = find(b)
    return len({find(v) for v in range(n)})


def scc_groups(n, arcs):
    """Strongly connected components by mutual reachability (Floyd-Warshall)."""
    reach = [[i == j for j in range(n)] for i in range(n)]
    for a, b in arcs:
        reach[a][b] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    if reach[k][j]:
                        reach[i][j] = True
    seen, groups = set(), []
    for v in range(n):
        if v not in seen:
            g = [u for u in range(n) if reach[v][u] and reach[u][v]]
            seen.update(g)
            groups.append(g)
    return groups


def directed_fas_size(fx):
    loops = sum(1 for a, b in zip(fx.src, fx.tgt) if a == b)
    arcs = [(a, b) for a, b in zip(fx.src, fx.tgt) if a != b]
    total = loops
    for group in scc_groups(fx.n, arcs):
        if len(group) < 2:
            continue
        index = {v: i for i, v in enumerate(group)}
        inner = [(index[a], index[b]) for a, b in arcs if a in index and b in index]
        k = len(group)
        if len(inner) <= 20:
            for size in range(len(inner) + 1):
                if any(acyclic(k, [x for i, x in enumerate(inner) if i not in cut], True)
                       for cut in itertools.combinations(range(len(inner)), size)):
                    total += size
                    break
        else:
            mult = [[0] * k for _ in range(k)]
            for a, b in inner:
                mult[a][b] += 1
            best = [0] * (1 << k)
            for subset in range(1, 1 << k):
                cost = None
                for v in range(k):
                    if subset >> v & 1:
                        before = subset & ~(1 << v)
                        extra = sum(mult[v][u] for u in range(k) if before >> u & 1)
                        c = best[before] + extra
                        cost = c if cost is None else min(cost, c)
                best[subset] = cost
            total += best[(1 << k) - 1]
    return total


@measure("gt_fas_size")
def _fas_size(fx, e):
    if fx.directed:
        return [directed_fas_size(fx)]
    edges = list(zip(fx.src, fx.tgt))
    return [len(edges) - (fx.n - components(fx.n, edges))]


@measure("gt_fas_valid", "gt_fas_eades_valid")
def _fas_one(fx, e):
    return [1]


@measure("gt_fas_eades_bound")
def _fas_bound(fx, e):
    return [1]


@measure("gt_fvs_size")
def _fvs_size(fx, e):
    edges = list(zip(fx.src, fx.tgt))
    forced = {a for a, b in edges if a == b}
    free = [v for v in range(fx.n) if v not in forced]
    for size in range(len(free) + 1):
        for cut in itertools.combinations(free, size):
            gone = forced | set(cut)
            kept = [(a, b) for a, b in edges if a not in gone and b not in gone]
            if acyclic(fx.n, kept, fx.directed):
                return [len(forced) + size]
    raise AssertionError("removing every node leaves no cycle")


@measure("gt_fvs_valid")
def _fvs_one(fx, e):
    return [1]


# ---- approximate matchings -------------------------------------------------------------
def weight_of(fx, i):
    return fx.weights[i] if fx.weights else 1.0


@measure("gt_match_greedy")
def _greedy(fx, e):
    order = sorted((i for i in range(len(fx.src)) if fx.src[i] != fx.tgt[i] and weight_of(fx, i) > 0),
                   key=lambda i: (-weight_of(fx, i), i))
    used, chosen = set(), []
    for i in order:
        a, b = fx.src[i], fx.tgt[i]
        if a not in used and b not in used:
            used |= {a, b}
            chosen.append(i)
    return sorted(chosen)


@measure("gt_match_path_growing")
def _growing(fx, e):
    rows = [[] for _ in range(fx.n)]
    for i in range(len(fx.src)):
        a, b = fx.src[i], fx.tgt[i]
        if a != b and weight_of(fx, i) > 0:
            rows[a].append((b, weight_of(fx, i), i))
            rows[b].append((a, weight_of(fx, i), i))
    alive = [True] * fx.n
    halves = ([], [])
    for start in range(fx.n):
        if not alive[start]:
            continue
        node, side = start, 0
        while True:
            options = [(w, -i, u) for u, w, i in rows[node] if alive[u]]
            alive[node] = False
            if not options:
                break
            w, neg, u = max(options)
            halves[side].append((-neg, w))
            side ^= 1
            node = u
    total = [sum(w for _, w in h) for h in halves]
    pick = 1 if total[1] > total[0] else 0
    return sorted(i for i, _ in halves[pick])


@measure("gt_match_valid")
def _match_valid(fx, e):
    return [1, 1, 1]


# ---- diversity ---------------------------------------------------------------------------
@measure("gt_diversity", "gt_diversity_weighted")
def _diversity(fx, e):
    weighted = bool(e.get("weighted"))
    incident = [[] for _ in range(fx.n)]
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        if a != b:
            w = weight_of(fx, i) if weighted else 1.0
            incident[a].append(w)
            incident[b].append(w)
    out = []
    for row in incident:
        total = sum(row)
        if len(row) < 2 or total <= 0:
            out.append(NAN)
            continue
        entropy = -sum(w / total * math.log(w / total) for w in row if w > 0)
        out.append(entropy / math.log(len(row)))
    return out


# ---- Voronoi cells ------------------------------------------------------------------------
def distances(fx):
    inf = float("inf")
    d = [[inf] * fx.n for _ in range(fx.n)]
    for v in range(fx.n):
        d[v][v] = 0.0
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        w = weight_of(fx, i) if fx.weighted else 1.0
        d[a][b] = min(d[a][b], w)
        if not fx.directed:
            d[b][a] = min(d[b][a], w)
    for k in range(fx.n):
        for i in range(fx.n):
            for j in range(fx.n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return d


def centers_of(n):
    return [0, n // 2] if n >= 2 else [0]


@measure("gt_voronoi_distance")
def _voronoi_distance(fx, e):
    d = distances(fx)
    out = []
    for v in range(fx.n):
        best = min(d[c][v] for c in centers_of(fx.n))
        out.append(-1.0 if math.isinf(best) else best)
    return out


@measure("gt_voronoi_cells")
def _voronoi_cells(fx, e):
    d = distances(fx)
    centers = centers_of(fx.n)
    out = []
    for v in range(fx.n):
        best = min((d[c][v], i) for i, c in enumerate(centers))
        out.append(-1 if math.isinf(best[0]) else best[1])
    return out


# ---- travelling salesman ---------------------------------------------------------------------
def tsp_closure(fx):
    """The closure distances of the simple weighted graph, or None when the
    graph is directed, has fewer than three nodes, or is disconnected."""
    if fx.directed or fx.n < 3:
        return None
    first = {}
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        if a != b:
            first.setdefault((min(a, b), max(a, b)), weight_of(fx, i))
    inf = float("inf")
    d = [[inf] * fx.n for _ in range(fx.n)]
    for v in range(fx.n):
        d[v][v] = 0.0
    for (a, b), w in first.items():
        d[a][b] = d[b][a] = w
    for k in range(fx.n):
        for i in range(fx.n):
            for j in range(fx.n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    if any(math.isinf(x) for row in d for x in row):
        return None
    return d


def optimal_tour_length(d):
    n = len(d)
    if n <= 10:
        best = float("inf")
        for perm in itertools.permutations(range(1, n)):
            length = d[0][perm[0]] + sum(d[a][b] for a, b in zip(perm, perm[1:])) + d[perm[-1]][0]
            best = min(best, length)
        return best
    m = n - 1
    inf = float("inf")
    table = [[inf] * m for _ in range(1 << m)]
    for j in range(m):
        table[1 << j][j] = d[0][j + 1]
    for subset in range(1, 1 << m):
        for last in range(m):
            here = table[subset][last]
            if here == inf:
                continue
            for nxt in range(m):
                if not subset >> nxt & 1:
                    grown = subset | 1 << nxt
                    cost = here + d[last + 1][nxt + 1]
                    if cost < table[grown][nxt]:
                        table[grown][nxt] = cost
    full = (1 << m) - 1
    return min(table[full][j] + d[j + 1][0] for j in range(m))


@measure("gt_tsp_exact_length")
def _tsp_exact(fx, e):
    d = tsp_closure(fx)
    return [-1] if d is None else [optimal_tour_length(d)]


@measure("gt_tsp_exact_valid")
def _tsp_exact_valid(fx, e):
    return [-1] if tsp_closure(fx) is None else [1]


@measure("gt_tsp_heuristics_valid")
def _tsp_heuristics_valid(fx, e):
    return [-1] if tsp_closure(fx) is None else [1] * 5


@measure("gt_tsp_heuristics_bound")
def _tsp_heuristics_bound(fx, e):
    d = tsp_closure(fx)
    return [-1] if d is None else [optimal_tour_length(d)] * 5


@measure("gt_tsp_christofides_ratio")
def _tsp_ratio(fx, e):
    d = tsp_closure(fx)
    return [-1] if d is None else [1.5 * optimal_tour_length(d)]


# ---- power-law fits ----------------------------------------------------------------------------
def degrees(fx):
    d = [0] * fx.n
    for a, b in zip(fx.src, fx.tgt):
        d[a] += 1
        d[b] += 1
    return d


def zeta(s, q, direct=2000):
    """Hurwitz zeta: direct sum plus the Euler-Maclaurin tail (B2, B4, B6)."""
    total = math.fsum((k + q) ** -s for k in range(direct))
    a = direct + q
    tail = (a ** (1 - s) / (s - 1) + a ** -s / 2 + s * a ** (-s - 1) / 12
            - s * (s + 1) * (s + 2) * a ** (-s - 3) / 720
            + s * (s + 1) * (s + 2) * (s + 3) * (s + 4) * a ** (-s - 5) / 30240)
    return total + tail


def above_xmin(fx, xmin):
    return sorted(x for x in degrees(fx) if x >= max(xmin, 1))


def loglik_discrete(alpha, xs, xmin):
    return -alpha * sum(math.log(x) for x in xs) - len(xs) * math.log(zeta(alpha, xmin))


def alpha_discrete(xs, xmin):
    f = lambda a: loglik_discrete(a, xs, xmin)  # noqa: E731
    lo, hi, h = 1.0001, 50.0, 1e-6
    for _ in range(100):
        mid = (lo + hi) / 2
        slope = (f(mid + h) - f(mid - h)) / (2 * h)
        if slope > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def distance_discrete(alpha, xs, xmin):
    """The Kolmogorov-Smirnov statistic over every integer x >= xmin: at each
    observed value the empirical function after and before its step against the
    model at x and at x - 1."""
    norm = zeta(alpha, xmin)
    n = len(xs)
    worst = 0.0
    for x in sorted(set(xs)):
        after = sum(1 for y in xs if y <= x) / n
        before = sum(1 for y in xs if y < x) / n
        at = 1 - zeta(alpha, x + 1) / norm
        below = 1 - zeta(alpha, x) / norm
        worst = max(worst, abs(after - at), abs(before - below))
    return worst


def fit_discrete(xs, xmin):
    alpha = alpha_discrete(xs, xmin)
    return alpha, loglik_discrete(alpha, xs, xmin), distance_discrete(alpha, xs, xmin)


def plfit_defined(fx, xmin):
    return len(set(above_xmin(fx, xmin))) >= 2


def corrected(fx, e, alpha, n):
    """alpha (n - 1) / n + 1 / n when the entry asks for the small-sample
    correction when the fit sees fewer than `small_sample_below` data points
    (the nodes with a positive degree)."""
    below = e.get("small_sample_below")
    if below and sum(1 for x in degrees(fx) if x >= 1) < below:
        return alpha * (n - 1) / n + 1 / n
    return alpha


@measure("gt_plfit_alpha", "gt_plfit_alpha_small", "gt_plfit_alpha_continuous",
         "gt_plfit_alpha_continuous_small")
def _plfit_alpha(fx, e):
    xmin = float(e.get("xmin", 2.0))
    if not plfit_defined(fx, xmin):
        return [-1]
    xs = above_xmin(fx, xmin)
    if e.get("discrete", True):
        alpha = fit_discrete(xs, xmin)[0]
    else:
        alpha = 1 + len(xs) / sum(math.log(x / xmin) for x in xs)
    return [corrected(fx, e, alpha, len(xs))]


@measure("gt_plfit_loglik", "gt_plfit_loglik_small")
def _plfit_loglik(fx, e):
    xmin = float(e.get("xmin", 2.0))
    if not plfit_defined(fx, xmin):
        return [-1]
    xs = above_xmin(fx, xmin)
    alpha = corrected(fx, e, alpha_discrete(xs, xmin), len(xs))
    return [loglik_discrete(alpha, xs, xmin)]


@measure("gt_plfit_distance")
def _plfit_distance(fx, e):
    xmin = float(e.get("xmin", 2.0))
    return [fit_discrete(above_xmin(fx, xmin), xmin)[2]] if plfit_defined(fx, xmin) else [-1]


@measure("gt_plfit_xmin", "gt_plfit_xmin_bounded")
def _plfit_xmin(fx, e):
    if not plfit_defined(fx, 1):
        return [-1]
    bound = e.get("alpha_max") or 0.0
    best = None
    values = sorted({x for x in degrees(fx) if x >= 1})
    for xmin in values:
        xs = above_xmin(fx, xmin)
        if len(xs) < 2 or len(set(xs)) < 2:
            continue
        alpha, _, d = fit_discrete(xs, xmin)
        if bound and alpha > bound:
            continue
        if best is None or d < best[0] - 1e-15:
            best = (d, xmin)
    return [-1] if best is None else [float(best[1])]


def main() -> None:
    spec = load_area(AREA)
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if "definition" not in v["oracles"] or not applies(v, fx):
                continue
            ospec = v["oracles"]["definition"]
            if name in ospec.get("undefined_on", []):
                continue
            f = MEASURES.get(variant)
            if f is None:
                continue
            write_values(ORACLE, name, variant, f(fx, v["params"]))
            count += 1
    print(f"definition ({AREA}): wrote {count} golden files")
    write_version(ORACLE, DEFINITION_VERSION)


if __name__ == "__main__":
    main()
