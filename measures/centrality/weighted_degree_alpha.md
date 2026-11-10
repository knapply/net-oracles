---
title: "Alpha-tuned degree and closeness"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Alpha-tuned degree and closeness {#concept-top}

Family: [Centrality](index.html). Subfamily: Degree and strength. Concept id: `weighted_degree_alpha`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(w(u,v)\)</td><td>weight of the edge from \(u\) to \(v\) (1 when the graph is unweighted)</td></tr><tr><td>\(k_i,\ s_i\)</td><td>degree and strength of node \(i\)</td></tr><tr><td>\(\alpha\ge 0\)</td><td>tuning parameter: 0 ignores weights, 1 uses them fully</td></tr><tr><td>\(d^{\alpha}(i,j)\)</td><td>length of the shortest path from \(i\) to \(j\) when an edge of weight \(w\) has length \(w^{-\alpha}\): \(\min_{\text{paths}}\sum_h w_h^{-\alpha}\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Alpha-tuned degree and closeness. Entries grouped here: Opsahl alpha-tuned degree and closeness.

<div class="formula-block"><p class="formula-name"><strong>Alpha-tuned degree (Opsahl et al. 2010)</strong> <span class="applies">applies to: weighted, undirected</span></p><div class="formula">\[C_D^{w\alpha}(i)=k_i^{\,1-\alpha}\,s_i^{\,\alpha}\]</div><p class="formula-where">\(\alpha=0\) gives the degree, \(\alpha=1\) the strength; values between mix the number of ties and their weights.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Alpha-tuned closeness</strong> <span class="applies">applies to: weighted, connected</span></p><div class="formula">\[C_C^{w\alpha}(i)=\Bigl[\sum_{j\ne i}d^{\alpha}(i,j)\Bigr]^{-1}\]</div><p class="formula-where">\(\alpha=0\) counts the number of edges on shortest paths (unweighted closeness), \(\alpha=1\) uses weights as in Dijkstra's method. The inverse of a sum of distances needs every distance to be finite.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#opsahl_alpha">Opsahl alpha-tuned degree and closeness</a></td><td><code>opsahl_alpha</code></td><td>1</td><td>Both formulas above; the tuning parameter \(\alpha\) and the treatment of unreachable nodes are the tool's arguments.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/tnet.html">tnet</a></th></tr></thead><tbody><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">Degree 0 and strength 0 give 0 for the degree version (with \(0^0\) read as 1 at \(\alpha=0\)); closeness needs distances and an isolate has none.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">The sum of distances is infinite; the definition is for connected graphs, and extensions (largest component only, or inverse distances) are separate choices.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">The paper defines the measures on weighted simple graphs; parallel edges are not covered and are commonly summed into one tie.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Edges with weight 0."><strong>Zero weights</strong></td><td class="def">Length \(w^{-\alpha}\) is infinite for \(w=0\) with \(\alpha&gt;0\): the edge cannot be used.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Edges with a negative weight."><strong>Negative weights</strong></td><td class="def">Outside the domain: \(w^{-\alpha}\) is undefined for non-integer \(\alpha\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(\alpha\ge 0\) in the paper; \(\alpha=0\) in the degree version needs \(0^0=1\) for nodes without ties.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Zero weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Negative weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Opsahl alpha-tuned degree and closeness {#opsahl_alpha}

Measure id: `opsahl_alpha`. Original family: Centrality.

**Definition.** Opsahl alpha-tuned degree and closeness.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/tnet.html">tnet</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's documentation; no comparison set up for this measure yet. <a href="#why-opsahl_alpha-tnet">details</a></td><td></td><td>documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-opsahl_alpha-tnet"></a>**[tnet](../../tools/tnet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. tnet 3.0.16 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (R package tnet: exported functions and help titles).

**Tools cited:** [opsahl2010node](../../references.html#opsahl2010node)
{% endraw %}
