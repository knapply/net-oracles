#!/usr/bin/env python3
"""Golden values from the format definitions for manifest/io_formats.yaml:
a plain parser of each format written from its description (edge list;
DIMACS challenge formats; McKay's graph6; LEDA; Matrix Market), sharing no
code with the engine. Cases and the packed encoding are in
derived/io_formats.py.

    python3 oracles/io_formats_definition_oracle.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import DEFINITION_VERSION  # noqa: E402
from derived import io_formats as D  # noqa: E402
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
    elif fn == "io_invalid":
        return [1 for _ in D.INVALID]
    else:
        return None
    return out


if __name__ == "__main__":
    run("definition", compute, DEFINITION_VERSION)
