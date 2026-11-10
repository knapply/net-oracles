---
title: "Minimum-weight matching"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Minimum-weight matching {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Matching. Concept id: `minimum_weight_matching`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(M\subseteq E\)</td><td>matching: a set of edges no two of which share an end</td></tr><tr><td>\(\nu(G)\)</td><td>size of a maximum matching</td></tr><tr><td>\(w(e)\)</td><td>edge weight</td></tr><tr><td>\(c(e)\)</td><td>cost of edge \(e\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

A matching of least total weight among the matchings of largest size, as input edge positions.

<div class="formula-block"><p class="formula-name"><strong>Minimum-weight maximum matching</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\min_{M\in\mathcal M_{\max}}\sum_{e\in M}w(e)\]</div><p class="formula-where">Least total weight among maximum-cardinality matchings (not among all matchings, since the empty set would win).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Minimum-cost full matching (Kuhn 1955; Jonker and Volgenant 1987)</strong> <span class="applies">applies to: bipartite</span></p><div class="formula">\[\min_{M\ \text{matching covering the smaller class}}\sum_{e\in M}c(e)\]</div><p class="formula-where">The assignment problem: every node of the smaller class is matched at least cost.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#min_weight_full_matching">Min weight full matching</a></td><td><code>min_weight_full_matching</code></td><td>1</td><td>A full matching of least total cost of a bipartite graph, as each node's mate (none if unmatched).</td></tr><tr><td><a href="#min_weight_matching">Min weight matching</a></td><td><code>min_weight_matching</code></td><td>1</td><td>The matching of least weight among maximum-cardinality matchings, as input edge positions.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">The empty matching.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">The empty matching.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Equal-cost matchings: the cost is unique, the matching is not.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables).">agrees</span></td></tr><tr><td title="Edges with a negative weight."><strong>Negative weights</strong></td><td class="def">Allowed: the minimum then prefers negative edges.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The node set splits into two classes with edges only between classes (periodic structure; two-mode data)."><strong>Bipartite or two-mode graph</strong></td><td class="def">The full-matching form applies; it needs the two classes.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random).">agrees</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Per component.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und).">agrees</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Negative weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Bipartite or two-mode graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (davis_twomode, southern_women, twomode_random). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## References {#concept-references}

[jonker1987shortest](../../references.html#jonker1987shortest), [kuhn1955hungarian](../../references.html#kuhn1955hungarian), [edmonds1965maximum](../../references.html#edmonds1965maximum), [edmonds1965paths](../../references.html#edmonds1965paths), [galil1986efficient](../../references.html#galil1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Min weight full matching {#min_weight_full_matching}

Measure id: `min_weight_full_matching`. Original family: Two-mode and bipartite.

**Definition.** A full matching of least total cost of a bipartite graph, as each node's mate (-1 if unmatched).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>minimum_weight_full_matching</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>min_weight_full_matching</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-12</td><td><code>nx.bipartite.minimum_weight_full_matching(G, top, weight = c): (total cost, 1 if it covers the smaller side); -1 where it raises</code></td><td></td></tr></tbody></table></div>

**References:** [jonker1987shortest](../../references.html#jonker1987shortest), [kuhn1955hungarian](../../references.html#kuhn1955hungarian)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Min weight matching {#min_weight_matching}

Measure id: `min_weight_matching`. Original family: Graph theory and combinatorics.

**Definition.** A matching of least total weight among the matchings of largest size, as input edge positions.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>min_weight_matching</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>matching_min_weight</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.min_weight_matching(G, weight = 'weight')</code></td><td></td></tr></tbody></table></div>

**References:** [edmonds1965maximum](../../references.html#edmonds1965maximum), [edmonds1965paths](../../references.html#edmonds1965paths), [galil1986efficient](../../references.html#galil1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
