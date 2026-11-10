---
title: "Stochastic matrix"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Stochastic matrix {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Graph matrices. Concept id: `stochastic_matrix`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(A=(a_{uv})\)</td><td>adjacency matrix: \(a_{uv}\) is the number of edges from \(u\) to \(v\) (the sum of their weights when weighted)</td></tr><tr><td>\(d^{\text{out}}_u\)</td><td>out-strength \(\sum_v a_{uv}\)</td></tr><tr><td>\(P\)</td><td>row-stochastic transition matrix</td></tr></tbody></table></div>

## Definition {#concept-definition}

Stochastic matrix. Entries grouped here: Stochastic matrix.

*Definition partly written:* The tool function is known by name only; the normalization it applies and its handling of sinks are not recorded.

<div class="formula-block"><p class="formula-name"><strong>Transition matrix of the random walk (Kemeny and Snell 1960)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[P_{uv}=\frac{a_{uv}}{d^{\text{out}}_u}\]</div><p class="formula-where">Each row sums to 1; defined when \(d^{\text{out}}_u&gt;0\) for every node.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_matrix_stochastic">Stochastic matrix</a></td><td><code>cat_matrix_stochastic</code></td><td>1</td><td>The row-normalized adjacency matrix; the treatment of rows with no out-edges is a convention the formula does not fix.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/igraph.html">igraph (R)</a></th></tr></thead><tbody><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">A node with \(d^{\text{out}}_u=0\) gives \(0/0\): the row is not defined by the formula (conventions set it to 0, or to a self-loop, or to uniform).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">Every row is 0/0; the matrix is not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Strength replaces degree; negative weights can give negative entries, so the result is stochastic only for non-negative weights.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details></div>

## Stochastic matrix {#cat_matrix_stochastic}

Measure id: `cat_matrix_stochastic`. Original family: Matrices and spectra.

**Definition.** Stochastic matrix.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_matrix_stochastic-igraph">details</a></td><td><code>stochastic_matrix</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_matrix_stochastic-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: stochastic\_matrix.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
