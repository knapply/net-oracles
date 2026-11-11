#!/usr/bin/env python3
"""Golden values from the definitions for manifest/generators_ext.yaml
(encodings in bindings/generators_ext.py, case tables and node numbering in
derived/generators_ext.py): each family's edge set from its defining rule on
node pairs, the textbook Pruefer coding, exhaustive search for graphicality,
and independent implementations of the documented realization rules whose
output is also checked for exact degrees and simplicity.

    python3 oracles/generators_ext_definition_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)
from derived import generators_ext as D  # noqa: E402

ORACLE = "definition"


def pairs(n, directed, joined):
    return D.normalize(((a, b) for a in range(n) for b in range(n)
                        if a != b and joined(a, b)), directed)


def barbell(m1, m2):
    n = 2 * m1 + m2
    left, right = range(m1), range(m1 + m2, n)
    edges = [(a, b) for part in (left, right) for a in part for b in part if a < b]
    edges += [(a, a + 1) for a in range(m1, m1 + m2 - 1)]
    edges += [(m1 - 1, m1)] + ([(m1 + m2 - 1, m1 + m2)] if m2 else [])
    return D.pack(n, D.normalize(edges, False))


def lollipop(m, n):
    edges = [(a, b) for a in range(m) for b in range(a + 1, m)]
    edges += [(a, a + 1) for a in range(m, m + n - 1)]
    edges += [(m - 1, m)] if n else []
    return D.pack(m + n, D.normalize(edges, False))


def petersen(n, k):
    edges = [(i, (i + 1) % n) for i in range(n)] + [(i, n + i) for i in range(n)]
    edges += [(n + i, n + (i + k) % n) for i in range(n)]
    return D.pack(2 * n, D.normalize(edges, False))


def turan(n, r):
    sizes = [n // r] * (r - n % r) + [n // r + 1] * (n % r)
    part = [p for p, size in enumerate(sizes) for _ in range(size)]
    return D.pack(n, pairs(n, False, lambda a, b: part[a] != part[b]))


def lcf(n, shifts, repeats):
    if n == 0:
        return D.pack(0, [])
    edges = [(i, (i + 1) % n) for i in range(n)]
    edges += [(i % n, (i + shifts[i % len(shifts)]) % n) for i in range(repeats * len(shifts))]
    return D.pack(n, D.normalize(edges, False))


def prufer_decode(sequence):
    n = len(sequence) + 2
    degree = [1 + sequence.count(v) for v in range(n)]
    edges = []
    for label in sequence:
        leaf = min(v for v in range(n) if degree[v] == 1)
        edges.append((leaf, label))
        degree[leaf] -= 1
        degree[label] -= 1
    last = [v for v in range(n) if degree[v] == 1]
    edges.append((last[0], last[1]))
    return D.pack(n, D.normalize(edges, False))


def prufer_encode(sequence):
    tree = prufer_decode(sequence)[1:]
    n = len(sequence) + 2
    adjacent = {v: set() for v in range(n)}
    for a, b in tree:
        adjacent[a].add(b)
        adjacent[b].add(a)
    out = []
    for _ in range(n - 2):
        leaf = min(v for v in adjacent if len(adjacent[v]) == 1)
        (parent,) = adjacent[leaf]
        out.append(parent)
        adjacent[parent].discard(leaf)
        del adjacent[leaf]
    return [(len(out),)] + [(v,) for v in out]


def check_degrees(edges, n, expected, directed=False):
    degree = [0] * n
    for a, b in edges:
        assert a != b and 0 <= a < n and 0 <= b < n
        degree[a] += 1
        if not directed:
            degree[b] += 1
    assert len(set(edges)) == len(edges)
    assert degree == expected, (degree, expected)


def havel_hakimi(degrees):
    n = len(degrees)
    left = list(degrees)
    edges = []
    while True:
        order = sorted(range(n), key=lambda v: (-left[v], v))
        pivot = order[0] if order else None
        if pivot is None or left[pivot] == 0:
            break
        d = left[pivot]
        left[pivot] = 0
        for t in order[1:1 + d]:
            assert left[t] > 0
            left[t] -= 1
            edges.append((min(pivot, t), max(pivot, t)))
    edges = sorted(edges)
    check_degrees(edges, n, list(degrees))
    return D.pack(n, edges)


def kleitman_wang(inn, outd):
    n = len(inn)
    li, lo = list(inn), list(outd)
    arcs = []
    while True:
        candidates = [v for v in range(n) if lo[v] > 0]
        if not candidates:
            break
        pivot = min(candidates, key=lambda v: (-lo[v], v))
        d = lo[pivot]
        lo[pivot] = 0
        targets = sorted((t for t in range(n) if t != pivot and li[t] > 0),
                         key=lambda t: (-li[t], -lo[t], t))
        assert len(targets) >= d
        for t in targets[:d]:
            li[t] -= 1
            arcs.append((pivot, t))
    assert all(x == 0 for x in li)
    arcs = sorted(arcs)
    check_degrees(arcs, n, list(outd), directed=True)
    got_in = [sum(1 for _, b in arcs if b == v) for v in range(n)]
    assert got_in == list(inn)
    return D.pack(n, arcs)


def gale_ryser(rows, columns):
    r, c = len(rows), len(columns)
    left = list(columns)
    edges = []
    for row in sorted(range(r), key=lambda v: (-rows[v], v)):
        chosen = sorted(range(c), key=lambda j: (-left[j], j))[:rows[row]]
        for j in chosen:
            assert left[j] > 0
            left[j] -= 1
            edges.append((row, r + j))
    edges = sorted(edges)
    degree = [0] * (r + c)
    for a, b in edges:
        degree[a] += 1
        degree[b] += 1
    assert degree == list(rows) + list(columns) and len(set(edges)) == len(edges)
    return D.pack(r + c, edges)


def complement(name, loops):
    n, edges, directed = D.graph(name)
    present = set(D.normalize(edges, directed))
    out = [(a, b) for a in range(n) for b in range(n) if (a != b or loops)
           and (directed or a <= b)
           and ((a, b) if directed else (min(a, b), max(a, b))) not in present]
    return D.pack(n, D.normalize(out, directed))


def product(op, first, second):
    (na, ea, da), (nb, eb, db) = D.graph(first), D.graph(second)
    adj_a = set(D.normalize(ea, da))
    adj_b = set(D.normalize(eb, db))

    def joined(g, a, b, directed):
        return (a, b) in g if directed else (min(a, b), max(a, b)) in g

    def rule(u, x, v, y):
        u_v = joined(adj_a, u, v, da)
        x_y = joined(adj_b, x, y, db)
        if op == 0:
            return (u == v and x_y) or (u_v and x == y)
        if op == 1:
            return u_v and x_y
        if op == 2:
            return (u == v and x_y) or (u_v and x == y) or (u_v and x_y)
        return u_v or (u == v and x_y)

    nodes = [(u, x) for u in range(na) for x in range(nb)]
    edges = [(u * nb + x, v * nb + y) for (u, x) in nodes for (v, y) in nodes
             if (da or u * nb + x <= v * nb + y) and rule(u, x, v, y)]
    return D.pack(na * nb, D.normalize(edges, da))


def full_citation(n, directed):
    arcs = [(i, j) if directed else (j, i) for i in range(n) for j in range(i)]
    return D.pack(n, D.normalize(arcs, directed))


def compute(engine):
    fn, family = engine["fn"], engine.get("family")
    if fn == "generators_ext_invalid":
        return [1 for _ in D.INVALID]
    out = []
    if family == "barbell":
        for case in D.BARBELL:
            out += barbell(*case)
    elif family == "lollipop":
        for case in D.LOLLIPOP:
            out += lollipop(*case)
    elif family == "generalized_petersen":
        for case in D.PETERSEN:
            out += petersen(*case)
    elif family == "turan":
        for case in D.TURAN:
            out += turan(*case)
    elif family == "lcf":
        for case in D.LCF:
            out += lcf(*case)
    elif family == "prufer_decode":
        for sequence in D.PRUFER_DECODE:
            out += prufer_decode(sequence)
    elif family == "prufer_encode":
        for sequence in D.PRUFER_ENCODE:
            out += prufer_encode(sequence)
    elif family == "graphical":
        for sequence in D.GRAPHICAL:
            out.append((int(D.graphical_reference(sequence)),))
    elif family == "digraphical":
        for inn, outd in D.DIGRAPHICAL:
            out.append((int(D.digraphical_reference(inn, outd)),))
    elif family == "bigraphical":
        for rows, columns in D.BIGRAPHICAL:
            out.append((int(D.bigraphical_reference(rows, columns)),))
    elif family == "havel_hakimi":
        for sequence in D.realization_cases(family):
            out += havel_hakimi(sequence)
    elif family == "kleitman_wang":
        for inn, outd in D.realization_cases(family):
            out += kleitman_wang(inn, outd)
    elif family == "gale_ryser":
        for rows, columns in D.realization_cases(family):
            out += gale_ryser(rows, columns)
    elif family == "complement":
        for name, loops in D.COMPLEMENT:
            if bool(loops) == bool(engine.get("loops", False)):
                out += complement(name, loops)
    elif family == "product":
        for first, second in D.PRODUCT_PAIRS:
            if D.graph(first)[2] == D.graph(second)[2]:
                out += product(engine["op"], first, second)
    elif family == "full_citation":
        for n in (0, 1, 2, 5):
            for directed in (False, True):
                out += full_citation(n, directed)
    else:
        raise ValueError(family or fn)
    return out


def main() -> None:
    spec = load_area("generators_ext")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            if "only_on" in v["oracles"][ORACLE] and name not in v["oracles"][ORACLE]["only_on"]:
                continue
            write_values(ORACLE, name, variant, compute(v["params"]))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (generators_ext): wrote {count} golden files")


if __name__ == "__main__":
    main()
