---
title: "Robins-Alexander clustering"
layout: default
parent: "Two-mode and bipartite"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Robins-Alexander clustering {#concept-top}

Family: [Two-mode and bipartite](index.html). Subfamily: Bipartite structure. Concept id: `robins_alexander`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(U,V\)</td><td>the two node classes of a bipartite graph; every edge joins a node of \(U\) to a node of \(V\)</td></tr><tr><td>\(B\)</td><td>biadjacency matrix, \(B_{uv}=1\) if \(u\in U\) and \(v\in V\) are joined, otherwise 0</td></tr><tr><td>\(N(x)\)</td><td>set of neighbours of node \(x\)</td></tr><tr><td>\(k_x\)</td><td>degree of node \(x\), \(|N(x)|\)</td></tr><tr><td>\(m\)</td><td>number of edges</td></tr><tr><td>\(C_4\)</td><td>number of 4-cycles in the graph</td></tr><tr><td>\(L_3\)</td><td>number of paths of length three (three edges, four distinct nodes)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Robins-Alexander clustering. Entries grouped here: Robins alexander.

<div class="formula-block"><p class="formula-name"><strong>Robins-Alexander clustering coefficient (Robins and Alexander 2004)</strong> <span class="applies">applies to: bipartite, simple</span></p><div class="formula">\[CC_{RA}=\frac{4\,C_4}{L_3}\]</div><p class="formula-where">Each 4-cycle contains four 3-paths, so the ratio is the fraction of 3-paths that are closed into a 4-cycle. Defined when \(L_3&gt;0\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#robins_alexander">Robins alexander</a></td><td><code>robins_alexander</code></td><td>1</td><td>A single graph-level coefficient; no node version and no parameter.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">Not defined: \(L_3=0\) so the ratio is 0/0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">Not defined: a star has no path with three edges, \(L_3=0\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">For \(K_{a,b}\) with \(a,b\ge2\) every 3-path closes, so \(CC_{RA}=1\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly two nodes."><strong>Two nodes</strong></td><td class="def">One edge, no 3-path: not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The node set splits into two classes with edges only between classes (periodic structure; two-mode data)."><strong>Bipartite or two-mode graph</strong></td><td class="def">The domain of the definition.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random).">agrees</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Not defined: the 3-path and 4-cycle counts are for simple graphs.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Star</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Two nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Bipartite or two-mode graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details></div>

## Robins alexander {#robins_alexander}

Measure id: `robins_alexander`. Original family: Two-mode and bipartite.

**Definition.** Robins alexander.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>robins_alexander_clustering</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>robins_alexander</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.bipartite.robins_alexander_clustering(G)</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/bipartite_nx.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/bipartite_nx.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
