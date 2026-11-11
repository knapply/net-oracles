#!/usr/bin/env python3
# oracle-env: infomap
# oracle-entries: infomap
"""Golden values from Infomap (Rosvall and Bergstrom 2008; the `infomap`
package on PyPI), run as a black box through its Python interface.

Two uses, one per kind of variant:

- `infomap_native*`: the codelength Infomap reports for its own best two-level
  partition of an undirected network (flow of Rosvall and Bergstrom 2008,
  visit rates proportional to node strength, no teleportation). The engine
  must find a codelength no larger; both are heuristics, so `le` is the
  comparison.
- `infomap_partition*`: Infomap's partition, scored with the definition oracle's
  map equation (communities_definition_oracle.map_equation; two levels,
  teleportation 0.15 recorded on directed networks). The engine's codelength
  must again be no larger. This isolates the search from flow conventions
  that differ between the tools for directed networks.

Ten trials, seed 1 on Infomap's side too. A network without edges has no
random walk and is written as -1, as the engine reports it.

    ~/oracle-envs/infomap/bin/python oracles/infomap_oracle.py
"""

from __future__ import annotations

import importlib.metadata

from infomap import Infomap

import communities_definition_oracle as defn
from tool_common import run

ORACLE = "infomap"


def infomap_run(fx, weighted, directed):
    im = Infomap(two_level=True, directed=directed, silent=True, num_trials=10, seed=1)
    for v in range(fx.n):
        im.add_node(v)
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        if a == b:
            continue
        im.add_link(a, b, fx.weights[i] if weighted else 1.0)
    im.run()
    modules = im.get_modules()
    return im.codelength, [modules.get(v, -1 - v) for v in range(fx.n)]


def compute(variant: str, spec: dict, fx):
    e = spec["params"]
    weighted = bool(e.get("weighted", False))
    if fx.n == 0:
        return None
    has_links = any(a != b for a, b in zip(fx.src, fx.tgt))
    if "_native" in variant:
        if fx.directed:
            return None
        if not has_links:
            return [-1.0]
        length, _ = infomap_run(fx, weighted, False)
        return [length]
    if not has_links:
        membership = [0] * fx.n  # no flow to optimize: any partition is a valid bound
    else:
        _, membership = infomap_run(fx, weighted, fx.directed)
    value = defn.map_equation(fx, membership, weighted)
    return [-1.0 if value is None else float(value)]


if __name__ == "__main__":
    run(ORACLE, f"infomap {importlib.metadata.version('infomap')}", compute)
