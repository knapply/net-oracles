---
title: "Entropy centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Entropy centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `entropy_centrality`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(d(s,t)\)</td><td>length of a shortest path from \(s\) to \(t\): number of edges, or the total of the edge lengths for a weighted graph; \(\infty\) if \(t\) cannot be reached from \(s\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Entropy centrality. Entries grouped here: Entropy.

*Definition partly written:* The per-node formula is not given in the sources read; only the construction from path shares and the base-2 logarithm is described.

<div class="formula-block"><p class="formula-name"><strong>Entropy centrality (Ortiz-Arroyo and Hussain 2008)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[H_{ce}(G)=-\sum_{v}p_v\log_2 p_v,\qquad p_v=\frac{\text{geodesic paths through }v}{\text{all geodesic paths}}\]</div><p class="formula-where">As described in the documentation of the tool: each node's term uses its share of the geodesic paths with a base-2 logarithm; the contribution of \(v\) is the change of the graph entropy when \(v\) is removed. The exact per-node expression is not stated in the sources read.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_entropy">Entropy</a></td><td><code>cat_entropy</code></td><td>1</td><td>Per-node entropy centrality as described above, optionally with weights and path direction.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/centiserve.html">centiserve</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">No paths: \(p_v\) is 0/0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">No geodesic paths: the shares are undefined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details></div>

## Entropy {#cat_entropy}

Measure id: `cat_entropy`. Original family: Graph theory and combinatorics.

**Definition.** Entropy.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/centiserve.html">centiserve</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_entropy-centiserve">details</a></td><td><code>entropy</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_entropy-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: entropy.

**Tools cited:** [jalili2015centiserver](../../references.html#jalili2015centiserver)
{% endraw %}
