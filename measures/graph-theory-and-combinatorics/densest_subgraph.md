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

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(E(S)\)</td><td>edges with both ends in \(S\)</td></tr><tr><td>\(\rho(S)\)</td><td>density \(|E(S)|/|S|\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Densest subgraph of a simple undirected network by Greedy++ peeling, as the best density and its nodes.

*Definition partly written:* The exact density of the four Goldberg entries (base, node weights, edge weights) is known by name only, and Goldberg's original paper is not among the checked sources; the unweighted objective and Greedy++ are defined.

<div class="formula-block"><p class="formula-name"><strong>Densest subgraph</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\rho^{*}=\max_{\emptyset\ne S\subseteq V}\frac{|E(S)|}{|S|}\]</div><p class="formula-where">The subgraph of maximum average degree divided by 2; solvable exactly by maximum flow, and approximately by greedy peeling.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Greedy++ (Boob et al. 2020)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\text{repeat }T\text{ times: peel the node of least load}+\text{degree; load}\mathrel{+}=\text{degree at removal; keep the densest prefix}\]</div><p class="formula-where">Iterated peeling that converges to \(\rho^{*}\) as \(T\) grows; each pass is an approximation with ratio 2 or better.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#ap_densest">Densest</a></td><td><code>ap_densest</code></td><td>1</td><td>The best density found by Greedy++ peeling and its node set, for a simple undirected graph.</td></tr><tr><td><a href="#cat_density_goldberg_maximum_subgraph">Goldberg Maximum Density Subgraph Algorithm</a></td><td><code>cat_density_goldberg_maximum_subgraph</code></td><td>1</td><td>Goldberg maximum-density subgraph; documented only.</td></tr><tr><td><a href="#cat_base_density_goldberg_maximum_subgraph">Goldberg Maximum Density Subgraph Algorithm Base</a></td><td><code>cat_base_density_goldberg_maximum_subgraph</code></td><td>1</td><td>Goldberg maximum-density subgraph, base version; documented only.</td></tr><tr><td><a href="#cat_density_edge_goldberg_maximum_per_subgraph_weight">Goldberg Maximum Density Subgraph Algorithm Node Weight Per Edge Weight</a></td><td><code>cat_density_edge_goldberg_maximum_per_subgraph_weight</code></td><td>1</td><td>Goldberg maximum-density subgraph with node weight per edge weight; documented only.</td></tr><tr><td><a href="#cat_density_goldberg_maximum_subgraph_weights">Goldberg Maximum Density Subgraph Algorithm Node Weights</a></td><td><code>cat_density_goldberg_maximum_subgraph_weights</code></td><td>1</td><td>Goldberg maximum-density subgraph with node weights; documented only.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/jgrapht.html">JGraphT</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">No subgraph; not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">\(\rho^{*}=0\).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">\(\rho^{*}=(n-1)/2\) with \(S=V\).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Several subgraphs reach \(\rho^{*}\): the density is unique, the set is not.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Parallel edges would add to \(|E(S)|\); the entry above is for simple graphs.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Complete graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## References {#concept-references}

[baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [vazirani2001approximation](../../references.html#vazirani2001approximation), [white2001fast](../../references.html#white2001fast)

## Densest {#ap_densest}

Measure id: `ap_densest`. Original family: Graph theory and combinatorics.

**Definition.** Densest subgraph of a simple undirected network by Greedy++ peeling, as the best density and its nodes.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>densest_subgraph</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ap_densest</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-15</td><td><code>nx.approximation.densest_subgraph(G_sorted, 2, method = 'greedy++'): (density, size)</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/approximation.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/approximation.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

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
