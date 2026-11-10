---
title: "Graph edit distance"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Graph edit distance {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Isomorphism and subgraph matching. Concept id: `graph_edit_distance`. 2 measures.

## Definition {#concept-definition}

Graph edit distance. Entries grouped here: Ged Walk; Graph edit distance.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_ged_walk">Ged Walk</a></td><td><code>cat_ged_walk</code></td><td>1</td></tr><tr><td><a href="#ged">Graph edit distance</a></td><td><code>ged</code></td><td>2</td></tr></tbody></table></div>

## Ged Walk {#cat_ged_walk}

Measure id: `cat_ged_walk`. Original family: Paths and distances.

**Definition.** Ged Walk.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_ged_walk-networkit">details</a></td><td><code>GedWalk</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_ged_walk-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: GedWalk.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Graph edit distance {#ged}

Measure id: `ged`. Original family: Graph theory and combinatorics.

**Definition.** Graph edit distance.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>graph_edit_distance; optimal_edit_paths; optimize_edit_paths; optimize_graph_edit_distance</code></td><td></td></tr><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-ged-jgrapht">details</a></td><td><code>ZhangShashaTreeEditDistance</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-ged-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: ZhangShashaTreeEditDistance.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ged</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>loops</td><td>self_loops</td><td>abs 0, rel 0</td><td><code>nx.graph_edit_distance(G1, G2) with G2 = ged_pair(fixture)</code></td><td>NetworkX's graph_edit_distance substitutes a self-loop for an ordinary edge at no cost when the loop's node is mapped onto one endpoint ((1, 1) against (0, 1), edit distance 0); the reference and the definition count deleting the loop and inserting the edge (2). exact edit distance is exponential; networks of at most 10 nodes</td></tr><tr><td><code>ged_labels</code></td><td>NetworkX</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.graph_edit_distance(G1, G2, node_match = equal labels, edge_match = equal labels) with G2 = ged_pair(fixture)</code></td><td>exact edit distance is exponential; networks of at most 10 nodes</td></tr><tr><td><code>ged_node_labels</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>loops</td><td>self_loops</td><td>abs 0, rel 0</td><td><code>nx.graph_edit_distance(G1, G2, node_match = equal labels) with G2 = ged_pair(fixture)</code></td><td>NetworkX's graph_edit_distance substitutes a self-loop for an ordinary edge at no cost when the loop's node is mapped onto one endpoint ((1, 1) against (0, 1), edit distance 0); the reference and the definition count deleting the loop and inserting the edge (2). exact edit distance is exponential; networks of at most 10 nodes</td></tr></tbody></table></div>

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f003">F003</a></td><td>NetworkX</td><td>defect</td><td>graph_edit_distance substitutes a self-loop for an ordinary edge at no cost</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
