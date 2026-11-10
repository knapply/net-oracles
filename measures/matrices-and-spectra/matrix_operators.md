---
title: "Graph matrix operators"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Graph matrix operators {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Graph matrices. Concept id: `matrix_operators`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(A=(a_{uv})\)</td><td>adjacency matrix: \(a_{uv}\) is the number of edges from \(u\) to \(v\) (the sum of their weights when weighted)</td></tr><tr><td>\(D=\operatorname{diag}(d_1,\dots,d_n)\)</td><td>degree matrix, \(d_u=\sum_v a_{uv}\) (row sums of \(A\))</td></tr><tr><td>\(\vec E\)</td><td>set of directed edges (each undirected edge as two directed ones)</td></tr><tr><td>\(B_H\)</td><td>Hashimoto (non-backtracking) matrix, indexed by directed edges</td></tr></tbody></table></div>

## Definition {#concept-definition}

Graph matrix operators. Entries grouped here: Graph matrix operators (adjacency, Laplacian, Hashimoto, incidence).

*Definition partly written:* One entry of a documented-only tool lists four operators together; which of them each tool exposes, and with which conventions, is not recorded.

<div class="formula-block"><p class="formula-name"><strong>Hashimoto non-backtracking matrix (Hashimoto 1989)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[(B_H)_{(u\to v),(x\to y)}=\begin{cases}1&amp;v=x\ \text{and}\ y\neq u\\0&amp;\text{otherwise}\end{cases}\]</div><p class="formula-where">A \(2m\times 2m\) matrix (for undirected input) on directed edges: edge \(u\to v\) leads to every edge out of \(v\) except the one returning to \(u\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#matrix_operators">Graph matrix operators (adjacency, Laplacian, Hashimoto, incidence)</a></td><td><code>matrix_operators</code></td><td>2</td><td>Collective entry of a documented tool for the adjacency, Laplacian, Hashimoto and incidence operators; the adjacency, Laplacian and incidence forms are written on their own concept pages (adjacency_matrix, laplacian_matrix, incidence_matrix) and the Hashimoto form above.</td></tr></tbody></table></div>

## Graph matrix operators (adjacency, Laplacian, Hashimoto, incidence) {#matrix_operators}

Measure id: `matrix_operators`. Original family: Matrices and spectra.

**Definition.** Graph matrix operators (adjacency, Laplacian, Hashimoto, incidence).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-matrix_operators-graphtool">details</a></td><td><code>AdjacencyOperator; CompactHashimotoOperator; HashimotoOperator; IncidenceOperator; LaplacianOperator; TransitionOperator; hashimoto; transition</code></td><td>API listing</td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-matrix_operators-ucinet">details</a></td><td><code>transition</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-matrix_operators-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: AdjacencyOperator; CompactHashimotoOperator; HashimotoOperator; IncidenceOperator; LaplacianOperator; TransitionOperator; hashimoto; transition.
- <a id="why-matrix_operators-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
