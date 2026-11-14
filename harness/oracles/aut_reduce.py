"""Inputs of the automorphism oracles (shared by the nauty and NetworkX
oracle scripts; the definition oracle works on count matrices instead, so it
shares nothing with this reduction).

reduce_graph turns a fixture, as the manifest entry reads it, into a simple
coloured graph that nauty, bliss and NetworkX can take:

  colours   node v has colour v % 2 under `parity`, 0 under `none`
  loops     a node's self-loops become part of its colour: whether it has
            one (`simple`) or how many (`multiplicity`)
  parallel  `simple`: each distinct pair (arc, when directed) is one edge;
            `multiplicity`: each distinct pair is subdivided by a new node
            coloured by the number of parallel edges, so that automorphisms
            of the coloured subdivision restricted to the original nodes are
            exactly the automorphisms of the multigraph, and the group
            orders are equal (an edge node is determined by its ends)

and returns (n_nodes, edges, colours, n_original): original nodes are the
first n_original nodes; a colour is the tuple (kind, user colour or
multiplicity, loop key), and color_ids turns tuples into small integers.
"""

from __future__ import annotations


def user_colors(n: int, kind: str) -> list[int]:
    return [0] * n if kind == "none" else [v % 2 for v in range(n)]


def reduce_graph(n: int, pairs, directed: bool, base: list[int], edges: str):
    """`base` is one user colour per node (see user_colors)."""
    multi = edges == "multiplicity"
    loops = [0] * n
    counts: dict = {}
    for a, b in pairs:
        if a == b:
            loops[a] += 1
        else:
            key = (a, b) if directed else (min(a, b), max(a, b))
            counts[key] = counts.get(key, 0) + 1
    tuples = [(0, base[v], loops[v] if multi else int(loops[v] > 0)) for v in range(n)]
    out_edges = []
    if multi:
        for index, key in enumerate(sorted(counts)):
            node = n + index
            tuples.append((1, counts[key], 0))
            out_edges.append((key[0], node))
            out_edges.append((node, key[1]))
    else:
        out_edges = sorted(counts)
    return len(tuples), out_edges, tuples, n


def color_ids(*tuple_lists):
    """Small integers for the colour tuples of several graphs, equal exactly when
    the tuples are equal (one table for all, so the graphs can be compared)."""
    table = {t: i for i, t in enumerate(sorted({t for tuples in tuple_lists for t in tuples}))}
    return [[table[t] for t in tuples] for tuples in tuple_lists]


def first_appearance(labels) -> list[int]:
    seen: dict = {}
    return [seen.setdefault(x, len(seen)) for x in labels]


def limbs16(value: int) -> list[int]:
    out = []
    while value:
        out.append(value & 0xFFFF)
        value >>= 16
    return out or [1]


def relabeled(n: int, pairs, directed: bool, seed: str):
    """Nodes renamed by a seeded shuffle, edges shuffled and (undirected) flipped:
    returns (perm, pairs) with perm[v] the new name of node v."""
    import random
    rng = random.Random(seed)
    perm = list(range(n))
    rng.shuffle(perm)
    out = []
    for a, b in pairs:
        a, b = perm[a], perm[b]
        if not directed and rng.random() < 0.5:
            a, b = b, a
        out.append((a, b))
    rng.shuffle(out)
    return perm, out


def rev_pairs(n: int, pairs):
    return list(range(n - 1, -1, -1)), [(n - 1 - a, n - 1 - b) for a, b in pairs][::-1]


def perturbed_pairs(n: int, pairs):
    return list(range(n)), list(pairs)[1:] + [(0, n - 1)]
