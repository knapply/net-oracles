---
title: "EigenTrust"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# EigenTrust {#concept-top}

Family: [Centrality](index.html). Subfamily: Spectral and walk-based. Concept id: `eigentrust`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(s_{ij}\)</td><td>local trust of \(i\) in \(j\) (edge value in \([0,1]\))</td></tr><tr><td>\(c_{ij}\)</td><td>normalized trust</td></tr></tbody></table></div>

## Definition {#concept-definition}

EigenTrust. Entries grouped here: Eigentrust.

<div class="formula-block"><p class="formula-name"><strong>EigenTrust (Kamvar et al. 2003)</strong> <span class="applies">applies to: directed, weighted</span></p><div class="formula">\[c_{ij}=\frac{\max(s_{ij},0)}{\sum_j\max(s_{ij},0)},\qquad t=\lim_{k\to\infty}\bigl(C^{\mathsf T}\bigr)^{k}c^{(0)},\quad c^{(0)}_i=\tfrac1{n}\]</div><p class="formula-where">Global trust values are the stationary vector of the row-normalized trust matrix: the principal left eigenvector. Negative local trust is clipped to 0.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_eigentrust">Eigentrust</a></td><td><code>cat_eigentrust</code></td><td>1</td><td>The limit above, computed by iteration until the total change over all nodes falls below a threshold; optionally normalized to sum 1.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/graphtool.html">graph-tool</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">\(t=1\) if normalized.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">Every row sum is 0: the row normalization is 0/0 and \(C\) is undefined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">A node with no positive outgoing trust has an undefined row \(c_{i\cdot}\) (0/0); the original algorithm replaces it by a pre-trusted distribution.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A self-trust \(s_{ii}\) enters the row as it is.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Edge values for parallel edges would be summed or must be given once; not covered.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Edges with a negative weight."><strong>Negative weights</strong></td><td class="def">Clipped to 0 before normalization by definition.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">Trust values must lie in \([0,1]\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Negative weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Eigentrust {#cat_eigentrust}

Measure id: `cat_eigentrust`. Original family: Matrices and spectra.

**Definition.** Eigentrust.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_eigentrust-graphtool">details</a></td><td><code>eigentrust</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_eigentrust-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: eigentrust.

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
