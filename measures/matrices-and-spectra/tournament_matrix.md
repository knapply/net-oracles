---
title: "Tournament matrix"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Tournament matrix {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Graph matrices. Concept id: `tournament_matrix`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(T=(t_{uv})\)</td><td>tournament matrix of a tournament: \(t_{uv}=1\) if \(u\) beats \(v\), else 0</td></tr><tr><td>\(s_u\)</td><td>score of \(u\), the number of nodes it beats</td></tr></tbody></table></div>

## Definition {#concept-definition}

Tournament matrix. Entries grouped here: Tournament matrix.

*Definition partly written:* The tool function is known by name only; its input requirements and output convention are not recorded.

<div class="formula-block"><p class="formula-name"><strong>Tournament matrix and scores (Harary, Norman and Cartwright 1965)</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[t_{uv}+t_{vu}=1\ (u\neq v),\quad t_{uu}=0,\quad s_u=\sum_vt_{uv}\]</div><p class="formula-where">Exactly one arc between every pair of nodes; the score vector is the row sums.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_matrix_tournament">Tournament matrix</a></td><td><code>cat_matrix_tournament</code></td><td>1</td><td>Tournament matrix as above; the tool entry is known by name only.</td></tr></tbody></table></div>

## Tournament matrix {#cat_matrix_tournament}

Measure id: `cat_matrix_tournament`. Original family: Matrices and spectra.

**Definition.** Tournament matrix.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_matrix_tournament-networkx">details</a></td><td><code>tournament_matrix</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_matrix_tournament-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: tournament\_matrix.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
