---
title: "Number of spanning trees"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Number of spanning trees {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Spanning trees and branchings. Concept id: `spanning_tree_count`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(L\)</td><td>Laplacian \(D-A\)</td></tr><tr><td>\(\tau(G)\)</td><td>number of spanning trees</td></tr><tr><td>\(L_{(r)}\)</td><td>\(L\) with row and column \(r\) removed</td></tr><tr><td>\(L^{\text{out}}_{(r)}\)</td><td>out-degree Laplacian \(D_{\text{out}}-A\) with row and column \(r\) removed</td></tr></tbody></table></div>

## Definition {#concept-definition}

Number of spanning trees (arborescences rooted at the root for a directed network) by the matrix-tree theorem.

<div class="formula-block"><p class="formula-name"><strong>Matrix-tree theorem (Kirchhoff 1847)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\tau(G)=\det L_{(r)}=\frac1n\prod_{i=2}^{n}\mu_i\]</div><p class="formula-where">Any cofactor of the Laplacian; also \(\frac1n\) times the product of the non-zero Laplacian eigenvalues. For a multigraph or weighted graph the Laplacian counts multiplicities, and the determinant is the sum over trees of the product of edge multiplicities (weights).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Directed matrix-tree theorem (Tutte 1948)</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[\tau_r(G)=\det L^{\text{out}}_{(r)}\]</div><p class="formula-where">The number of spanning arborescences oriented towards \(r\) (every node has a path to \(r\); each other node chooses one out-arc). With the in-degree Laplacian \(D_{\text{in}}-A\) the same determinant counts the arborescences oriented away from \(r\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#gb_spanning_trees">Spanning trees</a></td><td><code>gb_spanning_trees</code></td><td>1</td><td>The count \(\tau(G)\) for undirected input, or the number of arborescences rooted at a given node for directed input, as an exact integer.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">\(n=0\): the minor has no rows; the count by the formula is not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">The 0\(\times\)0 determinant is 1: one (empty) spanning tree.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (single_node).">agrees</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">No spanning tree: \(\tau=0\) (the Laplacian has a repeated zero eigenvalue).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und).">agrees</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop is in no tree: it cancels in \(D-A\) when counted once in \(A\) and in \(D\).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Multiplicities multiply: two parallel edges give two choices.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">A weighted count sums the products of the weights of the tree edges (not the number of trees).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">\(\tau(K_n)=n^{n-2}\) (Cayley).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir).">agrees</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">The directed count depends on the root and on the orientation of the arborescence.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Self-loops</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[kirchhoff1847ueber](../../references.html#kirchhoff1847ueber), [tutte1948dissection](../../references.html#tutte1948dissection)

## Spanning trees {#gb_spanning_trees}

Measure id: `gb_spanning_trees`. Original family: Traversal, trees and DAGs.

**Definition.** Number of spanning trees (arborescences rooted at the root for a directed network) by the matrix-tree theorem.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>number_of_spanning_trees</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_spanning_trees</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>nx.number_of_spanning_trees(M)</code></td><td></td></tr></tbody></table></div>

**References:** [kirchhoff1847ueber](../../references.html#kirchhoff1847ueber), [tutte1948dissection](../../references.html#tutte1948dissection)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
