---
title: "N-cliques"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# N-cliques {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Relaxed cliques and subgroups. Concept id: `n_cliques`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>simple undirected graph (direction ignored, parallel edges merged, loops dropped) with node set \(V\), \(n=|V|\)</td></tr><tr><td>\(d_G(u,v)\)</td><td>geodesic distance in the whole graph \(G\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

n-cliques: maximal sets whose members are all within distance n of each other in the whole network.

<div class="formula-block"><p class="formula-name"><strong>n-clique (Luce 1950; Alba 1973)</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[S\text{ is an }n\text{-clique}\iff d_G(u,v)\le n\ \forall u,v\in S,\ \text{and }S\text{ is maximal with this property}\]</div><p class="formula-where">Maximal sets whose members are all within \(n\) steps of each other, with distances measured in the whole graph (the connecting paths may pass through nodes outside \(S\)). Equivalent to the maximal cliques of the \(n\)-th power graph. For \(n=1\) these are the cliques.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#n_cliques">N cliques</a></td><td><code>n_cliques</code></td><td>2</td><td>The maximal cliques of the graph that joins nodes at distance at most \(n\) (n=2 is the usual choice), optionally with a minimum size.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/ucinet.html">UCINET</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">No sets.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">One set of one node.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (single_node).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Nodes in different components are at infinite distance and are never in a common n-clique.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">One n-clique, the whole node set.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">For \(n=2\) the whole graph is one 2-clique.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (star8).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(n&lt;1\) is meaningless.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Complete graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Star</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (star8). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[alba1973graph](../../references.html#alba1973graph), [luce1950connectivity](../../references.html#luce1950connectivity), [mokken1979cliques](../../references.html#mokken1979cliques)

## N cliques {#n_cliques}

Measure id: `n_cliques`. Original family: Cohesion and subgroups.

**Definition.** n-cliques: maximal sets whose members are all within distance n of each other in the whole network.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-n_cliques-ucinet">details</a></td><td><code>ncliques</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-n_cliques-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>n_cliques_2</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.find_cliques on the graph joining nodes at distance &lt;= 2 (single_source_shortest_path_length, cutoff 2)</code></td><td></td></tr><tr><td><code>n_cliques_3_min4</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.find_cliques on the distance-3 power graph, keeping cliques of at least 4</code></td><td></td></tr></tbody></table></div>

**References:** [alba1973graph](../../references.html#alba1973graph), [luce1950connectivity](../../references.html#luce1950connectivity), [mokken1979cliques](../../references.html#mokken1979cliques)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
