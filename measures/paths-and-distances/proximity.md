---
title: "Proximity"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Proximity {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Geometry. Concept id: `proximity`. 1 measure.

## Definition {#concept-definition}

Proximity. Entries grouped here: Proximity.

## Proximity {#proximity}

Measure id: `proximity`. Original family: Paths and distances.

**Definition.** Proximity.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-proximity-ucinet) | `Prestige: proximity prestige, rank, domain` | API listing |
| [s2 (sphere geometry)](../../tools/s2.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [sf (planar geometry)](../../tools/sf.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-proximity-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `proximity_knn_lonlat` | s2 (sphere geometry) | any | agrees |  |  | abs 1e-09, rel 1e-12 | `the 3 smallest entries of each row of s2::s2_distance_matrix(points, points, radius = 6371008.7714) except the diagonal, ties by index` |  |
| `proximity_knn_planar` | sf (planar geometry) | any | agrees |  |  | abs 0, rel 1e-12 | `the 3 smallest entries of each row of sf::st_distance(points, points) except the diagonal, ties by index` |  |
| `proximity_within_lonlat` | s2 (sphere geometry) | any | agrees |  |  | abs 1e-09, rel 1e-12 | `pairs i < j from s2::s2_dwithin_matrix(points, points, 3e6, radius = 6371008.7714), distances by s2::s2_distance_matrix` |  |
| `proximity_within_planar` | sf (planar geometry) | any | agrees |  |  | abs 0, rel 1e-12 | `pairs i < j from sf::st_is_within_distance(points, points, dist = 20), distances by sf::st_distance` |  |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [pebesma2018sf](../../references.html#pebesma2018sf), [tool_s2](../../references.html#tool_s2)
{% endraw %}
