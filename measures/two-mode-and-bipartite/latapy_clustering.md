---
title: "Latapy clustering"
layout: default
parent: "Two-mode and bipartite"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Latapy clustering {#concept-top}

Family: [Two-mode and bipartite](index.html). Subfamily: Bipartite structure. Concept id: `latapy_clustering`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(U,V\)</td><td>the two node classes of a bipartite graph; every edge joins a node of \(U\) to a node of \(V\)</td></tr><tr><td>\(B\)</td><td>biadjacency matrix, \(B_{uv}=1\) if \(u\in U\) and \(v\in V\) are joined, otherwise 0</td></tr><tr><td>\(N(x)\)</td><td>set of neighbours of node \(x\)</td></tr><tr><td>\(k_x\)</td><td>degree of node \(x\), \(|N(x)|\)</td></tr><tr><td>\(m\)</td><td>number of edges</td></tr><tr><td>\(N_2(u)\)</td><td>nodes other than \(u\) that share a neighbour with \(u\) (distance two)</td></tr><tr><td>\(cc_\bullet(u,v)\)</td><td>pairwise clustering of \(u\) and \(v\), \(\bullet\in\{\text{dot},\min,\max\}\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Latapy clustering. Entries grouped here: Latapy clustering.

*Definition partly written:* The definition is given from memory of the sum over the nodes at distance two; whether \\(u\\) itself belongs to \\(N(N(u))\\) in the original paper was not checked against its text, so the divisor in the edge cases is stated for nodes other than \\(u\\).

<div class="formula-block"><p class="formula-name"><strong>Pairwise clustering (Latapy, Magnien and Del Vecchio 2008)</strong> <span class="applies">applies to: bipartite, simple</span></p><div class="formula">\[cc_{\mathrm{dot}}(u,v)=\frac{|N(u)\cap N(v)|}{|N(u)\cup N(v)|},\quad cc_{\min}(u,v)=\frac{|N(u)\cap N(v)|}{\min(|N(u)|,|N(v)|)},\quad cc_{\max}(u,v)=\frac{|N(u)\cap N(v)|}{\max(|N(u)|,|N(v)|)}\]</div><p class="formula-where">Three ways to normalize the overlap of the neighbourhoods of two nodes of the same class (Jaccard, overlap relative to the smaller, relative to the larger).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Node clustering</strong> <span class="applies">applies to: bipartite, simple</span></p><div class="formula">\[cc_\bullet(u)=\frac{1}{|N_2(u)|}\sum_{v\in N_2(u)}cc_\bullet(u,v)\]</div><p class="formula-where">Mean pairwise clustering over the nodes at distance two. Defined when \(N_2(u)\ne\emptyset\); a node with no node at distance two has no value from the formula.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#latapy_clustering">Latapy clustering</a></td><td><code>latapy_clustering</code></td><td>1</td><td>Choice of \(\bullet\): dot (Jaccard), min or max overlap; the three modes differ only in the denominator of the pairwise term.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">\(N_2(u)=\emptyset\): the mean has no terms, so the formula gives no value (0/0).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">Every node has \(N_2=\emptyset\); not defined by the formula.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The node set splits into two classes with edges only between classes (periodic structure; two-mode data)."><strong>Bipartite or two-mode graph</strong></td><td class="def">The domain of the definition.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random).">agrees</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">In \(K_{a,b}\) all neighbourhoods of one class coincide, so \(cc_\bullet(u,v)=1\) in all three modes and \(cc_\bullet(u)=1\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">The three modes agree whenever the two neighbourhoods have equal size.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Bipartite or two-mode graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details></div>

## Latapy clustering {#latapy_clustering}

Measure id: `latapy_clustering`. Original family: Two-mode and bipartite.

**Definition.** Latapy clustering.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>latapy_clustering</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>latapy_clustering_dot</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.bipartite.latapy_clustering(G, mode = 'dot')</code></td><td></td></tr><tr><td><code>latapy_clustering_max</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.bipartite.latapy_clustering(G, mode = 'max')</code></td><td></td></tr><tr><td><code>latapy_clustering_min</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.bipartite.latapy_clustering(G, mode = 'min')</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/bipartite_nx.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/bipartite_nx.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
