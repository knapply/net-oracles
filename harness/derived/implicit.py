"""Deterministic inputs for the formula families of
validation/manifest.d/implicit.yaml, shared by the engine runner
(bindings/implicit.py) and both oracles.

Every family is checked on a table of cases that covers the empty graph,
one node, two nodes, the smallest valid sizes and a few larger ones, so the
fixture graph is not used. A case result is the node count and edge count,
then the sorted edge list: an undirected edge as (smaller, larger), an arc as
(source, target).

Node numbering (also in docs/drafts/convention_atlas.md):

- complete bipartite, complete multipartite, star, path, wheel, circulant:
  NetworkX's integer numbering;
- hypercube: the bit string (b_0, ..., b_{d-1}) of NetworkX's tuple label is
  the integer with b_0 as the most significant bit;
- de Bruijn B(k, n): the word w_0 ... w_{n-1} is the base-k integer with w_0
  most significant;
- Kautz K(m, d): the word w_0 ... w_d over m + 1 letters (no equal neighbours)
  is w_0 * m^d plus the base-m number whose digits are the ranks
  r_i = w_i - [w_i > w_{i-1}] for i = 1 .. d (r_1 most significant).
  NetworkX has no de Bruijn or Kautz generator; its oracle builds them as
  iterated line digraphs.
"""

from __future__ import annotations

BIPARTITE = [(0, 0), (0, 3), (3, 0), (1, 1), (2, 3), (5, 4), (9, 7)]
MULTIPARTITE = [[], [0], [1], [3], [1, 1], [2, 3], [1, 1, 1], [2, 0, 3, 1], [4, 4, 4],
                [1, 2, 3, 4, 5]]
STAR = [0, 1, 2, 3, 8, 20]
PATH = [0, 1, 2, 3, 10, 25]
WHEEL = [4, 5, 6, 9, 30]
HYPERCUBE = [1, 2, 3, 5, 7]
CIRCULANT = [(0, []), (1, []), (2, [1]), (3, [1]), (4, [1, 2]), (5, [2]), (6, [1, 3]),
             (7, [1, 2, 3]), (8, [4]), (9, [1, 8]), (10, [1, 3, 5]), (12, [2, 6, 5, 7]),
             (13, [5, 1]), (20, [1, 7, 10, 13, 7])]
DE_BRUIJN = [(2, 1), (2, 2), (2, 3), (2, 6), (3, 1), (3, 2), (3, 4), (4, 3), (5, 2)]
KAUTZ = [(1, 1), (1, 3), (2, 1), (2, 2), (2, 3), (2, 5), (3, 1), (3, 2), (3, 3), (4, 2)]

# Invalid parameters: (family, arguments, text the error message must contain).
INVALID = [
    ("wheel", [0], "n >= 4"),
    ("wheel", [3], "n >= 4"),
    ("circulant", [6, [0]], "circulant offset 0"),
    ("circulant", [6, [6]], "circulant offset 6"),
    ("circulant", [1, [1]], "circulant offset 1"),
    ("hypercube", [29], "edge count"),
    ("hypercube", [40], "at most 31"),
    ("de_bruijn", [1, 3], "at least 2 letters"),
    ("de_bruijn", [2, 0], "word length of at least 1"),
    ("de_bruijn", [2, 32], "exceeds the supported maximum"),
    ("kautz", [0, 2], "at least 1 move"),
    ("kautz", [2, 0], "order 0 is the complete digraph"),
    ("complete_bipartite", [70000, 70000, 0], "edge count"),
    ("complete_multipartite", [[70000, 70000]], "edge count"),
]


def normalize(edges, directed):
    return sorted({(a, b) if directed else (min(a, b), max(a, b)) for a, b in edges})


def pack(nodes, edges):
    """[(node count, edge count)] followed by the edges."""
    return [(nodes, len(edges))] + [tuple(e) for e in edges]


def cases(family):
    """The parameter tuples of a family (an entry name without the direction)."""
    table = {"complete_bipartite": BIPARTITE, "complete_multipartite": [(s,) for s in MULTIPARTITE],
             "star": [(n,) for n in STAR], "path": [(n,) for n in PATH],
             "wheel": [(n,) for n in WHEEL], "hypercube": [(d,) for d in HYPERCUBE],
             "circulant": CIRCULANT, "de_bruijn": DE_BRUIJN, "kautz": KAUTZ}
    return table[family]


def kautz_id(word, moves):
    """The documented node number of a Kautz word."""
    number = word[0]
    for prev, cur in zip(word, word[1:]):
        number = number * moves + (cur - (cur > prev))
    return number


def debruijn_id(word, letters):
    number = 0
    for digit in word:
        number = number * letters + digit
    return number
