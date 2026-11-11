---
title: "Bipartite modularity"
layout: default
parent: "Two-mode and bipartite"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Bipartite modularity {#concept-top}

Family: [Two-mode and bipartite](index.html). Subfamily: Bipartite structure. Concept id: `bipartite_modularity`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(U,V\)</td><td>the two node classes of a bipartite graph; every edge joins a node of \(U\) to a node of \(V\)</td></tr><tr><td>\(B\)</td><td>biadjacency matrix, \(B_{uv}=1\) if \(u\in U\) and \(v\in V\) are joined, otherwise 0</td></tr><tr><td>\(N(x)\)</td><td>set of neighbours of node \(x\)</td></tr><tr><td>\(k_x\)</td><td>degree of node \(x\), \(|N(x)|\)</td></tr><tr><td>\(m\)</td><td>number of edges</td></tr><tr><td>\(g_u,h_v\)</td><td>community label of \(u\in U\) and of \(v\in V\)</td></tr><tr><td>\(\delta\)</td><td>1 if the two labels are equal, otherwise 0</td></tr></tbody></table></div>

## Definition {#concept-definition}

Bipartite modularity. Entries grouped here: Bipartite modularity.

<div class="formula-block"><p class="formula-name"><strong>Bipartite modularity (Barber 2007)</strong> <span class="applies">applies to: bipartite, two_mode</span></p><div class="formula">\[Q_B=\frac1m\sum_{u\in U}\sum_{v\in V}\Bigl(B_{uv}-\frac{k_u k_v}{m}\Bigr)\,\delta(g_u,h_v)\]</div><p class="formula-where">Observed minus expected edges inside communities, where the expected number of edges between \(u\) and \(v\) is \(k_uk_v/m\) under the bipartite null model that keeps degrees. Defined for \(m&gt;0\); communities contain nodes of both classes and a node class is fixed by the input.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#bipartite_modularity">Bipartite modularity</a></td><td><code>bipartite_modularity</code></td><td>1</td><td>The single formula above, evaluated for a given assignment of nodes to communities; nothing is optimized.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">Not defined: the factor \(1/m\) and the expected term \(k_uk_v/m\) divide by \(m=0\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A group, source set, target set or sample that is empty, a single node, or the whole node set."><strong>Degenerate group or subset input</strong></td><td class="def">With every node in one community \(\delta\equiv1\) and the double sum is \(m-\sum k_uk_v/m=m-m=0\), so \(Q_B=0\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The node set splits into two classes with edges only between classes (periodic structure; two-mode data)."><strong>Bipartite or two-mode graph</strong></td><td class="def">This is the domain of the definition; each edge joins the two classes.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random).">agrees</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">An isolate has \(k=0\): all its terms are 0, so it changes nothing except through the labels.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Degenerate group or subset input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Bipartite or two-mode graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details></div>

## Bipartite modularity {#bipartite_modularity}

Measure id: `bipartite_modularity`. Original family: Two-mode and bipartite.

**Definition.** Bipartite modularity.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>bipartite_modularity</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.bipartite.modularity(G, blocks, top)</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/bipartite_nx.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/bipartite_nx.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
