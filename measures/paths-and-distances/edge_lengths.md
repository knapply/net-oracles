---
title: "Edge lengths (geometry)"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Edge lengths (geometry) {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Geometry. Concept id: `edge_lengths`. 1 measure.

## Definition {#concept-definition}

Edge lengths (geometry). Entries grouped here: Edge lengths.

## Edge lengths {#edge_lengths}

Measure id: `edge_lengths`. Original family: Paths and distances.

**Definition.** Edge lengths.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [s2 (sphere geometry)](../../tools/s2.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [sf (planar geometry)](../../tools/sf.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `edge_lengths_lonlat` | s2 (sphere geometry) | any | agrees |  |  | abs 1e-09, rel 1e-12 | `s2::s2_distance(s2_geog_point(lon, lat) of the two endpoints, radius = 6371008.7714)` |  |
| `edge_lengths_planar` | sf (planar geometry) | any | agrees |  |  | abs 0, rel 1e-12 | `sf::st_distance(point a, point b, by_element = TRUE) on planar points` |  |

**Tools cited:** [pebesma2018sf](../../references.html#pebesma2018sf), [tool_s2](../../references.html#tool_s2)
{% endraw %}
