---
title: "K-center and Gon heuristic"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# K-center and Gon heuristic {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Independent sets and approximation. Concept id: `k_center`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(K\subseteq V\)</td><td>set of \(k\) centres</td></tr><tr><td>\(d(v,K)\)</td><td>distance from \(v\) to the nearest centre</td></tr></tbody></table></div>

## Definition {#concept-definition}

K-center and Gon heuristic. Entries grouped here: Gon Heuristic; KCenters.

*Definition partly written:* Defined from the textbook problem and the farthest-first heuristic without a cited primary source (Gonzalez 1985 is not among the checked bibliography).

<div class="formula-block"><p class="formula-name"><strong>\(k\)-centre problem</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\min_{|K|=k}\ \max_{v\in V}d(v,K)\]</div><p class="formula-where">Choose \(k\) centres to minimize the largest distance of a node to its nearest centre (NP-hard).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Farthest-first heuristic (Gon)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[K_1=\{v_1\},\quad K_{i+1}=K_i\cup\{\arg\max_vd(v,K_i)\}\]</div><p class="formula-where">Greedy choice with a 2-approximation guarantee for metric distances; the first centre and ties decide the output.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_gon_heuristic">Gon Heuristic</a></td><td><code>cat_gon_heuristic</code></td><td>1</td><td>The farthest-first (Gon) heuristic; documented only.</td></tr><tr><td><a href="#cat_centers_k">KCenters</a></td><td><code>cat_centers_k</code></td><td>1</td><td>\(k\) centres; documented only.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/sknetwork.html">scikit-network</a></th><th><a href="../../tools/jgrapht.html">JGraphT</a></th></tr></thead><tbody><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">A centre must reach every node: with \(k&lt;c\) components the objective is \(\infty\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(k\ge1\); for \(k\ge n\) every node is its own centre and the objective is 0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Equal farthest nodes: not fixed by the definition.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details></div>

## Gon Heuristic {#cat_gon_heuristic}

Measure id: `cat_gon_heuristic`. Original family: Graph theory and combinatorics.

**Definition.** Gon Heuristic.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_gon_heuristic-jgrapht">details</a></td><td><code>GonHeuristic</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_gon_heuristic-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: GonHeuristic.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## KCenters {#cat_centers_k}

Measure id: `cat_centers_k`. Original family: Graph theory and combinatorics.

**Definition.** KCenters.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sknetwork.html">scikit-network</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_centers_k-sknetwork">details</a></td><td><code>KCenters</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_centers_k-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: KCenters.

**Tools cited:** [tool_sknetwork](../../references.html#tool_sknetwork)
{% endraw %}
