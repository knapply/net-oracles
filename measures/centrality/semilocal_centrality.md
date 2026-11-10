---
title: "Semi-local centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Semi-local centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `semilocal_centrality`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(\Gamma(v)\)</td><td>nearest neighbours of \(v\)</td></tr><tr><td>\(N(w)\)</td><td>number of nearest and next-nearest neighbours of \(w\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Semi-local centrality. Entries grouped here: Semilocal.

<div class="formula-block"><p class="formula-name"><strong>Semi-local centrality (Chen et al. 2012)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[Q(u)=\sum_{w\in\Gamma(u)}N(w),\qquad C_{\mathrm{SL}}(v)=\sum_{u\in\Gamma(v)}Q(u)\]</div><p class="formula-where">Sum over neighbours \(u\) of \(v\) of the neighbourhood sizes of the neighbours of \(u\); for directed graphs \(N(w)\) counts upstream nodes.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_semilocal">Semilocal</a></td><td><code>cat_semilocal</code></td><td>1</td><td>The formula above.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/centiserve.html">centiserve</a></th></tr></thead><tbody><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">\(C_{\mathrm{SL}}=0\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">\(C_{\mathrm{SL}}=0\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Whether \(v\) is its own neighbour changes \(N(w)\); the definition is for simple graphs.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Defined on neighbour sets.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details></div>

## Semilocal {#cat_semilocal}

Measure id: `cat_semilocal`. Original family: Graph theory and combinatorics.

**Definition.** Semilocal.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/centiserve.html">centiserve</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_semilocal-centiserve">details</a></td><td><code>semilocal</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_semilocal-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: semilocal.

**Tools cited:** [jalili2015centiserver](../../references.html#jalili2015centiserver)
{% endraw %}
