"""Cases of the file-format entries of validation/manifest.d/io_formats.yaml
(edge list, DIMACS, graph6, LEDA, Matrix Market), shared by the engine
runner (bindings/io_formats.py) and the oracles. Each case is the text of a
file; the result of reading it is packed the same way by every tool:

    (directed, n, m)                     one row
    (a, b, has_value, value)             m rows, sorted

with a and b the positions of the endpoints in the node order of the file
(first mention for edge lists, the numbers for the numbered formats), an
undirected edge written with a <= b, and `value` the edge value that the
format carries (weight, capacity or cost; 0 when there is none). Node ids
are text in the engine and ids or integers in the oracles, so only positions
are compared. `directed` may be forced for an edge list (None: the format
decides; an edge list is undirected).
"""

from __future__ import annotations

# ---- edge list: (text, directed option, delimiter for the oracles) -------
EDGELIST = [
    ("a b\nb c\nc a\n", False, None),
    ("a b\nb c\nc a\n", True, None),
    ("1 2 0.5\n2 3 1.5\n3 1 2\n", False, None),
    ("1 2 -0.5\n2 3 1e3\n", True, None),
    ("# header\n\n1 2\n  3   4  # tail\n", False, None),
    ("1 1\n1 2\n1 2\n", False, None),
    ("1 2\n1 2\n2 1\n", True, None),
    ("1\t2\n2\t3\n", False, None),
    ("1,2\n2,3\n", False, ","),
    ("", False, None),
    ("# only a comment\n", False, None),
    ("1 2\r\n2 3\r\n", False, None),
    ("x y\ny z", False, None),
    ("b a\na c\nc b\n", True, None),
]
# Node ids 0, 1, 2, ... in order of first mention, no loops or repeated
# edges, so NetworKit's reader (which numbers nodes itself) agrees.
EDGELIST_INT = [
    ("0 1\n1 2\n2 3\n", False),
    ("0 1\n0 2\n1 2\n", False),
    ("0 1\n1 2\n2 0\n", True),
    ("0 1\n2 0\n1 2\n# note\n", True),
    ("0 1\n1 2\n2 3\n3 4\n4 0\n0 2\n", False),
]

# ---- DIMACS (definition oracle only: no permissive tool reads it) ---------
DIMACS = [
    "c colouring\np edge 4 3\ne 1 2\ne 2 3\ne 4 4\n",
    "p col 3 0\n",
    "p edge 1 0\n",
    "p edge 0 0\n",
    "c comment\np sp 3 3\na 1 2 7\na 3 1 0.25\na 2 2 -1\n",
    "p sp 3 2\na 1 2 1\na 1 2 2\n",
    "p max 4 5\nn 1 s\nn 4 t\na 1 2 4\na 1 3 2\na 2 3 1\na 2 4 3\na 3 4 5\n",
    "p min 3 2\nn 1 5\nn 3 -5\na 1 2 0 10 3\na 2 3 1 9 0.5\n",
    "p edge 3 1\r\ne 1 3\r\n",
]

# DIMACS maximum flow, the one DIMACS form igraph reads (`p edge` needs flow data
# there, `sp` and `min` are not read): the sixth case of DIMACS.
DIMACS_FLOW = [DIMACS[6]]

# LEDA files written by python-igraph's write_leda (the builders are in
# oracles/io_formats_igraph_oracle.py, which checks the texts still match).
LEDA_IGRAPH = [
    "LEDA.GRAPH\nstring\ndouble\n-1\n# Vertices\n3\n|{a}|\n|{b}|\n|{c}|\n# Edges\n3\n1 2 0 |{2.5}|\n2 3 0 |{-1}|\n3 1 0 |{0.125}|\n",
    "LEDA.GRAPH\nvoid\nvoid\n-2\n# Vertices\n4\n|{}|\n|{}|\n|{}|\n|{}|\n# Edges\n4\n1 2 0 |{}|\n1 4 0 |{}|\n2 3 0 |{}|\n2 4 0 |{}|\n",
    "LEDA.GRAPH\nvoid\nvoid\n-2\n# Vertices\n0\n# Edges\n0\n",
    "LEDA.GRAPH\nvoid\nvoid\n-1\n# Vertices\n3\n|{}|\n|{}|\n|{}|\n# Edges\n2\n1 3 0 |{}|\n3 2 0 |{}|\n",
]

# ---- graph6 -----------------------------------------------------------------
GRAPH6 = [
    '?',
    '@',
    'A_',
    'Ch',
    'D~{',
    'Dhc',
    'IheA@GUAo',
    'F????',
    '~??~saCCA?_C?O?_?_?O?C??_?A??C??C??A???_??C???O???_???_???O???C????_???A????C????C????A?????_????C?????O?????_?????_?????O?????C??????_?????A??????C??????C??????A???????_??????C???????O???????_???????_???????O???????C????????_???????A????????C????????C????????A?????????_????????C?????????O?????????_?????????_?????????O??????????',
    '}hCGGC@?G?_@?@??_?G?@??C??G??G??C??@???G???_??@???@????_???G???@????C????G????G????C????@?????G?????_????@?????@??????_?????G?????@??????C??????G??????G??????C??????@???????G???????_??????@???????@????????_???????G???????@????????C????????G????????G????????C????????@?????????G?????????_????????@?????????@??????????_',
    'S`Ws[PC`SOADBW@Aa@WbH_c_?Gg_???E_',
    'a~aC^a_GCWO?c?{??????@_B?????E??????o?????????????????@_???@???KG???????Ca@???C???EO__qkF?K[zNw'
]
GRAPH6_HEADER = ">>graph6<<" + GRAPH6[4]

# ---- LEDA: (text, edge type) -------------------------------------------------
LEDA = [
    "LEDA.GRAPH\nstring\nvoid\n-2\n# nodes\n3\n|{a}|\n|{b}|\n|{c}|\n# edges\n2\n1 2 0 |{}|\n2 3 0 |{}|\n",
    "LEDA.GRAPH\nstring\ndouble\n-1\n# nodes\n3\n|{x}|\n|{y}|\n|{z}|\n# edges\n3\n1 2 0 |{2.5}|\n2 3 0 |{-1}|\n3 1 0 |{0.125}|\n",
    "LEDA.GRAPH\nvoid\nvoid\n-2\n3\n|{}|\n|{}|\n|{}|\n2\n1 3 0 |{}|\n3 2 0 |{}|\n",
    "LEDA.GRAPH\nstring\nint\n-1\n2\n|{p}|\n|{q}|\n2\n1 2 2 |{7}|\n2 1 1 |{8}|\n",
    "LEDA.GRAPH\nstring\nvoid\n-2\n0\n0\n",
    "LEDA.GRAPH\nstring\nvoid\n-2\n# nodes\n1\n|{only}|\n# edges\n0\n",
    "LEDA.GRAPH\r\nstring\r\nvoid\r\n-1\r\n2\r\n|{u}|\r\n|{v}|\r\n1\r\n1 2 0 |{}|\r\n",
]

# ---- Matrix Market ----------------------------------------------------------
MTX = [
    "%%MatrixMarket matrix coordinate real general\n% a comment\n3 3 2\n1 2 2.5\n3 3 1\n",
    "%%MatrixMarket matrix coordinate pattern symmetric\n3 3 2\n2 1\n3 2\n",
    "%%MatrixMarket matrix coordinate integer symmetric\n4 4 4\n1 1 5\n2 1 -3\n4 3 2\n4 1 7\n",
    "%%MatrixMarket matrix coordinate pattern general\n3 3 4\n1 2\n2 1\n2 3\n3 3\n",
    "%%MatrixMarket matrix array real general\n3 3\n0\n1\n0\n2\n0\n0\n0\n3\n4.5\n",
    "%%MatrixMarket matrix array real symmetric\n3 3\n1\n2\n0\n3\n4\n5\n",
    "%%MatrixMarket matrix coordinate real skew-symmetric\n3 3 2\n2 1 4\n3 2 -1.5\n",
    "%%MatrixMarket matrix coordinate real general\n1 1 1\n1 1 3\n",
    "%%MatrixMarket matrix coordinate real general\n0 0 0\n",
    "%%MatrixMarket matrix coordinate real general\n5 5 0\n",
    "%%MatrixMarket matrix coordinate real general\r\n2 2 1\r\n2 1 1e-3\r\n",
]

# Matrix Market files that NetworKit reads too: coordinate, not skew-symmetric.
MTX_COORDINATE = [t for t in MTX if " coordinate " in t.splitlines()[0]
                  and "skew" not in t.splitlines()[0]]

# ---- malformed input: (format, text, words the message must contain) -------
INVALID = [
    ("edgelist", "a b c d\n", "three fields"),
    ("edgelist", "a b\nb c heavy\n", "not a number"),
    ("dimacs", "e 1 2\n", "before the problem line"),
    ("dimacs", "p edge 2 1\ne 1 5\n", "outside"),
    ("dimacs", "p edge 2 2\ne 1 2\n", "declares 2 edges"),
    ("dimacs", "p tsp 2 1\n", "unknown problem type"),
    ("dimacs", "p sp 2 1\na 1 2 x\n", "not a number"),
    ("dimacs", "", "no problem line"),
    ("graph6", "D", "ends inside"),
    ("graph6", "DQ\x01\n", "not a graph6 character"),
    ("graph6", "DQcc\n", "complete graph"),
    ("graph6", "A`\n", "padding"),
    ("graph6", "DQc\nDQc\n", "more than one graph"),
    ("graph6", "", "no graph"),
    ("leda", "GRAPH\n", "LEDA.GRAPH"),
    ("leda", "LEDA.GRAPH\nvoid\nvoid\n-3\n", "-1 (directed)"),
    ("leda", "LEDA.GRAPH\nvoid\nvoid\n-2\n2\n|{a}|\n", "ends before"),
    ("leda", "LEDA.GRAPH\nvoid\nvoid\n-2\n1\n|{a}|\n1\n1 2 0 |{}|\n", "outside"),
    ("leda", "LEDA.GRAPH\nvoid\nvoid\n-2\n2\n|{a}|\n|{a}|\n0\n", "twice"),
    ("mtx", "", "empty"),
    ("mtx", "%%MatrixMarket matrix coordinate complex general\n1 1 0\n", "not graphs"),
    ("mtx", "%%MatrixMarket matrix coordinate real general\n2 3 0\n", "square"),
    ("mtx", "%%MatrixMarket matrix coordinate real general\n2 2 2\n1 1 1\n", "declares 2 entries"),
    ("mtx", "%%MatrixMarket matrix coordinate real general\n2 2 1\n3 1 1\n", "outside"),
    ("mtx", "%%MatrixMarket matrix array real general\n2 2\n1\n", "needs 4"),
]


def pack(directed, n_nodes, edges):
    """The packed result of reading one file: the header row, then one row per
    edge (a, b, has_value, value) sorted, an undirected edge as a <= b.
    `edges` is a list of (a, b, value or None) with node positions a and b."""
    rows = []
    for a, b, value in edges:
        if not directed and a > b:
            a, b = b, a
        rows.append((a, b, 0 if value is None else 1, 0.0 if value is None else float(value)))
    rows.sort()
    return [(int(directed), n_nodes, len(edges))] + rows


def edge_value(columns):
    """The column that holds the edge value of a file: weight, capacity or cost."""
    for name in ("weight", "cost", "capacity"):
        if name in columns:
            return name
    return None
