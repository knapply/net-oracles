---
title: "Edge load centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Edge load centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Betweenness, load and flow. Concept id: `edge_load_centrality`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(\mathrm{succ}_t(u)\)</td><td>neighbours \(w\) of \(u\) with \(d(u,w)+d(w,t)=d(u,t)\): the next nodes on shortest paths from \(u\) to \(t\)</td></tr><tr><td>\(f_{st}(u)\)</td><td>share of the unit sent from \(s\) to \(t\) that reaches \(u\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Load on every edge: NetworkX's edge load centrality, over ordered pairs of adjacent nodes.

<div class="formula-block"><p class="formula-name"><strong>Flow reaching a node (Goh et al. 2001)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[f_{st}(s)=1,\qquad f_{st}(w)=\sum_{u:\,w\in\mathrm{succ}_t(u)}\frac{f_{st}(u)}{|\mathrm{succ}_t(u)|}\]</div><p class="formula-where">A unit of flow is sent from \(s\) to \(t\); at every node it is split equally among the next nodes on shortest paths to \(t\).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Edge load</strong> <span class="applies">applies to: edge</span></p><div class="formula">\[\ell(u,w)=\sum_{s\ne t}\ \mathbf 1[w\in\mathrm{succ}_t(u)]\,\frac{f_{st}(u)}{|\mathrm{succ}_t(u)|}\]</div><p class="formula-where">Total flow carried by edge \((u,w)\) over all ordered pairs; the node load is the analogous sum of \(f_{st}(v)\) over \(s,t\ne v\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cx_edge_load">Edge load</a></td><td><code>cx_edge_load</code></td><td>1</td><td>The edge load above for every edge, optionally with the paths limited to a cutoff length.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">No edge; the result is empty.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (single_node).">agrees</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop is never a next step on a shortest path: load 0.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">The definition is stated on nodes and neighbour sets; how parallel edges share a node-level flow is not defined by the definition.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Pairs without a path send no flow.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und).">agrees</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Splitting equally at each node is the definition; it differs from splitting equally among whole shortest paths (betweenness) whenever shortest paths branch and rejoin.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables).">agrees</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Next nodes are those on minimum-total-length paths when weights are lengths.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir).">agrees</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Self-loops</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Edge weights</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## References {#concept-references}

[brandes2001faster](../../references.html#brandes2001faster), [brandes2007centrality](../../references.html#brandes2007centrality), [brandes2008variants](../../references.html#brandes2008variants), [goh2001universal](../../references.html#goh2001universal), [piraveenan2013percolation](../../references.html#piraveenan2013percolation)

## Edge load {#cx_edge_load}

Measure id: `cx_edge_load`. Original family: Centrality.

**Definition.** Load on every edge: NetworkX's edge load centrality, over ordered pairs of adjacent nodes.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>edge_load_centrality</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>cx_edge_load</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nx.edge_load_centrality(G), values for (u, v) and (v, u) of every edge</code></td><td></td></tr><tr><td><code>cx_edge_load_cutoff</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nx.edge_load_centrality(G, cutoff = 2)</code></td><td></td></tr></tbody></table></div>

**References:** [brandes2001faster](../../references.html#brandes2001faster), [brandes2007centrality](../../references.html#brandes2007centrality), [brandes2008variants](../../references.html#brandes2008variants), [goh2001universal](../../references.html#goh2001universal), [piraveenan2013percolation](../../references.html#piraveenan2013percolation)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
