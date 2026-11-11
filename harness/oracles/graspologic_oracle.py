#!/usr/bin/env python3
# oracle-env: graspologic
# oracle-entries: graspologic
"""Golden values from graspologic (Chung et al. 2019): its graph Laplacian
forms and its modularity (computed by graspologic-native, a Rust library),
where they match a manifest entry.

    ~/oracle-envs/graspologic/bin/python oracles/graspologic_oracle.py
"""

from __future__ import annotations

import importlib.metadata

import networkx as nx
import numpy as np
from graspologic.partition import modularity
from graspologic.utils import to_laplacian

from tool_common import adjacency, node_rule, run, weights

ORACLE = "graspologic"


def compute(variant: str, spec: dict, fx):
    e = spec["params"]
    fn = e["fn"]
    n = fx.n
    wt = bool(e.get("weighted"))
    if n == 0:
        return None
    if fn == "gm_laplacian" and e.get("normalized"):
        a = np.array(adjacency(fx, weighted=wt, loops="once"))
        lap = to_laplacian(a, form="I-DAD")
        return [float(x) for row in lap for x in row]
    if fn == "modularity" and e.get("partition") == "blocks3" and not fx.directed:
        g = nx.Graph()
        g.add_nodes_from(range(n))
        for a, b, w in zip(fx.src, fx.tgt, weights(fx)):
            x = w if wt else 1.0
            if g.has_edge(a, b):
                g[a][b]["weight"] += x
            else:
                g.add_edge(a, b, weight=x)
        labels = node_rule("blocks3", n)
        parts = {v: int(labels[v]) for v in range(n)}
        return [float(modularity(g, parts, weight_attribute="weight",
                                 resolution=e.get("resolution", 1.0)))]
    return None


if __name__ == "__main__":
    run(ORACLE, f"graspologic {importlib.metadata.version('graspologic')} "
                f"(graspologic-native {importlib.metadata.version('graspologic-native')})",
        compute)
