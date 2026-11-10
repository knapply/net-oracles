---
title: "Constant Potts model"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Constant Potts model {#concept-top}

Family: [Communities](index.html). Subfamily: Other detection algorithms. Concept id: `constant_potts_model`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\); every edge has a source and a target (the ends of an undirected edge are interchangeable)</td></tr><tr><td>\(e_c\)</td><td>edge weight inside community \(c\)</td></tr><tr><td>\(n_c\)</td><td>number of nodes of \(c\)</td></tr><tr><td>\(\gamma\)</td><td>resolution: the minimum internal density of a community</td></tr></tbody></table></div>

## Definition {#concept-definition}

Constant Potts model. Entries grouped here: Constant potts model (community).

*Note:* Documented only (NetworkX), never run; the formula is that of Traag, Van Dooren and Nesterov 2011.

<div class="formula-block"><p class="formula-name"><strong>Constant Potts model (Traag et al. 2011)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\mathcal H=-\sum_c\Bigl[e_c-\gamma\binom{n_c}{2}\Bigr]\]</div><p class="formula-where">Rewards edges inside communities and penalizes community size at a constant rate \(\gamma\) per pair; unlike modularity it is resolution-limit free. Minimized over partitions (a maximization of the negative).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_constant_model_potts-community">Constant potts model (community)</a></td><td><code>cat_constant_model_potts@community</code></td><td>1</td><td>The constant Potts model value of a partition.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">\(\mathcal H\le0\); the best partition is singletons for \(\gamma&gt;0\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">\(\binom{1}{2}=0\): contributes 0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Not edges between distinct nodes in this pair-based form.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Add to \(e_c\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Weights add to \(e_c\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(\gamma\) is a density threshold in \([0,1]\) for unweighted graphs.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A group, source set, target set or sample that is empty, a single node, or the whole node set."><strong>Degenerate group or subset input</strong></td><td class="def">Empty communities contribute 0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details><details><summary>Degenerate group or subset input</summary><ul><li>No tool entries.</li></ul></details></div>

## Constant potts model (community) {#cat_constant_model_potts-community}

Measure id: `cat_constant_model_potts@community`. Original family: Statistical fitting.

**Definition.** Constant potts model (community).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_constant_model_potts-community-networkx">details</a></td><td><code>constant_potts_model</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_constant_model_potts-community-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: constant\_potts\_model.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
