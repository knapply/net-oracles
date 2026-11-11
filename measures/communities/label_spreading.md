---
title: "Label spreading"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Label spreading {#concept-top}

Family: [Communities](index.html). Subfamily: Other detection algorithms. Concept id: `label_spreading`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\); every edge has a source and a target (the ends of an undirected edge are interchangeable)</td></tr><tr><td>\(W\)</td><td>symmetric weight matrix, \(D\) its diagonal degree matrix</td></tr><tr><td>\(Y\)</td><td>\(n\times K\) matrix of initial class indicators for the labelled nodes (0 rows for unlabelled)</td></tr><tr><td>\(S=D^{-1/2}WD^{-1/2}\)</td><td>normalized weight matrix</td></tr><tr><td>\(\alpha\in(0,1)\)</td><td>weight of neighbours against the initial labels</td></tr><tr><td>\(P=D^{-1}W\)</td><td>transition matrix, split into labelled (\(l\)) and unlabelled (\(u\)) blocks</td></tr></tbody></table></div>

## Definition {#concept-definition}

NetworkX's label spreading (harmonic function or local and global consistency): best class of every node and whether it ties.

<div class="formula-block"><p class="formula-name"><strong>Harmonic function (Zhu, Ghahramani and Lafferty 2003)</strong> <span class="applies">applies to: connected, undirected</span></p><div class="formula">\[f_u=(I-P_{uu})^{-1}P_{ul}f_l\]</div><p class="formula-where">Labels of the unlabelled nodes are the weighted average of their neighbours' values with the labelled values fixed; the probability that a random walk first hits each class. Needs every component to contain a labelled node.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Local and global consistency (Zhou et al. 2004)</strong> <span class="applies">applies to: connected, undirected</span></p><div class="formula">\[F^\star=(1-\alpha)(I-\alpha S)^{-1}Y\]</div><p class="formula-where">The fixed point of \(F\leftarrow\alpha SF+(1-\alpha)Y\); the class of node \(v\) is \(\arg\max_kF^\star_{vk}\). When several classes tie, the node is flagged as tied.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#nxo_label_spreading">Label spreading</a></td><td><code>nxo_label_spreading</code></td><td>1</td><td>The best class of every node and whether its top score ties: from the harmonic function (labelled nodes fixed) or from local and global consistency with \(\alpha\) and a fixed number of iterations.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">No propagation: unlabelled nodes keep zero scores.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">An isolate has \(D_{vv}=0\): not defined for the normalized matrix.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty, single_node, two_triangles_isolate, gnp_und_sparse).">agrees</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">A component without a labelled node has no information: scores 0 and the class is undetermined.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und).">agrees</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Equal top scores: the class is not determined by the definition.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables).">agrees</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Weights enter \(W\).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir).">agrees</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(\alpha\) must lie in \((0,1)\) for the inverse to exist; with a fixed iteration count the result is not yet the fixed point.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Isolated nodes</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty, single_node, two_triangles_isolate, gnp_und_sparse). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Edge weights</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Label spreading {#nxo_label_spreading}

Measure id: `nxo_label_spreading`. Original family: Communities.

**Definition.** NetworkX's label spreading (harmonic function or local and global consistency): best class of every node and whether it ties.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>harmonic_function; local_and_global_consistency</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nxo_harmonic_function</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.node_classification.harmonic_function(G), labels (v // 4) % 3 on nodes v % 4 == 0 (graph without weights)</code></td><td></td></tr><tr><td><code>nxo_local_global_weighted</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.node_classification.local_and_global_consistency(G, alpha = 0.9, max_iter = 12)</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/nx_order.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/nx_order.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
