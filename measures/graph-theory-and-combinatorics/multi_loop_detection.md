---
title: "Loop and multi-edge detection"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Loop and multi-edge detection {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Degree sequences and predicates. Concept id: `multi_loop_detection`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(s(e),t(e)\)</td><td>source and target of edge \(e\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Loop and multi-edge detection. Entries grouped here: Loop and multi-edge detection.

<div class="formula-block"><p class="formula-name"><strong>Loops and parallel edges</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\mathrm{has\_loop}\iff\exists e:\ s(e)=t(e);\qquad \mathrm{has\_multi}\iff\exists e\ne f:\ \{s(e),t(e)\}=\{s(f),t(f)\}\]</div><p class="formula-where">For directed edges compare ordered pairs \((s,t)\); for undirected edges compare unordered pairs. A graph with neither is simple.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#multi_loop_detection">Loop and multi-edge detection</a></td><td><code>multi_loop_detection</code></td><td>1</td><td>Detection of loops and of multiple edges.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/igraph.html">igraph (R)</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">Neither.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Detected by \(s(e)=t(e)\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Detected by equal endpoint pairs; for directed edges \(u\to v\) and \(v\to u\) are not parallel.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">A pair of opposite arcs is parallel as undirected edges and not as directed edges.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details></div>

## Loop and multi-edge detection {#multi_loop_detection}

Measure id: `multi_loop_detection`. Original family: Graph theory and combinatorics.

**Definition.** Loop and multi-edge detection.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-multi_loop_detection-igraph">details</a></td><td><code>any_loop; any_multiple; count_loops; count_multiple; is_simple; which_loop; which_multiple; which_mutual</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-multi_loop_detection-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: any\_loop; any\_multiple; count\_loops; count\_multiple; is\_simple; which\_loop; which\_multiple; which\_mutual.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
