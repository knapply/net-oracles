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

*Definition not yet written.*

## Group geometry {#group_geometry}

Measure id: `group_geometry`. Original family: Paths and distances.

**Definition.** Group geometry.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/s2.html">s2 (sphere geometry)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/sf.html">sf (planar geometry)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>group_geometry_lonlat</code></td><td>s2 (sphere geometry)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-12</td><td><code>size, s2::s2_centroid_agg(group points) as longitude and latitude, mean and root-mean-square of s2::s2_distance(member, centroid, radius = 6371008.7714)</code></td><td></td></tr><tr><td><code>group_geometry_planar</code></td><td>sf (planar geometry)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>size, sf::st_centroid(st_union(group points)), mean and root-mean-square of sf::st_distance(member, centroid)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [pebesma2018sf](../../references.html#pebesma2018sf), [tool_s2](../../references.html#tool_s2)
{% endraw %}
