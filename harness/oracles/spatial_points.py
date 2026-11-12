"""Coordinates for the spatial entries (manifest/spatial.yaml).

The fixtures carry no coordinates, so the oracles and the engine runner
derive them from the fixture size by this rule, which describes data, not
the measures. The runner (bindings/spatial.py) repeats it.

- Cartesian and planar coordinates are whole numbers in 0..9, one hash per
  axis, so many points coincide and many pairs tie in distance, and every
  distance the oracles compute is exact.
- Every seventh node (v %% 7 == 3) copies the location of node v - 1 (all
  axes), so coincident points exist in every network of four nodes or more.
- Longitude and latitude are hashed as in roles_definition_oracle.py
  (latitude uniform on the sphere); the third coordinate is a height in
  radius units, a multiple of 50000 below 2,000,000. A copied location
  keeps its own height, which is the height of the original plus 100000, so
  a pair at surface distance 0 and height difference exactly 100000 exists.
"""

from __future__ import annotations

import math

EARTH_RADIUS_M = 6371008.7714
SPAN = 10


def hash_unit(v: int, salt: int) -> float:
    """A number in [0, 1) from a node index, in exact integer arithmetic."""
    h = ((v + 1) * 2654435761 + salt * 40503 + 12345) % 4294967296
    h = (h ^ (h >> 13)) * 1274126177 % 4294967296
    return h / 4294967296.0


def source_node(v: int) -> int:
    return v - 1 if (v % 7 == 3 and v > 0) else v


def points(spec: dict, n: int) -> list[list[float]]:
    """One row of `dim` floats per node."""
    crs, dim = spec["crs"], spec.get("dim", 2)
    rows = []
    for v in range(n):
        s = source_node(v)
        if crs == "lonlat":
            row = [360.0 * hash_unit(s, 1) - 180.0,
                   math.degrees(math.asin(2.0 * hash_unit(s, 2) - 1.0))]
            if dim == 3:
                height = float(int(hash_unit(s, 3) * 40) * 50000)
                row.append(height + (100000.0 if s != v else 0.0))
        else:
            row = [float(int(hash_unit(s, axis) * SPAN)) for axis in range(1, dim + 1)]
        rows.append(row)
    return rows


def partition(rule: str, n: int) -> list[int]:
    if rule == "mod3":
        return [v % 3 for v in range(n)]
    if rule == "mod2":
        return [v % 2 for v in range(n)]
    raise ValueError(rule)
