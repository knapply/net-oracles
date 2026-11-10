---
title: "Butterflies"
layout: default
parent: "Two-mode and bipartite"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Butterflies {#concept-top}

Family: [Two-mode and bipartite](index.html). Subfamily: Bipartite structure. Concept id: `butterflies`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(U,V\)</td><td>the two node classes of a bipartite graph; every edge joins a node of \(U\) to a node of \(V\)</td></tr><tr><td>\(B\)</td><td>biadjacency matrix, \(B_{uv}=1\) if \(u\in U\) and \(v\in V\) are joined, otherwise 0</td></tr><tr><td>\(N(x)\)</td><td>set of neighbours of node \(x\)</td></tr><tr><td>\(k_x\)</td><td>degree of node \(x\), \(|N(x)|\)</td></tr><tr><td>\(m\)</td><td>number of edges</td></tr><tr><td>\(c(u,w)\)</td><td>number of common neighbours \(|N(u)\cap N(w)|\) of two nodes of one class</td></tr><tr><td>\(b(x)\)</td><td>number of butterflies containing node \(x\)</td></tr><tr><td>\(\bowtie_G\)</td><td>total number of butterflies in the graph</td></tr></tbody></table></div>

## Definition {#concept-definition}

Butterflies (4-cycles) at each node, counted over wedges of the lower-ranked endpoint.

<div class="formula-block"><p class="formula-name"><strong>Butterfly count at a node (Sanei-Mehri et al. 2018)</strong> <span class="applies">applies to: bipartite, simple</span></p><div class="formula">\[b(u)=\sum_{w\ne u,\;w\text{ in the class of }u}\binom{c(u,w)}{2}\]</div><p class="formula-where">A butterfly is a complete bipartite subgraph \(K_{2,2}\), i.e. a 4-cycle. A node \(u\) is in a butterfly with \(w\) of its own class for each pair of common neighbours of \(u\) and \(w\).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Total butterflies</strong> <span class="applies">applies to: bipartite, simple</span></p><div class="formula">\[\bowtie_G=\frac12\sum_{u\in U}b(u)=\frac14\sum_{x\in U\cup V}b(x)\]</div><p class="formula-where">Each butterfly has two nodes in each class, so the node counts add to \(4\bowtie_G\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#butterflies">Butterflies</a></td><td><code>butterflies</code></td><td>1</td><td>Per-node butterfly counts \(b(x)\) for every node, as in the first formula; the total is the second formula.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Not defined on multigraphs: the formula counts pairs of common neighbours of a simple bipartite graph, so parallel edges do not enter \(N(\cdot)\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A self-loop is not an edge between the classes, so a bipartite graph has none.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">All \(c(u,w)=0\), so every \(b(x)=0\) and the total is 0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">Every pair of leaves has one common neighbour, \(c=1\), \(\binom12=0\): no butterfly.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">For the complete bipartite graph \(K_{a,b}\) each node of the class of size \(a\) has \(b(u)=(a-1)\binom{b}{2}\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The node set splits into two classes with edges only between classes (periodic structure; two-mode data)."><strong>Bipartite or two-mode graph</strong></td><td class="def">The domain of the definition.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random).">agrees</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Star</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Bipartite or two-mode graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## References {#concept-references}

[barber2007modularity](../../references.html#barber2007modularity), [estrada2005spectral](../../references.html#estrada2005spectral), [hagberg2008exploring](../../references.html#hagberg2008exploring), [he2017birank](../../references.html#he2017birank), [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [kuhn1955hungarian](../../references.html#kuhn1955hungarian), [lakhal1998polynomial](../../references.html#lakhal1998polynomial), [latapy2008basic](../../references.html#latapy2008basic)

## Butterflies {#butterflies}

Measure id: `butterflies`. Original family: Two-mode and bipartite.

**Definition.** Butterflies (4-cycles) at each node, counted over wedges of the lower-ranked endpoint.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>butterflies</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>butterflies</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.bipartite.butterflies(G)</code></td><td></td></tr></tbody></table></div>

**References:** [barber2007modularity](../../references.html#barber2007modularity), [estrada2005spectral](../../references.html#estrada2005spectral), [hagberg2008exploring](../../references.html#hagberg2008exploring), [he2017birank](../../references.html#he2017birank), [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [kuhn1955hungarian](../../references.html#kuhn1955hungarian), [lakhal1998polynomial](../../references.html#lakhal1998polynomial), [latapy2008basic](../../references.html#latapy2008basic)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
