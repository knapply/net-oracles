#!/usr/bin/env python3
# oracle-env: networkit
"""Golden values from NetworKit (Staudt, Sazonovs and Meyerhenke 2016) for
manifest/io_formats.yaml: `EdgeListReader` (nodes numbered from 0, `#`
comments) and the Matrix Market reader (`readGraph` with `Format.MatrixMarket`),
run as black boxes on the case texts of derived/io_formats.py.

    ~/oracle-envs/networkit/bin/python oracles/io_formats_networkit_oracle.py
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

try:
    import networkit as nk
except ImportError:  # the tool is not installed here
    print("networkit is not installed")
    sys.exit(3)

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from derived import io_formats as D  # noqa: E402
from io_formats_common import run  # noqa: E402


def from_graph(g):
    weighted = g.isWeighted()
    edges = [(int(a), int(b), float(w) if weighted else None) for a, b, w in g.iterEdgesWeights()]
    return D.pack(g.isDirected(), g.numberOfNodes(), edges)


def read(text, suffix, reader):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / f"case{suffix}"
        path.write_bytes(text.encode("latin-1"))
        return from_graph(reader(str(path)))


def compute(engine):
    fn, subset = engine["fn"], engine.get("cases")
    out = []
    if fn == "io_edgelist" and subset == "int":
        for text, directed in D.EDGELIST_INT:
            out += read(text, ".el", nk.graphio.EdgeListReader(" ", 0, "#", True, directed).read)
    elif fn == "io_mtx" and subset == "coordinate":
        for text in D.MTX_COORDINATE:
            out += read(text, ".mtx", lambda p: nk.readGraph(p, nk.Format.MatrixMarket))
    else:
        return None
    return out


if __name__ == "__main__":
    run("networkit", compute, f"networkit {nk.__version__}")
