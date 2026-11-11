"""Deterministic inputs for the builders and operations of
validation/manifest.d/construct.yaml, shared by the engine runners
(bindings/construct.py) and both oracles.

- `first(fx)`: the distinct edges (or arcs) of the fixture, loops kept, as a
  sorted list (an undirected edge as (smaller, larger));
- `second(fx)`: the even-ranked edges of `first` plus the ring i - ((i + 1)
  mod n) for n >= 2 (directed: the arcs i -> (i + 1) mod n), sorted;
- `loop_free(edges)`: an edge list without self-loops.
"""

from __future__ import annotations


def normalize(edges, directed):
    return sorted({(a, b) if directed else (min(a, b), max(a, b)) for a, b in edges})


def first(fx):
    return normalize(zip(fx.src, fx.tgt), fx.directed)


def second(fx):
    kept = [e for i, e in enumerate(first(fx)) if i % 2 == 0]
    ring = [(i, (i + 1) % fx.n) for i in range(fx.n)] if fx.n >= 2 else []
    return normalize(kept + ring, fx.directed)


def loop_free(edges):
    return [e for e in edges if e[0] != e[1]]
