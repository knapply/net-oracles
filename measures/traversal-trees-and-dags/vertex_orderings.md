---
title: "Vertex orderings (max cardinality, degeneracy)"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Vertex orderings (max cardinality, degeneracy) {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Traversal and orderings. Concept id: `vertex_orderings`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(\sigma\)</td><td>vertex ordering</td></tr><tr><td>\(k(G)\)</td><td>degeneracy</td></tr></tbody></table></div>

## Definition {#concept-definition}

Vertex orderings (max cardinality, degeneracy). Entries grouped here: Vertex orderings (max cardinality, degeneracy); Maximum cardinality search.

<div class="formula-block"><p class="formula-name"><strong>Degeneracy ordering and core numbers (Matula and Beck 1983)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\sigma_t=\arg\min_{v\notin\{\sigma_1..\sigma_{t-1}\}}\deg_{G-\{\sigma_1..\sigma_{t-1}\}}(v),\qquad k(G)=\max_t\deg_{G-\{\sigma_1..\sigma_{t-1}\}}(\sigma_t)\]</div><p class="formula-where">Repeatedly remove a node of least remaining degree; the largest degree seen at removal is the degeneracy.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Maximum cardinality search (Tarjan and Yannakakis 1984)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\sigma_t=\arg\max_{v\ \text{unnumbered}}\bigl|N(v)\cap\{\sigma_1..\sigma_{t-1}\}\bigr|\]</div><p class="formula-where">Visit next an unvisited node with most visited neighbours; the reverse of the order is a perfect elimination ordering exactly when the graph is chordal (Berry, Blair and Heggernes 2004 for minimal triangulations).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#vertex_orderings">Vertex orderings (max cardinality, degeneracy)</a></td><td><code>vertex_orderings</code></td><td>2</td><td>Collective entry for orderings (maximum cardinality search, degeneracy ordering).</td></tr><tr><td><a href="#cat_cardinality_maximum_search">Maximum cardinality search</a></td><td><code>cat_cardinality_maximum_search</code></td><td>1</td><td>The maximum cardinality search ordering.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/pyigraph.html">igraph (Python)</a></th><th><a href="../../tools/jgrapht.html">JGraphT</a></th><th><a href="../../tools/boost.html">Boost Graph Library</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">Empty ordering; degeneracy not defined (max over nothing).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">Isolated nodes have degree 0 and are placed first by degeneracy ordering and, with 0 visited neighbours, tie with every other candidate in MCS.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">MCS restarts in each component by choosing any node; the ordering is not unique.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Both rules have ties at almost every step: the order is not unique and tools differ by tie rule; the degeneracy value is unique.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop adds to the degree in some conventions and is ignored in others.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details></div>

## Vertex orderings (max cardinality, degeneracy) {#vertex_orderings}

Measure id: `vertex_orderings`. Original family: Traversal, trees and DAGs.

**Definition.** Vertex orderings (max cardinality, degeneracy).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-vertex_orderings-jgrapht">details</a></td><td><code>DegeneracyOrderingIterator; MaximumCardinalityIterator</code></td><td>API listing</td></tr><tr><td><a href="../../tools/boost.html">Boost Graph Library</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-vertex_orderings-boost">details</a></td><td><code>maximum_adjacency_search</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-vertex_orderings-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: DegeneracyOrderingIterator; MaximumCardinalityIterator.
- <a id="why-vertex_orderings-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: maximum\_adjacency\_search.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht), [siek2002boost](../../references.html#siek2002boost)

## Maximum cardinality search {#cat_cardinality_maximum_search}

Measure id: `cat_cardinality_maximum_search`. Original family: Traversal, trees and DAGs.

**Definition.** Maximum cardinality search.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_cardinality_maximum_search-pyigraph">details</a></td><td><code>maximum_cardinality_search</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_cardinality_maximum_search-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: maximum\_cardinality\_search.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
