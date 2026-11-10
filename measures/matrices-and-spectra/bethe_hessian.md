---
title: "Bethe Hessian"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Bethe Hessian {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Graph matrices. Concept id: `bethe_hessian`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(A=(a_{uv})\)</td><td>adjacency matrix: \(a_{uv}\) is the number of edges from \(u\) to \(v\) (the sum of their weights when weighted)</td></tr><tr><td>\(D=\operatorname{diag}(d_1,\dots,d_n)\)</td><td>degree matrix, \(d_u=\sum_v a_{uv}\) (row sums of \(A\))</td></tr><tr><td>\(r\)</td><td>regularizer; \(r_c=\sqrt{\rho(B)}\) with \(\rho(B)\) the spectral radius of the non-backtracking matrix, estimated for sparse graphs by \(\sum_ud_u^2/\sum_ud_u-1\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Bethe Hessian. Entries grouped here: Bethe hessian.

<div class="formula-block"><p class="formula-name"><strong>Bethe Hessian (Saade et al. 2014)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[H(r)=(r^2-1)I-rA+D\]</div><p class="formula-where">Symmetric matrix defined for any real \(r\); the negative eigenvalues of \(H(r_c)\) count the communities in the spectral method of the paper. \(r_c\) depends on the degree sequence.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#gm_bethe_hessian">Bethe hessian</a></td><td><code>gm_bethe_hessian</code></td><td>1</td><td>The matrix \(H(r)\) at the default \(r\) of the tool or a chosen \(r\); weights enter through \(A\) and the strength in \(D\).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">\(n=0\): the 0\(\times\)0 matrix, but \(r_c\) is undefined (empty sums).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">\(\sum d=0\), so the estimate of \(r_c\) is 0/0; the matrix for a given \(r\) is \((r^2-1)I\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Parallel edges add to \(A\) and \(D\); the paper defines the matrix for simple graphs.</td><td><span class="st st-w st-nov" title="NetworkX does not implement the Bethe Hessian for multigraphs.">no value</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Defined for undirected graphs only.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">Any real \(r\) gives a matrix; \(r_c\) is real only when \(\sum d^2/\sum d\ge 1\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: no value. NetworkX does not implement the Bethe Hessian for multigraphs. <em>(conventions.json gm_bethe_hessian / gm_bethe_hessian)</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Bethe hessian {#gm_bethe_hessian}

Measure id: `gm_bethe_hessian`. Original family: Matrices and spectra.

**Definition.** Bethe hessian.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>bethe_hessian_matrix</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gm_bethe_hessian</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 1e-12, rel 1e-12</td><td><code>nx.bethe_hessian_matrix(G).toarray() (graph built without weights)</code></td><td>NetworkX does not implement the Bethe Hessian for multigraphs.</td></tr><tr><td><code>gm_bethe_hessian_weighted</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 1e-12, rel 1e-12</td><td><code>nx.bethe_hessian_matrix(G).toarray() (it reads the attribute 'weight')</code></td><td>NetworkX does not implement the Bethe Hessian for multigraphs.</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
