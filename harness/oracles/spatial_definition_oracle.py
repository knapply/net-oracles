#!/usr/bin/env python3
"""Golden values for edge lengths, proximity networks and group geometry of
located nodes in one to five dimensions, with a third coordinate on the
sphere (manifest/spatial.yaml), computed from the definitions
in exact or high-precision arithmetic.

This oracle shares no code with the engine and uses different methods:

- Cartesian and planar coordinates are whole numbers, so every distance
  is decided exactly. The Euclidean, Manhattan and Chebyshev distances and
  the p-th power sum of an integer p are exact integers; a pair is within
  a distance r when the exact sum is at most r**q (q = 2, 1, 1, p), and
  neighbours rank by that exact sum, then by index. A Minkowski distance
  with a p that is not a whole number is a 60-digit decimal power
  (decimal.Decimal). The engine forms the double distance and compares it.
- Longitude and latitude use 60-digit decimal arithmetic with sine, cosine
  and arctangent written here from their series (no libm, no mpmath). The
  great-circle distance is R atan2(|u x v|, u . v) on the exact unit
  vectors (the engine uses the haversine formula). With a height the
  default distance is sqrt(gc^2 + dz^2); with `chord` it is the length of
  the difference of the points (R + h) u on the sphere of radius R + h.
- A group's centroid is the coordinate mean (Cartesian, planar) or the
  normalized mean unit vector with the mean height (longitude and
  latitude); its dispersion is the mean and root mean square of the
  distances from it, under the entry's metric.

Rules for ties, stated once for every oracle of these entries: a pair at
exactly the distance r is within it (distance <= r), and neighbours at
equal distance rank by node index. Fixtures were chosen so that every
tie is exact in both arithmetics (whole coordinates; zero surface distance
with a height difference of exactly 100000 in the surface reading).

Undefined values (NaN) are written as empty lines.

    python3 oracles/spatial_definition_oracle.py
"""

from __future__ import annotations

import math
import sys
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,
                    load_fixture, write_values, write_version)  # noqa: E402
from spatial_points import EARTH_RADIUS_M, partition, points  # noqa: E402

ORACLE = "definition"
MAX_NODES = 80
getcontext().prec = 60
D = Decimal


# ---- Decimal elementary functions (series, no libm) ---------------------------

def _atan_series(t: Decimal) -> Decimal:
    """arctan t for |t| <= 0.1 by its Taylor series."""
    total, term, k = t, t, 0
    t2 = t * t
    eps = D(10) ** -(getcontext().prec + 2)
    while abs(term) > eps:
        k += 1
        term = -term * t2
        total += term / (2 * k + 1)
    return total


def _pi() -> Decimal:
    # Machin: pi = 16 atan(1/5) - 4 atan(1/239)
    def acot(x: int) -> Decimal:
        x_dec = D(x)
        total = term = D(1) / x_dec
        k, x2 = 0, x_dec * x_dec
        eps = D(10) ** -(getcontext().prec + 2)
        while abs(term) > eps:
            k += 1
            term = -term / x2
            total += term / (2 * k + 1)
        return total
    return 16 * acot(5) - 4 * acot(239)


PI = _pi()


def atan(t: Decimal) -> Decimal:
    if t < 0:
        return -atan(-t)
    if t > 1:
        return PI / 2 - atan(1 / t)
    halvings = 0
    while t > D("0.1"):
        t = t / (1 + (1 + t * t).sqrt())
        halvings += 1
    return _atan_series(t) * (2 ** halvings)


def atan2(y: Decimal, x: Decimal) -> Decimal:
    """atan2 for y >= 0."""
    if x > 0:
        return atan(y / x)
    if x < 0:
        return PI - atan(y / -x)
    return PI / 2 if y > 0 else D(0)


def _sin_cos(angle: Decimal) -> tuple[Decimal, Decimal]:
    """Both from Taylor series, the angle reduced into [-pi, pi]."""
    two_pi = 2 * PI
    angle = angle - two_pi * (angle / two_pi).to_integral_value()
    eps = D(10) ** -(getcontext().prec + 2)
    s = term = angle
    k = 1
    a2 = angle * angle
    while abs(term) > eps:
        term = -term * a2 / ((2 * k) * (2 * k + 1))
        s += term
        k += 1
    c = term = D(1)
    k = 1
    while abs(term) > eps:
        term = -term * a2 / ((2 * k - 1) * (2 * k))
        c += term
        k += 1
    return s, c


def unit_vector(lon: float, lat: float) -> tuple[Decimal, Decimal, Decimal]:
    lam = D(lon) * PI / 180
    phi = D(lat) * PI / 180
    sl, cl = _sin_cos(lam)
    sp, cp = _sin_cos(phi)
    return cp * cl, cp * sl, sp


# ---- Distances -----------------------------------------------------------------

R = D(EARTH_RADIUS_M)


def surface_distance(a, b, spec, rows=None) -> Decimal:
    """Distance between two located points under the entry (decimal)."""
    (u, hu), (v, hv) = a, b
    if spec.get("height", "surface") == "chord":
        p = [(R + hu) * c for c in u]
        q = [(R + hv) * c for c in v]
        return sum(((x - y) ** 2 for x, y in zip(p, q)), D(0)).sqrt()
    cross = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
    sin_part = sum((c * c for c in cross), D(0)).sqrt()
    cos_part = sum((x * y for x, y in zip(u, v)), D(0))
    great_circle = R * atan2(sin_part, cos_part)
    return (great_circle ** 2 + (hu - hv) ** 2).sqrt()


class Space:
    """Located points of one entry with exact (or decimal) distances."""

    def __init__(self, spec: dict, n: int):
        self.spec = spec
        self.crs = spec["crs"]
        rows = points(spec, n)
        self.rows = rows
        self.n = n
        if self.crs == "lonlat":
            self.located = [(unit_vector(r[0], r[1]), D(r[2]) if len(r) > 2 else D(0))
                            for r in rows]
        else:
            self.metric = spec.get("metric", "euclidean")
            self.p = spec.get("p", 2.0)

    # key: a number that is a strictly increasing function of the distance,
    # exact where the distance is.  power: the exponent q with distance**q = key.
    def key(self, i: int, j: int):
        if self.crs == "lonlat":
            return surface_distance(self.located[i], self.located[j], self.spec)
        a, b = self.rows[i], self.rows[j]
        diffs = [abs(int(x) - int(y)) for x, y in zip(a, b)]
        return self.key_of(diffs)

    def key_of(self, diffs):
        m = self.metric if self.crs == "cartesian" else "euclidean"
        if m == "euclidean":
            return sum(d * d for d in diffs)
        if m == "manhattan":
            return sum(diffs)
        if m == "chebyshev":
            return max(diffs)
        p = self.p
        if float(p).is_integer():
            return sum(d ** int(p) for d in diffs)
        return sum((D(d) ** D(p) for d in diffs), D(0))

    def distance(self, i: int, j: int) -> float:
        key = self.key(i, j)
        return self.to_distance(key)

    def to_distance(self, key) -> float:
        if self.crs == "lonlat":
            return float(key)
        m = self.metric if self.crs == "cartesian" else "euclidean"
        if m == "euclidean":
            return float(D(key).sqrt())
        if m in ("manhattan", "chebyshev"):
            return float(key)
        p = D(self.spec.get("p", 2.0))
        return float(D(key) ** (1 / p)) if key else 0.0

    def within(self, i: int, j: int, r: float) -> bool:
        key = self.key(i, j)
        if self.crs == "lonlat":
            return key <= D(r)
        m = self.metric if self.crs == "cartesian" else "euclidean"
        q = {"euclidean": 2, "manhattan": 1, "chebyshev": 1}.get(m)
        if q is not None:
            return Fraction(key) <= Fraction(r) ** q
        p = self.p
        if float(p).is_integer():
            return Fraction(key) <= Fraction(r) ** int(p)
        return D(key) <= D(r) ** D(p)


# ---- Entries -------------------------------------------------------------------

def edge_lengths(fx, spec):
    space = Space(spec, fx.n)
    return [space.distance(s, t) for s, t in zip(fx.src, fx.tgt)]


def proximity(fx, spec):
    space = Space(spec, fx.n)
    n = fx.n
    if spec.get("k", 0) > 0:
        out = []
        for i in range(n):
            ranked = sorted((space.key(i, j), j) for j in range(n) if j != i)
            out += [(float(i), float(j), space.to_distance(key))
                    for key, j in ranked[:spec["k"]]]
        return out
    r = float(spec["r"])
    return [(float(i), float(j), space.distance(i, j)) for i in range(n)
            for j in range(i + 1, n) if space.within(i, j, r)]


def group_geometry(fx, spec):
    labels = partition(spec["partition"], fx.n)
    groups = list(dict.fromkeys(labels))
    out = []
    for g in groups:
        members = [i for i in range(fx.n) if labels[i] == g]
        out.append(group_line(spec, members, fx.n))
    return out


def group_line(spec, members, n):
    crs = spec["crs"]
    rows = points(spec, n)
    dim = len(rows[0])
    if crs == "lonlat":
        vecs = [unit_vector(rows[i][0], rows[i][1]) for i in members]
        mean = [sum((v[c] for v in vecs), D(0)) / len(vecs) for c in range(3)]
        norm = sum((c * c for c in mean), D(0)).sqrt()
        lon = atan2_signed(mean[1], mean[0]) * 180 / PI
        lat = atan2_signed(mean[2], (mean[0] ** 2 + mean[1] ** 2).sqrt()) * 180 / PI
        center = [lon, lat]
        height = D(0)
        if dim == 3:
            height = sum((D(rows[i][2]) for i in members), D(0)) / len(members)
            center.append(height)
        c_loc = (tuple(m / norm for m in mean), height)
        dists = [surface_distance((unit_vector(rows[i][0], rows[i][1]),
                                   D(rows[i][2]) if dim == 3 else D(0)), c_loc, spec)
                 for i in members]
    else:
        m = spec.get("metric", "euclidean") if crs == "cartesian" else "euclidean"
        center = [Fraction(sum(int(rows[i][a]) for i in members), len(members))
                  for a in range(dim)]
        dists = [centroid_distance(m, spec.get("p", 2.0),
                                   [abs(Fraction(int(rows[i][a])) - center[a]) for a in range(dim)])
                 for i in members]
    mean_d = sum(dists, D(0)) / len(dists)
    rms = (sum((d * d for d in dists), D(0)) / len(dists)).sqrt()
    return tuple([float(len(members))] + [float(c) for c in center] + [float(mean_d), float(rms)])


def atan2_signed(y: Decimal, x: Decimal) -> Decimal:
    if y >= 0:
        return atan2(y, x)
    return -atan2(-y, x)


def centroid_distance(metric, p, diffs) -> Decimal:
    d = [D(f.numerator) / D(f.denominator) for f in diffs]
    if metric == "euclidean":
        return sum((x * x for x in d), D(0)).sqrt()
    if metric == "manhattan":
        return sum(d, D(0))
    if metric == "chebyshev":
        return max(d)
    pd = D(p)
    s = sum((x ** pd for x in d if x), D(0))
    return s ** (1 / pd) if s else D(0)


def evaluate(fx, spec):
    return {"spatial_edge_lengths": edge_lengths, "spatial_proximity": proximity,
            "spatial_group_geometry": group_geometry}[spec["fn"]](fx, spec)


def main() -> int:
    entries = load_area("spatial")
    written = 0
    for name in fixture_names():
        fx = load_fixture(name)
        if fx.n > MAX_NODES:
            continue
        for variant, spec in entries.items():
            if ORACLE not in spec["oracles"] or not applies(spec, fx):
                continue
            values = evaluate(fx, spec["params"])
            write_values(ORACLE, name, variant, values)
            written += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"Wrote {written} definition golden files for spatial.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
