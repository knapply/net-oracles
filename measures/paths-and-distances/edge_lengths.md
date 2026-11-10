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

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\((\lambda_i,\varphi_i)\)</td><td>longitude and latitude of node \(i\) in radians (geographic data)</td></tr><tr><td>\((x_i,y_i)\)</td><td>planar coordinates of node \(i\)</td></tr><tr><td>\(R\)</td><td>sphere radius (6 371 008.7714 m in the compared outputs)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Edge lengths (geometry). Entries grouped here: Edge lengths.

<div class="formula-block"><p class="formula-name"><strong>Great-circle length (haversine form, Sinnott 1984)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\ell_{ij}=2R\arcsin\sqrt{\sin^2\frac{\varphi_j-\varphi_i}{2}+\cos\varphi_i\cos\varphi_j\sin^2\frac{\lambda_j-\lambda_i}{2}}\]</div><p class="formula-where">Length of the arc on a sphere between the endpoints; equal to the other great-circle formulas (Vincenty's atan2 form on a sphere) up to rounding.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Planar length</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\ell_{ij}=\sqrt{(x_i-x_j)^2+(y_i-y_j)^2}\]</div><p class="formula-where">Euclidean distance between the endpoints.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#edge_lengths">Edge lengths</a></td><td><code>edge_lengths</code></td><td>2</td><td>The length of each edge from its endpoints' coordinates: great-circle on a sphere for longitude and latitude, Euclidean for planar coordinates.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/s2.html">s2 (sphere geometry)</a></th><th><a href="../../tools/sf.html">sf (planar geometry)</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">No edges: no lengths.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">No edges: no lengths.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Both endpoints coincide: length 0.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Parallel edges have equal length.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Lengths are symmetric.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense).">agrees</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense).">agrees</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li><strong>s2 (sphere geometry)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li><li><strong>sf (planar geometry)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Self-loops</summary><ul><li><strong>s2 (sphere geometry)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li><li><strong>sf (planar geometry)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>s2 (sphere geometry)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li><li><strong>sf (planar geometry)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>s2 (sphere geometry)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li><li><strong>sf (planar geometry)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## Edge lengths {#edge_lengths}

Measure id: `edge_lengths`. Original family: Paths and distances.

**Definition.** Edge lengths.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/s2.html">s2 (sphere geometry)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/sf.html">sf (planar geometry)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>edge_lengths_lonlat</code></td><td>s2 (sphere geometry)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-12</td><td><code>s2::s2_distance(s2_geog_point(lon, lat) of the two endpoints, radius = 6371008.7714)</code></td><td></td></tr><tr><td><code>edge_lengths_planar</code></td><td>sf (planar geometry)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-12</td><td><code>sf::st_distance(point a, point b, by_element = TRUE) on planar points</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [pebesma2018sf](../../references.html#pebesma2018sf), [tool_s2](../../references.html#tool_s2)
{% endraw %}
