---
title: "Local node connectivity"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Local node connectivity {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connectivity numbers. Concept id: `local_node_connectivity`. 4 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\), \(m=|E|\); every edge has a source and a target (the ends of an undirected edge are interchangeable)</td></tr><tr><td>\(\kappa(s,t)\)</td><td>maximum number of internally node-disjoint \(s\)-\(t\) paths (Menger 1927); for non-adjacent \(s,t\) the minimum number of nodes whose removal separates them</td></tr><tr><td>\(\lambda(s,t)\)</td><td>the edge analogue</td></tr></tbody></table></div>

## Definition {#concept-definition}

Local node connectivity of every ordered pair, as an n-by-n matrix.

<div class="formula-block"><p class="formula-name"><strong>Local node connectivity</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\kappa(s,t)=\min\{|X|:X\subseteq V\setminus\{s,t\},\ s,t\text{ separated in }G-X\}\quad(s,t\text{ non-adjacent})\]</div><p class="formula-where">For adjacent nodes no node set separates them, so the separator form is not defined and the path form (counting the direct edge as one path) applies. Computed by maximum flow in a node-split digraph (Even and Tarjan 1975).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Average node connectivity</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\bar\kappa(G)=\frac{\sum_{s\ne t}\kappa(s,t)}{n(n-1)}\]</div><p class="formula-where">Mean of \(\kappa(s,t)\) over ordered pairs.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#all_pairs_node">All pairs node</a></td><td><code>all_pairs_node</code></td><td>1</td><td>\(\kappa(s,t)\) for every ordered pair as an \(n\times n\) matrix (0 on the diagonal).</td></tr><tr><td><a href="#ap_local_connectivity">Ap local connectivity</a></td><td><code>ap_local_connectivity</code></td><td>1</td><td>The greedy approximation of \(\kappa(s,t)\) by successive node-disjoint shortest paths, with an optional cutoff on the number of paths.</td></tr><tr><td><a href="#average_node">Average node</a></td><td><code>average_node</code></td><td>2</td><td>The mean \(\bar\kappa(G)\) over ordered pairs.</td></tr><tr><td><a href="#local_connectivity">Local connectivity</a></td><td><code>local_connectivity</code></td><td>1</td><td>\(\kappa(s,t)\) or \(\lambda(s,t)\) for one pair (node 0 to node \(n-1\)).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/graphtool.html">graph-tool</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">No pair.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (single_node).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly two nodes."><strong>Two nodes</strong></td><td class="def">\(\kappa=1\) if tied (the direct edge).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (pair).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">0 across components.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A directed graph in which some node cannot reach another along edge directions although the graph may be weakly connected (not strongly connected)."><strong>Directed graph, unreachable pairs</strong></td><td class="def">0 when \(t\) is unreachable from \(s\); asymmetric for directed graphs.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (gnp_dir_sparse, weighted_dir, multi_loops_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Directed graphs give an asymmetric matrix.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Irrelevant.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Parallel edges do not add to node-disjoint paths beyond one direct edge.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">\(n-1\) for every pair.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">1 between leaves, 1 centre-leaf.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (star8).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">With a cutoff \(c\) the approximate value is at most \(c\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Two nodes</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (pair). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Directed graph, unreachable pairs</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (gnp_dir_sparse, weighted_dir, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Self-loops</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Complete graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Star</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (star8). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[esfahanian1984computing](../../references.html#esfahanian1984computing), [even1975algorithm](../../references.html#even1975algorithm), [even1975network](../../references.html#even1975network), [ford1956maximal](../../references.html#ford1956maximal), [harary1969graph](../../references.html#harary1969graph), [menger1927allgemeinen](../../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../../references.html#schnorr1979bottlenecks)

## All pairs node {#all_pairs_node}

Measure id: `all_pairs_node`. Original family: Components and connectivity.

**Definition.** Local node connectivity of every ordered pair, as an n-by-n matrix.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>conn_all_pairs_node</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.all_pairs_node_connectivity(G), with 0 on the diagonal</code></td><td></td></tr></tbody></table></div>

**References:** [esfahanian1984computing](../../references.html#esfahanian1984computing), [even1975algorithm](../../references.html#even1975algorithm), [even1975network](../../references.html#even1975network), [ford1956maximal](../../references.html#ford1956maximal), [harary1969graph](../../references.html#harary1969graph), [menger1927allgemeinen](../../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../../references.html#schnorr1979bottlenecks)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Ap local connectivity {#ap_local_connectivity}

Measure id: `ap_local_connectivity`. Original family: Graph theory and combinatorics.

**Definition.** Ap local connectivity.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ap_local_connectivity</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>[local_node_connectivity(G_sorted, 0, n - 1), local_node_connectivity(G_sorted, n - 1, 1, cutoff = 2)]</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Average node {#average_node}

Measure id: `average_node`. Original family: Components and connectivity.

**Definition.** Local node connectivity of every ordered pair, as an n-by-n matrix.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-average_node-graphtool">details</a></td><td><code>vertex_average</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-average_node-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: vertex\_average.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>conn_average_node</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-14</td><td><code>nx.average_node_connectivity(G)</code></td><td></td></tr></tbody></table></div>

**References:** [esfahanian1984computing](../../references.html#esfahanian1984computing), [even1975algorithm](../../references.html#even1975algorithm), [even1975network](../../references.html#even1975network), [ford1956maximal](../../references.html#ford1956maximal), [harary1969graph](../../references.html#harary1969graph), [menger1927allgemeinen](../../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../../references.html#schnorr1979bottlenecks)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)

## Local connectivity {#local_connectivity}

Measure id: `local_connectivity`. Original family: Components and connectivity.

**Definition.** Local connectivity.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>conn_local_edge</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.connectivity.local_edge_connectivity(G, 0, n - 1)</code></td><td></td></tr><tr><td><code>conn_local_node</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.connectivity.local_node_connectivity(G, 0, n - 1)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
