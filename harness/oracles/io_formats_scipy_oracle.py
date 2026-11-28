#!/usr/bin/env python3
"""Golden values from SciPy (Virtanen et al. 2020) for the Matrix Market entries
of manifest/io_formats.yaml: `scipy.io.mmread`, run as a black box on the case
texts of derived/io_formats.py. The matrix is the adjacency matrix: a `general`
or `skew-symmetric` matrix gives an arc per stored value (SciPy expands the skew
part), a `symmetric` one an edge per entry of the lower triangle; a `pattern`
matrix has no values.

    python3 oracles/io_formats_scipy_oracle.py
"""

from __future__ import annotations

import io
import sys
from pathlib import Path

import numpy as np
import scipy
import scipy.io
import scipy.sparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from derived import io_formats as D  # noqa: E402
from io_formats_common import run  # noqa: E402


def read(text):
    data = text.encode("latin-1")
    rows, cols, entries, fmt, field, symmetry = scipy.io.mminfo(io.BytesIO(data))
    m = scipy.io.mmread(io.BytesIO(data))
    if scipy.sparse.issparse(m):
        m = m.tocoo()
        triples = list(zip(m.row.tolist(), m.col.tolist(), m.data.tolist()))
    else:
        triples = [(i, j, float(m[i, j])) for i in range(rows) for j in range(cols) if m[i, j] != 0]
    if symmetry == "symmetric":
        triples = [t for t in triples if t[0] >= t[1]]
    edges = [(i, j, None if field == "pattern" else float(v)) for i, j, v in triples]
    return D.pack(symmetry != "symmetric", rows, edges)


def compute(engine):
    if engine["fn"] != "io_mtx":
        return None
    cases = D.MTX_COORDINATE if engine.get("cases") == "coordinate" else D.MTX
    out = []
    for text in cases:
        out += read(text)
    return out


if __name__ == "__main__":
    run("scipy", compute, f"scipy {scipy.__version__}, numpy {np.__version__}")  # the same string as spatial_scipy_oracle.py: one VERSION file per tool
