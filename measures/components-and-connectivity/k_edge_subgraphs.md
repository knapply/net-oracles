---
title: "K-edge subgraphs"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# K-edge subgraphs {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connected components. Concept id: `k_edge_subgraphs`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\), \(m=|E|\); every edge has a source and a target (the ends of an undirected edge are interchangeable)</td></tr><tr><td>\(\lambda(H)\)</td><td>edge connectivity of a subgraph \(H\) on its own</td></tr></tbody></table></div>

## Definition {#concept-definition}

K-edge subgraphs. Entries grouped here: K edge subgraphs.

<div class="formula-block"><p class="formula-name"><strong>Maximal k-edge-connected subgraphs (Zhou et al. 2012)</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[H\text{ is a maximal subgraph with }\lambda(H)\ge k\]</div><p class="formula-where">Connectivity is measured inside the subgraph, so, unlike the k-edge-connected components, the connecting paths must stay in the subgraph; the subgraphs are node-disjoint, and every one is contained in a \(k\)-edge-connected component.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#gb_k_edge_subgraphs">K edge subgraphs</a></td><td><code>gb_k_edge_subgraphs</code></td><td>1</td><td>The maximal subgraphs (as node sets) with internal edge connectivity at least \(k\) (\(k=2\) compared).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">None.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">One node (a trivial subgraph).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">Singletons.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Irrelevant.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Multigraphs: edge connectivity counts parallel edges.</td><td><span class="st st-w st-nov" title="NetworkX&#x27;s k_edge_subgraphs rejects multigraphs.">no value</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Defined on the undirected graph.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">The whole graph for \(k\le n-1\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: no value. NetworkX's k_edge_subgraphs rejects multigraphs. <em>(conventions.json gb_k_edge_subgraphs / gb_k_edge_subgraphs)</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details></div>

## K edge subgraphs {#gb_k_edge_subgraphs}

Measure id: `gb_k_edge_subgraphs`. Original family: Traversal, trees and DAGs.

**Definition.** K edge subgraphs.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>k_edge_subgraphs</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_k_edge_subgraphs</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 0, rel 0</td><td><code>nx.k_edge_subgraphs(G, 2)</code></td><td>NetworkX's k_edge_subgraphs rejects multigraphs.</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/traversal_b.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/traversal_b.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
