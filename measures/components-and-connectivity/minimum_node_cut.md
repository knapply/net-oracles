---
title: "Minimum node cut"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Minimum node cut {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Cuts and separators. Concept id: `minimum_node_cut`. 3 measures.

## Definition {#concept-definition}

A smallest set of nodes whose removal disconnects the network.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#min_node_cut">Min node cut</a></td><td><code>min_node_cut</code></td><td>1</td></tr><tr><td><a href="#node_cut">Node cut</a></td><td><code>node_cut</code></td><td>3</td></tr><tr><td><a href="#st_node_cut">St node cut</a></td><td><code>st_node_cut</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[esfahanian1984computing](../../references.html#esfahanian1984computing), [even1975algorithm](../../references.html#even1975algorithm), [even1975network](../../references.html#even1975network), [ford1956maximal](../../references.html#ford1956maximal), [hagberg2008exploring](../../references.html#hagberg2008exploring), [menger1927allgemeinen](../../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../../references.html#schnorr1979bottlenecks)

## Min node cut {#min_node_cut}

Measure id: `min_node_cut`. Original family: Components and connectivity.

**Definition.** Min node cut.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>flow_min_node_cut</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>len(nx.connectivity.minimum_st_node_cut(G, 0, n - 1)) on the simple graph; -1 if G.has_edge(0, n - 1)</code></td><td></td></tr><tr><td><code>flow_min_node_cut_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.minimum_cut_value(H, '0B', '(n-1)A') on the split digraph H: arcs vA -&gt; vB of capacity (v mod 3) + 1 and uB -&gt; vA for each arc u -&gt; v without a capacity (infinite)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Node cut {#node_cut}

Measure id: `node_cut`. Original family: Components and connectivity.

**Definition.** A smallest set of nodes whose removal disconnects the network.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>minimum_edge_cut; minimum_node_cut; minimum_st_edge_cut; minimum_st_node_cut</code></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-node_cut-igraph">details</a></td><td><code>is_min_separator; is_separator; min_separators; min_st_separators; stCuts; st_cuts; st_min_cuts</code></td><td>API listing</td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-node_cut-pyigraph">details</a></td><td><code>all_minimal_st_separators; all_st_cuts; all_st_mincuts; is_minimal_separator; is_separator; minimum_size_separators</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-node_cut-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: is\_min\_separator; is\_separator; min\_separators; min\_st\_separators; stCuts; st\_cuts; st\_min\_cuts.
- <a id="why-node_cut-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: all\_minimal\_st\_separators; all\_st\_cuts; all\_st\_mincuts; is\_minimal\_separator; is\_separator; minimum\_size\_separators.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>conn_node_cut</code></td><td>NetworkX</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) disconnected</td><td>defaults</td><td>abs 0, rel 0</td><td><code>[len(nx.minimum_node_cut(G)), 1]</code></td><td>NetworkX raises an error for a network that is not connected; the reference returns the empty cut.</td></tr><tr><td><code>conn_node_cut_networkx</code></td><td>NetworkX</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) disconnected</td><td>defaults</td><td>abs 0, rel 0</td><td><code>[len(nx.minimum_node_cut(G)), 1]</code></td><td>as for conn_node_cut</td></tr></tbody></table></div>

**References:** [esfahanian1984computing](../../references.html#esfahanian1984computing), [even1975algorithm](../../references.html#even1975algorithm), [even1975network](../../references.html#even1975network), [ford1956maximal](../../references.html#ford1956maximal), [hagberg2008exploring](../../references.html#hagberg2008exploring), [menger1927allgemeinen](../../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../../references.html#schnorr1979bottlenecks)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## St node cut {#st_node_cut}

Measure id: `st_node_cut`. Original family: Components and connectivity.

**Definition.** St node cut.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>conn_st_node_cut</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>[len(nx.connectivity.minimum_st_node_cut(G, 0, n - 1)), 1]; -1 if G.has_edge(0, n - 1)</code></td><td></td></tr><tr><td><code>conn_st_node_cut_networkx</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>sorted(nx.connectivity.minimum_st_node_cut(G, 0, n - 1))</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
