---
title: "Positional dominance"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Positional dominance {#concept-top}

Family: [Centrality](index.html). Subfamily: Partial rankings (netrankr). Concept id: `positional_dominance`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(A_{ut}\)</td><td>relation of \(u\) to \(t\) (a distance, a walk count, any attribute)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Positional dominance. Entries grouped here: Positional dominance.

<div class="formula-block"><p class="formula-name"><strong>Positional dominance (Brandes 2016)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[u\preceq v\ \Longleftrightarrow\ A_{ut}\le A_{vt}\ \ \forall t\ \ (\text{benefit}),\qquad A_{ut}\ge A_{vt}\ \ \forall t\ \ (\text{cost})\]</div><p class="formula-where">Total heterogeneity: rows are compared position by position. Generalizes neighbourhood inclusion (where \(A\) is the adjacency relation).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Total homogeneity</strong> <span class="applies">applies to: any</span></p><div class="formula">\[u\preceq v\ \Longleftrightarrow\ \operatorname{sort}\!\bigl(A_{u\cdot}\bigr)\le\operatorname{sort}\!\bigl(A_{v\cdot}\bigr)\ \text{componentwise}\]</div><p class="formula-where">Each row is first sorted (decreasingly for benefit variables, increasingly for cost) and then compared; weaker than the first form.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_dominance_positional">Positional dominance</a></td><td><code>cat_dominance_positional</code></td><td>1</td><td>Both forms above on a given relation matrix (map = FALSE and TRUE).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/netrankr.html">netrankr</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">Empty relation.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Equal rows dominate each other.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Infinite distances are valid entries; two rows both infinite at a position compare equal there.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">The relation matrix may be weighted; the comparison is on its entries.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details></div>

## Positional dominance {#cat_dominance_positional}

Measure id: `cat_dominance_positional`. Original family: Roles and positions.

**Definition.** Positional dominance.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dominance_positional-netrankr">details</a></td><td><code>positional_dominance</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dominance_positional-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: positional\_dominance.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)
{% endraw %}
