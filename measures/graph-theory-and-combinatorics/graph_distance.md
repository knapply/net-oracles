---
title: "Distances between graphs (Hamming, structural)"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Distances between graphs (Hamming, structural) {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Distances between graphs. Concept id: `graph_distance`. 3 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(A,B\)</td><td>adjacency matrices of two graphs on the same labelled node set</td></tr></tbody></table></div>

## Definition {#concept-definition}

Distances between graphs (Hamming, structural). Entries grouped here: Hdist; Sdmat; Structdist.

*Definition partly written:* Only the Hamming distance is defined here, from the quadratic-assignment literature; the structural distance and its matrix (cat\_structdist, cat\_sdmat) are known by name only.

<div class="formula-block"><p class="formula-name"><strong>Hamming distance of graphs (Hubert and Schultz 1976)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[d_H(A,B)=\sum_{u,v}|a_{uv}-b_{uv}|\]</div><p class="formula-where">The number of ordered pairs on which the two graphs differ (for undirected graphs, twice the number of differing edges); 0 iff equal. The nodes of both graphs are matched by label.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_hdist">Hdist</a></td><td><code>cat_hdist</code></td><td>1</td><td>Hamming distance; documented only.</td></tr><tr><td><a href="#cat_sdmat">Sdmat</a></td><td><code>cat_sdmat</code></td><td>1</td><td>Matrix of structural distances; documented only.</td></tr><tr><td><a href="#cat_structdist">Structdist</a></td><td><code>cat_structdist</code></td><td>1</td><td>Structural distance between graphs; documented only.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/sna.html">sna</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">Distance 0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Ordered pairs for digraphs; each undirected edge counts twice in this sum (or once, by convention).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">The absolute difference of weights, or 0/1 disagreement.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details></div>

## Hdist {#cat_hdist}

Measure id: `cat_hdist`. Original family: Graph theory and combinatorics.

**Definition.** Hdist.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_hdist-sna">details</a></td><td><code>hdist</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_hdist-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: hdist.

**Tools cited:** [butts2008sna](../../references.html#butts2008sna)

## Sdmat {#cat_sdmat}

Measure id: `cat_sdmat`. Original family: Graph theory and combinatorics.

**Definition.** Sdmat.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_sdmat-sna">details</a></td><td><code>sdmat</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_sdmat-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: sdmat.

**Tools cited:** [butts2008sna](../../references.html#butts2008sna)

## Structdist {#cat_structdist}

Measure id: `cat_structdist`. Original family: Graph theory and combinatorics.

**Definition.** Structdist.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_structdist-sna">details</a></td><td><code>structdist</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_structdist-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: structdist.

**Tools cited:** [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
