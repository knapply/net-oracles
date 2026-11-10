---
title: "Conductance"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Conductance {#concept-top}

Family: [Communities](index.html). Subfamily: Partition and cover quality. Concept id: `conductance`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\); every edge has a source and a target (the ends of an undirected edge are interchangeable)</td></tr><tr><td>\(S\)</td><td>a node set</td></tr><tr><td>\(\mathrm{cut}(S)\)</td><td>weight of edges between \(S\) and \(V\setminus S\)</td></tr><tr><td>\(\mathrm{vol}(S)=\sum_{v\in S}k_v\)</td><td>total degree of \(S\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Conductance. Entries grouped here: Isolated Interpartition Conductance; Set Conductance.

*Definition partly written:* cat\_conductance\_set and cat\_conductance\_interpartition\_isolated (NetworKit) are documented only and were never run; the interpartition form's aggregation over a partition (an average over communities, or the isolated variant) is not recorded in the sources.

<div class="formula-block"><p class="formula-name"><strong>Conductance of a set (Kannan, Vempala and Vetta 2004)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\phi(S)=\frac{\mathrm{cut}(S)}{\min\bigl(\mathrm{vol}(S),\mathrm{vol}(V\setminus S)\bigr)}\]</div><p class="formula-where">Fraction of the edge ends of the smaller side that leave the set; 0 for a union of components. Not defined when the smaller volume is 0.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_conductance_interpartition_isolated">Isolated Interpartition Conductance</a></td><td><code>cat_conductance_interpartition_isolated</code></td><td>1</td><td>Documented for NetworKit as isolated interpartition conductance of a partition; its aggregation is not recorded.</td></tr><tr><td><a href="#cat_conductance_set">Set Conductance</a></td><td><code>cat_conductance_set</code></td><td>1</td><td>The conductance \(\phi(S)\) of one node set.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkit.html">NetworKit</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">Not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A group, source set, target set or sample that is empty, a single node, or the whole node set."><strong>Degenerate group or subset input</strong></td><td class="def">An empty set or the whole node set has \(\mathrm{vol}=0\) on one side: not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">A set of isolates has volume 0: not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop adds to the volume but never to the cut.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Parallel edges add to the cut and the volume.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Weights enter cut and volume.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">A component has conductance 0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">\(\phi(S)=\frac{|S|(n-|S|)}{\min(|S|,n-|S|)(n-1)}\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Degenerate group or subset input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details></div>

## Isolated Interpartition Conductance {#cat_conductance_interpartition_isolated}

Measure id: `cat_conductance_interpartition_isolated`. Original family: Communities.

**Definition.** Isolated Interpartition Conductance.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_conductance_interpartition_isolated-networkit">details</a></td><td><code>IsolatedInterpartitionConductance</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_conductance_interpartition_isolated-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: IsolatedInterpartitionConductance.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Set Conductance {#cat_conductance_set}

Measure id: `cat_conductance_set`. Original family: Communities.

**Definition.** Set Conductance.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_conductance_set-networkit">details</a></td><td><code>SetConductance</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_conductance_set-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: SetConductance.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
