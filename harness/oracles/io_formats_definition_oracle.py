#!/usr/bin/env python3
"""Golden values from the format definitions for manifest/io_formats.yaml:
a plain parser of each format written from its description (edge list;
DIMACS challenge formats; McKay's graph6; LEDA; Matrix Market; METIS; SNAP;
KONECT; graph-tool binary; NCOL; LGL; adjacency matrices; CSV; TSPLIB;
partition and cover files), sharing no code with the engine. Cases and the packed encoding are in
derived/io_formats.py.

    python3 oracles/io_formats_definition_oracle.py
"""

from __future__ import annotations

import math
import re
import struct
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import DEFINITION_VERSION  # noqa: E402
from derived import io_formats as D  # noqa: E402
import io_formats_cases as C  # noqa: E402
from io_formats_common import run  # noqa: E402


def edgelist(text, directed, _delimiter=None):
    positions, edges = {}, []

    def node(name):
        return positions.setdefault(name, len(positions))
    for line in text.splitlines():
        line = line.split("#")[0]
        if line.strip().startswith("%"):
            continue
        fields = [f for f in re.split(r"[\s,]+", line) if f]
        if len(fields) == 1:
            node(fields[0])
        elif len(fields) >= 2:
            a, b = node(fields[0]), node(fields[1])
            edges.append((a, b, float(fields[2]) if len(fields) > 2 else None))
    return D.pack(bool(directed), len(positions), edges)


def dimacs(text):
    kind, n, edges = None, 0, []
    for line in text.splitlines():
        f = line.split()
        if not f or f[0] == "c" or f[0] == "n":
            continue
        if f[0] == "p":
            kind, n = f[1], int(f[2])
        elif f[0] == "e":
            edges.append((int(f[1]) - 1, int(f[2]) - 1, None))
        elif f[0] == "a":
            value = {"sp": f[3] if len(f) > 3 else None,
                     "max": f[3] if len(f) > 3 else None,
                     "min": f[5] if len(f) > 5 else None}[kind]
            edges.append((int(f[1]) - 1, int(f[2]) - 1, float(value)))
    return D.pack(kind in ("sp", "max", "min"), n, edges)


def graph6(text):
    data = text.strip()
    if data.startswith(">>graph6<<"):
        data = data[len(">>graph6<<"):]
    chars = [ord(c) - 63 for c in data]
    if chars[0] < 63:
        n, rest = chars[0], chars[1:]
    elif chars[1] < 63:
        n, rest = (chars[1] << 12) | (chars[2] << 6) | chars[3], chars[4:]
    else:
        n = 0
        for c in chars[2:8]:
            n = (n << 6) | c
        rest = chars[8:]
    bits = "".join(format(c, "06b") for c in rest)
    edges, k = [], 0
    for j in range(1, n):
        for i in range(j):
            if bits[k] == "1":
                edges.append((i, j, None))
            k += 1
    return D.pack(False, n, edges)


def leda(text):
    lines = [l.strip() for l in text.splitlines()]
    lines = [l for l in lines if l and not l.startswith("#")]
    edge_type, direction = lines[2], lines[3]
    n = int(lines[4])
    m = int(lines[5 + n])
    numeric = edge_type in ("int", "short", "long", "float", "double", "real")
    edges = []
    for l in lines[6 + n:6 + n + m]:
        a, b, _rev, label = l.split(None, 3)
        value = float(label[2:-2]) if numeric and label[2:-2] else None
        edges.append((int(a) - 1, int(b) - 1, value))
    return D.pack(direction == "-1", n, edges)


def mtx(text):
    lines = [l for l in text.splitlines() if l.strip()]
    banner = lines[0].lower().split()
    fmt, field, symmetry = banner[2], banner[3], banner[4]
    body = [l for l in lines[1:] if not l.startswith("%")]
    size = [int(x) for x in body[0].split()]
    n, rest = size[0], body[1:]
    directed = symmetry != "symmetric"
    edges = []

    def add(i, j, v):
        value = None if field == "pattern" else v
        if symmetry == "skew-symmetric":
            edges.append((i, j, value))
            edges.append((j, i, None if value is None else -value))
        else:
            edges.append((i, j, value))
    if fmt == "coordinate":
        for l in rest[:size[2]]:
            f = l.split()
            add(int(f[0]) - 1, int(f[1]) - 1, float(f[2]) if len(f) > 2 else None)
    else:
        values = [float(l) for l in rest]
        k = 0
        for j in range(n):
            first = {"general": 0, "symmetric": j, "skew-symmetric": j + 1}[symmetry]
            for i in range(first, n):
                if values[k] != 0:
                    add(i, j, values[k])
                k += 1
    return D.pack(directed, n, edges)


def metis(text):
    lines = [l for l in text.splitlines() if not l.lstrip().startswith("%")]
    while not lines[0].strip():
        lines.pop(0)
    head = lines[0].split()
    n, m = int(head[0]), int(head[1])
    code = (head[2] if len(head) > 2 else "0").zfill(3)
    sizes, weights, edge_weights = code[0] == "1", code[1] == "1", code[2] == "1"
    ncon = int(head[3]) if len(head) > 3 else (1 if weights else 0)
    edges = []
    for i, line in enumerate(lines[1:1 + n], start=1):
        fields = line.split()[int(sizes) + ncon:]
        step = 2 if edge_weights else 1
        for k in range(0, len(fields), step):
            j = int(fields[k])
            if j >= i:
                edges.append((i - 1, j - 1, float(fields[k + 1]) if edge_weights else None))
    assert len(edges) == m
    return D.pack(False, n, edges)


def snap(text):
    seen, edges, nodes = set(), [], set()
    for line in text.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        a, b = (int(x) for x in line.split())
        nodes |= {a, b}
        key = (min(a, b), max(a, b))
        if key not in seen:
            seen.add(key)
            edges.append((a, b, None))
    return D.pack(False, len(nodes), edges)


def konect(text):
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    directed = lines[0].split()[1] == "asym"
    edges, largest = [], 0
    for l in lines:
        if l.startswith("%"):
            continue
        f = l.split()
        a, b = int(f[0]), int(f[1])
        largest = max(largest, a, b)
        edges.append((a - 1, b - 1, float(f[2]) if len(f) > 2 else None))
    return D.pack(directed, largest, edges)


def gt(case):
    directed, n, edge_list = case
    data = C.gt_bytes(*case)
    assert data[:6] == b"\xe2\x9b\xbe gt" and data[6] == 1 and data[7] == 0
    at = 8
    (comment,) = struct.unpack_from("<Q", data, at)
    at += 8 + comment
    flag = data[at]
    (count,) = struct.unpack_from("<Q", data, at + 1)
    at += 9
    width = next(w for w in (1, 2, 4, 8) if count < 256 ** w)
    edges = []
    for v in range(count):
        (k,) = struct.unpack_from("<Q", data, at)
        at += 8
        for _ in range(k):
            edges.append((v, int.from_bytes(data[at:at + width], "little"), None))
            at += width
    return D.pack(bool(flag), count, edges)


def named(text, directed, weighted_rows):
    """NCOL and LGL: the edges as (source, target, weight) name triples."""
    position = {}

    def node(name):
        return position.setdefault(name, len(position))
    edges = []
    for a, b, w in weighted_rows:
        edges.append((node(a), node(b), w))
    return D.pack(bool(directed), len(position), edges), node


def ncol(text, directed):
    rows = [l.split() for l in text.splitlines() if l.strip()]
    return named(text, directed, [(r[0], r[1], float(r[2]) if len(r) > 2 else None) for r in rows])[0]


def lgl(text, directed):
    position, edges, current = {}, [], None

    def node(name):
        return position.setdefault(name, len(position))
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            current = node(line[1:].strip())
            continue
        f = line.split()
        edges.append((current, node(f[0]), float(f[1]) if len(f) > 1 else None))
    return D.pack(bool(directed), len(position), edges)


def adjacency(text, directed, comma=False):
    rows = [l for l in text.splitlines() if l.strip() and (comma or not l.lstrip().startswith("#"))]
    matrix = [[float(x) for x in (r.split(",") if comma else r.split())] for r in rows]
    n = len(matrix)
    edges = [(i, j, matrix[i][j]) for i in range(n) for j in range(n)
             if matrix[i][j] != 0 and (directed or j >= i)]
    return D.pack(directed, n, edges)


def csv_edges(text, directed):
    position, edges = {}, []

    def node(name):
        return position.setdefault(name, len(position))
    for line in text.splitlines():
        f = line.split(",")
        edges.append((node(f[0]), node(f[1]), float(f[2]) if len(f) > 2 else None))
    return D.pack(bool(directed), len(position), edges)


def csv_adjlist(text, directed):
    position, edges = {}, []

    def node(name):
        return position.setdefault(name, len(position))
    for line in text.splitlines():
        f = line.split(",")
        source = node(f[0])
        edges += [(source, node(t), None) for t in f[1:]]
    return D.pack(bool(directed), len(position), edges)


def csv_matrix(text, directed, labelled):
    rows = [l.split(",") for l in text.splitlines() if l.strip()]
    if labelled:
        rows = [r[1:] for r in rows[1:]]
    n = len(rows)
    edges = [(i, j, float(rows[i][j])) for i in range(n) for j in range(n)
             if float(rows[i][j]) != 0 and (directed or j >= i)]
    return D.pack(directed, n, edges)


def nint(x):
    return int(x + 0.5)


def tsp_distance(kind, a, b):
    d = [abs(x - y) for x, y in zip(a, b)]
    if kind.startswith("EUC"):
        return nint(math.sqrt(sum(x * x for x in d)))
    if kind.startswith("CEIL"):
        return math.ceil(math.sqrt(sum(x * x for x in d)))
    if kind.startswith("MAX"):
        return max(nint(x) for x in d)
    if kind.startswith("MAN"):
        return sum(nint(x) for x in d)
    if kind == "ATT":
        r = math.sqrt(sum(x * x for x in d) / 10.0)
        t = nint(r)
        return t + 1 if t < r else t
    assert kind == "GEO"

    def radians(x):
        deg = nint(x)
        return 3.141592 * (deg + 5.0 * (x - deg) / 3.0) / 180.0
    (la, lo), (lb, lq) = [(radians(p[0]), radians(p[1])) for p in (a, b)]
    q1, q2, q3 = math.cos(lo - lq), math.cos(la - lb), math.cos(la + lb)
    return int(6378.388 * math.acos(0.5 * ((1 + q1) * q2 - (1 - q1) * q3)) + 1.0)


def explicit_pairs(shape, n):
    """The (row, column) of each entry of an explicit matrix, from the
    specification's description of each EDGE_WEIGHT_FORMAT."""
    full = [(i, j) for i in range(n) for j in range(n)]
    by_row = {"UPPER_ROW": lambda i, j: j > i, "LOWER_ROW": lambda i, j: j < i,
              "UPPER_DIAG_ROW": lambda i, j: j >= i, "LOWER_DIAG_ROW": lambda i, j: j <= i}
    by_col = {"UPPER_COL": by_row["UPPER_ROW"], "LOWER_COL": by_row["LOWER_ROW"],
              "UPPER_DIAG_COL": by_row["UPPER_DIAG_ROW"], "LOWER_DIAG_COL": by_row["LOWER_DIAG_ROW"]}
    if shape == "FULL_MATRIX":
        return full
    if shape in by_row:
        return [(i, j) for i, j in full if by_row[shape](i, j)]
    keep = by_col[shape]
    return [(i, j) for j, i in sorted((j, i) for i, j in full if keep(i, j))]


def tsplib(text):
    header, section, rows = {}, None, {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line == "EOF":
            continue
        if line.endswith("_SECTION"):
            section = line
            rows[section] = []
        elif ":" in line and section is None:
            key, value = line.split(":", 1)
            header[key.strip()] = value.strip()
        else:
            rows[section] += line.split()
    n = int(header["DIMENSION"])
    kind = header["EDGE_WEIGHT_TYPE"]
    directed = header["TYPE"] == "ATSP"
    if kind == "EXPLICIT":
        values = [float(x) for x in rows["EDGE_WEIGHT_SECTION"]]
        edges, seen = [], {}
        for (i, j), w in zip(explicit_pairs(header["EDGE_WEIGHT_FORMAT"], n), values):
            if i == j:
                continue
            if directed:
                edges.append((i, j, w))
            elif (min(i, j), max(i, j)) not in seen:
                seen[(min(i, j), max(i, j))] = w
                edges.append((min(i, j), max(i, j), w))
        return D.pack(directed, n, edges)
    flat = rows["NODE_COORD_SECTION"]
    width = 4 if kind.endswith("3D") else 3
    points = [[float(x) for x in flat[k + 1:k + width]] for k in range(0, len(flat), width)]
    edges = [(i, j, float(tsp_distance(kind, points[i], points[j])))
             for i in range(n) for j in range(i + 1, n)]
    return D.pack(False, n, edges)


def partition(text):
    return C.pack_partition([int(l) if l.strip() else None for l in text.splitlines()])


def partition_edgelist(text, first):
    rows = [re.split(r"[\s,]+", l.strip()) for l in text.splitlines() if l.strip()]
    values = [None] * len(rows)
    for node, community in rows:
        values[int(node) - first] = int(community)
    return C.pack_partition(values)


def cover(text):
    return C.pack_cover([(node, c) for c, line in enumerate(text.splitlines()) for node in line.split()])


def membership(text, first):
    pairs = []
    for line in text.splitlines():
        f = line.split()
        if f:
            pairs += [(int(f[0]) - first, c) for c in sorted({int(x) for x in f[1:]})]
    return C.pack_cover(pairs)


def compute(engine):
    fn, subset = engine["fn"], engine.get("cases")
    out = []
    if fn == "io_edgelist" and subset == "int":
        for text, directed in D.EDGELIST_INT:
            out += edgelist(text, directed)
    elif fn == "io_edgelist":
        for text, directed, delimiter in D.EDGELIST:
            out += edgelist(text, directed, delimiter)
    elif fn == "io_dimacs":
        for text in (D.DIMACS_FLOW if subset == "flow" else D.DIMACS):
            out += dimacs(text)
    elif fn == "io_graph6":
        for text in D.GRAPH6 + [D.GRAPH6_HEADER]:
            out += graph6(text)
    elif fn == "io_leda":
        for text in (D.LEDA_IGRAPH if subset == "igraph" else D.LEDA):
            out += leda(text)
    elif fn == "io_mtx":
        for text in (D.MTX_COORDINATE if subset == "coordinate" else D.MTX):
            out += mtx(text)
    elif fn == "io_metis":
        for text in C.METIS:
            out += metis(text)
    elif fn == "io_snap":
        for text in C.SNAP:
            out += snap(text)
    elif fn == "io_konect":
        for text in C.KONECT:
            out += konect(text)
    elif fn == "io_graphtoolbinary":
        for case in C.GT:
            out += gt(case)
    elif fn == "io_ncol":
        for text, directed in C.NCOL:
            out += ncol(text, directed)
    elif fn == "io_lgl":
        for text, directed in C.LGL:
            out += lgl(text, directed)
    elif fn == "io_adjacency":
        for text, directed in C.ADJACENCY:
            out += adjacency(text, directed)
    elif fn == "io_csv" and subset == "adjlist":
        for text, directed in C.CSV_ADJLIST:
            out += csv_adjlist(text, directed)
    elif fn == "io_csv" and subset == "matrix":
        for text, directed, _weighted, labelled in C.CSV_MATRIX:
            out += csv_matrix(text, directed, labelled)
    elif fn == "io_csv":
        for text, directed, _weighted in C.CSV_EDGES:
            out += csv_edges(text, directed)
    elif fn == "io_tsplib":
        for text in (C.TSPLIB_EXPLICIT if subset == "explicit" else C.TSPLIB):
            out += tsplib(text)
    elif fn == "io_partition_formats" and subset == "edgelist":
        for text, first, _ in C.PARTITION_EDGELIST:
            out += partition_edgelist(text, first)
    elif fn == "io_partition_formats" and subset == "cover":
        for text in C.COVER:
            out += cover(text)
    elif fn == "io_partition_formats" and subset == "membership":
        for text, first in C.COVER_EDGELIST:
            out += membership(text, first)
    elif fn == "io_partition_formats":
        for text in C.PARTITION:
            out += partition(text)
    elif fn == "io_invalid":
        return [1 for _ in D.INVALID + C.INVALID]
    else:
        return None
    return out


if __name__ == "__main__":
    run("definition", compute, DEFINITION_VERSION)
