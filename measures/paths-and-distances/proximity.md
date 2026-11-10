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

*Definition not yet written.*

## Proximity {#proximity}

Measure id: `proximity`. Original family: Paths and distances.

**Definition.** Proximity.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-proximity-ucinet">details</a></td><td><code>Prestige: proximity prestige, rank, domain</code></td><td>API listing</td></tr><tr><td><a href="../../tools/s2.html">s2 (sphere geometry)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/sf.html">sf (planar geometry)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-proximity-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>proximity_knn_lonlat</code></td><td>s2 (sphere geometry)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-12</td><td><code>the 3 smallest entries of each row of s2::s2_distance_matrix(points, points, radius = 6371008.7714) except the diagonal, ties by index</code></td><td></td></tr><tr><td><code>proximity_knn_planar</code></td><td>sf (planar geometry)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-12</td><td><code>the 3 smallest entries of each row of sf::st_distance(points, points) except the diagonal, ties by index</code></td><td></td></tr><tr><td><code>proximity_within_lonlat</code></td><td>s2 (sphere geometry)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-12</td><td><code>pairs i &lt; j from s2::s2_dwithin_matrix(points, points, 3e6, radius = 6371008.7714), distances by s2::s2_distance_matrix</code></td><td></td></tr><tr><td><code>proximity_within_planar</code></td><td>sf (planar geometry)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-12</td><td><code>pairs i &lt; j from sf::st_is_within_distance(points, points, dist = 20), distances by sf::st_distance</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [pebesma2018sf](../../references.html#pebesma2018sf), [tool_s2](../../references.html#tool_s2)
{% endraw %}
