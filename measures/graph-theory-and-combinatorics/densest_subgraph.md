---
title: "Densest subgraph"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Densest subgraph {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Independent sets and approximation. Concept id: `densest_subgraph`. 5 measures.

## Definition {#concept-definition}

Densest subgraph of a simple undirected network by Greedy++ peeling, as the best density and its nodes.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#ap_densest">Densest</a></td><td><code>ap_densest</code></td><td>1</td></tr><tr><td><a href="#cat_density_goldberg_maximum_subgraph">Goldberg Maximum Density Subgraph Algorithm</a></td><td><code>cat_density_goldberg_maximum_subgraph</code></td><td>1</td></tr><tr><td><a href="#cat_base_density_goldberg_maximum_subgraph">Goldberg Maximum Density Subgraph Algorithm Base</a></td><td><code>cat_base_density_goldberg_maximum_subgraph</code></td><td>1</td></tr><tr><td><a href="#cat_density_edge_goldberg_maximum_per_subgraph_weight">Goldberg Maximum Density Subgraph Algorithm Node Weight Per Edge Weight</a></td><td><code>cat_density_edge_goldberg_maximum_per_subgraph_weight</code></td><td>1</td></tr><tr><td><a href="#cat_density_goldberg_maximum_subgraph_weights">Goldberg Maximum Density Subgraph Algorithm Node Weights</a></td><td><code>cat_density_goldberg_maximum_subgraph_weights</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [vazirani2001approximation](../../references.html#vazirani2001approximation), [white2001fast](../../references.html#white2001fast)

## Densest {#ap_densest}

Measure id: `ap_densest`. Original family: Graph theory and combinatorics.

**Definition.** Densest subgraph of a simple undirected network by Greedy++ peeling, as the best density and its nodes.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>densest_subgraph</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ap_densest</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-15</td><td><code>nx.approximation.densest_subgraph(G_sorted, 2, method = 'greedy++'): (density, size)</code></td><td></td></tr></tbody></table></div>

**References:** [baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [vazirani2001approximation](../../references.html#vazirani2001approximation), [white2001fast](../../references.html#white2001fast)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Goldberg Maximum Density Subgraph Algorithm {#cat_density_goldberg_maximum_subgraph}

Measure id: `cat_density_goldberg_maximum_subgraph`. Original family: Inference (QAP, null models).

**Definition.** Goldberg Maximum Density Subgraph Algorithm.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_density_goldberg_maximum_subgraph-jgrapht">details</a></td><td><code>GoldbergMaximumDensitySubgraphAlgorithm</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_density_goldberg_maximum_subgraph-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: GoldbergMaximumDensitySubgraphAlgorithm.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Goldberg Maximum Density Subgraph Algorithm Base {#cat_base_density_goldberg_maximum_subgraph}

Measure id: `cat_base_density_goldberg_maximum_subgraph`. Original family: Inference (QAP, null models).

**Definition.** Goldberg Maximum Density Subgraph Algorithm Base.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_base_density_goldberg_maximum_subgraph-jgrapht">details</a></td><td><code>GoldbergMaximumDensitySubgraphAlgorithmBase</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_base_density_goldberg_maximum_subgraph-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: GoldbergMaximumDensitySubgraphAlgorithmBase.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Goldberg Maximum Density Subgraph Algorithm Node Weight Per Edge Weight {#cat_density_edge_goldberg_maximum_per_subgraph_weight}

Measure id: `cat_density_edge_goldberg_maximum_per_subgraph_weight`. Original family: Inference (QAP, null models).

**Definition.** Goldberg Maximum Density Subgraph Algorithm Node Weight Per Edge Weight.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_density_edge_goldberg_maximum_per_subgraph_weight-jgrapht">details</a></td><td><code>GoldbergMaximumDensitySubgraphAlgorithmNodeWeightPerEdgeWeight</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_density_edge_goldberg_maximum_per_subgraph_weight-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: GoldbergMaximumDensitySubgraphAlgorithmNodeWeightPerEdgeWeight.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Goldberg Maximum Density Subgraph Algorithm Node Weights {#cat_density_goldberg_maximum_subgraph_weights}

Measure id: `cat_density_goldberg_maximum_subgraph_weights`. Original family: Inference (QAP, null models).

**Definition.** Goldberg Maximum Density Subgraph Algorithm Node Weights.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_density_goldberg_maximum_subgraph_weights-jgrapht">details</a></td><td><code>GoldbergMaximumDensitySubgraphAlgorithmNodeWeights</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_density_goldberg_maximum_subgraph_weights-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: GoldbergMaximumDensitySubgraphAlgorithmNodeWeights.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
