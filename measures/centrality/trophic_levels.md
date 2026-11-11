---
title: "Trophic levels and incoherence"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Trophic levels and incoherence {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `trophic_levels`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(k^{\mathrm{in}}(v),\,k^{\mathrm{out}}(v)\)</td><td>in-degree (edges with target \(v\)) and out-degree (edges with source \(v\)) in a directed graph</td></tr><tr><td>\(A_{ij}\)</td><td>number of edges from \(i\) to \(j\)</td></tr><tr><td>\(s_i\)</td><td>trophic level of node \(i\)</td></tr><tr><td>\(x_{ij}=s_j-s_i\)</td><td>trophic difference along edge \(i\to j\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Trophic incoherence parameter of a directed network: the standard deviation of the trophic differences (Johnson et al.).

<div class="formula-block"><p class="formula-name"><strong>Trophic levels (Levine 1980)</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[s_i=1+\frac{1}{k^{\mathrm{in}}(i)}\sum_{j}A_{ji}\,s_j\quad(k^{\mathrm{in}}(i)&gt;0),\qquad s_i=1\ \text{for basal nodes } (k^{\mathrm{in}}(i)=0)\]</div><p class="formula-where">Level 1 for nodes that receive no edges; otherwise one more than the mean level of the nodes pointing at \(i\). A linear system with a unique solution when every node is reachable from a basal node.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Trophic incoherence (Johnson et al. 2014)</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[q=\sqrt{\frac{\sum_{ij}A_{ij}(x_{ij}-1)^2}{\sum_{ij}A_{ij}}}=\sqrt{\langle x^2\rangle-1}\]</div><p class="formula-where">Standard deviation of the trophic differences around their mean 1; 0 for a perfectly layered (coherent) network.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cx_trophic">Trophic</a></td><td><code>cx_trophic</code></td><td>1</td><td>Trophic levels, trophic differences and the incoherence parameter, as above.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">Level 1; no edges so the incoherence is 0/0.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (single_node).">agrees</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">All nodes basal; incoherence 0/0.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop makes \(i\) its own source: it distorts \(s_i\); the definition assumes no loops (cannibalism needs a convention).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">\(A_{ij}\) counts parallel edges as weights in the sums.</td><td><span class="st st-w st-nov" title="NetworkX&#x27;s trophic_differences unpacks MultiDiGraph edges as pairs and fails on multigraphs.">no value</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Components without a basal node have no unique solution.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und).">agrees</span></td></tr><tr><td title="A directed graph in which some node cannot reach another along edge directions although the graph may be weakly connected (not strongly connected)."><strong>Directed graph, unreachable pairs</strong></td><td class="def">Nodes not reachable from a basal node make the system singular.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (gnp_dir_sparse, weighted_dir, multi_loops_dir).">agrees</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Defined for directed graphs; undirected input has no trophic structure.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense).">agrees</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Edgeless graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Self-loops</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: no value. NetworkX's trophic_differences unpacks MultiDiGraph edges as pairs and fails on multigraphs. <em>(conventions.json cx_trophic / cx_trophic_differences)</em></li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Directed graph, unreachable pairs</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (gnp_dir_sparse, weighted_dir, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## References {#concept-references}

[johnson2014trophic](../../references.html#johnson2014trophic), [levine1980several](../../references.html#levine1980several), [mones2012hierarchy](../../references.html#mones2012hierarchy), [tarjan1972depth](../../references.html#tarjan1972depth)

## Trophic {#cx_trophic}

Measure id: `cx_trophic`. Original family: Centrality.

**Definition.** Trophic incoherence parameter of a directed network: the standard deviation of the trophic differences (Johnson et al.).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>trophic_differences; trophic_incoherence_parameter; trophic_levels</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>cx_trophic_differences</code></td><td>NetworkX</td><td>directed</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>direction, multi_edges</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.trophic_differences(G)[(u, v)] for every edge</code></td><td>NetworkX's trophic_differences unpacks MultiDiGraph edges as pairs and fails on multigraphs.</td></tr><tr><td><code>cx_trophic_incoherence</code></td><td>NetworkX</td><td>directed</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>direction, multi_edges</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.trophic_incoherence_parameter(G)</code></td><td>NetworkX's trophic_differences unpacks MultiDiGraph edges as pairs and fails on multigraphs.</td></tr><tr><td><code>cx_trophic_incoherence_cannibalism</code></td><td>NetworkX</td><td>directed</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>direction, multi_edges</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.trophic_incoherence_parameter(G, cannibalism = True)</code></td><td>NetworkX's trophic_differences unpacks MultiDiGraph edges as pairs and fails on multigraphs.</td></tr><tr><td><code>cx_trophic_levels</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nx.trophic_levels(G) (an error is undefined)</code></td><td></td></tr><tr><td><code>cx_trophic_levels_weighted</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nx.trophic_levels(G, weight = 'weight')</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/centrality_extra.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/centrality_extra.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**References:** [johnson2014trophic](../../references.html#johnson2014trophic), [levine1980several](../../references.html#levine1980several), [mones2012hierarchy](../../references.html#mones2012hierarchy), [tarjan1972depth](../../references.html#tarjan1972depth)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
