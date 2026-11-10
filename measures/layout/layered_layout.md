---
title: "Layered and tree layouts"
layout: default
parent: "Layout"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Layered and tree layouts {#concept-top}

Family: [Layout](index.html). Subfamily: Layout algorithms. Concept id: `layered_layout`. 5 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(L_k\)</td><td>the set of nodes in layer \(k\)</td></tr><tr><td>\(\pi_k(v)\)</td><td>position of node \(v\) within layer \(k\)</td></tr><tr><td>\(N_{k-1}(v)\)</td><td>neighbours of \(v\) in layer \(k-1\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Layered and tree layouts. Entries grouped here: Barycenter Greedy Two Layered Bipartite Layout2 D; Layout tree unrooted; Median Greedy Two Layered Bipartite Layout2 D; Sugiyama layered layout; Two Layered Bipartite Layout2 D.

*Definition partly written:* Only the Sugiyama barycenter ordering rule is written. Reingold-Tilford tree drawing and the two-layer bipartite greedy (barycenter, median) functions are named by the sources only; the layer assignment and crossing-reduction steps of the full method are not written.

<div class="formula-block"><p class="formula-name"><strong>Barycenter ordering (Sugiyama, Tagawa and Toda 1981)</strong> <span class="applies">applies to: any, directed</span></p><div class="formula">\[\operatorname{bary}(v)=\frac{1}{|N_{k-1}(v)|}\sum_{u\in N_{k-1}(v)}\pi_{k-1}(u),\qquad \text{sort }L_k\text{ by }\operatorname{bary}\]</div><p class="formula-where">Within a layer, nodes are ordered by the mean position of their neighbours in the previous layer to reduce edge crossings; sweeps run down and up repeatedly. Defined for nodes with at least one neighbour in the adjacent layer; ties and such nodes need a rule not given by the formula.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#layout_sugiyama">Sugiyama layered layout</a></td><td><code>layout_sugiyama</code></td><td>2</td><td>The layered drawing whose crossing-reduction step uses the barycenter rule above (after layer assignment); ordering ties are broken by an unspecified rule.</td></tr></tbody></table></div>

## Barycenter Greedy Two Layered Bipartite Layout2 D {#cat_barycenter_bipartite_d_greedy_layered_layout2_two}

Measure id: `cat_barycenter_bipartite_d_greedy_layered_layout2_two`. Original family: Layout.

**Definition.** Barycenter Greedy Two Layered Bipartite Layout2 D.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_barycenter_bipartite_d_greedy_layered_layout2_two-jgrapht">details</a></td><td><code>BarycenterGreedyTwoLayeredBipartiteLayout2D</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_barycenter_bipartite_d_greedy_layered_layout2_two-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: BarycenterGreedyTwoLayeredBipartiteLayout2D.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Layout tree unrooted {#cat_layout_tree_unrooted}

Measure id: `cat_layout_tree_unrooted`. Original family: Layout.

**Definition.** Layout tree unrooted.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphlayouts.html">graphlayouts</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: graphlayouts is documented-only in this survey; listed in its documentation. <a href="#why-cat_layout_tree_unrooted-graphlayouts">details</a></td><td><code>layout_tree_unrooted</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_layout_tree_unrooted-graphlayouts"></a>**[graphlayouts](../../tools/graphlayouts.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. graphlayouts (1.2.5) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of graphlayouts 1.2.5: help topics.

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Median Greedy Two Layered Bipartite Layout2 D {#cat_bipartite_d_greedy_layered_layout2_median_two}

Measure id: `cat_bipartite_d_greedy_layered_layout2_median_two`. Original family: Layout.

**Definition.** Median Greedy Two Layered Bipartite Layout2 D.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_bipartite_d_greedy_layered_layout2_median_two-jgrapht">details</a></td><td><code>MedianGreedyTwoLayeredBipartiteLayout2D</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_bipartite_d_greedy_layered_layout2_median_two-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: MedianGreedyTwoLayeredBipartiteLayout2D.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Sugiyama layered layout {#layout_sugiyama}

Measure id: `layout_sugiyama`. Original family: Layout.

**Definition.** Sugiyama layered layout.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-layout_sugiyama-igraph">details</a></td><td><code>layout_with_sugiyama</code></td><td>API listing</td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-layout_sugiyama-pyigraph">details</a></td><td><code>layout_sugiyama</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-layout_sugiyama-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: layout\_with\_sugiyama.
- <a id="why-layout_sugiyama-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: layout\_sugiyama.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Two Layered Bipartite Layout2 D {#cat_bipartite_d_layered_layout2_two}

Measure id: `cat_bipartite_d_layered_layout2_two`. Original family: Layout.

**Definition.** Two Layered Bipartite Layout2 D.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_bipartite_d_layered_layout2_two-jgrapht">details</a></td><td><code>TwoLayeredBipartiteLayout2D</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_bipartite_d_layered_layout2_two-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: TwoLayeredBipartiteLayout2D.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
