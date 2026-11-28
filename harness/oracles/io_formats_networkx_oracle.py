#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for
manifest/io_formats.yaml: `parse_edgelist` (as a multigraph, so repeated edges
and loops stay), `from_graph6_bytes` and `parse_leda`, run as black boxes on the
case texts of derived/io_formats.py. Node positions are the order of
`G.nodes`; a LEDA edge label is read as the value when the edge type is numeric.

    python3 oracles/io_formats_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from derived import io_formats as D  # noqa: E402
from io_formats_common import run  # noqa: E402


def from_graph(g, directed, value=None):
    position = {v: i for i, v in enumerate(g.nodes)}
    edges = [(position[a], position[b], value(d) if value else None)
             for a, b, d in g.edges(data=True)]
    return D.pack(directed, len(position), edges)


def edgelist(text, directed, delimiter):
    lines = text.splitlines()
    rows = [l.split("#")[0].replace(",", " ").split() for l in lines]
    rows = [r for r in rows if r]
    weighted = bool(rows) and all(len(r) == 3 for r in rows)
    g = nx.parse_edgelist(lines, comments="#", delimiter=delimiter,
                          create_using=nx.MultiDiGraph if directed else nx.MultiGraph,
                          nodetype=str, data=(("weight", float),) if weighted else False)
    return from_graph(g, bool(directed), (lambda d: d["weight"]) if weighted else None)


def leda(text):
    lines = [l.strip() for l in text.splitlines()]
    edge_type = [l for l in lines if l and not l.startswith("#")][2]
    numeric = edge_type in ("int", "short", "long", "float", "double", "real")
    g = nx.parse_leda(lines)
    return from_graph(g, g.is_directed(),
                      (lambda d: float(d["label"]) if d.get("label") else None) if numeric else None)


def compute(engine):
    fn, subset = engine["fn"], engine.get("cases")
    out = []
    if fn == "io_edgelist" and subset == "int":
        for text, directed in D.EDGELIST_INT:
            out += edgelist(text, directed, None)
    elif fn == "io_edgelist":
        for text, directed, delimiter in D.EDGELIST:
            out += edgelist(text, directed, delimiter)
    elif fn == "io_graph6":
        for text in D.GRAPH6 + [D.GRAPH6_HEADER]:
            out += from_graph(nx.from_graph6_bytes(text.encode()), False)
    elif fn == "io_leda":
        for text in (D.LEDA_IGRAPH if subset == "igraph" else D.LEDA):
            out += leda(text)
    else:
        return None
    return out


if __name__ == "__main__":
    run("networkx", compute, f"networkx {nx.__version__}")
