---
title: "K-truss"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# K-truss {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Cores, trusses and cohesive blocks. Concept id: `k_truss`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>simple undirected graph (direction ignored, parallel edges merged, loops dropped) with node set \(V\), \(n=|V|\)</td></tr><tr><td>\(\mathrm{sup}_S(e)\)</td><td>support of edge \(e=\{u,v\}\) in the subgraph \(S\): the number of triangles of \(S\) containing it, i.e. \(|N_S(u)\cap N_S(v)|\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

The k-truss: the edges in at least k - 2 triangles of the subgraph, and the nodes they touch.

<div class="formula-block"><p class="formula-name"><strong>k-truss (Wang and Cheng 2012)</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[T_k=\text{the largest subgraph with }\mathrm{sup}_{T_k}(e)\ge k-2\ \ \forall e\in T_k\]</div><p class="formula-where">Every edge of the \(k\)-truss lies in at least \(k-2\) triangles of the truss; the set of nodes is those touched by the surviving edges. Unique for each \(k\) and possibly empty.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Truss number of an edge</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[\tau(e)=\max\{k:e\in T_k\}\]</div><p class="formula-where">The largest \(k\) whose truss contains the edge; at least 2 for every edge of a simple graph.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#k_truss">K truss</a></td><td><code>k_truss</code></td><td>1</td><td>The edges (and nodes touched by them) of the \(k\)-truss \(T_k\) for a given \(k\), on the simple undirected graph.</td></tr><tr><td><a href="#truss">Truss</a></td><td><code>truss</code></td><td>1</td><td>The truss number \(\tau(e)\) of every edge of the simple undirected graph.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">No edges: empty truss.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">Empty truss for \(k\ge2\).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td></tr><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">Fewer than \(k\) nodes cannot hold a \(k\)-truss (a \(k\)-truss has at least \(k\) nodes).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (pair, single_node).">agrees</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Dropped: a loop is not in any triangle.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Merged: support is a count of triangles, not of edge multiplicity.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Direction ignored.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense).">agrees</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">Every edge has support \(n-2\): the \(n\)-truss is the whole graph, \(\tau(e)=n\).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir).">agrees</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">No triangles: only \(k=2\)-truss (all edges) exists.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (star8).">agrees</span></td></tr><tr><td title="The node set splits into two classes with edges only between classes (periodic structure; two-mode data)."><strong>Bipartite or two-mode graph</strong></td><td class="def">No triangles: \(\tau(e)=2\).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random).">agrees</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Too few nodes for the formula</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (pair, single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Self-loops</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Complete graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Star</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (star8). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Bipartite or two-mode graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## References {#concept-references}

[batagelj2003algorithm](../../references.html#batagelj2003algorithm), [carmi2007model](../../references.html#carmi2007model), [goltsev2006k](../../references.html#goltsev2006k), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hebertdufresne2016multi](../../references.html#hebertdufresne2016multi), [seidman1983network](../../references.html#seidman1983network), [wang2012truss](../../references.html#wang2012truss)

## K truss {#k_truss}

Measure id: `k_truss`. Original family: Cohesion and subgroups.

**Definition.** The k-truss: the edges in at least k - 2 triangles of the subgraph, and the nodes they touch.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>k_truss</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>k_truss_3_edges</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.k_truss(G, 3), G the simple undirected graph without loops: the fixture edges whose pair it keeps</code></td><td></td></tr><tr><td><code>k_truss_3_nodes</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.k_truss(G, 3), G the simple undirected graph without loops: its nodes</code></td><td></td></tr><tr><td><code>k_truss_4_edges</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.k_truss(G, 4), G the simple undirected graph without loops: the fixture edges whose pair it keeps</code></td><td></td></tr><tr><td><code>k_truss_4_nodes</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.k_truss(G, 4), G the simple undirected graph without loops: its nodes</code></td><td></td></tr></tbody></table></div>

**References:** [batagelj2003algorithm](../../references.html#batagelj2003algorithm), [carmi2007model](../../references.html#carmi2007model), [goltsev2006k](../../references.html#goltsev2006k), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hebertdufresne2016multi](../../references.html#hebertdufresne2016multi), [seidman1983network](../../references.html#seidman1983network), [wang2012truss](../../references.html#wang2012truss)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Truss {#truss}

Measure id: `truss`. Original family: Cohesion and subgroups.

**Definition.** Truss number of every edge: the largest k whose k-truss contains it.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>truss_numbers</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>the largest k with the edge in nx.k_truss(G, k), G the simple undirected graph without loops (0 for loops)</code></td><td></td></tr></tbody></table></div>

**References:** [batagelj2003algorithm](../../references.html#batagelj2003algorithm), [carmi2007model](../../references.html#carmi2007model), [goltsev2006k](../../references.html#goltsev2006k), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hebertdufresne2016multi](../../references.html#hebertdufresne2016multi), [seidman1983network](../../references.html#seidman1983network), [wang2012truss](../../references.html#wang2012truss)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
