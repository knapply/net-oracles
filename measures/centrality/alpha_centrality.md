---
title: "Alpha centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Alpha centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `alpha_centrality`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(A\)</td><td>adjacency matrix: \(A_{uv}\) is the number of edges from \(u\) to \(v\), or their total weight for a weighted graph</td></tr><tr><td>\(\alpha\)</td><td>attenuation of indirect influence</td></tr><tr><td>\(e\)</td><td>exogenous source vector (all ones by default)</td></tr><tr><td>\(\lambda_1\)</td><td>largest eigenvalue of \(A\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Alpha centrality. Entries grouped here: Alpha.

<div class="formula-block"><p class="formula-name"><strong>Alpha centrality (Bonacich and Lloyd 2001)</strong> <span class="applies">applies to: directed, weighted</span></p><div class="formula">\[x=\alpha A^{\mathsf T}x+e\quad\Longleftrightarrow\quad x=(I-\alpha A^{\mathsf T})^{-1}e\]</div><p class="formula-where">Each node receives an exogenous amount \(e_v\) plus \(\alpha\) times the scores of its in-neighbours. The solution exists when \(I-\alpha A^{\mathsf T}\) is non-singular, and the series converges for \(\alpha&lt;1/\lambda_1\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_alpha">Alpha</a></td><td><code>cat_alpha</code></td><td>1</td><td>The formula above for the given \(\alpha\) and exogenous vector.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/pyigraph.html">igraph (Python)</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">\(x=e\) (no edges), or \(e/(1-\alpha A_{vv})\) with a loop.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">\(x=e\): scores equal the exogenous input.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">\(A_{vv}\) enters the equation; a loop adds a self-feedback term.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">\(A\) counts parallel edges, so influence is multiplied.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">The transpose matters: score flows along edge direction from source to target.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Weights enter \(A\) as strengths.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Edges with a negative weight."><strong>Negative weights</strong></td><td class="def">The linear system is still defined; the interpretation as attenuated walks is lost.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(\alpha\ge 1/\lambda_1\): the walk series diverges although the linear solution may exist; \(\alpha=1/\lambda_i\) makes the matrix singular.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Negative weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Alpha {#cat_alpha}

Measure id: `cat_alpha`. Original family: Graph theory and combinatorics.

**Definition.** Alpha.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_alpha-pyigraph">details</a></td><td><code>alpha</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_alpha-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: alpha.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
