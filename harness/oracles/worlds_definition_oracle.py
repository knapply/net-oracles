#!/usr/bin/env python3
"""Definition oracle for centrality across sampled possible worlds
(manifest/worlds.yaml; statistics as in ../bindings/worlds.py).

Worlds. Edge e (fixture order) exists in world w when bit w % 64 of its
mask word w // 64 is set. The word is drawn from Philox4x32-10 (Salmon et
al. 2011), key = the seed's two 32-bit halves, counter = (block low, block
high, stream low, stream high) with stream = (e << 24) | word, 64-bit draws
taken high word first. Bit b is set when the uniform number
U = 0.r1 r2 r3 ... (r_i = bit b of the i-th draw) is below the keep
probability, compared bit by bit with the probability's binary expansion
until every bit is decided or the expansion ends (an exact Bernoulli
draw). Implemented here from those definitions, sharing no code with the
engine.

Values. In each world, from scratch: breadth-first distances (edge
weights ignored, loops never on a path), then

  closeness   Wasserman-Faust: (r / S) (r / (n - 1)) for r nodes reached at
              total distance S, 0 when none (distances into the node when
              directed)
  harmonic    sum of 1 / d over the nodes reaching the node (Fractions,
              rounded once)
  reach       number of other nodes reaching the node
  summary     per node over the worlds: mean, standard deviation (divisor
              k - 1), quantiles 0.05, 0.5, 0.95 (linear, Hyndman-Fan type
              7), from the oracle's own closeness values

    python3 oracles/worlds_definition_oracle.py
"""

from __future__ import annotations

import sys
from collections import deque
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
MASK32 = 0xFFFFFFFF
LEVELS = (0.05, 0.5, 0.95)


def philox(counter, key):
    """One Philox4x32-10 block (Salmon et al. 2011, Random123 constants)."""
    m0, m1, w0, w1 = 0xD2511F53, 0xCD9E8D57, 0x9E3779B9, 0xBB67AE85
    c, k = list(counter), list(key)
    for rnd in range(10):
        if rnd:
            k = [(k[0] + w0) & MASK32, (k[1] + w1) & MASK32]
        p0, p1 = m0 * c[0], m1 * c[2]
        c = [((p1 >> 32) ^ c[1] ^ k[0]) & MASK32, p1 & MASK32,
             ((p0 >> 32) ^ c[3] ^ k[1]) & MASK32, p0 & MASK32]
    return c


def draws(seed, stream):
    """64-bit draws of stream `stream` under `seed`, high 32 bits first."""
    key = [seed & MASK32, seed >> 32]
    block = 0
    while True:
        out = philox([block & MASK32, block >> 32, stream & MASK32, stream >> 32], key)
        block += 1
        yield (out[0] << 32) | out[1]
        yield (out[2] << 32) | out[3]


def keep_bit(seed, edge, world, keep):
    """Whether edge `edge` exists in world `world`."""
    word, bit = divmod(world, 64)
    if keep >= 1.0:
        return True
    if keep <= 0.0:
        return False
    rest = keep
    for r in draws(seed, (edge << 24) | word):
        rest *= 2.0
        u = (r >> bit) & 1
        if rest >= 1.0:
            rest -= 1.0
            if u == 0:
                return True
        elif u == 1:
            return False
        if rest == 0.0:
            return False
    raise AssertionError("unreachable")


def world_edges(fx, spec, world):
    keep = float(spec.get("keep", 0.9))
    seed = int(spec.get("seed", 0))
    return [(a, b) for e, (a, b) in enumerate(zip(fx.src, fx.tgt))
            if keep_bit(seed, e, world, keep)]


def into_rows(n, edges, directed):
    """Neighbours a search from v follows to find the nodes reaching v."""
    rows = [set() for _ in range(n)]
    for a, b in edges:
        if a == b:
            continue
        rows[b].add(a)
        if not directed:
            rows[a].add(b)
    return rows


def distances(rows, source):
    dist = {source: 0}
    queue = deque([source])
    while queue:
        v = queue.popleft()
        for u in rows[v]:
            if u not in dist:
                dist[u] = dist[v] + 1
                queue.append(u)
    del dist[source]
    return dist


def world_values(fx, spec, world, stat):
    rows = into_rows(fx.n, world_edges(fx, spec, world), fx.directed)
    out = []
    for v in range(fx.n):
        d = distances(rows, v)
        r, s = len(d), sum(d.values())
        if stat == "closeness":
            out.append(0.0 if r == 0 else (r / s) * (r / (fx.n - 1)))
        elif stat == "harmonic":
            out.append(float(sum((Fraction(1, x) for x in d.values()), Fraction(0))))
        else:
            out.append(float(r))
    return out


def quantile(sorted_values, level):
    pos = level * (len(sorted_values) - 1)
    lo = int(pos // 1)
    hi = min(lo + 1, len(sorted_values) - 1)
    frac = pos - lo
    return sorted_values[lo] + frac * (sorted_values[hi] - sorted_values[lo])


def compute(fx, spec):
    if fx.n == 0:
        return []
    worlds = int(spec["worlds"])
    stat = spec["stat"]
    stat_values = "closeness" if stat == "summary" else stat
    matrix = [world_values(fx, spec, w, stat_values) for w in range(worlds)]
    if stat != "summary":
        return [matrix[w][v] for v in range(fx.n) for w in range(worlds)]
    out = []
    for v in range(fx.n):
        xs = [matrix[w][v] for w in range(worlds)]
        k = len(xs)
        mean = float(sum(Fraction(x) for x in xs) / k)
        var = float(sum((Fraction(x) - Fraction(mean)) ** 2 for x in xs) / (k - 1))
        xs.sort()
        out.append([mean, var ** 0.5, k] + [quantile(xs, q) for q in LEVELS])
    return out


def main() -> None:
    spec = load_area("worlds")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if "definition" not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (possible worlds): wrote {count} golden files")


if __name__ == "__main__":
    main()
