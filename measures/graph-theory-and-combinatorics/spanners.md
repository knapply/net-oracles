---
title: "Spanners"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Spanners {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Spanners, contraction and reduction. Concept id: `spanners`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(t\)</td><td>stretch factor</td></tr><tr><td>\(H\)</td><td>spanning subgraph</td></tr></tbody></table></div>

## Definition {#concept-definition}

Spanners. Entries grouped here: Greedy Multiplicative Spanner; Spanner ok.

<div class="formula-block"><p class="formula-name"><strong>\(t\)-spanner (Baswana and Sen 2007)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[H\subseteq G,\quad d_H(u,v)\le t\,d_G(u,v)\ \ \forall u,v\]</div><p class="formula-where">A sparse subgraph that stretches no distance by more than \(t\). For \(t=2k-1\) the randomized algorithm gives expected size \(O(kn^{1+1/k})\). The graph itself is a \(t\)-spanner for every \(t\ge1\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_greedy_multiplicative_spanner">Greedy Multiplicative Spanner</a></td><td><code>cat_greedy_multiplicative_spanner</code></td><td>1</td><td>Greedy multiplicative spanner; documented only.</td></tr><tr><td><a href="#gb_spanner_ok">Spanner ok</a></td><td><code>gb_spanner_ok</code></td><td>1</td><td>The check that a computed spanner has stretch at most \(t\) (here 3) for every connected pair.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/jgrapht.html">JGraphT</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">The empty spanner.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Pairs in different components have \(d=\infty\) in both graphs; the condition holds trivially for them.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Spanners are defined for simple graphs; parallel edges are collapsed or rejected.</td><td><span class="st st-w st-nov" title="NetworkX&#x27;s spanner rejects multigraphs.">no value</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Distances are weighted lengths.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(t&lt;1\) cannot hold (\(d_H\ge d_G\)); \(t=1\) forces \(H\) to preserve all distances.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: no value. NetworkX's spanner rejects multigraphs. <em>(conventions.json gb_spanner_ok / gb_spanner_ok)</em></li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Greedy Multiplicative Spanner {#cat_greedy_multiplicative_spanner}

Measure id: `cat_greedy_multiplicative_spanner`. Original family: Graph theory and combinatorics.

**Definition.** Greedy Multiplicative Spanner.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_greedy_multiplicative_spanner-jgrapht">details</a></td><td><code>GreedyMultiplicativeSpanner</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_greedy_multiplicative_spanner-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: GreedyMultiplicativeSpanner.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Spanner ok {#gb_spanner_ok}

Measure id: `gb_spanner_ok`. Original family: Traversal, trees and DAGs.

**Definition.** Spanner ok.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>spanner</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_spanner_ok</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 0, rel 0</td><td><code>stretch check of nx.spanner(nx.Graph(M), 3, seed=1)</code></td><td>NetworkX's spanner rejects multigraphs.</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/traversal_b.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/traversal_b.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
