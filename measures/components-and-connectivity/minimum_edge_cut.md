---
title: "Minimum edge cut"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Minimum edge cut {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Cuts and separators. Concept id: `minimum_edge_cut`. 2 measures.

## Definition {#concept-definition}

A smallest set of edges whose removal disconnects the network.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#edge_cut">Edge cut</a></td><td><code>edge_cut</code></td><td>2</td></tr><tr><td><a href="#st_edge_cut">St edge cut</a></td><td><code>st_edge_cut</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[esfahanian1984computing](../../references.html#esfahanian1984computing), [even1975algorithm](../../references.html#even1975algorithm), [even1975network](../../references.html#even1975network), [ford1956maximal](../../references.html#ford1956maximal), [hagberg2008exploring](../../references.html#hagberg2008exploring), [menger1927allgemeinen](../../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../../references.html#schnorr1979bottlenecks)

## Edge cut {#edge_cut}

Measure id: `edge_cut`. Original family: Components and connectivity.

**Definition.** A smallest set of edges whose removal disconnects the network.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-edge_cut-networkit">details</a></td><td><code>EdgeCut</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-edge_cut-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: EdgeCut.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>conn_edge_cut</code></td><td>NetworkX</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) disconnected</td><td>defaults</td><td>abs 0, rel 0</td><td><code>[len(nx.minimum_edge_cut(G)), 1]</code></td><td>as for conn_node_cut</td></tr></tbody></table></div>

**References:** [esfahanian1984computing](../../references.html#esfahanian1984computing), [even1975algorithm](../../references.html#even1975algorithm), [even1975network](../../references.html#even1975network), [ford1956maximal](../../references.html#ford1956maximal), [hagberg2008exploring](../../references.html#hagberg2008exploring), [menger1927allgemeinen](../../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../../references.html#schnorr1979bottlenecks)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [staudt2016networkit](../../references.html#staudt2016networkit)

## St edge cut {#st_edge_cut}

Measure id: `st_edge_cut`. Original family: Components and connectivity.

**Definition.** St edge cut.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>conn_st_edge_cut</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.connectivity.minimum_st_edge_cut(G, 0, n - 1), as pairs (u, v)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
