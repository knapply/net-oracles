---
title: "Group geometry"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Group geometry {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Geometry. Concept id: `group_geometry`. 1 measure.

## Definition {#concept-definition}

Group geometry. Entries grouped here: Group geometry.

## Group geometry {#group_geometry}

Measure id: `group_geometry`. Original family: Paths and distances.

**Definition.** Group geometry.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [s2 (sphere geometry)](../../tools/s2.html) | ✓ checked, agrees |  |  |
| [sf (planar geometry)](../../tools/sf.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `group_geometry_lonlat` | s2 (sphere geometry) | any | agrees |  |  | abs 1e-09, rel 1e-12 | `size, s2::s2_centroid_agg(group points) as longitude and latitude, mean and root-mean-square of s2::s2_distance(member, centroid, radius = 6371008.7714)` |  |
| `group_geometry_planar` | sf (planar geometry) | any | agrees |  |  | abs 1e-12, rel 1e-12 | `size, sf::st_centroid(st_union(group points)), mean and root-mean-square of sf::st_distance(member, centroid)` |  |

**Tools cited:** [pebesma2018sf](../../references.html#pebesma2018sf), [tool_s2](../../references.html#tool_s2)
{% endraw %}
