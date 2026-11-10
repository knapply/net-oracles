---
title: "Prestige"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Prestige {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `prestige`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(d(s,t)\)</td><td>length of a shortest path from \(s\) to \(t\): number of edges, or the total of the edge lengths for a weighted graph; \(\infty\) if \(t\) cannot be reached from \(s\)</td></tr><tr><td>\(I(v)\)</td><td>nodes that can reach \(v\) (the influence domain of \(v\)), \(v\) excluded</td></tr></tbody></table></div>

## Definition {#concept-definition}

Prestige. Entries grouped here: Prestige.

<div class="formula-block"><p class="formula-name"><strong>Indegree prestige</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[P_D(v)=k^{\mathrm{in}}(v)\]</div><p class="formula-where">The simplest prestige: number of incoming ties (Wasserman and Faust 1994); row- or column-normalized versions rescale the matrix first.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Eigenvector prestige</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[P_E=\lambda^{-1}A^{\mathsf T}P_E\]</div><p class="formula-where">Eigenvector centrality of the transposed graph: prestige comes from the prestige of those who choose you.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Domain and proximity prestige (Lin 1976)</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[P_I(v)=\frac{|I(v)|}{n-1},\qquad P_P(v)=\frac{|I(v)|/(n-1)}{\sum_{u\in I(v)}d(u,v)/|I(v)|}\]</div><p class="formula-where">Share of the nodes that reach \(v\), and that share divided by their mean distance to \(v\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_prestige">Prestige</a></td><td><code>cat_prestige</code></td><td>1</td><td>The listed prestige types of the tool (in-degree, normalized in-degree, eigenvector, domain and proximity-weighted domain prestige), selected by an argument.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/sna.html">sna</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">\(P_D=0\); domain prestige is 0/0 (\(n-1=0\)).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">\(P_D=0\), \(|I(v)|=0\): proximity prestige is 0/0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">The diagonal is ignored by default in the tool; the indegree definition counts a loop as an incoming tie if loops are data.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Indegree counts every edge; domain prestige counts nodes.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Prestige is a directed notion: incoming ties. An undirected graph makes it equal to degree.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Edge values are strengths in the in-degree; lengths in the proximity measure.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details></div>

## Prestige {#cat_prestige}

Measure id: `cat_prestige`. Original family: Graph theory and combinatorics.

**Definition.** Prestige.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_prestige-sna">details</a></td><td><code>prestige</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_prestige-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: prestige.

**Tools cited:** [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
