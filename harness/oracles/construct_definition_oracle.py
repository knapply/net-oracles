#!/usr/bin/env python3
"""Golden values from the definitions for manifest/construct.yaml (encodings
in bindings/construct.py): brute-force set logic on the edge lists of
derived/construct.py, and closed-form edge lists for the generators.

    python3 oracles/construct_definition_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)
from derived import construct as D  # noqa: E402

ORACLE = "definition"


def pairs(n, directed, sel):
    edges = [(a, b) for a in range(n) for b in range(n) if sel(a, b)]
    return D.normalize(edges, directed)


def tree_edges(arity, height):
    n = sum(arity ** k for k in range(height + 1))
    return n, [((i - 1) // arity, i) for i in range(1, n)]


def shape(name, n):
    """(node count, edges) of a generator of size n."""
    directed = name.endswith("_dir")
    base = name[:-4] if directed else name
    if base == "empty":
        return n, []
    if base == "complete":
        return n, pairs(n, directed, lambda a, b: a != b)
    if base == "complete_bipartite":
        h = n // 2
        return n, pairs(n, False, lambda a, b: a < h <= b)
    if base == "star":
        return n, pairs(n, directed, lambda a, b: a == 0 and b > 0)
    if base == "path":
        return n, pairs(n, directed, lambda a, b: b == a + 1)
    if base == "cycle":
        return n, pairs(n, directed, lambda a, b: n > 0 and b == (a + 1) % n)
    if base == "wheel":
        # hub 0 joined to the rim 1..n-1; the rim is a cycle when it has at
        # least three nodes and a path otherwise
        rim = list(range(1, n))
        edges = [(0, v) for v in rim]
        if len(rim) >= 3:
            edges += [(rim[i], rim[(i + 1) % len(rim)]) for i in range(len(rim))]
        elif len(rim) == 2:
            edges.append((1, 2))
        return n, D.normalize(edges, False)
    if base == "lattice":
        rows = 3
        e = [(r * n + c, r * n + c + 1) for r in range(rows) for c in range(n - 1)]
        e += [(r * n + c, (r + 1) * n + c) for r in range(rows - 1) for c in range(n)]
        return rows * n, D.normalize(e, False)
    if base == "tree_binary":
        return tree_edges(2, min(n, 5))
    if base == "tree_ternary":
        return tree_edges(3, min(n, 4))
    if base == "hypercube":
        size = 2 ** min(n, 8)
        return size, pairs(size, False, lambda a, b: bin(a ^ b).count("1") == 1)
    if base == "ladder":
        e = [(i, i + 1) for i in range(n - 1)] + [(n + i, n + i + 1) for i in range(n - 1)]
        e += [(i, i + n) for i in range(n)]
        return 2 * n, D.normalize(e, False)
    raise ValueError(name)


def line_graph(fx):
    edges = D.loop_free(D.first(fx))
    out = set()
    for i, (a, b) in enumerate(edges):
        for j, (c, d) in enumerate(edges):
            if i == j:
                continue
            if fx.directed:
                if b == c:
                    out.add((i, j))
            elif {a, b} & {c, d}:
                out.add((min(i, j), max(i, j)))
    return len(edges), sorted(out)


def simple_paths(fx, cutoff):
    n = fx.n
    arcs = set(D.loop_free(D.first(fx)))
    if not fx.directed:
        arcs |= {(b, a) for a, b in arcs}
    found = []

    def extend(path):
        if path[-1] == n - 1:
            found.append(list(path))
            return
        if len(path) - 1 == cutoff:
            return
        for v in range(n):
            if v not in path and (path[-1], v) in arcs:
                extend(path + [v])

    if n >= 2:
        extend([0])
    return sorted(found)


def compute(engine, fx):
    fn = engine["fn"]
    if fn == "deterministic_generators":
        n, edges = shape(engine["shape"], fx.n)
        return [n] + [list(e) for e in edges]
    if fn == "line_graph":
        n, edges = line_graph(fx)
        return [n] + [list(e) for e in edges]
    if fn == "paths_simple":
        return simple_paths(fx, engine["cutoff"])
    a, b = set(D.first(fx)), set(D.second(fx))
    if fn == "op_union":
        edges = a | b
    elif fn == "op_intersection":
        edges = a & b
    elif fn == "op_difference":
        edges = a - b
    elif fn == "op_compose":
        edges = {(u, w) for (u, v) in a for (v2, w) in b if v == v2}
    else:
        raise ValueError(fn)
    return [fx.n] + [list(e) for e in sorted(edges)]


def main() -> None:
    spec = load_area("construct")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, compute(v["params"], fx))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (construct): wrote {count} golden files")


if __name__ == "__main__":
    main()
