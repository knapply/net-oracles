---
title: "Graph edit distance"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Graph edit distance {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Isomorphism and subgraph matching. Concept id: `graph_edit_distance`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(c_{\mathrm{ni}},c_{\mathrm{nd}},c_{\mathrm{ns}},c_{\mathrm{ei}},c_{\mathrm{ed}},c_{\mathrm{es}}\)</td><td>costs of node/edge insertion, deletion and substitution (1, 1, 0 or 1 by default)</td></tr><tr><td>\(\phi\)</td><td>partial injective node mapping between the graphs</td></tr></tbody></table></div>

## Definition {#concept-definition}

Graph edit distance. Entries grouped here: Ged Walk; Graph edit distance.

*Definition partly written:* cat\_ged\_walk is known by name only.

<div class="formula-block"><p class="formula-name"><strong>Graph edit distance (Sanfeliu and Fu 1983; Abu-Aisheh et al. 2015)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\mathrm{GED}(G_1,G_2)=\min_{\phi}\Bigl(\sum_{\text{unmapped }v}c_{\mathrm{nd/ni}}+\sum_{v\mapsto\phi(v)}c_{\mathrm{ns}}+\sum_{\text{edges not preserved}}c_{\mathrm{ed/ei}}\Bigr)\]</div><p class="formula-where">The least total cost of node and edge insertions, deletions and substitutions that turn \(G_1\) into \(G_2\); exact computation is exponential, so it is feasible only for small graphs. With unit costs and no labels it counts the unmatched nodes and the edges that do not map onto edges.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_ged_walk">Ged Walk</a></td><td><code>cat_ged_walk</code></td><td>1</td><td>Graph edit distance by a walk-based method as listed by a documented tool; not specified in the sources.</td></tr><tr><td><a href="#ged">Graph edit distance</a></td><td><code>ged</code></td><td>2</td><td>The exact edit distance with unit costs, optionally with node and edge labels that must match for a free substitution.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/networkit.html">NetworKit</a></th><th><a href="../../tools/jgrapht.html">JGraphT</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">Distance to the empty graph is \(n+m\) (delete every node and edge).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">Two single nodes: distance 0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop and an ordinary edge are different edges: replacing one by the other costs a deletion and an insertion (2); a rule that substitutes at no cost changes the distance.</td><td><span class="st st-w st-conv" title="NetworkX&#x27;s graph_edit_distance substitutes a self-loop for an ordinary edge at no cost when the loop&#x27;s node is mapped onto one endpoint ((1, 1) against (0, 1), edit distance 0); the reference and the definition count deleting the loop and inserting the edge (2).">differs</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Arcs are compared as ordered pairs.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Edge weights are not edit costs unless a label comparison is set.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">Costs must be non-negative for the minimum to be a metric.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li><strong>NetworkX</strong>: differs. NetworkX's graph_edit_distance substitutes a self-loop for an ordinary edge at no cost when the loop's node is mapped onto one endpoint ((1, 1) against (0, 1), edit distance 0); the reference and the definition count deleting the loop and inserting the edge (2). <em>(conventions.json ged / ged)</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Ged Walk {#cat_ged_walk}

Measure id: `cat_ged_walk`. Original family: Paths and distances.

**Definition.** Ged Walk.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_ged_walk-networkit">details</a></td><td><code>GedWalk</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_ged_walk-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: GedWalk.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Graph edit distance {#ged}

Measure id: `ged`. Original family: Graph theory and combinatorics.

**Definition.** Graph edit distance.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>graph_edit_distance; optimal_edit_paths; optimize_edit_paths; optimize_graph_edit_distance</code></td><td></td></tr><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-ged-jgrapht">details</a></td><td><code>ZhangShashaTreeEditDistance</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-ged-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: ZhangShashaTreeEditDistance.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ged</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>loops</td><td>self_loops</td><td>abs 0, rel 0</td><td><code>nx.graph_edit_distance(G1, G2) with G2 = ged_pair(fixture)</code></td><td>NetworkX's graph_edit_distance substitutes a self-loop for an ordinary edge at no cost when the loop's node is mapped onto one endpoint ((1, 1) against (0, 1), edit distance 0); the reference and the definition count deleting the loop and inserting the edge (2). exact edit distance is exponential; networks of at most 10 nodes</td></tr><tr><td><code>ged_labels</code></td><td>NetworkX</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.graph_edit_distance(G1, G2, node_match = equal labels, edge_match = equal labels) with G2 = ged_pair(fixture)</code></td><td>exact edit distance is exponential; networks of at most 10 nodes</td></tr><tr><td><code>ged_node_labels</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>loops</td><td>self_loops</td><td>abs 0, rel 0</td><td><code>nx.graph_edit_distance(G1, G2, node_match = equal labels) with G2 = ged_pair(fixture)</code></td><td>NetworkX's graph_edit_distance substitutes a self-loop for an ordinary edge at no cost when the loop's node is mapped onto one endpoint ((1, 1) against (0, 1), edit distance 0); the reference and the definition count deleting the loop and inserting the edge (2). exact edit distance is exponential; networks of at most 10 nodes</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/similarity.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/similarity.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f003">F003</a></td><td>NetworkX</td><td>defect</td><td>graph_edit_distance substitutes a self-loop for an ordinary edge at no cost</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
