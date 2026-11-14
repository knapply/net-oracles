#!/usr/bin/env python3
"""Definition oracle for the automorphism measures: the group order and the
orbit partition from the definition, with no use of refinement beyond a
necessary condition for pruning.

An automorphism is a permutation of the nodes that keeps every node's colour
and, for every ordered pair, the pair's entry (whether the pair is tied, or
how many parallel edges it has under `multiplicity`; self-loops are the
diagonal and count under the same rule). Existence of an automorphism that
fixes some nodes and sends v to c is decided by backtracking over partial
maps, checking every pair of mapped nodes; candidates are pruned only by
colour classes of the repeated neighbour-colour refinement, which every
isomorphism preserves. The group order is then the product, along any
sequence of nodes, of the orbit of each node under the automorphisms fixing
the earlier ones (orbit-stabilizer), and the orbits are the sets of nodes c
with an automorphism v -> c.

Canonical-form entries: a canonical form is a function of the isomorphism
class, so seeded relabelings of a fixture must give the same form: the
oracle counts how many of 8 seeded relabelings are isomorphic to it (by the
same backtracking), and for the pair checks whether the fixture is
isomorphic to rev(fixture) and perturbed(fixture).

    python3 oracles/automorphisms_definition_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from aut_reduce import limbs16, perturbed_pairs, relabeled, rev_pairs  # noqa: E402
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
RELABELINGS = 8
FACTS: dict = {}


def matrix_of(n, pairs, directed, multi):
    """Entry of every ordered pair; the diagonal holds the self-loops."""
    counts = [[0] * n for _ in range(n)]
    for a, b in pairs:
        counts[a][b] += 1
        if not directed and a != b:
            counts[b][a] += 1
    return [[c if multi else int(c > 0) for c in row] for row in counts]


def colors_of(n, kind):
    return [0] * n if kind == "none" else [v % 2 for v in range(n)]


def refine(mats, colors_list, directed):
    """Repeated neighbour-colour refinement of several graphs at once, so that
    equal colours are comparable across graphs. Returns colours per graph."""
    cols = [list(c) for c in colors_list]
    classes = -1
    while True:
        table: dict = {}
        nxt = []
        for mat, col in zip(mats, cols):
            n = len(mat)
            row = []
            for v in range(n):
                out = tuple(sorted((mat[v][u], col[u]) for u in range(n) if u != v and mat[v][u]))
                inc = tuple(sorted((mat[u][v], col[u]) for u in range(n) if u != v and mat[u][v])) \
                    if directed else ()
                row.append((col[v], mat[v][v], out, inc))
            nxt.append(row)
        for row in nxt:
            for sig in row:
                table.setdefault(sig, len(table))
        cols = [[table[s] for s in row] for row in nxt]
        if len(table) == classes:
            return cols
        classes = len(table)


def exists_map(a_mat, b_mat, a_col, b_col, directed, fixed, extra=None):
    """Whether some bijection f with f(u) = fixed[u] (and f(extra[0]) = extra[1]) keeps
    colours and every ordered-pair entry from graph a to graph b."""
    n = len(a_mat)
    start_a = list(a_col)
    start_b = list(b_col)
    tag = max(a_col + b_col + [0]) + 1
    pre = dict(fixed)
    if extra:
        pre[extra[0]] = extra[1]
    for k, (u, w) in enumerate(sorted(pre.items())):
        start_a[u] = tag + k
        start_b[w] = tag + k
    ca, cb = refine([a_mat, b_mat], [start_a, start_b], directed)
    if sorted(ca) != sorted(cb):
        return False
    pool: dict = {}
    for w in range(n):
        pool.setdefault(cb[w], []).append(w)
    # Order: fixed nodes first, then breadth-first by adjacency, smallest class first.
    order = sorted(pre)
    seen = set(order)
    frontier = list(order)
    while len(seen) < n:
        if not frontier:
            frontier = [min((v for v in range(n) if v not in seen),
                            key=lambda v: (len(pool[ca[v]]), v))]
            seen.add(frontier[0])
            order.append(frontier[0])
        nxt = []
        for v in frontier:
            for u in range(n):
                if u not in seen and (a_mat[v][u] or a_mat[u][v]):
                    seen.add(u)
                    order.append(u)
                    nxt.append(u)
        frontier = nxt
    image: dict = {}
    used: set = set()

    def place(i):
        if i == n:
            return True
        u = order[i]
        for w in ([pre[u]] if u in pre else pool[ca[u]]):
            if w in used or cb[w] != ca[u]:
                continue
            if a_mat[u][u] != b_mat[w][w]:
                continue
            if all(a_mat[u][x] == b_mat[w][image[x]] and a_mat[x][u] == b_mat[image[x]][w]
                   for x in image):
                image[u] = w
                used.add(w)
                if place(i + 1):
                    return True
                del image[u]
                used.discard(w)
        return False
    return place(0)


def group_facts(n, mat, col, directed):
    """(order, orbit labels) from the definition."""
    refined = refine([mat], [col], directed)[0]
    order = 1
    fixed: dict = {}
    for v in range(n):
        orbit = sum(1 for c in range(n)
                    if refined[c] == refined[v]
                    and (c == v or exists_map(mat, mat, col, col, directed, fixed, (v, c))))
        order *= orbit
        fixed[v] = v
    labels = list(range(n))
    for v in range(n):
        for c in range(v):
            if labels[c] != labels[v] and refined[c] == refined[v] \
                    and exists_map(mat, mat, col, col, directed, {}, (v, c)):
                old = labels[v]
                labels = [labels[c] if x == old else x for x in labels]
    seen: dict = {}
    return order, [seen.setdefault(x, len(seen)) for x in labels]


def compute(fx, spec):
    e = spec["params"]
    multi = e.get("edges", "simple") == "multiplicity"
    kind = e.get("colors", "none")
    n = fx.n
    pairs = list(zip(fx.src, fx.tgt))
    if e["fn"] == "automorphism":
        key = (fx.name, kind, multi)
        if key not in FACTS:
            mat = matrix_of(n, pairs, fx.directed, multi)
            FACTS[key] = group_facts(n, mat, colors_of(n, kind), fx.directed)
        order, labels = FACTS[key]
        return labels if e["output"] == "orbits" else limbs16(order)
    mat = matrix_of(n, pairs, fx.directed, multi)
    col = colors_of(n, kind)

    def iso_to(perm, other_pairs):
        other = matrix_of(n, other_pairs, fx.directed, multi)
        moved = [0] * n
        for v in range(n):
            moved[perm[v]] = col[v]
        return exists_map(mat, other, col, moved, fx.directed, {})
    if e["check"] == "relabelings":
        return [sum(iso_to(*relabeled(n, pairs, fx.directed, f"def-{fx.name}-{s}"))
                    for s in range(RELABELINGS))]
    return [int(iso_to(*rev_pairs(n, pairs))), int(iso_to(*perturbed_pairs(n, pairs)))]


def main() -> None:
    manifest = load_area("automorphisms")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        if fx.n == 0:
            continue
        for variant, spec in manifest.items():
            if ORACLE not in spec["oracles"] or not applies(spec, fx):
                continue
            write_values(ORACLE, name, variant, compute(fx, spec))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition: wrote {count} golden files")


if __name__ == "__main__":
    main()
