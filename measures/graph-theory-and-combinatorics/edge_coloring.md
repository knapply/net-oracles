---
title: "Edge coloring"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Edge coloring {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Coloring. Concept id: `edge_coloring`. 3 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(\Delta\)</td><td>maximum degree</td></tr><tr><td>\(\chi'(G)\)</td><td>chromatic index: least number of colours of a proper edge colouring</td></tr></tbody></table></div>

## Definition {#concept-definition}

Edge coloring. Entries grouped here: Bipartite edge color; Greedy edge color; Misra gries edge color.

*Definition partly written:* Defined from the textbook notion without a cited primary source (Vizing 1964 and the Misra-Gries paper are not among the checked bibliography); the three documented entries are described from their names and the guarantees below are known results, not tool statements.

<div class="formula-block"><p class="formula-name"><strong>Proper edge colouring</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[c:E\to\{1,\dots,k\},\quad c(e)\neq c(f)\ \text{whenever }e,f\text{ share an end}\]</div><p class="formula-where">Each colour class is a matching. \(\chi'(G)\ge\Delta\); Vizing's theorem gives \(\chi'\le\Delta+1\) for simple graphs, and \(\chi'=\Delta\) for bipartite graphs.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_bipartite_color_edge">Bipartite edge color</a></td><td><code>cat_bipartite_color_edge</code></td><td>1</td><td>Edge colouring of a bipartite graph with exactly \(\Delta\) colours.</td></tr><tr><td><a href="#cat_color_edge_greedy">Greedy edge color</a></td><td><code>cat_color_edge_greedy</code></td><td>1</td><td>Greedy colouring: edges in a given order each get the smallest colour not used at its ends; at most \(2\Delta-1\) colours.</td></tr><tr><td><a href="#cat_color_edge_gries_misra">Misra gries edge color</a></td><td><code>cat_color_edge_gries_misra</code></td><td>1</td><td>Misra-Gries edge colouring, which uses at most \(\Delta+1\) colours.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/rustworkx.html">rustworkx</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">No edges: no colours needed.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop shares an end with itself: no proper edge colouring in the simple sense.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Parallel edges share both ends, so need different colours, and the bound \(\Delta+1\) fails.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The node set splits into two classes with edges only between classes (periodic structure; two-mode data)."><strong>Bipartite or two-mode graph</strong></td><td class="def">\(\chi'=\Delta\) (König).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">\(\chi'=\Delta\) (all edges meet at the centre).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">\(\chi'(K_n)=n-1\) for even \(n\), \(n\) for odd \(n\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Bipartite or two-mode graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Star</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details></div>

## Bipartite edge color {#cat_bipartite_color_edge}

Measure id: `cat_bipartite_color_edge`. Original family: Two-mode and bipartite.

**Definition.** Bipartite edge color.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_bipartite_color_edge-rustworkx">details</a></td><td><code>graph_bipartite_edge_color</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_bipartite_color_edge-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: graph\_bipartite\_edge\_color.

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Greedy edge color {#cat_color_edge_greedy}

Measure id: `cat_color_edge_greedy`. Original family: Graph theory and combinatorics.

**Definition.** Greedy edge color.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_color_edge_greedy-rustworkx">details</a></td><td><code>graph_greedy_edge_color</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_color_edge_greedy-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: graph\_greedy\_edge\_color.

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Misra gries edge color {#cat_color_edge_gries_misra}

Measure id: `cat_color_edge_gries_misra`. Original family: Graph theory and combinatorics.

**Definition.** Misra gries edge color.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_color_edge_gries_misra-rustworkx">details</a></td><td><code>graph_misra_gries_edge_color</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_color_edge_gries_misra-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: graph\_misra\_gries\_edge\_color.

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
