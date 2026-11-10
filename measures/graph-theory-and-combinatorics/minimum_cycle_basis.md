---
title: "Minimum cycle basis"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Minimum cycle basis {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Cycles. Concept id: `minimum_cycle_basis`. 3 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(\ell(C)\)</td><td>length of a cycle \(C\): its number of edges</td></tr><tr><td>\(c\)</td><td>number of connected components</td></tr><tr><td>\(w(e)\)</td><td>edge weight, 1 when unweighted</td></tr><tr><td>\(w(C)\)</td><td>weight of a cycle, the sum of its edge weights</td></tr></tbody></table></div>

## Definition {#concept-definition}

A minimum cycle basis of an undirected network and the weight of each cycle (de Pina).

<div class="formula-block"><p class="formula-name"><strong>Minimum cycle basis (de Pina 1995; Kavitha et al. 2009)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\mathcal B^{*}=\arg\min_{\mathcal B\ \text{cycle basis}}\sum_{C\in\mathcal B}w(C),\qquad |\mathcal B^{*}|=m-n+c\]</div><p class="formula-where">A basis of the cycle space over GF(2) of least total weight. Cycle weights are the same multiset for every minimum basis (matroid property), so the sorted weights and the total are unique even if the cycles are not.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#gb_mcb_weight">Mcb weight</a></td><td><code>gb_mcb_weight</code></td><td>1</td><td>The total weight of a minimum cycle basis.</td></tr><tr><td><a href="#min_basis">Min basis</a></td><td><code>min_basis</code></td><td>1</td><td>A minimum cycle basis, as cycles; which basis is returned is a tie rule.</td></tr><tr><td><a href="#min_basis_weights">Min basis weights</a></td><td><code>min_basis_weights</code></td><td>1</td><td>The weight of each cycle of a minimum basis (unique as a multiset).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">Empty basis, weight 0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">Empty basis.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">One basis per component.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop is a cycle of its own weight.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Two parallel edges form a cycle of their total weight; two parallel loops, two cycles. A simple graph has neither.</td><td><a class="st st-w st-conv" href="#why-min_basis-networkx" title="NetworkX&#x27;s simple graph merges parallel edges and repeated loops, whose cycles the reference lists after NetworkX&#x27;s basis (the basis of the multigraph has m - n + c cycles).">differs</a></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Several minimum bases; weights are unique.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Edges with weight 0."><strong>Zero weights</strong></td><td class="def">Cycles of weight 0 are allowed and enter the basis first.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Edges with a negative weight."><strong>Negative weights</strong></td><td class="def">Negative weights break the minimality argument (cycle weights can be negative): outside the definition.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Unweighted: cycle lengths.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: differs. NetworkX's simple graph merges parallel edges and repeated loops, whose cycles the reference lists after NetworkX's basis (the basis of the multigraph has m - n + c cycles). <em>(conventions.json cycle_basis / cyc_basis)</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Zero weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Negative weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[depina1995applications](../../references.html#depina1995applications), [dias2013efficient](../../references.html#dias2013efficient), [gupta2021finding](../../references.html#gupta2021finding), [hagberg2008exploring](../../references.html#hagberg2008exploring), [itai1978finding](../../references.html#itai1978finding), [johnson1975finding](../../references.html#johnson1975finding), [kavitha2009cycle](../../references.html#kavitha2009cycle), [kirchhoff1847ueber](../../references.html#kirchhoff1847ueber)

## Mcb weight {#gb_mcb_weight}

Measure id: `gb_mcb_weight`. Original family: Traversal, trees and DAGs.

**Definition.** Mcb weight.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_mcb_weight</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 1e-09, rel 1e-09</td><td><code>total weight of nx.minimum_cycle_basis(G, weight)</code></td><td>NetworkX's minimum_cycle_basis rejects multigraphs.</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Min basis {#min_basis}

Measure id: `min_basis`. Original family: Graph theory and combinatorics.

**Definition.** A minimum cycle basis of an undirected network and the weight of each cycle (de Pina).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (multi-edges): as for cyc_basis. <a href="#why-min_basis-networkx">details</a></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-min_basis-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (multi-edges) on inputs tagged multi\_edges. as for cyc\_basis. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 1 comparisons differ and 18 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>cyc_min_basis_check</code></td><td>NetworkX</td><td>undirected</td><td>differs</td><td>multi_edges</td><td>multi_edges</td><td>abs 0, rel 0</td><td><code>the count and the cycle/independence tests of nx.minimum_cycle_basis(G)</code></td><td>as for cyc_basis</td></tr></tbody></table></div>

**References:** [depina1995applications](../../references.html#depina1995applications), [dias2013efficient](../../references.html#dias2013efficient), [gupta2021finding](../../references.html#gupta2021finding), [hagberg2008exploring](../../references.html#hagberg2008exploring), [itai1978finding](../../references.html#itai1978finding), [johnson1975finding](../../references.html#johnson1975finding), [kavitha2009cycle](../../references.html#kavitha2009cycle), [kirchhoff1847ueber](../../references.html#kirchhoff1847ueber)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Min basis weights {#min_basis_weights}

Measure id: `min_basis_weights`. Original family: Graph theory and combinatorics.

**Definition.** A minimum cycle basis of an undirected network and the weight of each cycle (de Pina).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (multi-edges, self-loops and weights): as for cyc_basis. <a href="#why-min_basis_weights-networkx">details</a></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-min_basis_weights-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (multi-edges, self-loops and weights) on inputs tagged multi\_edges. cyc\_min\_basis\_weights: as for cyc\_basis. cyc\_min\_basis\_weights\_weighted: Two parallel edges form a cycle of their total weight for the reference value and the definition (two parallel loops, two cycles); NetworkX's simple graph keeps one edge per pair and has no such cycle. Mapping: the reference value computed with NetworkX's Graph/DiGraph reading (parallel edges collapse, one self-loop per node kept) agrees with the tool within abs 1e-12, rel 1e-12 on all 1 comparison where the difference occurs. Tolerance before mapping: abs 1e-12, rel 1e-12 (0 means exact equality). 1 comparisons differ and 23 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>cyc_min_basis_weights</code></td><td>NetworkX</td><td>undirected</td><td>differs</td><td>multi_edges</td><td>multi_edges</td><td>abs 1e-12, rel 1e-12</td><td><code>weights of the cycles of nx.minimum_cycle_basis(G)</code></td><td>as for cyc_basis</td></tr><tr><td><code>cyc_min_basis_weights_weighted</code></td><td>NetworkX</td><td>undirected</td><td>differs</td><td>multi_edges</td><td>multi_edges, self_loops, weights</td><td>abs 1e-12, rel 1e-12</td><td><code>weights of the cycles of nx.minimum_cycle_basis(G, weight = 'weight')</code></td><td>Two parallel edges form a cycle of their total weight for the reference and the definition (two parallel loops, two cycles); NetworkX's simple graph keeps one edge per pair and has no such cycle.</td></tr></tbody></table></div>

**References:** [depina1995applications](../../references.html#depina1995applications), [dias2013efficient](../../references.html#dias2013efficient), [gupta2021finding](../../references.html#gupta2021finding), [hagberg2008exploring](../../references.html#hagberg2008exploring), [itai1978finding](../../references.html#itai1978finding), [johnson1975finding](../../references.html#johnson1975finding), [kavitha2009cycle](../../references.html#kavitha2009cycle), [kirchhoff1847ueber](../../references.html#kirchhoff1847ueber)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
