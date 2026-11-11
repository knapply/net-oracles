---
title: "Small-world quotient"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Small-world quotient {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Clustering and transitivity. Concept id: `small_world_index`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(C,\;L\)</td><td>average clustering and characteristic (mean shortest-path) path length of the graph, over connected pairs</td></tr><tr><td>\(C_r,\;L_r\)</td><td>the same for an equivalent random graph (degree-preserving randomization, Maslov and Sneppen 2002)</td></tr><tr><td>\(C_\ell\)</td><td>clustering of an equivalent lattice graph</td></tr></tbody></table></div>

## Definition {#concept-definition}

Small-world coefficient omega of a connected undirected network against random and lattice references (Telesford et al.).

<div class="formula-block"><p class="formula-name"><strong>Small-world coefficient sigma (Humphries and Gurney 2008)</strong> <span class="applies">applies to: connected, undirected</span></p><div class="formula">\[\sigma=\frac{C/C_r}{L/L_r}\]</div><p class="formula-where">Small-world when \(\sigma&gt;1\). The random reference is a stochastic ensemble average, so values depend on the randomization.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Small-world coefficient omega (Telesford et al. 2011)</strong> <span class="applies">applies to: connected, undirected</span></p><div class="formula">\[\omega=\frac{L_r}{L}-\frac{C}{C_\ell}\]</div><p class="formula-where">Near 0 for a small world, towards \(-1\) lattice-like, towards \(+1\) random-like. Needs a lattice reference.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Observed ingredients (Watts and Strogatz 1998)</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[C=\bar C,\qquad L=\frac{1}{|P|}\sum_{(s,t)\in P}d(s,t)\]</div><p class="formula-where">The observed clustering and mean distance over the set \(P\) of connected ordered pairs \(s\ne t\), the two inputs of both coefficients.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#small_world">Small world</a></td><td><code>small_world</code></td><td>1</td><td>The coefficient \(\omega\) of Telesford et al. computed from the observed values and random and lattice references.</td></tr><tr><td><a href="#small_world_observed">Small world observed</a></td><td><code>small_world_observed</code></td><td>2</td><td>Only the observed pair (clustering, mean distance over connected pairs) of the simple undirected reading, without a random or lattice reference.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/igraph.html">igraph (R)</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">No clustering or distances: not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td></tr><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">A degree-preserving swap involves four nodes, so with fewer the random reference cannot differ from the graph, and the lattice reference needs enough nodes: the references are not meaningful.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (pair, single_node).">agrees</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">\(L\) is over connected pairs only for the observed values; \(\sigma\) and \(\omega\) are stated for connected graphs, so not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und).">agrees</span></td></tr><tr><td title="The node set splits into two classes with edges only between classes (periodic structure; two-mode data)."><strong>Bipartite or two-mode graph</strong></td><td class="def">No triangles, so \(C=0\) and, for a triangle-free graph, \(C_r=0\) as well: the ratio \(C/C_r\) is 0/0 and \(\sigma\) is not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random).">agrees</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">No rewiring changes a complete graph: \(C=C_r=1\) and \(L=L_r=1\), so \(\sigma=1\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir).">agrees</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">No swap of two edges yields a different graph, so a random reference with a different edge set does not exist.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (star8).">agrees</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">The ensemble size and the number of swaps per edge are parameters; the coefficient is an estimate whose value varies with them and with the random seed.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li><strong>igraph (R)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Too few nodes for the formula</summary><ul><li><strong>igraph (R)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (pair, single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>igraph (R)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Bipartite or two-mode graph</summary><ul><li><strong>igraph (R)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Complete graph</summary><ul><li><strong>igraph (R)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Star</summary><ul><li><strong>igraph (R)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (star8). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[colizza2006detecting](../../references.html#colizza2006detecting), [erdos2010simple](../../references.html#erdos2010simple), [hagberg2008exploring](../../references.html#hagberg2008exploring), [humphries2008network](../../references.html#humphries2008network), [maslov2002specificity](../../references.html#maslov2002specificity), [sporns2004small](../../references.html#sporns2004small), [telesford2011ubiquity](../../references.html#telesford2011ubiquity), [zhou2004rich](../../references.html#zhou2004rich)

## Small world {#small_world}

Measure id: `small_world`. Original family: Generators and rewiring.

**Definition.** Small-world coefficient omega of a connected undirected network against random and lattice references (Telesford et al.).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>omega; sigma</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>small_world_omega</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td></td><td>defaults, normalization</td><td>abs 0.05, rel 0</td><td><code>mean of nx.omega(G, niter = 2, nrand = 10, seed = s) over s = 0..9; -1 where it raises (disconnected graphs)</code></td><td>As for small_world_sigma; on path10 every clustering coefficient is 0, so NetworkX divides 0 by 0 and raises ZeroDivisionError, where the reference returns NaN.</td></tr><tr><td><code>small_world_sigma</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td></td><td>ties</td><td>abs 0.15, rel 0</td><td><code>mean of nx.sigma(G, niter = 20, nrand = 20, seed = s) over s = 0..9; -1 where it raises (disconnected graphs)</code></td><td>The means over random graphs are compared on the small networks only, to keep the NetworkX oracle fast; on a star NetworkX's random_reference redraws forever (every draw is rejected), where the reference stops each round after 100 (m + 1) rejected draws.</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/rewiring.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/rewiring.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**References:** [colizza2006detecting](../../references.html#colizza2006detecting), [erdos2010simple](../../references.html#erdos2010simple), [hagberg2008exploring](../../references.html#hagberg2008exploring), [humphries2008network](../../references.html#humphries2008network), [maslov2002specificity](../../references.html#maslov2002specificity), [sporns2004small](../../references.html#sporns2004small), [telesford2011ubiquity](../../references.html#telesford2011ubiquity), [zhou2004rich](../../references.html#zhou2004rich)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Small world observed {#small_world_observed}

Measure id: `small_world_observed`. Original family: Descriptive statistics.

**Definition.** Small world observed.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>small_world_observed</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-15, rel 1e-13</td><td><code>nx.transitivity and the mean of nx.shortest_path_length over connected pairs (simple undirected graph)</code></td><td></td></tr><tr><td><code>small_world_observed</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-15, rel 1e-13</td><td><code>igraph::transitivity(type = 'global') and mean_distance(unconnected = TRUE) on simplify(as_undirected(g))</code></td><td></td></tr><tr><td><code>small_world_observed_local</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-15, rel 1e-13</td><td><code>nx.average_clustering and the mean of nx.shortest_path_length over connected pairs</code></td><td></td></tr><tr><td><code>small_world_observed_local</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-15, rel 1e-13</td><td><code>igraph::transitivity(type = 'average', isolates = 'zero') and mean_distance(unconnected = TRUE)</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/groups.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/groups.yaml); [harness/golden/igraph/](https://github.com/knapply/net-oracles/tree/main/harness/golden/igraph/); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
