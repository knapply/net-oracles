---
title: "Permanence"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Permanence {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `permanence`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(k(v)\)</td><td>degree of \(v\): number of edge ends at \(v\) (a self-loop contributes 2 in an undirected graph)</td></tr><tr><td>\(I(v)\)</td><td>number of neighbours of \(v\) in its own community</td></tr><tr><td>\(E_{\max}(v)\)</td><td>largest number of neighbours of \(v\) in any single other community</td></tr><tr><td>\(c_{\mathrm{in}}(v)\)</td><td>clustering coefficient of the neighbours of \(v\) inside its community</td></tr></tbody></table></div>

## Definition {#concept-definition}

Permanence. Entries grouped here: Permanence Centrality.

*Definition partly written:* Handling of nodes with no external neighbour is not recorded in the sources read.

<div class="formula-block"><p class="formula-name"><strong>Permanence (Chakraborty et al. 2014)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\mathrm{Perm}(v)=\frac{I(v)}{E_{\max}(v)}\cdot\frac{1}{k(v)}-\bigl(1-c_{\mathrm{in}}(v)\bigr)\]</div><p class="formula-where">How firmly \(v\) belongs to its community: pull of internal neighbours against the strongest external pull, minus the lack of internal clustering. Lies in \([-1,1]\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_permanence">Permanence Centrality</a></td><td><code>cat_permanence</code></td><td>1</td><td>The formula above for a given partition; computed on request, so changing the partition changes the values.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkit.html">NetworKit</a></th></tr></thead><tbody><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">\(k(v)=0\): division by zero.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">Not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(E_{\max}(v)=0\) (no external neighbour) makes the first term a division by zero; the definition needs a convention.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Permanence Centrality {#cat_permanence}

Measure id: `cat_permanence`. Original family: Centrality.

**Definition.** Permanence Centrality.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_permanence-networkit">details</a></td><td><code>PermanenceCentrality</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_permanence-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: PermanenceCentrality.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
