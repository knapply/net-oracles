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

*Definition not yet written.*

## Edge lengths {#edge_lengths}

Measure id: `edge_lengths`. Original family: Paths and distances.

**Definition.** Edge lengths.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/s2.html">s2 (sphere geometry)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/sf.html">sf (planar geometry)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>edge_lengths_lonlat</code></td><td>s2 (sphere geometry)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-12</td><td><code>s2::s2_distance(s2_geog_point(lon, lat) of the two endpoints, radius = 6371008.7714)</code></td><td></td></tr><tr><td><code>edge_lengths_planar</code></td><td>sf (planar geometry)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-12</td><td><code>sf::st_distance(point a, point b, by_element = TRUE) on planar points</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [pebesma2018sf](../../references.html#pebesma2018sf), [tool_s2](../../references.html#tool_s2)
{% endraw %}
