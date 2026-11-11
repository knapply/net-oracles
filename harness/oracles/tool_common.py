"""Shared plumbing for the reference-tool oracles that run in their own
environments (`# oracle-env:` scripts): fixture conversions that do not
depend on any graph library, the deterministic node rules the manifest
names, and the loop that writes golden files.

Each tool script defines `compute(variant, spec, fx)` returning the values
to write (or None when the tool has no answer for that variant and
fixture) and calls `run(ORACLE, version, compute)`. An exception raised by
the tool on one fixture is reported and writes nothing, so the comparison
shows it as not run until the manifest records it as undefined.
"""

from __future__ import annotations

import sys
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_fixture,  # noqa: E402
                    load_manifest_by_area, write_values, write_version)

import math  # noqa: E402

# How each area writes values that are not finite (its manifest header):
# (NaN, +infinity). None leaves the value as it is; () is an empty line.
ENCODING = {
    "assortativity": (-999, None), "centrality_extra": (-999, -1000),
    "descriptive": (-999, -1000), "distance_measures": (-999, -1000),
    "temporal": (-999, -1000), "topography": (-1, None), "groups": (-1, None),
    "resilience": (-1, None), "twomode": (-1, None), "connectivity": (-1, None),
    "communities": (-1, None),
    "spectral": ((), None), "roles": ((), None), "positions": ((), None),
}


def encode(area: str, values):
    nan, inf = ENCODING.get(area, (None, None))

    def one(x):
        if isinstance(x, (list, tuple)):
            return tuple(one(y) for y in x)
        x = float(x)
        if math.isnan(x) and nan is not None:
            return nan
        if math.isinf(x) and x > 0 and inf is not None:
            return inf
        if math.isinf(x) and x < 0 and area == "distance_measures":
            return -1001
        return x
    return [one(x) for x in values]


def weights(fx) -> list[float]:
    return fx.weights if fx.weighted else [1.0] * len(fx.src)


def has_loops(fx) -> bool:
    return any(a == b for a, b in zip(fx.src, fx.tgt))


def loops_matter(e: dict, fx) -> bool:
    """True when the engine's loop convention (`loops: twice | ignore`)
    changes the answer on this fixture and a tool that counts an undirected
    loop once cannot reproduce it."""
    mode = e.get("loops", "once")
    if mode == "once" or not has_loops(fx):
        return False
    return mode == "ignore" or not fx.directed


def has_multi(fx) -> bool:
    seen = set()
    for a, b in zip(fx.src, fx.tgt):
        key = (a, b) if fx.directed else (min(a, b), max(a, b))
        if key in seen:
            return True
        seen.add(key)
    return False


def simple_edges(fx, *, loops: bool = False, keep: str = "first",
                 undirected: bool = False) -> list[tuple[int, int, float]]:
    """Edges with parallel copies collapsed (undirected pairs as (min, max)).
    keep: which weight a collapsed pair keeps (first | min | max | sum).
    undirected: also collapse the two directions of a directed pair."""
    out: dict[tuple[int, int], float] = {}
    for a, b, w in zip(fx.src, fx.tgt, weights(fx)):
        if a == b and not loops:
            continue
        key = (a, b) if fx.directed and not undirected else (min(a, b), max(a, b))
        if key not in out:
            out[key] = w
        elif keep == "min":
            out[key] = min(out[key], w)
        elif keep == "max":
            out[key] = max(out[key], w)
        elif keep == "sum":
            out[key] += w
    return [(a, b, w) for (a, b), w in out.items()]


def adjacency(fx, *, weighted: bool = False, loops: str = "once", simple: bool = False):
    """Dense adjacency as nested lists. Undirected edges fill both cells;
    loops: once (a loop adds 1 to A[v][v]), twice (adds 2 when undirected),
    ignore. simple: entries are 0/1 (weights ignored when not weighted)."""
    n = fx.n
    a = [[0.0] * n for _ in range(n)]
    for u, v, w in zip(fx.src, fx.tgt, weights(fx)):
        x = w if weighted else 1.0
        if u == v:
            if loops == "ignore":
                continue
            a[u][u] += x * (2 if loops == "twice" and not fx.directed else 1)
            continue
        a[u][v] += x
        if not fx.directed:
            a[v][u] += x
    if simple:
        a = [[(1.0 if x else 0.0) for x in row] for row in a]
    return a


def node_rule(rule: str, n: int) -> list[float]:
    """The deterministic node values the manifest names."""
    if rule == "mod3":
        return [float(v % 3) for v in range(n)]
    if rule == "mod2":
        return [float(v % 2) for v in range(n)]
    if rule == "mod3plus1":
        return [float(v % 3 + 1) for v in range(n)]
    if rule == "blocks3":
        return [float(3 * v // n) for v in range(n)]
    if rule == "num7":
        return [float(7 * v % 11) for v in range(n)]
    if rule == "num3":
        return [float(3 * v % 5) for v in range(n)]
    if rule == "id":
        return [float(v) for v in range(n)]
    raise ValueError(f"unknown node rule {rule!r}")


def groups_of(labels) -> list[list[int]]:
    out: dict = {}
    for v, c in enumerate(labels):
        out.setdefault(c, []).append(v)
    return list(out.values())


def run(oracle: str, version: str, compute, *, raw: bool = False) -> None:
    """raw: write values as the tool returns them (NaN, inf), as the R
    oracles do, instead of the area's markers."""
    areas = load_manifest_by_area()
    manifest = {k: v for entries in areas.values() for k, v in entries.items()}
    area_of = {k: a for a, entries in areas.items() for k in entries}
    count = errors = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, spec in manifest.items():
            if oracle not in spec["oracles"] or not applies(spec, fx):
                continue
            try:
                values = compute(variant, spec, fx)
            except Exception as exc:  # the tool rejected this input
                errors += 1
                first = traceback.format_exception_only(type(exc), exc)[-1].strip()
                print(f"  {variant} on {name}: {first[:200]}")
                continue
            if values is not None:
                write_values(oracle, name, variant,
                             values if raw else encode(area_of[variant], values))
                count += 1
    write_version(oracle, version)
    print(f"{version}: wrote {count} golden files ({errors} inputs rejected by the tool)")
