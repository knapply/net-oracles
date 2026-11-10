---
title: "Common spanning trees of two graphs"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Common spanning trees of two graphs {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Spanning trees and branchings. Concept id: `common_spanning_trees`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(G_1,G_2\)</td><td>two graphs on the same node set</td></tr></tbody></table></div>

## Definition {#concept-definition}

Common spanning trees of two graphs. Entries grouped here: Two graphs common spanning trees.

*Definition partly written:* The definition is written from the name of the documented entry; its algorithm is not recorded and no primary source is cited.

<div class="formula-block"><p class="formula-name"><strong>Common spanning tree</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[T\ \text{is a spanning tree of }G_1\ \text{and of }G_2\]</div><p class="formula-where">A tree whose edges all lie in both graphs; exists only if the intersection graph \(G_1\cap G_2\) is connected, and then it is a spanning tree of that intersection.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_common_spanning_tree_two">Two graphs common spanning trees</a></td><td><code>cat_common_spanning_tree_two</code></td><td>1</td><td>A spanning tree common to both graphs; documented only.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/boost.html">Boost Graph Library</a></th></tr></thead><tbody><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">If \(G_1\cap G_2\) is disconnected there is no common spanning tree: not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details></div>

## Two graphs common spanning trees {#cat_common_spanning_tree_two}

Measure id: `cat_common_spanning_tree_two`. Original family: Traversal, trees and DAGs.

**Definition.** Two graphs common spanning trees.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/boost.html">Boost Graph Library</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_common_spanning_tree_two-boost">details</a></td><td><code>two_graphs_common_spanning_trees</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_common_spanning_tree_two-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: two\_graphs\_common\_spanning\_trees.

**Tools cited:** [siek2002boost](../../references.html#siek2002boost)
{% endraw %}
