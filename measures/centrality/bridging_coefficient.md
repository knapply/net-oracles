---
title: "Bridging coefficient"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Bridging coefficient {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `bridging_coefficient`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(k(v)\)</td><td>degree of \(v\): number of edge ends at \(v\) (a self-loop contributes 2 in an undirected graph)</td></tr><tr><td>\(N(v)\)</td><td>set of neighbours of \(v\) (nodes joined to \(v\) by an edge, \(v\) itself excluded)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Bridging coefficient. Entries grouped here: Bridging coefficient.

<div class="formula-block"><p class="formula-name"><strong>Bridging coefficient (Hwang et al. 2008)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[BC(v)=\frac{1/k(v)}{\sum_{u\in N(v)}1/k(u)}\]</div><p class="formula-where">Reciprocal of the degree of \(v\) relative to the reciprocal degrees of its neighbours; large when \(v\) has low degree among high-degree neighbours.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#bridging_coefficient">Bridging coefficient</a></td><td><code>bridging_coefficient</code></td><td>1</td><td>The formula above (documented in the tool; not run).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ucinet.html">UCINET</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">Not defined: \(N(v)=\emptyset\), the denominator is 0 and \(1/k(v)\) is \(1/0\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">Not defined (division by zero).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Defined on simple graphs; a loop would make \(v\) its own neighbour.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">Every degree is \(n-1\): the denominator is \((n-1)\cdot\frac1{n-1}=1\), so \(BC=1/(n-1)\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">Leaf: \((1/1)/(1/(n-1))=n-1\); centre: \((1/(n-1))/(n-1)=1/(n-1)^2\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Star</summary><ul><li>No tool entries.</li></ul></details></div>

## Bridging coefficient {#bridging_coefficient}

Measure id: `bridging_coefficient`. Original family: Roles and positions.

**Definition.** Bridging coefficient.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-bridging_coefficient-ucinet">details</a></td><td></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-bridging_coefficient-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
