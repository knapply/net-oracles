---
title: "Graph bisection"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Graph bisection {#concept-top}

Family: [Communities](index.html). Subfamily: Graph bisection and partitioning. Concept id: `graph_bisection`. 3 measures.

## Definition {#concept-definition}

Graph bisection. Entries grouped here: Greedy node swap bipartition (community); Kernighan lin; Spectral Partitioner.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_bipartition_greedy_swap-community">Greedy node swap bipartition (community)</a></td><td><code>cat_bipartition_greedy_swap@community</code></td><td>1</td></tr><tr><td><a href="#cnx_kernighan_lin">Kernighan lin</a></td><td><code>cnx_kernighan_lin</code></td><td>1</td></tr><tr><td><a href="#cat_partitioner_spectral">Spectral Partitioner</a></td><td><code>cat_partitioner_spectral</code></td><td>1</td></tr></tbody></table></div>

## Greedy node swap bipartition (community) {#cat_bipartition_greedy_swap-community}

Measure id: `cat_bipartition_greedy_swap@community`. Original family: Generators and rewiring.

**Definition.** Greedy node swap bipartition (community).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_bipartition_greedy_swap-community-networkx">details</a></td><td><code>greedy_node_swap_bipartition</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_bipartition_greedy_swap-community-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: greedy\_node\_swap\_bipartition.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Kernighan lin {#cnx_kernighan_lin}

Measure id: `cnx_kernighan_lin`. Original family: Communities.

**Definition.** Kernighan lin.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>kernighan_lin_bisection</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nx_kernighan_lin</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.community.kernighan_lin_bisection(G_sorted, (first half, rest), max_iter = 10, weight = 'weight' if weighted)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Spectral Partitioner {#cat_partitioner_spectral}

Measure id: `cat_partitioner_spectral`. Original family: Communities.

**Definition.** Spectral Partitioner.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_partitioner_spectral-networkit">details</a></td><td><code>SpectralPartitioner</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_partitioner_spectral-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: SpectralPartitioner.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
