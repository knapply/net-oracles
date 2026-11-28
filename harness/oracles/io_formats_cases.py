"""Cases of the file formats added after the line formats of
derived/io_formats.py (METIS, SNAP, KONECT, graph-tool binary, NCOL, LGL,
adjacency matrices, CSV, TSPLIB, partitions and covers), shared by the engine
runner (bindings/io_formats.py) and the oracles of manifest/io_formats.yaml.
Each case is the text (or bytes) of a file, and the result of reading it is
packed as in derived/io_formats.py (`pack`), or by `pack_partition` and
`pack_cover` below.

The cases live here (oracles/), not in derived/, because every file of derived/ is part of
every oracle script's input hash: adding a case there would rerun all oracles.
A changed case makes the engine entry disagree with its stale golden, which
`compare.py` reports as a failure, so a stale golden cannot pass.
"""

from __future__ import annotations

from derived.io_formats import pack  # noqa: F401  (the shared packed encoding)

# ---- METIS: the files NetworKit reads (it ignores node weights and sizes) ----
METIS = [
    "3 2\n2 3\n1\n1\n",
    "3 2 1\n2 5 3 7\n1 5\n1 7\n",
    "4 3 0\n2\n1 3\n2 4\n3\n",
    "% c\n3 3\n2 3\n1 3\n1 2\n",
    "3 2 10\n5 2 3\n6 1\n7 1\n",
    "3 2 11\n5 2 9 3 8\n6 1 9\n7 1 8\n",
    "3 1\n2\n1\n\n",
    "2 1\n2\n1\n",
    "4 3 1\n2 2.5\n1 2.5 3 1\n2 1 3 3\n\n",
    "0 0\n",
    "3 0\n\n\n\n",
    "3 2\r\n2 3\r\n1\r\n1\r\n",
]
# Entries that carry a node weight or size, which the packed result leaves out.

# ---- SNAP: the files NetworKit reads (undirected, each edge once); its node
# remapping follows a hash order, so the cases number their nodes 0, 1, 2, ...
# and are read without remapping, the node being its number --------------------
SNAP = [
    "# c\n0\t1\n1\t2\n",
    "# Nodes: 4\n3 1\n1 2\n3 2\n0 2\n",
    "0 1\n1 0\n",
    "0 0\n",
    "# x\n",
    "0 1\n0 1\n1 0\n",
    "2 0\r\n0 1\r\n",
    "3 1\n2 3\n\n1 2\n0 3\n",
    "# Directed graph\n0 1\n1 2\n",
]

# ---- KONECT: nodes are the numbers, so a position is the number minus 1 ----
KONECT = [
    "% sym unweighted\n1 2\n2 3\n",
    "% sym unweighted\n% 2 3 3\n1 2\n2 3\n",
    "% sym posweighted\n1 2 3\n2 3 4\n",
    "% asym unweighted\n3 1\n1 3\n",
    "% sym signed\n1 2 -1\n",
    "% sym unweighted\n5 5\n",
    "% asym posweighted\n1 2 5\n2 3 0.5\n",
    "% sym unweighted\r\n1 2\r\n",
    "% sym unweighted\n\n1 2\n% mid\n2 3\n",
    "% sym unweighted\n1 1\n",
]

# ---- graph-tool binary: (directed, nodes, edges); files from gt_bytes -------
GT = [
    (False, 4, [(0, 1), (1, 2), (2, 3)]),
    (True, 3, [(0, 1), (2, 0)]),
    (False, 0, []),
    (False, 5, []),
    (False, 4, [(0, 1), (1, 2), (2, 2)]),
    (True, 4, [(0, 1), (0, 2), (0, 3), (3, 0), (3, 3)]),
    (False, 300, [(i, (i + 7) % 300) for i in range(300)]),
    (True, 70000, [(0, 69999), (69999, 5), (1, 2)]),
]


def gt_bytes(directed, n_nodes, edges):
    """The bytes of a graph-tool `.gt` file (little-endian, no comment, no
    properties) for the given edges, each listed under its first endpoint, as
    the format's description says. Written here from that description."""
    import struct
    width = 1 if n_nodes < 1 << 8 else 2 if n_nodes < 1 << 16 else 4
    rows = [[] for _ in range(n_nodes)]
    for a, b in edges:
        rows[a].append(b)
    out = bytearray(b"\xe2\x9b\xbe gt" + bytes([1, 0]) + struct.pack("<Q", 0))
    out += bytes([int(directed)]) + struct.pack("<Q", n_nodes)
    for row in rows:
        out += struct.pack("<Q", len(row))
        for b in row:
            out += b.to_bytes(width, "little")
    out += struct.pack("<Q", 0)
    return bytes(out)


# ---- NCOL and LGL: (text, directed); the cases are all weighted or none -----
NCOL = [
    ("a b\nb c\nc a\n", False),
    ("a b\nb c\nc a\n", True),
    ("a b 2.5\nb c 1\n", False),
    ("a b 2.5\nb c 1\n", True),
    ("a  b\n\nb c\n", False),
    ("a b\na b\nb a\n", False),
    ("a b\na b\nb a\n", True),
    ("a a\n", False),
    ("1 2\n3 4\n", False),
    ("a b\r\nb c\r\n", False),
    ("a b 1e3\n", False),
    ("a\tb\n", True),
    ("a b -1\nb c 0.125\n", True),
    ("", False),
    ("# c\na b\n", False),
]
LGL = [
    ("# a\nb\nc\n# b\nc\n", False),
    ("# a\nb\nc\n# b\nc\n", True),
    ("# a\nb 2.5\nc 1\n# b\nc 3\n", False),
    ("# a\nb 2.5\nc 1\n# b\nc 3\n", True),
    ("# a\n# b\n# c\n", False),
    ("# a\nb\n# b\na\n", False),
    ("# a\nb\n# b\na\n", True),
    ("# a\nb\n\n# c\nd\n", False),
    ("#a\nb\n", False),
    ("# a\nb\nb\n", False),
    ("# a\na\n", True),
    ("# a\r\nb\r\n", False),
    ("", False),
    ("  # a\n  b  \n", False),
    ("# a\nb -1\n# b\nc 0.125\n", True),
]

# ---- adjacency matrices: (text, directed) -----------------------------------
ADJACENCY = [
    ("0 1 0\n1 0 1\n0 1 0\n", False),
    ("0 1 0\n1 0 1\n0 1 0\n", True),
    ("0 1 1\n0 0 0\n1 0 0\n", True),
    ("0 2 0\n2 0 1\n0 1 0\n", False),
    ("1 0\n0 0\n", False),
    ("2 0\n0 0\n", False),
    ("# c\n0 1\n1 0\n", False),
    ("0 1\n1 0\n\n", True),
    ("0 0.5\n0.5 0\n", False),
    ("", False),
    ("0\n", False),
    ("0 1\r\n1 0\r\n", False),
    ("0 -1\n-1 0\n", True),
    ("0 1\n0 0\n", True),
]

# ---- CSV: (text, directed, weighted, jgrapht flags) -------------------------
CSV_EDGES = [
    ("a,b\nb,c\nc,a\n", False, False),
    ("a,b\nb,c\nc,a\n", True, False),
    ("a,b,2.5\nb,c,1\n", False, True),
    ("a,b,2.5\nb,c,1\nc,a,3\n", True, True),
    ("a,b\na,b\nb,a\na,a\n", False, False),
    ("a,b\r\nb,c\r\n", False, False),
    ("x,y\ny,z\nz,x\nx,w\n", True, False),
]
CSV_ADJLIST = [
    ("a,b,c\nb,c\nc\nd\n", False),
    ("a,b,c\nb,c\nc\nd\n", True),
    ("a,b\nb,a\n", False),
    ("a,b\na,b\n", True),
    ("a,b,c\r\nb,c\r\n", True),
]
# (text, directed, weighted, labelled): the matrix forms JGraphT reads, as
# directed graphs (it reads a symmetric matrix as each edge twice).
CSV_MATRIX = [
    ("0,1,0\n0,0,1\n0,0,0\n", True, False, False),
    ("0,1,0\n1,0,1\n0,1,0\n", True, False, False),
    (",a,b,c\na,0,1,0\nb,0,0,1\nc,0,0,0\n", True, False, True),
    ("0,2.5,0\n0,0,1\n0,0,0\n", True, True, False),
    (",a,b,c\na,0,2.5,0\nb,0,0,1\nc,0,0,0\n", True, True, True),
    ("1,2.5,0\n0,0,-1\n3,0,0\n", True, True, False),
]

# ---- TSPLIB: coordinate forms (the ones JGraphT reads), (text, directed) ----
_TSP = "NAME: t\nTYPE: TSP\nCOMMENT: x\nDIMENSION: 4\n"
TSPLIB = [
    _TSP + "EDGE_WEIGHT_TYPE: EUC_2D\nNODE_COORD_SECTION\n1 0 0\n2 3 4\n3 6 8\n4 0 10\nEOF\n",
    _TSP + "EDGE_WEIGHT_TYPE: CEIL_2D\nNODE_COORD_SECTION\n1 0 0\n2 3 4.2\n3 6 8\n4 0 10\nEOF\n",
    _TSP + "EDGE_WEIGHT_TYPE: MAX_2D\nNODE_COORD_SECTION\n1 0 0\n2 3 4\n3 6 8\n4 0 10\nEOF\n",
    _TSP + "EDGE_WEIGHT_TYPE: MAN_2D\nNODE_COORD_SECTION\n1 0 0\n2 3 4\n3 6 8\n4 0 10\nEOF\n",
    _TSP + "EDGE_WEIGHT_TYPE: EUC_3D\nNODE_COORD_SECTION\n1 0 0 0\n2 3 4 0\n3 6 8 1\n4 0 10 2\nEOF\n",
    _TSP + "EDGE_WEIGHT_TYPE: ATT\nNODE_COORD_SECTION\n1 0 0\n2 30 40\n3 60 80\n4 0 100\nEOF\n",
    _TSP + "EDGE_WEIGHT_TYPE: GEO\nNODE_COORD_SECTION\n1 38.24 20.42\n2 39.57 26.15\n3 40.56 25.32\n4 36.26 23.12\nEOF\n",
    "NAME:t\nTYPE:TSP\nDIMENSION:3\nEDGE_WEIGHT_TYPE:EUC_2D\nNODE_COORD_SECTION\n1 0 0\n2 3 4\n3 6 8\nEOF\n",
    _TSP + "EDGE_WEIGHT_TYPE: EUC_2D\nNODE_COORD_SECTION\n1 0.5 0.5\n2 1.5e1 2.5e0\n3 -3 4\n4 7 -8.25\nEOF\n",
]
# Explicit matrices: no tool reads them as graphs, so the definition checks them
# (every format of the specification, one set of six weights).
TSPLIB_EXPLICIT = [
    _TSP + "EDGE_WEIGHT_TYPE: EXPLICIT\nEDGE_WEIGHT_FORMAT: " + shape + "\nEDGE_WEIGHT_SECTION\n" + data + "\nEOF\n"
    for shape, data in [
        ("FULL_MATRIX", "0 1 2 3\n1 0 4 5\n2 4 0 6\n3 5 6 0"),
        ("UPPER_ROW", "1 2 3 4 5 6"),
        ("LOWER_ROW", "1 2 4 3 5 6"),
        ("UPPER_DIAG_ROW", "0 1 2 3 0 4 5 0 6 0"),
        ("LOWER_DIAG_ROW", "0 1 0 2 4 0 3 5 6 0"),
        ("UPPER_COL", "1 2 4 3 5 6"),
        ("LOWER_COL", "1 2 3 4 5 6"),
        ("UPPER_DIAG_COL", "0 1 0 2 4 0 3 5 6 0"),
        ("LOWER_DIAG_COL", "0 1 2 3 0 4 5 0 6 0"),
    ]
] + [
    "NAME: a\nTYPE: ATSP\nDIMENSION: 3\nEDGE_WEIGHT_TYPE: EXPLICIT\nEDGE_WEIGHT_FORMAT: FULL_MATRIX\n"
    "EDGE_WEIGHT_SECTION\n0 1 2\n3 0 4\n5 6 0\nEOF\n"
]

# ---- partitions and covers --------------------------------------------------
# Partition files, line i the community of node i (NetworKit's PartitionReader).
PARTITION = ["0\n0\n1\n", "5\n5\n2\n7\n", "3\n", "", "0\n1", "0\r\n1\r\n", "1 \n2\n"]
# Partition edge lists: (text, first node id, separator).
PARTITION_EDGELIST = [
    ("1\t0\n2\t0\n3\t1\n", 1, "\t"),
    ("1 0\n2 0\n3 1\n", 1, " "),
    ("0 0\n1 0\n2 1\n", 0, " "),
    ("1\t5\n3\t5\n2\t9\n", 1, "\t"),
    ("1\t0\r\n2\t1\r\n", 1, "\t"),
    ("", 1, "\t"),
]
# Cover files, one community per line (nodes numbered from 0).
COVER = ["0 1\n1 2\n", "0 1 2\n", "0\n1\n2\n", "3 4\n0 4\n", "1 2\n2 3\n3 1\n", ""]
# Cover edge lists: `node c1 c2 ...`, nodes numbered from `first`.
COVER_EDGELIST = [
    ("1 5 6\n2 5\n3 7\n", 1),
    ("1 0\n", 1),
    ("0 1 2\n1 2\n2 0\n", 0),
    ("", 1),
]


def pack_partition(communities):
    """One partition: (n, assigned, 0) then (node, community, 0) per node with
    a community (`communities` lists them in node order, None for none)."""
    rows = [(i, c, 0) for i, c in enumerate(communities) if c is not None]
    return [(len(communities), len(rows), 0)] + rows


def pack_cover(memberships):
    """One cover: (0, memberships, 0) then the sorted (node, community, 0)
    pairs; `memberships` is a list of (node, community)."""
    rows = sorted((int(n), int(c), 0) for n, c in memberships)
    return [(0, len(rows), 0)] + rows


# ---- malformed input of the formats above: (format, text, words) ------------
INVALID = [
    ("metis", "", "no header"),
    ("metis", "2 1\n2\n", "ends after 1"),
    ("metis", "2 1\n3\n1\n", "outside"),
    ("metis", "2 2\n2\n1\n", "declares 2 edges"),
    ("metis", "2 1 1\n2\n1\n", "without its edge weight"),
    ("snap", "a b\n", "not a non-negative integer"),
    ("snap", "1 2 3\n", "two node numbers"),
    ("konect", "1 2\n", "first line"),
    ("konect", "% bip unweighted\n1 2\n", "bipartite"),
    ("konect", "% sym unweighted\n0 1\n", "positive integer"),
    ("gt", b"not a gt file", "bad magic"),
    ("gt", b"\xe2\x9b\xbe gt\x01\x00", "truncated"),
    ("ncol", "a\n", "one field"),
    ("ncol", "a b x\n", "not a number"),
    ("lgl", "a\n", "before the first"),
    ("lgl", "# a b\n", "exactly one"),
    ("adjacency", "0 1\n0 0\n", "not symmetric"),
    ("adjacency", "0 1\n", "square"),
    ("csv", "a\n", "fields"),
    ("csv", "a,\"b\n", "not closed"),
    ("csv-adjlist", "a,,b\n", "empty"),
    ("csv-matrix", ",a,a\na,0,0\na,0,0\n", "repeated"),
    ("tsplib", "TYPE: TSP\n", "no DIMENSION"),
    ("tsplib", "TYPE: HCP\nDIMENSION: 2\nEDGE_WEIGHT_TYPE: EUC_2D\n", "not read"),
    ("partition", "1 2\n", "one community"),
    ("partition-edgelist", "a 1\na 2\n", "twice"),
    ("cover", "a a\n", "twice"),
    ("cover-edgelist", "a x\n", "not a non-negative"),
]
