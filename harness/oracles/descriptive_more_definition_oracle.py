#!/usr/bin/env python3
"""Definition oracle for dyad census, degree distribution, Krackhardt
dimensions, ego composition, symmetrize, dichotomize, Simmelian ties,
cocitation, partition quality and the motif census: every quantity
evaluated by enumeration over the fixture's edge list (exact fractions where
a formula divides), sharing no code with the engine.

    python3 oracles/descriptive_more_definition_oracle.py

Encodings: see ../bindings/descriptive_more.py (NaN is -999).
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
UNDEF = -999.0


def f(x):
    """Fraction (or None for 0 / 0) to the marker-encoded float."""
    return UNDEF if x is None else float(x)


def ratio(a, b):
    return None if b == 0 else Fraction(a) / Fraction(b)


def arcs_of(fx):
    """Distinct arcs between distinct nodes (an undirected edge is two)."""
    arcs = set()
    for a, b in zip(fx.src, fx.tgt):
        if a == b:
            continue
        arcs.add((a, b))
        if not fx.directed:
            arcs.add((b, a))
    return arcs


def mutual_ties(fx):
    arcs = arcs_of(fx)
    return {(a, b) for (a, b) in arcs if (b, a) in arcs}


def dyad_census(fx):
    arcs = arcs_of(fx)
    m = a = z = 0
    for i, j in combinations(range(fx.n), 2):
        k = ((i, j) in arcs) + ((j, i) in arcs)
        if k == 2:
            m += 1
        elif k == 1:
            a += 1
        else:
            z += 1
    return [float(m), float(a), float(z)]


def degrees(fx, mode, loops):
    d = [0] * fx.n
    for a, b in zip(fx.src, fx.tgt):
        if a == b and not loops:
            continue
        if not fx.directed or mode == "all":
            d[a] += 1
            d[b] += 1
        elif mode == "out":
            d[a] += 1
        else:
            d[b] += 1
    return d


def degree_distribution(fx, e):
    d = degrees(fx, e.get("mode", "all"), e.get("loops", True))
    n = len(d)
    hist = [0] * (max(d) + 1)
    for x in d:
        hist[x] += 1
    mean = Fraction(sum(d), n)
    var = sum((Fraction(x) - mean) ** 2 for x in d) / n
    s = sorted(d)
    gini = ratio(sum((2 * (i + 1) - n - 1) * x for i, x in enumerate(s)), n * sum(d))
    return [float(c) for c in hist] + [float(mean), float(var), float(min(d)), float(max(d)),
                                      f(gini)]


def weak_components(fx):
    parent = list(range(fx.n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in zip(fx.src, fx.tgt):
        parent[find(a)] = find(b)
    groups = {}
    for v in range(fx.n):
        groups.setdefault(find(v), []).append(v)
    return list(groups.values())


def krackhardt(fx):
    n = fx.n
    arcs = arcs_of(fx)
    comps = weak_components(fx)
    pairs = n * (n - 1) // 2
    connected = sum(len(c) * (len(c) - 1) // 2 for c in comps)
    conn = ratio(connected, pairs)
    reach = [[False] * n for _ in range(n)]
    for a, b in arcs:
        reach[a][b] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                row_k = reach[k]
                row_i = reach[i]
                for j in range(n):
                    if row_k[j]:
                        row_i[j] = True
    ordered = sum(1 for i in range(n) for j in range(n) if i != j and reach[i][j])
    mutual = sum(1 for i in range(n) for j in range(n)
                 if i != j and reach[i][j] and reach[j][i])
    hier = None if ordered == 0 else 1 - Fraction(mutual, ordered)
    minimum = n - len(comps)
    eff = None if n < 2 else 1 - Fraction(len(arcs) - minimum, n * (n - 1) - minimum)
    # Least upper boundedness: k is an upper bound of i and j when k reaches
    # both (a node reaches itself); u is a least upper bound when it is an
    # upper bound reached by every upper bound. A violation is a pair in one
    # weak component with none; the score is 1 - V / sum (c - 1)(c - 2) / 2.
    for v in range(n):
        reach[v][v] = True
    violations = 0
    for comp in comps:
        for i, j in combinations(comp, 2):
            upper = [k for k in range(n) if reach[k][i] and reach[k][j]]
            if not any(all(reach[k][u] for k in upper) for u in upper):
                violations += 1
    most = sum((len(c) - 1) * (len(c) - 2) // 2 for c in comps if len(c) >= 3)
    lub = ratio(most - violations, most)
    return [f(conn), f(hier), f(eff), f(lub)]


def alters(fx, mode):
    out = [set() for _ in range(fx.n)]
    for a, b in zip(fx.src, fx.tgt):
        if a == b:
            continue
        if not fx.directed or mode == "all":
            out[a].add(b)
            out[b].add(a)
        elif mode == "out":
            out[a].add(b)
        else:
            out[b].add(a)
    return out


def ego_composition(fx, e):
    n = fx.n
    code = [v % 3 for v in range(n)]
    levels = sorted(set(code))
    k = len(levels)
    nb = alters(fx, e.get("mode", "all"))
    cols = {name: [] for name in ("alters", "blau", "shannon", "iqv", "same")}
    shares = []
    for v in range(n):
        counts = [sum(1 for u in nb[v] if code[u] == lv) for lv in levels]
        total = sum(counts)
        cols["alters"].append(float(total))
        if total == 0:
            for name in ("blau", "shannon", "iqv", "same"):
                cols[name].append(UNDEF)
            shares.extend([UNDEF] * k)
            continue
        p = [Fraction(c, total) for c in counts]
        blau = 1 - sum(x * x for x in p)
        cols["blau"].append(float(blau))
        cols["shannon"].append(-sum(float(x) * math.log(float(x)) for x in p if x > 0))
        cols["iqv"].append(UNDEF if k == 1 else float(blau / (1 - Fraction(1, k))))
        cols["same"].append(float(Fraction(counts[levels.index(code[v])], total)))
        shares.extend(float(x) for x in p)
    return (cols["alters"] + cols["blau"] + cols["shannon"] + cols["iqv"] + cols["same"]
            + shares)


def pair_weights(fx):
    """{(low, high): [a, b]} with a = W[low][high], b = W[high][low]; parallel
    weights added in input order, loops dropped."""
    w = {}
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        if a == b:
            continue
        x = fx.weights[i] if fx.weighted else 1.0
        lo, hi = min(a, b), max(a, b)
        entry = w.setdefault((lo, hi), [0.0, 0.0])
        if fx.directed:
            entry[0 if a == lo else 1] += x
        else:
            entry[0] += x
            entry[1] += x
    return w


def symmetrize(fx, e):
    method = e["method"]
    out = []
    for (lo, hi), (a, b) in sorted(pair_weights(fx).items()):
        v = {"max": max(a, b), "min": min(a, b), "sum": a + b, "mean": (a + b) / 2,
             "product": a * b, "upper": a, "lower": b,
             "strong": float(a != 0 and b != 0), "weak": float(a != 0 or b != 0)}[method]
        if v != 0:
            out.append((lo, hi, v))
    return out


def dichotomize(fx, e):
    ties = {}
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        key = (a, b) if fx.directed or a <= b else (b, a)
        ties[key] = ties.get(key, 0.0) + (fx.weights[i] if fx.weighted else 1.0)
    if e["by"] == "cutoff":
        c = e["value"]
        test = {"ge": lambda w: w >= c, "gt": lambda w: w > c, "le": lambda w: w <= c,
                "lt": lambda w: w < c, "eq": lambda w: w == c, "ne": lambda w: w != c}[e["rule"]]
        return sorted(k for k, w in ties.items() if test(w))
    n = fx.n
    possible = n * (n - 1) if fx.directed else n * (n - 1) // 2
    limit = math.floor(e["value"] * possible)
    cand = {k: w for k, w in ties.items() if k[0] != k[1]}
    kept = []
    for w in sorted(set(cand.values()), reverse=True):
        group = [k for k, x in cand.items() if x == w]
        if len(kept) + len(group) > limit:
            break
        kept += group
    return sorted(kept)


def simmelian(fx):
    mt = mutual_ties(fx)
    nbrs = {v: {b for (a, b) in mt if a == v} for v in range(fx.n)}
    return sorted((a, b) for (a, b) in mt if a < b and nbrs[a] & nbrs[b])


def cocitation(fx, e):
    arcs = arcs_of(fx)
    out = []
    for i, j in combinations(range(fx.n), 2):
        if e["kind"] == "cocitation":
            c = sum(1 for k in range(fx.n) if (k, i) in arcs and (k, j) in arcs)
        else:
            c = sum(1 for k in range(fx.n) if (i, k) in arcs and (j, k) in arcs)
        if c > 0:
            out.append((i, j, float(c)))
    return out


def partition_quality(fx):
    n = fx.n
    block = [v % 3 for v in range(n)]
    arcs = arcs_of(fx)
    ties = [(a, b) for (a, b) in arcs if fx.directed or a < b]
    intra = sum(1 for a, b in ties if block[a] == block[b])
    if fx.directed:
        pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
    else:
        pairs = list(combinations(range(n), 2))
    tied = set(ties)
    correct = sum(1 for (i, j) in pairs if ((i, j) in tied) == (block[i] == block[j]))
    return [f(ratio(intra, len(ties))), f(ratio(correct, len(pairs)))]


def undirected_adj(fx):
    adj = {v: set() for v in range(fx.n)}
    for a, b in zip(fx.src, fx.tgt):
        if a != b:
            adj[a].add(b)
            adj[b].add(a)
    return adj


def motif_census(fx, e):
    size = e["size"]
    if fx.directed:
        return directed_triads(fx)
    adj = undirected_adj(fx)
    counts = [0] * (2 if size == 3 else 6)
    for sub in combinations(range(fx.n), size):
        edges = [(a, b) for a, b in combinations(sub, 2) if b in adj[a]]
        deg = {v: 0 for v in sub}
        for a, b in edges:
            deg[a] += 1
            deg[b] += 1
        # connected: grow from the first node
        seen, stack = {sub[0]}, [sub[0]]
        while stack:
            v = stack.pop()
            for u in sub:
                if u not in seen and u in adj[v]:
                    seen.add(u)
                    stack.append(u)
        if len(seen) != size:
            continue
        if size == 3:
            counts[0 if len(edges) == 2 else 1] += 1
        else:
            top = max(deg.values())
            idx = {(3, 3): 0, (3, 2): 1, (4, 2): 2, (4, 3): 3, (5, 3): 4, (6, 3): 5}[
                (len(edges), top)]
            counts[idx] += 1
    return [float(c) for c in counts]


TRIADS = ["021D", "021U", "021C", "111D", "111U", "030T", "030C", "201", "120D", "120U",
          "120C", "210", "300"]


def triad_type(arcs, nodes):
    """The MAN code of a triad of a simple digraph from its three dyads and,
    for 021, 111, 120 and 030, the arrangement (Davis and Leinhardt)."""
    a, b, c = nodes
    m = [(x, y) for x, y in combinations(nodes, 2) if (x, y) in arcs and (y, x) in arcs]
    asym = [(x, y) for x in nodes for y in nodes
            if x != y and (x, y) in arcs and (y, x) not in arcs]
    nm, na = len(m), len(asym)
    outd = {v: sum(1 for (x, _) in asym if x == v) for v in nodes}
    ind = {v: sum(1 for (_, y) in asym if y == v) for v in nodes}
    if (nm, na) == (0, 2):
        if max(outd.values()) == 2:
            return "021D"
        if max(ind.values()) == 2:
            return "021U"
        return "021C"
    if (nm, na) == (1, 1):
        (x, y), (p, q) = m[0], asym[0]
        # 111D (Holland and Leinhardt): the asymmetric arc points into the
        # mutual dyad, 111U: it points out of it.
        return "111D" if q in (x, y) and p not in (x, y) else "111U"
    if (nm, na) == (0, 3):
        return "030C" if max(outd.values()) == 1 else "030T"
    if (nm, na) == (2, 0):
        return "201"
    if (nm, na) == (1, 2):
        (x, y) = m[0]
        z = next(v for v in nodes if v not in (x, y))
        if outd[z] == 2:
            return "120D"
        if ind[z] == 2:
            return "120U"
        return "120C"
    if (nm, na) == (2, 1):
        return "210"
    if (nm, na) == (3, 0):
        return "300"
    return None


def directed_triads(fx):
    arcs = arcs_of(fx)
    counts = {t: 0 for t in TRIADS}
    for nodes in combinations(range(fx.n), 3):
        t = triad_type(arcs, nodes)
        if t:
            counts[t] += 1
    return [float(counts[t]) for t in TRIADS]


def compute(fx, e):
    fn = e["fn"]
    if fn == "dyad_census":
        return dyad_census(fx)
    if fn == "degree_distribution":
        return degree_distribution(fx, e)
    if fn == "krackhardt_dimensions":
        values = krackhardt(fx)
        return values[3:] if e.get("part") == "lubness" else values[:3]
    if fn == "ego_composition":
        return ego_composition(fx, e)
    if fn == "symmetrize":
        return symmetrize(fx, e)
    if fn == "dichotomize":
        return dichotomize(fx, e)
    if fn == "simmelian_ties":
        return simmelian(fx)
    if fn == "cocitation":
        return cocitation(fx, e)
    if fn == "partition_quality":
        return partition_quality(fx)
    if fn == "motif_census":
        return motif_census(fx, e)
    raise ValueError(fn)


def main() -> None:
    spec = load_area("descriptive_more")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (descriptive_more): wrote {count} golden files")


if __name__ == "__main__":
    main()
