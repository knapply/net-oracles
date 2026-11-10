---
title: "Inverse line graph"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Inverse line graph {#concept-top}

Family: [Data transforms](index.html). Subfamily: Graph operators. Concept id: `inverse_line_graph`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(L(R)\)</td><td>line graph of \(R\)</td></tr><tr><td>\(R\)</td><td>a root graph of \(H\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Inverse line graph. Entries grouped here: Inverse line graph.

*Definition partly written:* The sources give only the name of the documented entry; the algorithm and its handling of non-line graphs and of non-unique roots are not recorded.

<div class="formula-block"><p class="formula-name"><strong>Inverse line graph (root graph)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[R\ \text{is a root graph of}\ H\iff L(R)\cong H\]</div><p class="formula-where">Given \(H\), find a graph \(R\) whose line graph is isomorphic to \(H\); defined only when \(H\) is a line graph, and then \(R\) is not always unique (\(K_3\) is the line graph of both \(K_3\) and \(K_{1,3}\)). See the concept line_graph for \(L\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_inverse_line">Inverse line graph</a></td><td><code>cat_inverse_line</code></td><td>1</td><td>The root graph of a line graph; documented only and not run.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">The null graph is the line graph of the null graph or of any edgeless graph, so the root is not unique.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">A graph that is not a line graph has no root: the operation is not defined for it.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">\(K_n\) is the line graph of the star \(K_{1,n}\) (and \(K_3\) also of \(K_3\)).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Too few nodes for the formula</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details></div>

## Inverse line graph {#cat_inverse_line}

Measure id: `cat_inverse_line`. Original family: Generators and rewiring.

**Definition.** Inverse line graph.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_inverse_line-networkx">details</a></td><td><code>inverse_line_graph</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_inverse_line-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: inverse\_line\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
