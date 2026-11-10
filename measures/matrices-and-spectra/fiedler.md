---
title: "Fiedler value and vector"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Fiedler value and vector {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Spectra. Concept id: `fiedler`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(L\)</td><td>Laplacian matrix (combinatorial or normalized)</td></tr><tr><td>\(0=\mu_1\le\mu_2\le\cdots\le\mu_n\)</td><td>eigenvalues of \(L\)</td></tr><tr><td>\(f\)</td><td>Fiedler vector: an eigenvector of \(\mu_2\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Fiedler value and vector. Entries grouped here: Fiedler.

<div class="formula-block"><p class="formula-name"><strong>Algebraic connectivity (Fiedler 1973)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[a(G)=\mu_2(L),\qquad Lf=\mu_2f,\ \ f\perp\mathbf 1\]</div><p class="formula-where">The second-smallest Laplacian eigenvalue; positive exactly when the graph is connected (\(n\ge 2\)). The Fiedler vector is orthogonal to the constant vector and is unique up to sign when \(\mu_2\) is simple.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Normalized form</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\mu_2(\mathcal L),\qquad \mathcal L=I-D^{-1/2}AD^{-1/2}\]</div><p class="formula-where">Same definition with the normalized Laplacian; the eigenvector then lives on the \(D^{1/2}\)-scaled space.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#gm_fiedler">Fiedler</a></td><td><code>gm_fiedler</code></td><td>1</td><td>Value \(\mu_2\) (algebraic connectivity) or the vector \(f\); combinatorial or normalized Laplacian; the spectral bisection splits nodes by the sign of \(f\).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">\(n=0\): no eigenvalues; not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">\(n=1\): there is no second eigenvalue; not defined.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (single_node).">agrees</span></td></tr><tr><td title="The graph has exactly two nodes."><strong>Two nodes</strong></td><td class="def">\(L\) has eigenvalues 0 and \(2w\); \(f\propto(1,-1)\), unique up to sign, so a sign rule decides the reported vector.</td><td><a class="st st-w st-conv" href="#why-gm_fiedler-networkx" title="For two nodes NetworkX returns [1, -1] without solving;">differs</a></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">\(\mu_2=0\) with multiplicity at least 2, so \(f\) is not unique (any vector of the null space orthogonal to \(\mathbf 1\)).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und).">agrees</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">A repeated \(\mu_2\) makes \(f\) non-unique; the sign of \(f\) is arbitrary even when \(\mu_2\) is simple.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables).">agrees</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Weights enter \(A\) and \(D\); negative weights break positive semidefiniteness and the connectivity reading.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir).">agrees</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Parallel edges add to \(A\) and \(D\).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Two nodes</summary><ul><li><strong>NetworkX</strong>: differs. For two nodes NetworkX returns [1, -1] without solving; <em>(conventions.json gm_fiedler / gm_fiedler_vector)</em></li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Edge weights</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## Fiedler {#gm_fiedler}

Measure id: `gm_fiedler`. Original family: Matrices and spectra.

**Definition.** Fiedler.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (defaults, normalization and ties): For two nodes NetworkX returns [1, -1] without solving. <a href="#why-gm_fiedler-networkx">details</a></td><td><code>algebraic_connectivity; fiedler_vector; spectral_bisection</code></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gm_fiedler-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (defaults, normalization and ties) on inputs tagged two\_nodes. For two nodes NetworkX returns \[1, -1\] without solving; the reference returns the unit vector with its first entry negative. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-06, rel 1e-05 (0 means exact equality). 2 comparisons differ and 85 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gm_fiedler_value</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-10, rel 1e-09</td><td><code>nx.algebraic_connectivity(G, tol = 1e-10, method = 'tracemin_lu') (directed graphs through NetworkX's _preprocess_graph, then weight = 'weight', as spectral_ordering reads them)</code></td><td></td></tr><tr><td><code>gm_fiedler_value_normalized_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-10, rel 1e-09</td><td><code>nx.algebraic_connectivity(G, weight = 'weight', normalized = True, tol = 1e-10, method = 'tracemin_lu')</code></td><td></td></tr><tr><td><code>gm_fiedler_vector</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>two_nodes</td><td>defaults</td><td>abs 1e-06, rel 1e-05</td><td><code>nx.fiedler_vector(G) (default method tracemin_pcg, tol 1e-8)</code></td><td>For two nodes NetworkX returns [1, -1] without solving; the reference returns the unit vector with its first entry negative (the backend returns NetworkX's [1, -1]).</td></tr><tr><td><code>gm_fiedler_vector_normalized</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>two_nodes</td><td>defaults, normalization, ties</td><td>abs 1e-06, rel 1e-05</td><td><code>nx.fiedler_vector(G, normalized = True)</code></td><td>For two nodes NetworkX returns [1, -1] without solving; the reference returns the unit vector with its first entry negative. NetworkX's tracemin_pcg iteration for the normalized Laplacian does not converge on these graphs and, having no iteration cap, never returns.</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
