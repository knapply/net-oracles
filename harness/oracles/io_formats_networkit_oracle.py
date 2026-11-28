#!/usr/bin/env python3
# oracle-env: networkit
"""Golden values from NetworKit (Staudt, Sazonovs and Meyerhenke 2016) for
manifest/io_formats.yaml: `EdgeListReader` (nodes numbered from 0, `#`
comments), the Matrix Market, METIS, SNAP, KONECT and graph-tool binary readers
(`readGraph`) and the partition and cover readers of `graphio`, run as black
boxes on the case texts of derived/io_formats.py and io_formats_cases.py.

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
import io_formats_cases as C  # noqa: E402
from io_formats_common import run  # noqa: E402


def from_graph(g):
    weighted = g.isWeighted()
    edges = [(int(a), int(b), float(w) if weighted else None) for a, b, w in g.iterEdgesWeights()]
    return D.pack(g.isDirected(), g.numberOfNodes(), edges)


def write_case(tmp, text, suffix):
    path = Path(tmp) / f"case{suffix}"
    path.write_bytes(text if isinstance(text, bytes) else text.encode("latin-1"))
    return str(path)


def read(text, suffix, reader):
    with tempfile.TemporaryDirectory() as tmp:
        return from_graph(reader(write_case(tmp, text, suffix)))


def numbers(text):
    """The integers a case text mentions, in order."""
    return [int(word) for word in text.replace(",", " ").split() if word.lstrip("-").isdigit()]


def partition_rows(vector):
    none = 2 ** 64 - 1
    return C.pack_partition([None if c == none else int(c) for c in vector])


def cover_rows(cover, nodes):
    return C.pack_cover([(v, c) for v in range(nodes) for c in cover.subsetsOf(v)])


def partitions(subset):
    """NetworKit's readers of partition and cover files, one result per case."""
    out = []
    with tempfile.TemporaryDirectory() as tmp:
        if subset is None:
            for text in C.PARTITION:
                path = write_case(tmp, text, ".part")
                out += partition_rows(nk.graphio.PartitionReader().read(path).getVector())
        elif subset == "edgelist":
            for text, first, sep in C.PARTITION_EDGELIST:
                path = write_case(tmp, text, ".el")
                out += partition_rows(nk.graphio.EdgeListPartitionReader(first, sep).read(path).getVector())
        elif subset == "cover":
            for text in C.COVER:
                path = write_case(tmp, text, ".cov")
                nodes = max(numbers(text), default=-1) + 1
                cover = nk.graphio.CoverReader().read(path, nk.Graph(nodes))
                out += cover_rows(cover, nodes)
        else:
            for text, first in C.COVER_EDGELIST:
                path = write_case(tmp, text, ".elc")
                nodes = max((n - first + 1 for n in [int(l.split()[0]) for l in text.splitlines() if l.split()]), default=0)
                cover = nk.graphio.EdgeListCoverReader(first).read(path, nk.Graph(nodes))
                out += cover_rows(cover, nodes)
    return out


def compute(engine):
    fn, subset = engine["fn"], engine.get("cases")
    out = []
    if fn == "io_edgelist" and subset == "int":
        for text, directed in D.EDGELIST_INT:
            out += read(text, ".el", nk.graphio.EdgeListReader(" ", 0, "#", True, directed).read)
    elif fn == "io_mtx" and subset == "coordinate":
        for text in D.MTX_COORDINATE:
            out += read(text, ".mtx", lambda p: nk.readGraph(p, nk.Format.MatrixMarket))
    elif fn == "io_metis":
        for text in C.METIS:
            out += read(text, ".graph", lambda p: nk.readGraph(p, nk.Format.METIS))
    elif fn == "io_snap":
        for text in C.SNAP:
            out += read(text, ".txt", lambda p: nk.graphio.SNAPGraphReader(False, False, 0).read(p))
    elif fn == "io_konect":
        for text in C.KONECT:
            out += read(text, ".konect", lambda p: nk.readGraph(p, nk.Format.KONECT))
    elif fn == "io_graphtoolbinary":
        for case in C.GT:
            out += read(C.gt_bytes(*case), ".gt", lambda p: nk.readGraph(p, nk.Format.GraphToolBinary))
    elif fn == "io_partition_formats":
        return partitions(subset)
    else:
        return None
    return out


if __name__ == "__main__":
    run("networkit", compute, f"networkit {nk.__version__}")
