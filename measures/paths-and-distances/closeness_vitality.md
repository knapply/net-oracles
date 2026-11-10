---
title: "Closeness vitality"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Closeness vitality {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Distance summaries. Concept id: `closeness_vitality`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\); every edge has a source and a target</td></tr><tr><td>\(W(G)\)</td><td>Wiener index: \(\sum_{\{s,t\}}d(s,t)\) over unordered pairs of distinct nodes (ordered pairs for a directed graph)</td></tr><tr><td>\(G-v\)</td><td>the graph without node \(v\) and its edges</td></tr></tbody></table></div>

## Definition {#concept-definition}

Wiener index of the network minus that of the network without the node, for every node.

<div class="formula-block"><p class="formula-name"><strong>Closeness vitality (Koschutzki et al. 2005)</strong> <span class="applies">applies to: connected</span></p><div class="formula">\[\mathrm{CV}(v)=W(G)-W(G-v)\]</div><p class="formula-where">The change in the sum of distances when \(v\) is deleted. Defined when both indices are finite: \(G\) connected and \(v\) not a cut node. Convention: \(W(G-v)=\infty\) for a cut node gives \(-\infty\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#dm_closeness_vitality">Closeness vitality</a></td><td><code>dm_closeness_vitality</code></td><td>2</td><td>\(W(G)-W(G-v)\) for every node from exact distances (the weighted form uses edge lengths).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/centiserve.html">centiserve</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">\(G-v\) has no nodes: \(W=0\), \(\mathrm{CV}=0\).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (single_node).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly two nodes."><strong>Two nodes</strong></td><td class="def">\(W(G)=1\), \(W(G-v)=0\): CV 1.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (pair).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">\(W(G)=\infty\): \(\infty-\infty\) or \(\infty-\text{finite}\): not defined or infinite.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A directed graph in which some node cannot reach another along edge directions although the graph may be weakly connected (not strongly connected)."><strong>Directed graph, unreachable pairs</strong></td><td class="def">Not strongly connected: \(W\) infinite.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (gnp_dir_sparse, weighted_dir, multi_loops_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Lengths replace counts.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">\(W(G)=\binom n2\), \(W(G-v)=\binom{n-1}2\): \(\mathrm{CV}=n-1\).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">Removing the centre disconnects the leaves: \(W(G-v)=\infty\): \(\mathrm{CV}=-\infty\).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (star8).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Two nodes</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (pair). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Directed graph, unreachable pairs</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (gnp_dir_sparse, weighted_dir, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Edge weights</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Complete graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Star</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (star8). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## References {#concept-references}

[gutman1994selected](../../references.html#gutman1994selected), [hage1995eccentricity](../../references.html#hage1995eccentricity), [klein1995hyper](../../references.html#klein1995hyper), [koschutzki2005centrality](../../references.html#koschutzki2005centrality), [latora2001efficient](../../references.html#latora2001efficient), [marchiori2000harmony](../../references.html#marchiori2000harmony), [randic1993novel](../../references.html#randic1993novel), [schultz1989topological](../../references.html#schultz1989topological)

## Closeness vitality {#dm_closeness_vitality}

Measure id: `dm_closeness_vitality`. Original family: Paths and distances.

**Definition.** Wiener index of the network minus that of the network without the node, for every node.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>closeness_vitality</code></td><td></td></tr><tr><td><a href="../../tools/centiserve.html">centiserve</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-dm_closeness_vitality-centiserve">details</a></td><td><code>closeness.vitality</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-dm_closeness_vitality-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: closeness.vitality.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>dm_closeness_vitality</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.closeness_vitality(G) (an error is undefined)</code></td><td></td></tr><tr><td><code>dm_closeness_vitality_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.closeness_vitality(G, weight = 'weight')</code></td><td></td></tr></tbody></table></div>

**References:** [gutman1994selected](../../references.html#gutman1994selected), [hage1995eccentricity](../../references.html#hage1995eccentricity), [klein1995hyper](../../references.html#klein1995hyper), [koschutzki2005centrality](../../references.html#koschutzki2005centrality), [latora2001efficient](../../references.html#latora2001efficient), [marchiori2000harmony](../../references.html#marchiori2000harmony), [randic1993novel](../../references.html#randic1993novel), [schultz1989topological](../../references.html#schultz1989topological)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [jalili2015centiserver](../../references.html#jalili2015centiserver)
{% endraw %}
