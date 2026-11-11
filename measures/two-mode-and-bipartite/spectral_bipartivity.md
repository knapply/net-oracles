---
title: "Spectral bipartivity"
layout: default
parent: "Two-mode and bipartite"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Spectral bipartivity {#concept-top}

Family: [Two-mode and bipartite](index.html). Subfamily: Bipartite structure. Concept id: `spectral_bipartivity`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(A\)</td><td>symmetric adjacency matrix of an undirected graph</td></tr><tr><td>\(\lambda_j,\varphi_j\)</td><td>eigenvalues of \(A\) and the corresponding orthonormal eigenvectors</td></tr><tr><td>\(\varphi_j(i)\)</td><td>component \(i\) of \(\varphi_j\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Spectral bipartivity. Entries grouped here: Spectral bipartivity.

<div class="formula-block"><p class="formula-name"><strong>Spectral bipartivity of a graph (Estrada and Rodriguez-Velazquez 2005)</strong> <span class="applies">applies to: undirected, unweighted</span></p><div class="formula">\[b_s(G)=\frac{\operatorname{tr}\cosh(A)}{\operatorname{tr}\exp(A)}=\frac{\sum_j\cosh\lambda_j}{\sum_j e^{\lambda_j}}\]</div><p class="formula-where">The even-length closed walks (counted by \(\cosh A\)) over all closed walks (counted by \(\exp A\)). It is 1 exactly when the graph is bipartite. Defined when \(n\ge1\).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Spectral bipartivity of a node</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[b_s(i)=\frac{\sum_j\varphi_j(i)^2\cosh\lambda_j}{\sum_j\varphi_j(i)^2e^{\lambda_j}}=\frac{(\cosh A)_{ii}}{(\exp A)_{ii}}\]</div><p class="formula-where">The same ratio for closed walks that start and end at node \(i\); the graph value is the ratio of the sums over all nodes.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#spectral_bipartivity">Spectral bipartivity</a></td><td><code>spectral_bipartivity</code></td><td>1</td><td>Graph value (first formula) or the value of selected nodes (second formula); the same measure, evaluated for all nodes or a subset.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">Not defined: \(\operatorname{tr}\exp(A)\) is an empty sum, 0/0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">\(A=0\), \(\cosh A=\exp A=I\): \(b_s=1\) (an edgeless graph is bipartite).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop adds an odd closed walk (\(A_{ii}&gt;0\)), so \(b_s&lt;1\); a loop-free input is required to read 1 as bipartite.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Defined on the multiplicity matrix \(A\); parallel edges raise the entries and change the value.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">Eigenvalues \(n-1\) once and \(-1\) with multiplicity \(n-1\): \(b_s=\dfrac{\cosh(n-1)+(n-1)\cosh1}{e^{n-1}+(n-1)e^{-1}}\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The node set splits into two classes with edges only between classes (periodic structure; two-mode data)."><strong>Bipartite or two-mode graph</strong></td><td class="def">The spectrum is symmetric (\(\lambda\) and \(-\lambda\) pair up), so \(\sum\sinh\lambda_j=0\) and \(b_s=1\).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random).">agrees</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">The formula uses a symmetric \(A\); for a directed graph the eigen-decomposition is not the one above, so the definition is not stated.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Bipartite or two-mode graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details></div>

## Spectral bipartivity {#spectral_bipartivity}

Measure id: `spectral_bipartivity`. Original family: Two-mode and bipartite.

**Definition.** Spectral bipartivity.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>spectral_bipartivity</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>spectral_bipartivity</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nx.bipartite.spectral_bipartivity(G, nodes = list(G)) and nx.bipartite.spectral_bipartivity(G)</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/bipartite_nx.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/bipartite_nx.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
