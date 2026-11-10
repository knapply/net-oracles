---
title: "Spectral modularity bipartition"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Spectral modularity bipartition {#concept-top}

Family: [Communities](index.html). Subfamily: Graph bisection and partitioning. Concept id: `spectral_modularity_bipartition`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\); every edge has a source and a target (the ends of an undirected edge are interchangeable)</td></tr><tr><td>\(B_{ij}=A_{ij}-\tfrac{k_ik_j}{2m}\)</td><td>modularity matrix</td></tr><tr><td>\(u_1\)</td><td>leading eigenvector of \(B\)</td></tr><tr><td>\(s_i\in\{\pm1\}\)</td><td>side of node \(i\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Spectral modularity bipartition. Entries grouped here: Spectral modularity bipartition (community).

*Definition partly written:* Documented only (NetworkX), never run; the formula is Newman's spectral bipartition, and the tool's handling of degenerate eigenvectors and options is not recorded.

<div class="formula-block"><p class="formula-name"><strong>Spectral bisection by modularity (Newman 2006)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[s_i=\begin{cases}+1&amp;u_{1,i}&gt;0\\-1&amp;u_{1,i}\le0\end{cases},\qquad \Delta Q=\frac1{4m}s^{\mathsf T}Bs\]</div><p class="formula-where">Split by the sign of the leading eigenvector of \(B\); no split if its largest eigenvalue is not positive.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_bipartition_modularity_spectral-community">Spectral modularity bipartition (community)</a></td><td><code>cat_bipartition_modularity_spectral@community</code></td><td>1</td><td>The two-way split of a graph by the leading eigenvector of the modularity matrix.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">\(B\) undefined (\(m=0\)).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">A repeated leading eigenvalue leaves the eigenvector undetermined; zero components (isolates) have no sign.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Components give degenerate eigenvectors.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">No positive eigenvalue: no split.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details></div>

## Spectral modularity bipartition (community) {#cat_bipartition_modularity_spectral-community}

Measure id: `cat_bipartition_modularity_spectral@community`. Original family: Communities.

**Definition.** Spectral modularity bipartition (community).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_bipartition_modularity_spectral-community-networkx">details</a></td><td><code>spectral_modularity_bipartition</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_bipartition_modularity_spectral-community-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: spectral\_modularity\_bipartition.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
