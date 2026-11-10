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

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(S\)</td><td>a group of \(m\) located nodes</td></tr><tr><td>\(c\)</td><td>centroid of the group: the mean coordinate (planar) or the geographic midpoint, the normalized mean of the unit vectors (longitude and latitude)</td></tr><tr><td>\(\ell(i,c)\)</td><td>distance from node \(i\) to the centroid: Euclidean or great-circle</td></tr></tbody></table></div>

## Definition {#concept-definition}

Group geometry. Entries grouped here: Group geometry.

*Definition partly written:* No primary publication defines these summaries; the definitions follow the description of the compared outputs (size, centroid, mean and root-mean-square distance from the centroid per group).

<div class="formula-block"><p class="formula-name"><strong>Group geometry</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\bar\ell=\frac1m\sum_{i\in S}\ell(i,c),\qquad \ell_{\mathrm{rms}}=\sqrt{\frac1m\sum_{i\in S}\ell(i,c)^2}\]</div><p class="formula-where">Size \(m\), centroid, mean distance and root-mean-square distance from the centroid. Defined for \(m\ge1\); for a geographic group the mean unit vector can be 0 (antipodal points), when the midpoint is not defined.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#group_geometry">Group geometry</a></td><td><code>group_geometry</code></td><td>2</td><td>Per group: size, centroid, mean distance and root-mean-square distance of the members from the centroid.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/s2.html">s2 (sphere geometry)</a></th><th><a href="../../tools/sf.html">sf (planar geometry)</a></th></tr></thead><tbody><tr><td title="A group, source set, target set or sample that is empty, a single node, or the whole node set."><strong>Degenerate group or subset input</strong></td><td class="def">An empty group has no centroid; a single node has distance 0 to its own centroid.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Degenerate group or subset input</summary><ul><li>No tool entries.</li></ul></details></div>

## Group geometry {#group_geometry}

Measure id: `group_geometry`. Original family: Paths and distances.

**Definition.** Group geometry.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/s2.html">s2 (sphere geometry)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/sf.html">sf (planar geometry)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>group_geometry_lonlat</code></td><td>s2 (sphere geometry)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-12</td><td><code>size, s2::s2_centroid_agg(group points) as longitude and latitude, mean and root-mean-square of s2::s2_distance(member, centroid, radius = 6371008.7714)</code></td><td></td></tr><tr><td><code>group_geometry_planar</code></td><td>sf (planar geometry)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>size, sf::st_centroid(st_union(group points)), mean and root-mean-square of sf::st_distance(member, centroid)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [pebesma2018sf](../../references.html#pebesma2018sf), [tool_s2](../../references.html#tool_s2)
{% endraw %}
