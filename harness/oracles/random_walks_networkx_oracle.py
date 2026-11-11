#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for random
walks and random-walk sampling (manifest/random_walks.yaml,
entries with a `networkx` oracle).

  end     the share of 20000 paths of 4 moves from node 0 that end at each
          node, from nx.generate_random_paths(G, 20000, path_length = 4,
          source = 0, seed = 1): NetworkX's own sampler, compared with the
          engine's by distribution
  visits  the personalized PageRank of node 0 with damping 0.8 and dangling
          nodes returning to node 0, nx.pagerank: the stationary distribution
          of a walk that restarts at node 0 with probability 0.2

NetworkX reads the fixture as a simple graph (nx.Graph or nx.DiGraph).

    python3 oracles/random_walks_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)

ORACLE = "networkx"
PATHS = 20000
END_STEPS = 4
RESTART = 0.2


def simple(fx, weighted):
    g = nx.DiGraph() if fx.directed else nx.Graph()
    g.add_nodes_from(range(fx.n))
    for e, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        g.add_edge(a, b, weight=fx.weights[e] if weighted and fx.weighted else 1.0)
    return g


def compute(fx, spec):
    weighted = bool(spec.get("weighted"))
    if fx.n == 0 or (weighted and fx.weighted and any(w < 0 for w in fx.weights)):
        return []
    g = simple(fx, weighted)
    if spec["fn"] == "random_walk":
        count = np.zeros(fx.n)
        for path in nx.generate_random_paths(g, PATHS, path_length=END_STEPS, source=0,
                                             weight="weight", seed=1):
            count[path[-1]] += 1
        return list(count / PATHS)
    rank = nx.pagerank(g, alpha=1 - RESTART, personalization={0: 1.0}, dangling={0: 1.0},
                       weight="weight", tol=1e-14, max_iter=100000)
    return [rank[v] for v in range(fx.n)]


def main() -> None:
    spec = load_area("random_walks")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            o = v["oracles"].get(ORACLE)
            if o is None or not applies(v, fx):
                continue
            if ("only_on" in o and name not in o["only_on"]) or \
                    set(fx.tags) & set(o.get("undefined_when", [])):
                continue
            try:
                values = compute(fx, v["params"])
            except Exception as exc:  # NetworkX fails where the answer is undefined
                print(f"  {name} {variant}: {type(exc).__name__}")
                continue
            write_values(ORACLE, name, variant, values)
            count += 1
    write_version(ORACLE, f"networkx {nx.__version__}")
    print(f"networkx (random walks): wrote {count} golden files")


if __name__ == "__main__":
    main()
