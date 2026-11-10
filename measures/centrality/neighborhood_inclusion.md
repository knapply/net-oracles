---
title: "Neighborhood inclusion"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Neighborhood inclusion {#concept-top}

Family: [Centrality](index.html). Subfamily: Partial rankings (netrankr). Concept id: `neighborhood_inclusion`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(N(v)\)</td><td>set of neighbours of \(v\) (nodes joined to \(v\) by an edge, \(v\) itself excluded)</td></tr><tr><td>\(N[v]\)</td><td>closed neighbourhood \(N(v)\cup\{v\}\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Neighborhood inclusion. Entries grouped here: Neighborhood inclusion; Neighborhood inclusion, positional dominance, rank intervals.

<div class="formula-block"><p class="formula-name"><strong>Neighbourhood inclusion (Schoch and Brandes 2016)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[u\preceq v\ \Longleftrightarrow\ N(u)\subseteq N[v]\]</div><p class="formula-where">A preorder: \(u\) is dominated by \(v\) when every neighbour of \(u\) is a neighbour of \(v\) or \(v\) itself. If \(u\preceq v\) then \(c(u)\le c(v)\) for every centrality index defined by a path algebra (closeness, betweenness, eigenvector, subgraph, and others).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_inclusion_neighborhood">Neighborhood inclusion</a></td><td><code>cat_inclusion_neighborhood</code></td><td>1</td><td>The relation above as a matrix \(P_{uv}=1\) when \(u\preceq v\).</td></tr><tr><td><a href="#partial_ranking">Neighborhood inclusion, positional dominance, rank intervals</a></td><td><code>partial_ranking</code></td><td>1</td><td>Procedure bundling neighbourhood inclusion, positional dominance and rank intervals of one tool.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/netrankr.html">netrankr</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">Empty relation.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">The node is included in itself: the only comparable pair is \((v,v)\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">An isolate has \(N(u)=\emptyset\): included in every node.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop puts \(v\) in \(N(v)\); the definition is for simple graphs.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Neighbour sets ignore multiplicity.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Nodes with \(N(u)\subseteq N[v]\) and \(N(v)\subseteq N[u]\) are mutually included (equal in every index).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">The definition is for undirected graphs.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">Every leaf is dominated by the centre; leaves are mutually included.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">All nodes are mutually included.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Star</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details></div>

## Neighborhood inclusion {#cat_inclusion_neighborhood}

Measure id: `cat_inclusion_neighborhood`. Original family: Graph theory and combinatorics.

**Definition.** Neighborhood inclusion.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_inclusion_neighborhood-netrankr">details</a></td><td><code>neighborhood_inclusion</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_inclusion_neighborhood-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: neighborhood\_inclusion.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Neighborhood inclusion, positional dominance, rank intervals {#partial_ranking}

Measure id: `partial_ranking`. Original family: Centrality.

**Definition.** Neighborhood inclusion, positional dominance, rank intervals.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's documentation; no comparison set up for this measure yet. <a href="#why-partial_ranking-netrankr">details</a></td><td></td><td>documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-partial_ranking-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (R package netrankr: exported functions and help titles).

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)
{% endraw %}
