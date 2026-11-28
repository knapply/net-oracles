"""Shared inputs and tests of the random layout entries of
validation/manifest.d/layout.yaml (layout_random_properties and
layout_random_distribution), used by the engine runner
(bindings/layout.py) and the oracles, so every tool is judged by the same
statements.

A layout of n nodes is an (n, 2) array. A tool draws in its own box; the
tests first map it to the unit square, [0, 1)^2.
"""

from __future__ import annotations

import math

import numpy as np

SAMPLE = 20000
BOX = (-1.0, 1.0)


def unit_uniform_flags(x, y):
    """Five flags for two coordinate samples in [0, 1): Kolmogorov-Smirnov
    against uniform for each (statistic below 1.95 / sqrt(n), level 0.001),
    both means within 5 standard errors, |correlation| below 5 / sqrt(n), and
    the coordinates are distinct (more than 99% different values)."""
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    n = len(x)
    flags = []
    for v in (x, y):
        v = np.sort(v)
        i = np.arange(1, n + 1)
        d = max(float((i / n - v).max()), float((v - (i - 1) / n).max()))
        flags.append(int(d < 1.95 / math.sqrt(n)))
    se = math.sqrt(1.0 / 12.0 / n)
    flags.append(int(abs(float(x.mean()) - 0.5) < 5 * se and abs(float(y.mean()) - 0.5) < 5 * se))
    flags.append(int(abs(float(np.corrcoef(x, y)[0, 1])) < 5 / math.sqrt(n)))
    flags.append(int(len(set(np.round(x, 12))) > 0.99 * n))
    return tuple(flags)


def property_flags(layout, n, low=BOX[0], high=BOX[1]):
    """Four flags for a tool's random layout function `layout(n, edgeless, seed)`
    returning an (n, 2) array in the box [low, high)^2 (`edgeless` is True for the
    graph with no edges, False for the fixture's own graph, which the function
    knows): finite and inside the box; the same seed twice gives the same
    coordinates; the edgeless graph of the same size gives the same
    coordinates; another seed gives different ones (n > 0)."""
    a = np.asarray(layout(n, False, 7), dtype=float)
    inside = bool(np.isfinite(a).all() and (a >= low).all() and (a < high).all())
    same = bool(np.array_equal(a, np.asarray(layout(n, False, 7), dtype=float)))
    edgeless = bool(np.array_equal(a, np.asarray(layout(n, True, 7), dtype=float)))
    other = bool(n == 0 or not np.array_equal(a, np.asarray(layout(n, False, 8), dtype=float)))
    return (int(inside), int(same), int(edgeless), int(other))


def distribution_flags(layout, low=BOX[0], high=BOX[1]):
    """`unit_uniform_flags` of `layout(SAMPLE, True, 1)` mapped to the unit square."""
    a = (np.asarray(layout(SAMPLE, True, 1), dtype=float) - low) / (high - low)
    return unit_uniform_flags(a[:, 0], a[:, 1])
