#!/usr/bin/env python3
# oracle-entries: scipy
"""Golden values for edge lengths, proximity networks and group geometry of
located nodes (manifest/spatial.yaml) from scipy.spatial, used
as a black box:

- `scipy.spatial.distance` gives the Euclidean, Manhattan (cityblock),
  Chebyshev and Minkowski distances for edge lengths and for the dispersion
  of a group around its centroid;
- `scipy.spatial.cKDTree` answers the proximity entries: `query_pairs(r, p)`
  for the pairs within r (the tree's boundary rule is checked by the
  entries' tie fixtures) and `query(x, k = n, p)` for the neighbours, which
  are then re-ranked by (distance, index) because the tree breaks ties
  arbitrarily; the rule is the one every oracle of these entries states.
- Longitude and latitude: the chord entries put the points (R + h) u on a
  cKDTree and use the Euclidean metric. The surface reading
  sqrt(gc^2 + dz^2) is not a tree metric, so there the great-circle part is
  numpy's atan2 of |u x v| and u . v on the unit vectors and the height
  difference comes from scipy.spatial.distance.cdist; pairs are compared
  by brute force.

    python3 oracles/spatial_scipy_oracle.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
import scipy
from scipy.spatial import cKDTree
from scipy.spatial import distance as sd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from common import (applies, fixture_names, load_area, load_fixture, write_values,
                    write_version)  # noqa: E402
from spatial_points import EARTH_RADIUS_M, partition, points  # noqa: E402

ORACLE = "scipy"
R = EARTH_RADIUS_M


def p_of(spec) -> float:
    m = spec.get("metric", "euclidean") if spec["crs"] == "cartesian" else "euclidean"
    return {"euclidean": 2.0, "manhattan": 1.0, "chebyshev": math.inf}.get(m, spec.get("p"))


def pair_distance(a, b, p) -> float:
    if p == 2.0:
        return float(sd.euclidean(a, b))
    if p == 1.0:
        return float(sd.cityblock(a, b))
    if math.isinf(p):
        return float(sd.chebyshev(a, b))
    return float(sd.minkowski(a, b, p))


def unit_vectors(rows):
    lon, lat = np.radians(rows[:, 0]), np.radians(rows[:, 1])
    return np.stack([np.cos(lat) * np.cos(lon), np.cos(lat) * np.sin(lon), np.sin(lat)], axis=1)


def surface_matrix(rows):
    """sqrt(gc^2 + dz^2) for every pair."""
    u = unit_vectors(rows)
    n = len(rows)
    gc = np.zeros((n, n))
    for i in range(n):
        cross = np.linalg.norm(np.cross(u[i], u), axis=1)
        dot = u @ u[i]
        gc[i] = R * np.arctan2(cross, dot)
    height = rows[:, 2:3] if rows.shape[1] > 2 else np.zeros((n, 1))
    dz = sd.cdist(height, height, "cityblock")
    return np.sqrt(gc ** 2 + dz ** 2)


class Model:
    """Distances, pair search and neighbour search of one entry."""

    def __init__(self, spec, n):
        self.spec, self.n = spec, n
        rows = np.array(points(spec, n), dtype=float).reshape(n, -1)
        self.lonlat = spec["crs"] == "lonlat"
        self.surface = self.lonlat and spec.get("height", "surface") == "surface"
        if self.lonlat:
            self.rows = rows
            if self.surface:
                self.matrix = surface_matrix(rows)
                self.p = 2.0
            else:
                h = rows[:, 2] if rows.shape[1] > 2 else np.zeros(n)
                self.coords = (R + h)[:, None] * unit_vectors(rows)
                self.p = 2.0
        else:
            self.coords = rows
            self.p = p_of(spec)
        if not self.surface and n:
            self.tree = cKDTree(self.coords)

    def distance(self, i, j) -> float:
        if self.surface:
            return float(self.matrix[i, j])
        return pair_distance(self.coords[i], self.coords[j], self.p)

    def pairs_within(self, r):
        if self.surface:
            return [(i, j) for i in range(self.n) for j in range(i + 1, self.n)
                    if self.matrix[i, j] <= r]
        found = self.tree.query_pairs(r, p=self.p, output_type="ndarray")
        return sorted((int(i), int(j)) for i, j in found)

    def neighbours(self, i, k):
        if self.surface:
            dist = self.matrix[i]
            idx = np.arange(self.n)
        else:
            dist, idx = self.tree.query(self.coords[i], k=self.n, p=self.p)
            dist, idx = np.atleast_1d(dist), np.atleast_1d(idx)
        ranked = sorted((float(d), int(j)) for d, j in zip(dist, idx) if int(j) != i)
        return ranked[:k]


def edge_lengths(fx, spec):
    m = Model(spec, fx.n)
    return [m.distance(s, t) for s, t in zip(fx.src, fx.tgt)]


def proximity(fx, spec):
    m = Model(spec, fx.n)
    if spec.get("k", 0) > 0:
        out = []
        for i in range(fx.n):
            out += [(float(i), float(j), d) for d, j in m.neighbours(i, spec["k"])]
        return out
    return [(float(i), float(j), m.distance(i, j)) for i, j in m.pairs_within(float(spec["r"]))]


def group_geometry(fx, spec):
    m = Model(spec, fx.n)
    labels = partition(spec["partition"], fx.n)
    out = []
    for g in dict.fromkeys(labels):
        members = [i for i in range(fx.n) if labels[i] == g]
        if m.lonlat:
            u = unit_vectors(m.rows)[members]
            mean = u.mean(axis=0)
            lon = math.degrees(math.atan2(mean[1], mean[0]))
            lat = math.degrees(math.atan2(mean[2], math.hypot(mean[0], mean[1])))
            center = [lon, lat]
            rows = np.vstack([m.rows, [lon, lat] + ([float(m.rows[members, 2].mean())]
                                                    if m.rows.shape[1] > 2 else [])])
            if m.rows.shape[1] > 2:
                center.append(float(m.rows[members, 2].mean()))
            c = len(rows) - 1
            if m.surface:
                local = surface_matrix(rows)
                dists = [float(local[i, c]) for i in members]
            else:
                h = rows[:, 2] if rows.shape[1] > 2 else np.zeros(len(rows))
                coords = (R + h)[:, None] * unit_vectors(rows)
                dists = [pair_distance(coords[i], coords[c], 2.0) for i in members]
        else:
            center = list(m.coords[members].mean(axis=0))
            dists = [pair_distance(m.coords[i], np.array(center), m.p) for i in members]
        d = np.array(dists)
        out.append(tuple([float(len(members))] + [float(c) for c in center]
                         + [float(d.mean()), float(math.sqrt((d * d).mean()))]))
    return out


def evaluate(fx, spec):
    return {"spatial_edge_lengths": edge_lengths, "spatial_proximity": proximity,
            "spatial_group_geometry": group_geometry}[spec["fn"]](fx, spec)


def main() -> int:
    entries = load_area("spatial")
    written = 0
    for name in fixture_names():
        fx = load_fixture(name)
        if fx.n > 400:
            continue
        for variant, spec in entries.items():
            if ORACLE not in spec["oracles"] or not applies(spec, fx):
                continue
            write_values(ORACLE, name, variant, evaluate(fx, spec["params"]))
            written += 1
    write_version(ORACLE, f"scipy {scipy.__version__} (spatial.distance, cKDTree), numpy {np.__version__}")
    print(f"Wrote {written} scipy golden files for spatial.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
