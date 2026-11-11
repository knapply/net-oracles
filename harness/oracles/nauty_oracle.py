#!/usr/bin/env python3
# oracle-env: pynauty
"""Golden values from nauty 2.8.8 (McKay and Piperno 2014) through pynauty:
orbits of the automorphism group (automorphic equivalence) and its order
(the number of isomorphisms between a network and its node-reversed copy).

Networks with parallel edges are not representable in nauty (undefined);
loops are given as the vertex's own adjacency.

    python3 oracles/nauty_oracle.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import pynauty

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_fixture, load_manifest, write_values,
                    write_version)  # noqa: E402

ORACLE = "nauty"
CAP = 5000


def graph(fx, labels: bool, reverse: bool = False):
    """The network, or its node-reversed copy i -> n-1-i; vertices are
    coloured by index parity when `labels` (the manifest's label rule)."""
    adj = {v: set() for v in range(fx.n)}
    flip = (lambda v: fx.n - 1 - v) if reverse else (lambda v: v)
    for a, b in zip(fx.src, fx.tgt):
        a, b = flip(a), flip(b)
        adj[a].add(b)
        if not fx.directed:
            adj[b].add(a)
    coloring = []
    if labels:
        coloring = [s for s in ({v for v in range(fx.n) if v % 2 == 0},
                                {v for v in range(fx.n) if v % 2 == 1}) if s]
    return pynauty.Graph(fx.n, directed=fx.directed,
                         adjacency_dict={v: sorted(w) for v, w in adj.items()},
                         vertex_coloring=coloring)


def main() -> None:
    manifest = load_manifest()
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        if "multi_edges" in fx.tags or fx.n == 0:
            continue
        for variant, spec in manifest.items():
            if ORACLE not in spec["oracles"] or not applies(spec, fx):
                continue
            if variant == "automorphic_equivalence":
                _, _, _, orbits, _ = pynauty.autgrp(graph(fx, False))
                write_values(ORACLE, name, variant, orbits)
            elif variant in ("vf2pp_iso", "vf2pp_iso_labels"):
                _, g1, g2, _, _ = pynauty.autgrp(graph(fx, variant.endswith("labels")))
                labels = variant.endswith("labels")
                # Isomorphisms onto the reversed copy: as many as the
                # automorphisms when the two (coloured) graphs are isomorphic.
                g_a, g_b = graph(fx, labels), graph(fx, labels, True)
                # nauty's certificate is the adjacency matrix in canonical
                # order; the vertex colours in that order must agree as well.
                color = [v % 2 if labels else 0 for v in range(fx.n)]
                same = (pynauty.certificate(g_a) == pynauty.certificate(g_b)
                        and [color[v] for v in pynauty.canon_label(g_a)]
                        == [color[v] for v in pynauty.canon_label(g_b)])
                size = round(g1 * 10 ** g2) if same else 0
                c = min(size, CAP)
                write_values(ORACLE, name, variant, [(c, 1 if c else 0)])
            else:
                continue
            count += 1
    write_version(ORACLE, f"nauty via pynauty {pynauty.__version__} (nauty {getattr(pynauty, "nauty_version", None) or getattr(pynauty, "_nauty_version", "?")})")
    print(f"nauty (pynauty {pynauty.__version__}): wrote {count} golden files")


if __name__ == "__main__":
    main()
