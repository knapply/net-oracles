#!/usr/bin/env python3
"""Definition oracle for NetworkX's bipartite measures: exact rational
arithmetic from the published formulas, brute-force enumeration of
4-cycles, 3-paths, and matchings, the matrix exponential as its power
series, BiRank's limit as the projection of the start vector onto the
leading eigenspace, and the minimum vertex cover as an integer program
(SciPy's HiGHS). Shares no code with the engine. Inputs and encodings:
../bindings/bipartite_nx.py.

    python3 oracles/bipartite_nx_definition_oracle.py
"""

from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, FIXTURES, applies, fixture_names,  # noqa: E402
                    load_area, load_fixture, write_values, write_version)

ORACLE = "definition"
AREA = "bipartite_nx"
MEASURES = {}


def measure(name):
    def wrap(f):
        MEASURES[name] = f
        return f
    return wrap


def sets(fx):
    """(successor sets, predecessor sets) of the simple graph."""
    succ = {v: set() for v in range(fx.n)}
    pred = {v: set() for v in range(fx.n)}
    for a, b in zip(fx.src, fx.tgt):
        if a == b:
            continue
        succ[a].add(b)
        pred[b].add(a)
        if not fx.directed:
            succ[b].add(a)
            pred[a].add(b)
    return succ, pred


def top(fx):
    t = json.loads((FIXTURES / fx.name / "meta.json").read_text()).get("type")
    if t is not None:
        return [v for v in range(fx.n) if t[v] == 0]
    return list(range(0, fx.n, 2))


def two_colouring(fx):
    succ, pred = sets(fx)
    nb = {v: succ[v] | pred[v] for v in range(fx.n)}
    colour = {}
    for comp_start in range(fx.n):
        if comp_start in colour:
            continue
        comp, frontier = {comp_start}, [comp_start]
        while frontier:
            v = frontier.pop()
            for w in nb[v]:
                if w not in comp:
                    comp.add(w)
                    frontier.append(w)
        starts = sorted(v for v in comp if succ[v])
        if not starts:
            for v in comp:
                colour[v] = 0
            continue
        # Parity of the distance from the start.
        dist = {starts[0]: 0}
        layer = [starts[0]]
        while layer:
            nxt = []
            for v in layer:
                for w in nb[v]:
                    if w not in dist:
                        dist[w] = dist[v] + 1
                        nxt.append(w)
            layer = nxt
        for v in comp:
            colour[v] = 1 - dist[v] % 2
        if any(colour[v] == colour[w] for v in comp for w in nb[v]):
            return None
    return [colour[v] for v in range(fx.n)]


@measure("bipartite_color")
def _bc(fx, e):
    c = two_colouring(fx)
    return c if c is not None else [-1] * fx.n


@measure("projection")
def _proj(fx, e):
    succ, pred = sets(fx)
    out = []
    for u in top(fx):
        reach = sorted({v for x in succ[u] for v in succ[x]} - {u})
        for v in reach:
            common = succ[u] & pred[v]
            if e["weight"] == "count":
                w = len(common)
            elif e["weight"] == "newman":
                w = sum((Fraction(1, len(succ[x]) - 1) for x in common if len(succ[x]) > 1),
                        Fraction(0))
            elif e["weight"] == "jaccard":
                w = Fraction(len(common), len(succ[u] | pred[v]))
            else:
                w = Fraction(len(common), min(len(succ[u]), len(pred[v])))
            out.append((u, v, float(w)))
    return out


@measure("latapy_clustering")
def _lat(fx, e):
    if two_colouring(fx) is None:
        return [-1] * fx.n
    succ, _ = sets(fx)
    out = []
    for v in range(fx.n):
        far = {u for x in succ[v] for u in succ[x]} - {v}
        total = Fraction(0)
        for u in far:
            inter = len(succ[u] & succ[v])
            denom = {"dot": len(succ[u] | succ[v]), "min": min(len(succ[u]), len(succ[v])),
                     "max": max(len(succ[u]), len(succ[v]))}[e["mode"]]
            total += Fraction(inter, denom)
        out.append(float(total / len(far)) if far and total else 0.0)
    return out


def four_cycles(fx):
    """Every 4-cycle, as a frozenset of its four edges."""
    succ, _ = sets(fx)
    found = set()
    for a in range(fx.n):
        for c in range(a + 1, fx.n):
            common = sorted(succ[a] & succ[c])
            for b, d in itertools.combinations(common, 2):
                found.add(frozenset([frozenset((a, b)), frozenset((b, c)), frozenset((c, d)),
                                     frozenset((d, a))]))
    return found


@measure("butterflies")
def _bf(fx, e):
    count = [0] * fx.n
    for cyc in four_cycles(fx):
        for v in set().union(*cyc):
            count[v] += 1
    return count


@measure("robins_alexander")
def _ra(fx, e):
    succ, _ = sets(fx)
    m = sum(len(s) for s in succ.values()) // 2
    if fx.n < 4 or m < 3:
        return [0]
    paths = set()
    for v in range(fx.n):
        for u in succ[v]:
            for w in succ[u] - {v}:
                for x in succ[w] - {v, u}:
                    paths.add(min((v, u, w, x), (x, w, u, v)))
    if not paths:
        return [0]
    return [float(Fraction(4 * len(four_cycles(fx)), len(paths)))]


@measure("node_redundancy")
def _nr(fx, e):
    succ, _ = sets(fx)
    out = []
    for v in range(fx.n):
        k = len(succ[v])
        if k < 2:
            out.append(-1.0)
            continue
        pairs = sum(1 for a, b in itertools.combinations(sorted(succ[v]), 2)
                    if (succ[a] & succ[b]) - {v})
        out.append(float(Fraction(2 * pairs, k * (k - 1))))
    return out


def adjacency(fx):
    a = np.zeros((fx.n, fx.n))
    succ, _ = sets(fx)
    for u in range(fx.n):
        for v in succ[u]:
            a[u, v] = 1.0
    return a


def expm_series(a):
    """sum_k A^k / k! until the terms vanish."""
    result = np.eye(len(a))
    term = np.eye(len(a))
    for k in range(1, 400):
        term = term @ a / k
        result = result + term
        if np.abs(term).max() < 1e-300 or np.abs(term).max() < 1e-18 * np.abs(result).max():
            break
    return result


@measure("spectral_bipartivity")
def _sb(fx, e):
    a = adjacency(fx)
    ep, em = expm_series(a), expm_series(-a)
    cosh = 0.5 * (ep + em)
    return [cosh[i, i] / ep[i, i] for i in range(fx.n)] + [np.trace(cosh) / np.trace(ep)]


@measure("birank")
def _br(fx, e):
    t = top(fx)
    if len(t) in (0, fx.n):
        return [-1] * fx.n
    tset = set(t)
    b = [v for v in range(fx.n) if v not in tset]
    succ, _ = sets(fx)
    w = np.zeros((len(b), len(t)))
    for i, u in enumerate(b):
        for j, v in enumerate(t):
            if v in succ[u]:
                w[i, j] = 1.0
    if not w.any():
        # No tie between the sides: S = 0 and the ranking is 0 / 0.
        return [float("nan")] * fx.n
    dp = w.sum(axis=0)
    dp[dp == 0] = 1.0
    du = w.sum(axis=1)
    du[du == 0] = 1.0
    s = w / np.sqrt(du)[:, None] / np.sqrt(dp)[None, :]
    # The limit of p <- S^T S p from the uniform start: its projection onto
    # the leading eigenspace of S^T S, then u = S p, both L1-normalized.
    vals, vecs = np.linalg.eigh(s.T @ s)
    lead = vals >= vals.max() * (1 - 1e-9)
    p0 = np.ones(len(t)) / len(t)
    p = vecs[:, lead] @ (vecs[:, lead].T @ p0)
    u = s @ p
    p, u = p / np.abs(p).sum(), u / np.abs(u).sum()
    out = [0.0] * fx.n
    for j, v in enumerate(t):
        out[v] = p[j]
    for i, v in enumerate(b):
        out[v] = u[i]
    return out


@measure("bipartite_modularity")
def _bm(fx, e):
    succ, _ = sets(fx)
    red = set(top(fx))
    label = [3 * v // fx.n for v in range(fx.n)]
    deg = {v: len(succ[v]) for v in range(fx.n)}
    m = sum(deg[v] for v in red)
    if m == 0:
        return [0.0]
    q = Fraction(0)
    for c in set(label):
        members = {v for v in range(fx.n) if label[v] == c}
        inside = sum(1 for u in members for v in succ[u] if v in members) // 2
        k = sum(deg[v] for v in members & red)
        d = sum(deg[v] for v in members - red)
        q += Fraction(inside, m) - Fraction(k * d, m * m)
    return [float(q)]


@measure("vertex_cover")
def _vc(fx, e):
    from scipy.optimize import Bounds, LinearConstraint, milp

    succ, _ = sets(fx)
    t = set(top(fx))
    edges = sorted({(min(a, b), max(a, b)) for a in range(fx.n) for b in succ[a]})
    if any((a in t) == (b in t) for a, b in edges):
        return [-1]
    if not edges:
        return [(0, 1)]
    a = np.zeros((len(edges), fx.n))
    for i, (u, v) in enumerate(edges):
        a[i, u] = a[i, v] = 1
    res = milp(np.ones(fx.n), constraints=LinearConstraint(a, lb=1),
               integrality=np.ones(fx.n), bounds=Bounds(0, 1))
    return [(int(round(res.fun)), 1)]


def _bip_edges(fx):
    succ, _ = sets(fx)
    t = set(top(fx))
    edges = sorted({(min(a, b), max(a, b)) for a in range(fx.n) for b in succ[a]})
    if any((a in t) == (b in t) for a, b in edges):
        return None, None
    return edges, t


def _assignment(fx, edges, cost, need):
    """Integer program: choose edges, each node at most once, `need` edges
    in all; minimize the total cost. None if infeasible."""
    from scipy.optimize import Bounds, LinearConstraint, milp

    if not edges:
        return 0.0 if need == 0 else None
    a = np.zeros((fx.n, len(edges)))
    for j, (u, v) in enumerate(edges):
        a[u, j] = a[v, j] = 1
    cons = [LinearConstraint(a, ub=1), LinearConstraint(np.ones((1, len(edges))), lb=need, ub=need)]
    res = milp(np.array(cost), constraints=cons, integrality=np.ones(len(edges)),
               bounds=Bounds(0, 1))
    return None if res.status != 0 else res.fun


@measure("hopcroft_karp")
def _hk(fx, e):
    edges, t = _bip_edges(fx)
    if edges is None:
        return [-1]
    if not edges:
        return [(0, 1)]
    from scipy.optimize import Bounds, LinearConstraint, milp
    a = np.zeros((fx.n, len(edges)))
    for j, (u, v) in enumerate(edges):
        a[u, j] = a[v, j] = 1
    res = milp(-np.ones(len(edges)), constraints=LinearConstraint(a, ub=1),
               integrality=np.ones(len(edges)), bounds=Bounds(0, 1))
    return [(int(round(-res.fun)), 1)]


@measure("nx_eppstein_size")
def _epp_size(fx, e):
    # Eppstein's procedure returns a maximum matching (Hopcroft and Karp
    # 1973): its size is the integer program's optimum.
    return _hk(fx, e)


@measure("min_weight_full_matching")
def _mwfm(fx, e):
    edges, t = _bip_edges(fx)
    if edges is None:
        return [-1]
    cost = [float((u + 2 * v) % 7 + 1) for u, v in edges]
    small = min(len(t), fx.n - len(t))
    best = _assignment(fx, edges, cost, small)
    return [-1] if best is None else [(round(best, 9), 1)]


def perfect_matchings_exist(n, edges, removed):
    """Whether the graph minus the nodes in `removed` has a perfect matching."""
    nb = {v: set() for v in range(n)}
    for u, v in edges:
        nb[u].add(v)
        nb[v].add(u)

    @lru_cache(maxsize=None)
    def ok(mask):
        free = [v for v in range(n) if not mask >> v & 1]
        if not free:
            return True
        v = free[0]
        return any(not mask >> w & 1 and ok(mask | 1 << v | 1 << w) for w in nb[v])

    return ok(sum(1 << v for v in removed))


@measure("maximal_extendability")
def _me(fx, e):
    succ, _ = sets(fx)
    edges = sorted({(min(a, b), max(a, b)) for a in range(fx.n) for b in succ[a]})
    n = 2 * fx.n
    cover = [(2 * a, 2 * b + 1) for a, b in edges] + [(2 * b, 2 * a + 1) for a, b in edges]
    if n > 20:
        return None
    nb = {v: set() for v in range(n)}
    for u, v in cover:
        nb[u].add(v)
        nb[v].add(u)
    seen, stack = {0}, [0]
    while stack:
        for w in nb[stack.pop()]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    if len(seen) < n or not perfect_matchings_exist(n, cover, ()):
        return [-1]
    # k-extendable: every matching of k edges lies in a perfect matching.
    k = 0
    while True:
        bad = False
        for m in itertools.combinations(cover, k + 1):
            nodes = [x for edge in m for x in edge]
            if len(set(nodes)) < len(nodes):
                continue
            if not perfect_matchings_exist(n, cover, nodes):
                bad = True
                break
        if bad:
            break
        k += 1
        if 2 * (k + 1) > n:
            break
    return [-1] if k == 0 else [k]


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
