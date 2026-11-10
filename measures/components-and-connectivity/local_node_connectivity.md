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

## Definition {#concept-definition}

Local node connectivity of every ordered pair, as an n-by-n matrix.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#all_pairs_node">All pairs node</a></td><td><code>all_pairs_node</code></td><td>1</td></tr><tr><td><a href="#ap_local_connectivity">Ap local connectivity</a></td><td><code>ap_local_connectivity</code></td><td>1</td></tr><tr><td><a href="#average_node">Average node</a></td><td><code>average_node</code></td><td>2</td></tr><tr><td><a href="#local_connectivity">Local connectivity</a></td><td><code>local_connectivity</code></td><td>1</td></tr></tbody></table></div>

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
