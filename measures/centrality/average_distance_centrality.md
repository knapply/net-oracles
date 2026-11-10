---
title: "Average distance centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Average distance centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Distance-based. Concept id: `average_distance_centrality`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(d(s,t)\)</td><td>length of a shortest path from \(s\) to \(t\): number of edges, or the total of the edge lengths for a weighted graph; \(\infty\) if \(t\) cannot be reached from \(s\)</td></tr><tr><td>\(N_0\)</td><td>number of ordered pairs of distinct nodes joined by a directed path</td></tr><tr><td>\(N_{-v}\)</td><td>number of those pairs that are still connected after \(v\) is removed</td></tr></tbody></table></div>

## Definition {#concept-definition}

Average distance centrality. Entries grouped here: Averagedis; Pairwisedis.

<div class="formula-block"><p class="formula-name"><strong>Average distance (del Rio et al. 2009)</strong> <span class="applies">applies to: connected</span></p><div class="formula">\[C_{\mathrm{avg}}(v)=\frac{\sum_{w\in V}d(v,w)}{n-1}\]</div><p class="formula-where">Mean distance from \(v\) to the other nodes: the inverse of normalized closeness; low values mean central. Defined for strongly connected graphs.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Pairwise disconnectivity index (Potapov et al. 2008)</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[\mathrm{Dis}(v)=\frac{N_0-N_{-v}}{N_0}=1-\frac{N_{-v}}{N_0}\]</div><p class="formula-where">Fraction of the initially connected ordered pairs that lose every path when \(v\) is removed. Needs at least one edge between two different nodes.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_averagedis">Averagedis</a></td><td><code>cat_averagedis</code></td><td>1</td><td>The mean distance, first formula.</td></tr><tr><td><a href="#cat_pairwisedis">Pairwisedis</a></td><td><code>cat_pairwisedis</code></td><td>1</td><td>The pairwise disconnectivity index, second formula.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/centiserve.html">centiserve</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">Mean distance 0/0; \(N_0=0\) so \(\mathrm{Dis}\) is 0/0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">\(N_0=0\): the index is undefined (needs at least one edge).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">The mean distance is undefined (infinite distances); \(\mathrm{Dis}(v)=0\) for an isolate (removing it disconnects no pair).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Mean distance infinite for unreachable nodes: not defined; the index counts only pairs connected at the start.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Loops do not change distances or paths; the average distance is documented for loop-free graphs.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">Removing the centre disconnects every pair of leaves, so \(N_{-v}=0\) over leaf pairs; each leaf's removal disconnects only the pairs that contain it.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Star</summary><ul><li>No tool entries.</li></ul></details></div>

## Averagedis {#cat_averagedis}

Measure id: `cat_averagedis`. Original family: Graph theory and combinatorics.

**Definition.** Averagedis.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/centiserve.html">centiserve</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_averagedis-centiserve">details</a></td><td><code>averagedis</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_averagedis-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: averagedis.

**Tools cited:** [jalili2015centiserver](../../references.html#jalili2015centiserver)

## Pairwisedis {#cat_pairwisedis}

Measure id: `cat_pairwisedis`. Original family: Graph theory and combinatorics.

**Definition.** Pairwisedis.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/centiserve.html">centiserve</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_pairwisedis-centiserve">details</a></td><td><code>pairwisedis</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_pairwisedis-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: pairwisedis.

**Tools cited:** [jalili2015centiserver](../../references.html#jalili2015centiserver)
{% endraw %}
