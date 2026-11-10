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

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(\ell(i,j)\)</td><td>distance between located nodes \(i\) and \(j\) (great-circle or Euclidean)</td></tr><tr><td>\(r\)</td><td>search radius</td></tr><tr><td>\(k\)</td><td>number of nearest neighbours</td></tr></tbody></table></div>

## Definition {#concept-definition}

Proximity. Entries grouped here: Proximity.

*Definition partly written:* No primary publication defines these queries; they follow the description of the compared outputs. UCINET's proximity (documented only, never run) is not recorded in detail.

<div class="formula-block"><p class="formula-name"><strong>Proximity within a distance</strong> <span class="applies">applies to: any</span></p><div class="formula">\[E_r=\{\{i,j\}:i&lt;j,\ \ell(i,j)\le r\}\]</div><p class="formula-where">All pairs closer than or at distance \(r\), with their distances.</p></div>

<div class="formula-block"><p class="formula-name"><strong>k nearest neighbours</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\mathrm{kNN}(i)=\text{the }k\text{ nodes }j\ne i\text{ with the smallest }\ell(i,j)\]</div><p class="formula-where">Ties are broken by an ordering rule (node index), which is not part of the definition; defined when \(n&gt;k\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#proximity">Proximity</a></td><td><code>proximity</code></td><td>3</td><td>Pairs within a given distance and the \(k\) nearest other points of each point, from node coordinates.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ucinet.html">UCINET</a></th><th><a href="../../tools/s2.html">s2 (sphere geometry)</a></th><th><a href="../../tools/sf.html">sf (planar geometry)</a></th></tr></thead><tbody><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">With \(n\le k\) a node has fewer than \(k\) other points.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (pair, single_node).">agrees</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (pair, single_node).">agrees</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Equidistant points: the choice among them is not determined by the definition.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables).">agrees</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables).">agrees</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">The node itself is excluded from its own neighbours.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Not applicable: proximity is a function of coordinates.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Too few nodes for the formula</summary><ul><li><strong>s2 (sphere geometry)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (pair, single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li><li><strong>sf (planar geometry)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (pair, single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li><strong>s2 (sphere geometry)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li><li><strong>sf (planar geometry)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Self-loops</summary><ul><li><strong>s2 (sphere geometry)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li><li><strong>sf (planar geometry)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>s2 (sphere geometry)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li><li><strong>sf (planar geometry)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

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
