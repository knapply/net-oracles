---
title: "Maximum branching"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Maximum branching {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Spanning trees and branchings. Concept id: `maximum_branching`. 4 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(w(e)\)</td><td>edge weight</td></tr><tr><td>\(B\subseteq E\)</td><td>arc set with in-degree \(\le1\) at every node and no cycle: a branching</td></tr><tr><td>\(r\)</td><td>root of an arborescence</td></tr></tbody></table></div>

## Definition {#concept-definition}

Optimum branching or spanning arborescence of a directed network (Edmonds), as input edge positions and total weight.

*Definition partly written:* cat\_branching\_dag\_to is known by name only (the branching it builds from a DAG is not specified in the sources).

<div class="formula-block"><p class="formula-name"><strong>Optimum branching (Edmonds 1967; Chu and Liu 1965)</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[B^{*}=\arg\max_{B\ \text{branching}}\sum_{e\in B}w(e),\qquad \text{an arborescence: a branching with }n-1\text{ arcs, every node reachable from }r\]</div><p class="formula-where">A branching is an acyclic arc set with in-degree at most 1; the maximum-weight one is found by contracting cycles (Edmonds, Camerini et al. 1979, Gabow et al. 1986). Arcs of non-positive weight can be left out of a maximum branching (but not out of a spanning arborescence).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Greedy branching</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[\text{add arcs in decreasing weight while in-degree}\le1\text{ and no cycle arises}\]</div><p class="formula-where">A heuristic: it returns a branching but not necessarily one of maximum weight.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#branching">Branching</a></td><td><code>branching</code></td><td>1</td><td>An optimum branching or arborescence (by edge positions) and its total weight.</td></tr><tr><td><a href="#gb_branching_weight">Branching weight</a></td><td><code>gb_branching_weight</code></td><td>1</td><td>The total weight of an optimum branching.</td></tr><tr><td><a href="#cat_branching_dag_to">Dag to branching</a></td><td><code>cat_branching_dag_to</code></td><td>1</td><td>A branching built from a DAG by a documented tool; the sources record only the name.</td></tr><tr><td><a href="#nxs_greedy_branching">Greedy branching</a></td><td><code>nxs_greedy_branching</code></td><td>1</td><td>The greedy heuristic branching, not the optimum.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">The empty branching of weight 0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">The empty branching.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop is a cycle: never in a branching.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">At most one of the parallel arcs into a node can be used: the heaviest.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Equal weights give several optimum branchings with the same total weight.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables).">agrees</span></td></tr><tr><td title="Edges with weight 0."><strong>Zero weights</strong></td><td class="def">A zero-weight arc adds nothing to the weight: optimum branchings may or may not contain it.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Edges with a negative weight."><strong>Negative weights</strong></td><td class="def">A negative arc is left out of a maximum branching; a spanning arborescence may be forced to contain it.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A directed graph in which some node cannot reach another along edge directions although the graph may be weakly connected (not strongly connected)."><strong>Directed graph, unreachable pairs</strong></td><td class="def">A spanning arborescence from \(r\) exists only if every node is reachable from \(r\); a branching always exists.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (gnp_dir_sparse, weighted_dir, multi_loops_dir).">agrees</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Needs a digraph.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense).">agrees</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Self-loops</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Zero weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Negative weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Directed graph, unreachable pairs</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (gnp_dir_sparse, weighted_dir, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## References {#concept-references}

[boruvka1926jistem](../../references.html#boruvka1926jistem), [camerini1979note](../../references.html#camerini1979note), [chu1965shortest](../../references.html#chu1965shortest), [edmonds1967optimum](../../references.html#edmonds1967optimum), [gabow1986efficient](../../references.html#gabow1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kruskal1956shortest](../../references.html#kruskal1956shortest), [prim1957shortest](../../references.html#prim1957shortest)

## Branching {#branching}

Measure id: `branching`. Original family: Traversal, trees and DAGs.

**Definition.** Optimum branching or spanning arborescence of a directed network (Edmonds), as input edge positions and total weight.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>maximum_branching; maximum_spanning_arborescence; minimal_branching; minimum_branching; minimum_spanning_arborescence</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>tree_max_arborescence</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.maximum_spanning_arborescence(M, attr = 'weight').size(weight = 'weight'); -1 on NetworkXException</code></td><td></td></tr><tr><td><code>tree_max_branching</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.maximum_branching(M, attr = 'weight').size(weight = 'weight')</code></td><td></td></tr><tr><td><code>tree_min_arborescence</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.minimum_spanning_arborescence(M, attr = 'weight').size(weight = 'weight'); -1 on NetworkXException</code></td><td></td></tr><tr><td><code>tree_min_branching</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.minimum_branching(M, attr = 'weight').size(weight = 'weight')</code></td><td></td></tr><tr><td><code>tree_minimal_branching</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.algorithms.tree.branchings.minimal_branching(M, attr = 'weight').size(weight = 'weight')</code></td><td></td></tr></tbody></table></div>

**References:** [boruvka1926jistem](../../references.html#boruvka1926jistem), [camerini1979note](../../references.html#camerini1979note), [chu1965shortest](../../references.html#chu1965shortest), [edmonds1967optimum](../../references.html#edmonds1967optimum), [gabow1986efficient](../../references.html#gabow1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kruskal1956shortest](../../references.html#kruskal1956shortest), [prim1957shortest](../../references.html#prim1957shortest)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Branching weight {#gb_branching_weight}

Measure id: `gb_branching_weight`. Original family: Traversal, trees and DAGs.

**Definition.** Branching weight.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>branching_weight</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_branching_weight</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.maximum_branching(M, preserve_attrs=True)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Dag to branching {#cat_branching_dag_to}

Measure id: `cat_branching_dag_to`. Original family: Traversal, trees and DAGs.

**Definition.** Dag to branching.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_branching_dag_to-networkx">details</a></td><td><code>dag_to_branching</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_branching_dag_to-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: dag\_to\_branching.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Greedy branching {#nxs_greedy_branching}

Measure id: `nxs_greedy_branching`. Original family: Graph theory and combinatorics.

**Definition.** Greedy branching.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>greedy_branching</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nxs_greedy_branching_max</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>sorted(greedy_branching(D, attr = 'weight', kind = 'max').edges())</code></td><td></td></tr><tr><td><code>nxs_greedy_branching_min</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>sorted(greedy_branching(D, attr = 'weight', kind = 'min').edges())</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
