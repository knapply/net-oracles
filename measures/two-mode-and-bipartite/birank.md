---
title: "BiRank"
layout: default
parent: "Two-mode and bipartite"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# BiRank {#concept-top}

Family: [Two-mode and bipartite](index.html). Subfamily: Bipartite structure. Concept id: `birank`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(U,P\)</td><td>the two node classes</td></tr><tr><td>\(W\)</td><td>\(|U|\times|P|\) matrix of non-negative edge weights between the classes</td></tr><tr><td>\(D_U,D_P\)</td><td>diagonal matrices of the row sums and column sums of \(W\)</td></tr><tr><td>\(S\)</td><td>\(D_U^{-1/2}WD_P^{-1/2}\), the symmetrically normalized weight matrix</td></tr><tr><td>\(\alpha,\beta\)</td><td>damping parameters in \([0,1)\)</td></tr><tr><td>\(u_0,p_0\)</td><td>prior score vectors on \(U\) and \(P\) (query vectors)</td></tr><tr><td>\(u,p\)</td><td>BiRank scores of the two classes</td></tr></tbody></table></div>

## Definition {#concept-definition}

BiRank scores of both node sets of a bipartite graph: the fixed point of damped, normalized propagation between the sets.

<div class="formula-block"><p class="formula-name"><strong>BiRank fixed point (He et al. 2017)</strong> <span class="applies">applies to: bipartite, weighted</span></p><div class="formula">\[p=\alpha\,S^{\top}u+(1-\alpha)\,p_0,\qquad u=\beta\,S\,p+(1-\beta)\,u_0\]</div><p class="formula-where">Scores are the fixed point of damped propagation between the two classes, reached by iterating the two equations alternately. For \(\alpha,\beta&lt;1\) the iteration converges because the spectral radius of \(S\) is at most 1. Defined when every row and column sum of \(W\) is positive (otherwise \(D^{-1/2}\) has a zero on the diagonal).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#birank">Birank</a></td><td><code>birank</code></td><td>1</td><td>One formula; the choice of \(\alpha\), \(\beta\), the priors and the stopping rule decide the output. The fixed point is unique, so iteration count and tolerance only matter for how closely it is approached.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">Not defined: \(D_U\) and \(D_P\) are zero, so \(S\) has no finite entries.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">Not defined for the normalization: a node with zero weighted degree makes \(D^{-1/2}\) infinite.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">For \(\alpha=\beta=1\) the damping vanishes and the fixed point need not be unique; for \(\alpha,\beta\in[0,1)\) it is.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The node set splits into two classes with edges only between classes (periodic structure; two-mode data)."><strong>Bipartite or two-mode graph</strong></td><td class="def">The formula is stated for bipartite input with a given class split.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random).">agrees</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Weights enter through \(W\), then through the normalization \(S\); unit weights give the unweighted score.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details><details><summary>Bipartite or two-mode graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[he2017birank](../../references.html#he2017birank)

## Birank {#birank}

Measure id: `birank`. Original family: Two-mode and bipartite.

**Definition.** BiRank scores of both node sets of a bipartite graph: the fixed point of damped, normalized propagation between the sets.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>birank</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>birank</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.bipartite.birank(G, top, max_iter = 1000, tol = 1e-10)</code></td><td></td></tr></tbody></table></div>

**References:** [he2017birank](../../references.html#he2017birank)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
