---
title: "Lowest common ancestor in DAGs"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Lowest common ancestor in DAGs {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `dag_lca`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(\mathrm{anc}(v)\)</td><td>ancestors of \(v\) including \(v\) itself</td></tr><tr><td>\(\mathrm{LCA}(u,v)\)</td><td>set of lowest common ancestors</td></tr></tbody></table></div>

## Definition {#concept-definition}

Lowest common ancestor of each node pair in a DAG; pairs with no common ancestor get the none mark u32::MAX.

<div class="formula-block"><p class="formula-name"><strong>Lowest common ancestors in a DAG (Aho, Hopcroft and Ullman 1976; Bender et al. 2005)</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[\mathrm{LCA}(u,v)=\{a\in\mathrm{anc}(u)\cap\mathrm{anc}(v):\ \text{no }b\in\mathrm{anc}(u)\cap\mathrm{anc}(v),\ b\neq a,\ a\leadsto b\}\]</div><p class="formula-where">The common ancestors that are not an ancestor of another common ancestor. In a DAG this set can have more than one element (unlike in a tree), so a single answer needs a choice rule.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#dag_lca">Dag lca</a></td><td><code>dag_lca</code></td><td>1</td><td>One lowest common ancestor for each pair, or a none mark when the pair has no common ancestor.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">\(\mathrm{LCA}(u,u)=\{u\}\).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (single_node).">agrees</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">No common ancestor: \(\mathrm{LCA}\) is empty, so there is no answer.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und).">agrees</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">\(|\mathrm{LCA}|&gt;1\): every member is a correct answer, so which one a tool returns is a convention.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables).">agrees</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Needs a DAG; ancestors follow arcs backwards.</td><td><a class="st st-w st-conv" href="#why-dag_lca-networkx" title="When a pair has several lowest common ancestors NetworkX starts its walk from the first common ancestor in Python&#x27;s set order and the reference from the one of smallest index, so they can return different, equally valid ancestors (checked pair by pair on the corpus: every differing answer of both is a lowest common ancestor). dag_lca_check confirms every reference answer.">differs</a></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>NetworkX</strong>: differs. When a pair has several lowest common ancestors NetworkX starts its walk from the first common ancestor in Python's set order and the reference from the one of smallest index, so they can return different, equally valid ancestors (checked pair by pair on the corpus: every differing answer of both is a lowest common ancestor). dag_lca_check confirms every reference answer. <em>(conventions.json dag_lca / dag_lca)</em></li></ul></details></div>

## References {#concept-references}

[aho1972transitive](../../references.html#aho1972transitive), [aho1976finding](../../references.html#aho1976finding), [bender2005lowest](../../references.html#bender2005lowest), [cooper2001simple](../../references.html#cooper2001simple), [cytron1991efficiently](../../references.html#cytron1991efficiently), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kahn1962topological](../../references.html#kahn1962topological), [knuth1974structured](../../references.html#knuth1974structured)

## Dag lca {#dag_lca}

Measure id: `dag_lca`. Original family: Traversal, trees and DAGs.

**Definition.** Lowest common ancestor of each node pair in a DAG; pairs with no common ancestor get the none mark u32::MAX.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (direction and ties): When a pair has several lowest common ancestors NetworkX starts its walk from the first common ancestor in Python's set order and the reference from... <a href="#why-dag_lca-networkx">details</a></td><td><code>lowest_common_ancestor; tree_all_pairs_lowest_common_ancestor</code></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-dag_lca-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (direction and ties) on inputs tagged directed and undirected. When a pair has several lowest common ancestors NetworkX starts its walk from the first common ancestor in Python's set order and the reference from the one of smallest index, so they can return different, equally valid ancestors (checked pair by pair on the corpus: every differing answer of both is a lowest common ancestor). dag\_lca\_check confirms every reference answer. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 11 comparisons differ and 45 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>dag_lca</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>directed, undirected</td><td>direction, ties</td><td>abs 0, rel 0</td><td><code>dict(nx.all_pairs_lowest_common_ancestor(D, pairs)) for every pair u &lt;= v, -1 if absent</code></td><td>When a pair has several lowest common ancestors NetworkX starts its walk from the first common ancestor in Python's set order and the reference from the one of smallest index, so they can return different, equally valid ancestors (checked pair by pair on the corpus: every differing answer of both is a lowest common ancestor). dag_lca_check confirms every reference answer.</td></tr><tr><td><code>dag_lca_check</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>[number of pairs nx.all_pairs_lowest_common_ancestor(D, pairs) answers, 1]</code></td><td></td></tr></tbody></table></div>

**References:** [aho1972transitive](../../references.html#aho1972transitive), [aho1976finding](../../references.html#aho1976finding), [bender2005lowest](../../references.html#bender2005lowest), [cooper2001simple](../../references.html#cooper2001simple), [cytron1991efficiently](../../references.html#cytron1991efficiently), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kahn1962topological](../../references.html#kahn1962topological), [knuth1974structured](../../references.html#knuth1974structured)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
