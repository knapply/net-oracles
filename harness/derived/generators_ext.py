"""Deterministic inputs for the named graphs, graph operations and degree
realizations of validation/manifest.d/generators_ext.yaml, shared by the
engine runner (bindings/generators_ext.py) and both oracles.

Every family is checked on a table of cases (the fixture graph is not used).
A case result is the node count and edge count, then the sorted edge list
(an undirected edge as (smaller, larger), an arc as (source, target)); for
the graphicality questions a case result is the single value 1 or 0.

Node numbering (also in docs/drafts/convention_atlas.md):

- barbell, lollipop, generalized Petersen, Turan, LCF, Dorogovtsev-
  Goltsev-Mendes: NetworkX's integer numbering (Turan: NetworkX's parts, the
  smaller ones first);
- hexagonal and triangular lattices: NetworkX labels the nodes by pairs
  (column, row); the integer is the rank of the pair among the surviving
  pairs in lexicographic order;
- graph products: node (u, x) of G x H is u * |H| + x;
- complement: the graph's own numbering.
"""

from __future__ import annotations

import itertools

BARBELL = [(2, 0), (2, 1), (3, 0), (3, 2), (4, 3), (5, 1), (4, 0)]
LOLLIPOP = [(2, 0), (2, 3), (3, 0), (3, 2), (5, 4), (4, 1)]
PETERSEN = [(3, 1), (4, 1), (4, 2), (5, 2), (6, 3), (7, 3), (8, 3), (10, 2), (10, 3), (12, 5)]
TURAN = [(1, 1), (2, 1), (5, 1), (5, 2), (5, 5), (7, 3), (8, 3), (10, 4), (6, 6), (9, 2)]
LCF = [(0, [3], 2), (6, [3], 6), (12, [5, -5], 6), (14, [5, -5], 7), (10, [0], 10), (5, [], 3),
       (8, [2, -2], 4), (1, [1], 1), (2, [1], 2), (6, [3, -3], 0), (7, [2, 3, -5], 3)]
DGM = [0, 1, 2, 3, 4, 5]
HEXAGONAL = [(1, 1, False), (1, 2, False), (2, 2, False), (3, 2, False), (2, 3, False),
             (3, 5, False), (4, 4, False), (0, 3, False), (3, 0, False),
             (2, 2, True), (2, 4, True), (3, 4, True), (4, 2, True), (3, 6, True)]
TRIANGULAR = [(1, 1, False), (1, 2, False), (2, 1, False), (2, 2, False), (3, 3, False),
              (4, 5, False), (5, 4, False), (0, 2, False), (2, 0, False),
              (3, 5, True), (4, 6, True), (5, 5, True), (3, 6, True)]
PRUFER_DECODE = [[], [0], [1], [3, 3, 3], [1, 0, 4, 4], [2, 2, 0, 1, 2], [5, 5, 5, 5, 6, 6],
                 [0, 0, 0], [4, 3, 2, 1, 0, 5, 7, 7]]
# Trees for the encoding: the trees of these Pruefer sequences (NetworkX
# builds them), so the sequence to recover is known to the oracle.
PRUFER_ENCODE = PRUFER_DECODE
GRAPHICAL = [[], [0], [0, 0], [1], [1, 1], [2, 2, 2], [2, 2, 1], [3, 3, 3, 3], [3, 3, 1, 1],
             [3, 2, 2, 2, 1], [4, 1, 1, 1, 1], [5, 1, 1], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5],
             [6, 3, 3, 3, 3, 3, 3], [2, 2, 2, 2, 2, 2], [5, 5, 4, 3, 2, 2, 2, 1],
             [-1, 1], [1, 1, 1], [3, 3, 2, 2, 2], [7, 7, 7, 7, 7, 7, 7, 7], [4, 4, 4, 1, 1, 1, 1, 0]]
# (in-degrees, out-degrees)
DIGRAPHICAL = [([], []), ([0], [0]), ([1], [1]), ([1, 1], [1, 1]), ([2, 0], [0, 2]),
               ([1, 2, 1, 0], [2, 0, 1, 1]), ([1, 1, 1], [1, 1, 1]), ([2, 2, 2], [2, 2, 2]),
               ([3, 0, 0, 0], [0, 1, 1, 1]), ([0, 1, 1, 1], [3, 0, 0, 0]),
               ([2, 1, 1, 0], [1, 1, 1, 1]), ([1, 1, 1, 1], [2, 2, 0, 0]),
               ([1, 0, 1], [0, 1, 1]), ([2, 2, 1, 1], [1, 2, 2, 1]), ([-1, 1], [0, 0]),
               ([2, 1], [1, 2])]
# (row degrees, column degrees)
BIGRAPHICAL = [([], []), ([0], [0]), ([1], [1]), ([2], [1, 1]), ([3, 0], [1, 1]),
               ([3, 2, 2, 1], [2, 2, 2, 1, 1]), ([2, 2], [2, 2]), ([3, 3], [2, 2, 2]),
               ([3, 3, 3], [3, 3, 3]), ([4, 1], [3, 2]), ([1, 1, 1], [3]), ([2, 2, 2], [3, 3]),
               ([2, 1], [2, 1]), ([5, 3, 3, 1], [4, 4, 3, 1]), ([2, 0], [1, 1]),
               ([1, 1, 2], [2, 1, 1]), ([-1, 1], [0, 0])]

# Graphs for the complement and the products: (node count, edges, directed).
GRAPHS = {
    "null": (0, [], False),
    "single": (1, [], False),
    "loop": (1, [(0, 0)], False),
    "edge": (2, [(0, 1)], False),
    "path3": (3, [(0, 1), (1, 2)], False),
    "triangle": (3, [(0, 1), (0, 2), (1, 2)], False),
    "cycle4": (4, [(0, 1), (1, 2), (2, 3), (0, 3)], False),
    "isolates": (3, [], False),
    "mixed": (5, [(0, 1), (1, 3), (2, 3), (0, 4), (2, 2)], False),
    "star4": (4, [(0, 1), (0, 2), (0, 3)], False),
    "arcs3": (3, [(0, 1), (1, 2), (2, 0)], True),
    "arcs4": (4, [(0, 1), (1, 0), (1, 2), (3, 3), (0, 3)], True),
    "arc": (2, [(0, 1)], True),
}
COMPLEMENT = [("null", False), ("single", False), ("loop", False), ("edge", False),
              ("path3", False), ("triangle", False), ("cycle4", False), ("isolates", False),
              ("mixed", False), ("mixed", True), ("star4", False), ("arcs3", False),
              ("arcs4", False), ("arc", False), ("loop", True), ("path3", True)]
PRODUCT_PAIRS = [("path3", "edge"), ("edge", "path3"), ("cycle4", "triangle"),
                 ("isolates", "edge"), ("single", "triangle"), ("null", "edge"),
                 ("edge", "null"), ("mixed", "loop"), ("loop", "mixed"), ("star4", "path3"),
                 ("arcs3", "arc"), ("arc", "arcs4"), ("arcs4", "arcs3")]

# Parameters outside the documented domain: (kind label, text the error
# message must contain). The kind labels are those of bindings/generators_ext.py.
INVALID = [
    ("barbell", [1, 0], "at least 2 nodes"),
    ("lollipop", [1, 3], "at least 2 nodes"),
    ("generalized_petersen", [2, 1], "n >= 3"),
    ("generalized_petersen", [6, 4], "1 <= k <= n / 2"),
    ("turan", [3, 4], "1 <= r <= n"),
    ("turan", [3, 0], "1 <= r <= n"),
    ("dgm", [17], "generations"),
    ("hexagonal", [3, 3, 1], "even number of columns"),
    ("triangular", [2, 5, 1], "rows > 2 and columns > 4"),
    ("havel_hakimi", [3, 3, 1, 1], "not graphical"),
    ("kleitman_wang", [2, 2, 0, 0, 2], "not digraphical"),
    ("gale_ryser", [2, 3, 0, 1, 1], "not bigraphical"),
    ("prufer_decode", [5], "outside"),
]

FAMILIES = {
    "barbell": BARBELL, "lollipop": LOLLIPOP, "generalized_petersen": PETERSEN,
    "turan": TURAN, "lcf": LCF, "dgm": DGM, "hexagonal": HEXAGONAL, "triangular": TRIANGULAR,
}


def normalize(edges, directed):
    return sorted({(a, b) if directed else (min(a, b), max(a, b)) for a, b in edges})


def pack(nodes, edges):
    """[(node count, edge count)] followed by the edges."""
    return [(nodes, len(edges))] + [tuple(e) for e in edges]


def cases(family):
    """The parameter tuples of a family."""
    return FAMILIES[family]


def graph(name):
    return GRAPHS[name]


def realization_cases(family):
    """Degree sequences realized by the construction families."""
    if family == "havel_hakimi":
        return [s for s in GRAPHICAL if all(x >= 0 for x in s) and sum(s) % 2 == 0
                and graphical_reference(s)]
    if family == "kleitman_wang":
        return [c for c in DIGRAPHICAL if digraphical_reference(*c)]
    return [c for c in BIGRAPHICAL if bigraphical_reference(*c)]


def graphical_reference(sequence):
    """Whether some simple graph has the degrees, by exhaustive search: each
    node in turn picks its remaining neighbours among the later nodes."""
    if any(x < 0 for x in sequence):
        return False
    remaining = list(sequence)
    n = len(remaining)

    def place(node):
        if node == n:
            return True
        need = remaining[node]
        later = range(node + 1, n)
        for chosen in itertools.combinations(later, need):
            if all(remaining[t] > 0 for t in chosen):
                for t in chosen:
                    remaining[t] -= 1
                ok = place(node + 1)
                for t in chosen:
                    remaining[t] += 1
                if ok:
                    return True
        return False

    return sum(sequence) % 2 == 0 and place(0)


def bigraphical_reference(rows, columns):
    """Whether some simple bipartite graph has the degrees, by exhaustive
    search: each row in turn picks its columns."""
    if any(x < 0 for x in rows + columns):
        return False
    remaining = list(columns)

    def place(row):
        if row == len(rows):
            return all(x == 0 for x in remaining)
        for chosen in itertools.combinations(range(len(columns)), rows[row]):
            if all(remaining[c] > 0 for c in chosen):
                for c in chosen:
                    remaining[c] -= 1
                ok = place(row + 1)
                for c in chosen:
                    remaining[c] += 1
                if ok:
                    return True
        return False

    return place(0)


def digraphical_reference(in_degrees, out_degrees):
    """Whether some simple digraph has the degrees, by exhaustive search:
    each node in turn picks its out-neighbours."""
    if any(x < 0 for x in in_degrees + out_degrees):
        return False
    remaining = list(in_degrees)
    n = len(remaining)

    def place(node):
        if node == n:
            return all(x == 0 for x in remaining)
        others = [t for t in range(n) if t != node]
        for chosen in itertools.combinations(others, out_degrees[node]):
            if all(remaining[t] > 0 for t in chosen):
                for t in chosen:
                    remaining[t] -= 1
                ok = place(node + 1)
                for t in chosen:
                    remaining[t] += 1
                if ok:
                    return True
        return False

    return place(0)
