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

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\); every edge has a source and a target (the ends of an undirected edge are interchangeable)</td></tr><tr><td>\((A,B)\)</td><td>a bisection of \(V\) into two parts of fixed sizes</td></tr><tr><td>\(D_v\)</td><td>external minus internal cost of \(v\): edge weight to the other part minus to its own part</td></tr><tr><td>\(c_{ab}\)</td><td>weight of the edge \(\{a,b\}\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Graph bisection. Entries grouped here: Greedy node swap bipartition (community); Kernighan lin; Spectral Partitioner.

*Definition partly written:* cat\_partitioner\_spectral (NetworKit) and cat\_bipartition\_greedy\_swap@community (NetworkX) are documented only and were never run; their objectives and options are not recorded in the sources.

<div class="formula-block"><p class="formula-name"><strong>Kernighan-Lin gain (Kernighan and Lin 1970)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[g(a,b)=D_a+D_b-2c_{ab}\]</div><p class="formula-where">Reduction in cut weight when \(a\in A\) and \(b\in B\) are swapped. A pass swaps the pair of largest gain, locks both nodes, and applies the prefix of swaps with the largest total gain; passes repeat until no gain or a pass limit. A local search: it does not guarantee the minimum bisection, and the result depends on the starting partition and tie-breaking.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_bipartition_greedy_swap-community">Greedy node swap bipartition (community)</a></td><td><code>cat_bipartition_greedy_swap@community</code></td><td>1</td><td>Documented for NetworkX as a greedy node-swap bipartition; not recorded in detail.</td></tr><tr><td><a href="#cnx_kernighan_lin">Kernighan lin</a></td><td><code>cnx_kernighan_lin</code></td><td>1</td><td>A bisection improved by the Kernighan-Lin procedure from a given starting partition, with a pass limit and optional weights.</td></tr><tr><td><a href="#cat_partitioner_spectral">Spectral Partitioner</a></td><td><code>cat_partitioner_spectral</code></td><td>1</td><td>Documented for NetworKit as a spectral partitioner; not recorded in detail.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/networkit.html">NetworKit</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">No bisection.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">Cannot bisect one node.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (single_node).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly two nodes."><strong>Two nodes</strong></td><td class="def">One node on each side.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (pair).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">A bisection with cut 0 exists if components fit the sizes.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Never cut.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Add to the cut weight.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Weights are cut costs.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Equal gains: the pair chosen depends on iteration order.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">Part sizes must be fixed (here: halves); the pass limit bounds the effort.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Two nodes</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (pair). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Self-loops</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Edge weights</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

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
