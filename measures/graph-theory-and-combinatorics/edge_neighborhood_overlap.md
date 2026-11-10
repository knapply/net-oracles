---
title: "Edge neighborhood overlap"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Edge neighborhood overlap {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Similarity and link prediction. Concept id: `edge_neighborhood_overlap`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(N(v)\)</td><td>set of neighbours of \(v\) (adjacent nodes); \(d_v=|N(v)|\) in a simple graph</td></tr></tbody></table></div>

## Definition {#concept-definition}

Edge neighborhood overlap. Entries grouped here: Edge nei overlap.

*Definition partly written:* Defined from a textbook form; the documented entry is known by name only and its variants (self-loops, denominator) are not recorded.

<div class="formula-block"><p class="formula-name"><strong>Neighbourhood overlap of an edge (Easley and Kleinberg 2010)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[O(u,v)=\frac{|N(u)\cap N(v)|}{|(N(u)\cup N(v))\setminus\{u,v\}|}\]</div><p class="formula-where">Fraction of the neighbours of the edge's ends that are shared; 0 when the edge joins nodes with no other neighbours (denominator 0 is a convention: 0 or not defined).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_edge_nei_overlap">Edge nei overlap</a></td><td><code>cat_edge_nei_overlap</code></td><td>1</td><td>Neighbourhood overlap of each edge; documented only.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/bct.html">BCT (Octave)</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">No edge.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly two nodes."><strong>Two nodes</strong></td><td class="def">A single edge: denominator 0, \(0/0\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">\(O=1\) for every edge of \(K_n\), \(n\ge3\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">\(O=0\): leaves share no neighbour with the centre.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Neighbour sets ignore multiplicity.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Two nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Star</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details></div>

## Edge nei overlap {#cat_edge_nei_overlap}

Measure id: `cat_edge_nei_overlap`. Original family: Graph theory and combinatorics.

**Definition.** Edge nei overlap.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/bct.html">BCT (Octave)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_edge_nei_overlap-bct">details</a></td><td><code>edge_nei_overlap_bd; edge_nei_overlap_bu</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_edge_nei_overlap-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: edge\_nei\_overlap\_bd; edge\_nei\_overlap\_bu.

**Tools cited:** [rubinov2010complex](../../references.html#rubinov2010complex)
{% endraw %}
