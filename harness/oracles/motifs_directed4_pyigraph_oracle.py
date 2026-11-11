#!/usr/bin/env python3
# oracle-env: pyigraph
"""Golden values from python-igraph (Csardi and Nepusz 2006) for the directed
size-4 motif census: `Graph.motifs_randesu(size=4)` on the simple digraph
(simplify removes loops and parallel arcs). It returns one count per
isoclass, NaN for the 19 classes that are not weakly connected; the NaN
entries are dropped, leaving the 199 connected classes in igraph's id order.
igraph is run as a black box.

    ~/oracle-envs/pyigraph/bin/python oracles/motifs_directed4_pyigraph_oracle.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

try:
    import igraph as ig
except ImportError:  # the tool is not installed here
    print("python-igraph is not installed")
    sys.exit(3)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture, write_values,  # noqa: E402
                    write_version)

ORACLE = "pyigraph"
AREA = "motifs_directed4"


def census(fx):
    g = ig.Graph(n=fx.n, edges=list(zip(fx.src, fx.tgt)), directed=True)
    g.simplify(multiple=True, loops=True)
    counts = g.motifs_randesu(size=4)
    return [int(c) for c in counts if not math.isnan(c)]


def main() -> None:
    spec = load_area(AREA)
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, census(fx))
            count += 1
    print(f"python-igraph {ig.__version__} ({AREA}): wrote {count} golden files")
    write_version(ORACLE, f"python-igraph {ig.__version__}")


if __name__ == "__main__":
    main()
