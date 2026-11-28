#!/usr/bin/env python3
# oracle-env: pyigraph
"""Golden values from python-igraph (GPL, run as a black box) for
manifest/io_formats.yaml. igraph reads only the DIMACS maximum-flow form
(`Graph.Read_DIMACS`), and writes LEDA without reading it (`Graph.write_leda`);
it reads NCOL, LGL and adjacency matrices (`Read_Ncol`, `Read_Lgl`,
`Read_Adjacency`, the cases of io_formats_cases.py):

  io_dimacs_flow   the graph read by Read_DIMACS (directed), capacity as value
  io_leda_igraph   the graph that wrote each text of derived LEDA_IGRAPH; the
                   texts are rebuilt here and must equal the committed ones

    python3 oracles/io_formats_pyigraph_oracle.py
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

import igraph

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from derived import io_formats as D  # noqa: E402
import io_formats_cases as C  # noqa: E402
from io_formats_common import run  # noqa: E402


def packed(g, value=None):
    edges = [(e.source, e.target, e[value] if value else None) for e in g.es]
    return D.pack(g.is_directed(), g.vcount(), edges)


def dimacs_flow(text):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "a.max"
        path.write_text(text)
        return packed(igraph.Graph.Read_DIMACS(str(path), directed=True), "capacity")


def leda_graphs():
    a = igraph.Graph(3, [(0, 1), (1, 2), (2, 0)], directed=True)
    a.vs["name"] = ["a", "b", "c"]
    a.es["weight"] = [2.5, -1, 0.125]
    return [(a, {"names": "name", "weights": "weight"}, "weight"),
            (igraph.Graph(4, [(0, 1), (1, 2), (1, 3), (0, 3)]), {}, None),
            (igraph.Graph(0), {}, None),
            (igraph.Graph(3, [(0, 2), (2, 1)], directed=True), {}, None)]


def leda_igraph():
    out = []
    with tempfile.TemporaryDirectory() as tmp:
        for (g, kw, value), text in zip(leda_graphs(), D.LEDA_IGRAPH, strict=True):
            path = Path(tmp) / "a.gw"
            g.write_leda(str(path), **kw)
            if path.read_text() != text:
                raise SystemExit("igraph's LEDA text differs from derived LEDA_IGRAPH; update the constant")
            out += packed(g, value)
    return out


def read_file(text, suffix, reader):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / f"case{suffix}"
        path.write_bytes(text.encode("latin-1"))
        g = reader(str(path))
        return packed(g, "weight" if "weight" in g.es.attributes() else None)


def compute(engine):
    fn, subset = engine["fn"], engine.get("cases")
    if fn == "io_dimacs" and subset == "flow":
        return [row for text in D.DIMACS_FLOW for row in dimacs_flow(text)]
    if fn == "io_leda" and subset == "igraph":
        return leda_igraph()
    out = []
    if fn == "io_ncol":
        for text, directed in C.NCOL:
            out += read_file(text, ".ncol", lambda p: igraph.Graph.Read_Ncol(p, directed=directed))
    elif fn == "io_lgl":
        for text, directed in C.LGL:
            out += read_file(text, ".lgl", lambda p: igraph.Graph.Read_Lgl(p, directed=directed))
    elif fn == "io_adjacency":
        for text, directed in C.ADJACENCY:
            mode = "directed" if directed else "undirected"
            out += read_file(text, ".adj", lambda p: igraph.Graph.Read_Adjacency(p, mode=mode, attribute="weight"))
    else:
        return None
    return out


if __name__ == "__main__":
    run("pyigraph", compute, f"python-igraph {igraph.__version__}")
