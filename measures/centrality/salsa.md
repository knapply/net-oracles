---
title: "SALSA"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# SALSA {#concept-top}

Family: [Centrality](index.html). Subfamily: Spectral and walk-based. Concept id: `salsa`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(k^{\mathrm{in}}(i),\,k^{\mathrm{out}}(h)\)</td><td>in- and out-degree</td></tr></tbody></table></div>

## Definition {#concept-definition}

SALSA. Entries grouped here: Salsa.

*Definition partly written:* The closed-form stationary distribution and the edge cases of the tool's implementation are not recorded in the sources read.

<div class="formula-block"><p class="formula-name"><strong>SALSA authority chain (Lempel and Moran 2001)</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[P^{\mathrm{auth}}_{ij}=\sum_{h:\,h\to i,\ h\to j}\frac{1}{k^{\mathrm{in}}(i)}\cdot\frac{1}{k^{\mathrm{out}}(h)}\]</div><p class="formula-where">Transition probability of a random walk on the authorities of the bipartite hub-authority graph: step back along an in-edge of \(i\) to a hub \(h\), then forward along one of \(h\)'s out-edges to \(j\). The authority scores are the stationary distribution of this chain; the hub chain is defined symmetrically.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_salsa">Salsa</a></td><td><code>cat_salsa</code></td><td>1</td><td>SALSA hub or authority scores of one tool.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/centiserve.html">centiserve</a></th></tr></thead><tbody><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">Nodes without in-edges are not authorities; nodes without out-edges are not hubs.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">The stationary distribution is determined per connected component of the bipartite graph, weighted by the component's share.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details></div>

## Salsa {#cat_salsa}

Measure id: `cat_salsa`. Original family: Centrality.

**Definition.** Salsa.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/centiserve.html">centiserve</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_salsa-centiserve">details</a></td><td><code>salsa</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_salsa-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: salsa.

**Tools cited:** [jalili2015centiserver](../../references.html#jalili2015centiserver)
{% endraw %}
