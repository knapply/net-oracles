---
title: "Eigenvectors of graph matrices"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Eigenvectors of graph matrices {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Spectra. Concept id: `eigenvectors_matrix`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(M\)</td><td>a graph matrix: adjacency, Laplacian, normalized Laplacian, modularity or other</td></tr><tr><td>\(\lambda_i,\ x_i\)</td><td>eigenvalue and eigenvector, \(Mx_i=\lambda_ix_i\), \(\|x_i\|_2=1\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Eigenvectors of graph matrices. Entries grouped here: Eigenvectors of graph matrices.

<div class="formula-block"><p class="formula-name"><strong>Eigenpairs of a symmetric matrix (Golub and Van Loan 2013)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[Mx_i=\lambda_ix_i,\qquad x_i^{\top}x_j=\delta_{ij}\]</div><p class="formula-where">A real symmetric \(M\) has real eigenvalues and an orthonormal set of eigenvectors; each \(x_i\) is determined up to sign, and up to rotation within an eigenspace when \(\lambda_i\) is repeated. A non-symmetric \(M\) (directed input) can have complex eigenpairs.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#eigenvectors_matrix">Eigenvectors of graph matrices</a></td><td><code>eigenvectors_matrix</code></td><td>1</td><td>Eigenvectors of any of the graph matrices; which matrix, how many vectors, the ordering of eigenvalues and the sign rule are properties of the tool.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkit.html">NetworKit</a></th></tr></thead><tbody><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Repeated eigenvalues make the eigenvectors non-unique (any orthonormal basis of the eigenspace); a sign flip is always allowed, so two correct results can differ by sign.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">A non-symmetric matrix has right and left eigenvectors that differ, and possibly complex ones.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details></div>

## Eigenvectors of graph matrices {#eigenvectors_matrix}

Measure id: `eigenvectors_matrix`. Original family: Matrices and spectra.

**Definition.** Eigenvectors of graph matrices.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-eigenvectors_matrix-networkit">details</a></td><td><code>SpectralCentrality; adjacencyEigenvector; adjacencyEigenvectors; eigenvectors; laplacianEigenvector; laplacianEigenvectors; symmetricEigenvectors</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-eigenvectors_matrix-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: SpectralCentrality; adjacencyEigenvector; adjacencyEigenvectors; eigenvectors; laplacianEigenvector; laplacianEigenvectors; symmetricEigenvectors.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
