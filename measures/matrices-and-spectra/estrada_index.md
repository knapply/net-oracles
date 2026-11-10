---
title: "Estrada index"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Estrada index {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Spectra. Concept id: `estrada_index`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(\lambda_1\ge\cdots\ge\lambda_n\)</td><td>eigenvalues of \(A\)</td></tr><tr><td>\(x_i(u)\)</td><td>component of the \(i\)-th unit eigenvector at \(u\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Estrada index. Entries grouped here: Estrada index.

<div class="formula-block"><p class="formula-name"><strong>Estrada index (sum of subgraph centralities; Estrada and Rodriguez-Velazquez 2005)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[EE(G)=\sum_{i=1}^{n}e^{\lambda_i}=\operatorname{tr}\,e^{A}=\sum_{u\in V}\sum_{i=1}^{n}x_i(u)^2e^{\lambda_i}\]</div><p class="formula-where">Weighted count of closed walks of every length (\(\operatorname{tr}\,A^k/k!\) summed over \(k\)); always defined, since the series converges for every finite \(A\). Subgraph centrality of \(u\) is \((e^{A})_{uu}\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#estrada_index">Estrada index</a></td><td><code>estrada_index</code></td><td>1</td><td>The sum \(\operatorname{tr}\,e^{A}\) of the exponentials of the adjacency eigenvalues; a variant over another matrix (Laplacian) is a different index.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">\(n=0\): empty sum, 0 (and \(\operatorname{tr}\,e^{A}=0\) for the 0\(\times\)0 matrix).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">\(A=0\), all \(\lambda_i=0\): \(EE=n\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Loops put entries on the diagonal of \(A\) and change the spectrum; the definition does not exclude them.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">The eigenvalue form needs a symmetric \(A\); \(\operatorname{tr}\,e^{A}\) is defined for directed input too (real part when eigenvalues are complex).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details></div>

## Estrada index {#estrada_index}

Measure id: `estrada_index`. Original family: Matrices and spectra.

**Definition.** Estrada index.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-estrada_index-networkx">details</a></td><td><code>estrada_index</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-estrada_index-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: estrada\_index.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
