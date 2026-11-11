#!/usr/bin/env python3
# oracle-env: cdlib
# oracle-entries: cdlib
"""Golden values from cdlib (Rossetti, Milli, and Cazabet 2019): its
partition-comparison scores and its modularity, used as black boxes.

The partitions compared are the ones the R igraph oracle compares
(r_communities.R): blocks, node v of n in group floor(3 v / n), against
stripes, group (7 v) mod 4. cdlib computes some scores itself and hands
others to scikit-learn; either way the call is cdlib's.

    ~/oracle-envs/cdlib/bin/python oracles/cdlib_oracle.py
"""

from __future__ import annotations

import importlib.metadata
import math

import networkx as nx
from cdlib import NodeClustering, evaluation

from tool_common import groups_of, node_rule, run

ORACLE = "cdlib"


def clustering(labels, graph=None):
    return NodeClustering(groups_of(labels), graph=graph, method_name="fixed")


def compute(variant: str, spec: dict, fx):
    e = spec["params"]
    fn = e["fn"]
    n = fx.n
    if fn == "compare_partitions":
        if n == 0:
            return None
        g = nx.Graph()
        g.add_nodes_from(range(n))
        a = clustering([3 * v // n for v in range(n)], g)
        b = clustering([(7 * v) % 4 for v in range(n)], g)
        m = e["method"]
        if m == "vi":
            # cdlib reports the variation of information in bits; the
            # engine (like igraph) in nats.
            r = evaluation.variation_of_information(a, b)
            return [float(getattr(r, "score", r)) * math.log(2)]
        elif m == "nmi":
            r = evaluation.normalized_mutual_information(a, b)
        elif m == "adjusted_rand":
            r = evaluation.adjusted_rand_index(a, b)
        elif m == "ami":
            r = evaluation.adjusted_mutual_information(a, b)
        elif m == "rand" and hasattr(evaluation, "rand_index"):
            r = evaluation.rand_index(a, b)
        else:
            return None
        return [float(getattr(r, "score", r))]
    if fn == "modularity" and e.get("partition") == "blocks3" and not fx.directed \
            and e.get("resolution", 1.0) == 1.0 and not e.get("weighted"):
        g = nx.MultiGraph()
        g.add_nodes_from(range(n))
        g.add_edges_from(zip(fx.src, fx.tgt))
        labels = node_rule("blocks3", n)
        r = evaluation.newman_girvan_modularity(g, clustering(labels, g))
        return [float(r.score)]
    return None


if __name__ == "__main__":
    run(ORACLE, f"cdlib {importlib.metadata.version('cdlib')}", compute)
