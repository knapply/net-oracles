---
title: "Connected components"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Connected components {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connected components. Concept id: `connected_components`. 5 measures.

## Definition {#concept-definition}

Weak or strong components: a label for every node and the size of each component.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#components">Components</a></td><td><code>components</code></td><td>13</td></tr><tr><td><a href="#cat_component_count">Count components</a></td><td><code>cat_component_count</code></td><td>1</td></tr><tr><td><a href="#nxo_kosaraju">Kosaraju</a></td><td><code>nxo_kosaraju</code></td><td>1</td></tr><tr><td><a href="#cat_component_connected_parallel">Parallel Connected Components</a></td><td><code>cat_component_connected_parallel</code></td><td>1</td></tr><tr><td><a href="#strong_partition">Strong partition</a></td><td><code>strong_partition</code></td><td>2</td></tr></tbody></table></div>

## Components {#components}

Measure id: `components`. Original family: Descriptive statistics.

**Definition.** Weak or strong components: a label for every node and the size of each component.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>connected_components; is_biconnected; is_connected; is_strongly_connected; is_weakly_connected; kosaraju_strongly_connected_components; node_connected_component; number_connected_components; number_strongly_connected_components; number_weakly_connected_components; strongly_connected_components; weakly_connected_components</code></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>clusters; component_distribution; components; decompose; is_biconnected; is_connected; largest_component; subcomponent</code></td><td></td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>components; decompose; is_biconnected; is_connected; subcomponent</code></td><td></td></tr><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-components-sna">details</a></td><td><code>component.dist; component.largest; component.size.byvertex; components; is.connected</code></td><td>API listing</td></tr><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-components-graphtool">details</a></td><td><code>extract_largest_component; label_components; label_largest_component; label_out_component</code></td><td>API listing</td></tr><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>ConnectedComponents; StronglyConnectedComponents; WeaklyConnectedComponents</code></td><td></td></tr><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>connected_components; connected_subgraphs; is_connected; is_strongly_connected; is_weakly_connected; node_connected_component; number_connected_components; number_strongly_connected_components; number_weakly_connected_components; strongly_connected_components; weakly_connected_components</code></td><td></td></tr><tr><td><a href="../../tools/sknetwork.html">scikit-network</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>get_connected_components; get_largest_connected_component; is_connected</code></td><td></td></tr><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-components-jgrapht">details</a></td><td><code>ConnectivityInspector</code></td><td>API listing</td></tr><tr><td><a href="../../tools/boost.html">Boost Graph Library</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-components-boost">details</a></td><td><code>connected_components; incremental_components; st_connected; strong_components</code></td><td>API listing</td></tr><tr><td><a href="../../tools/bct.html">BCT (Octave)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-components-bct">details</a></td><td><code>get_components; number_of_components</code></td><td>API listing</td></tr><tr><td><a href="../../tools/gephi.html">Gephi toolkit</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>ConnectedComponents</code></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-components-ucinet">details</a></td><td><code>component; numcomp</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-components-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: component.dist; component.largest; component.size.byvertex; components; is.connected.
- <a id="why-components-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: extract\_largest\_component; label\_components; label\_largest\_component; label\_out\_component.
- <a id="why-components-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: ConnectivityInspector.
- <a id="why-components-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: connected\_components; incremental\_components; st\_connected; strong\_components.
- <a id="why-components-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: get\_components; number\_of\_components.
- <a id="why-components-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>components_strong</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.strongly_connected_components / nx.connected_components</code></td><td></td></tr><tr><td><code>components_strong</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>igraph::components(g, mode = 'strong')$membership</code></td><td></td></tr><tr><td><code>components_strong</code></td><td>igraph (Python)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>python-igraph: g.connected_components(mode="strong").membership</code></td><td></td></tr><tr><td><code>components_strong</code></td><td>NetworKit</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nk.components.StronglyConnectedComponents(G) (ConnectedComponents when undirected)</code></td><td></td></tr><tr><td><code>components_strong</code></td><td>rustworkx</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>rx.strongly_connected_components(G) (connected_components when undirected)</code></td><td></td></tr><tr><td><code>components_strong</code></td><td>scikit-network</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td>defaults</td><td>abs 0, rel 0</td><td><code>sknetwork.topology.get_connected_components(A, connection = 'strong')</code></td><td>scikit-network rejects an adjacency matrix without entries ('The input matrix is empty').</td></tr><tr><td><code>components_strong</code></td><td>Gephi toolkit</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>Gephi toolkit 0.11.3: ConnectedComponents, node column 'strongcompnum' (directed networks; 'componentnumber' for undirected)</code></td><td></td></tr><tr><td><code>components_weak</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.weakly_connected_components / nx.connected_components</code></td><td></td></tr><tr><td><code>components_weak</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>igraph::components(g, mode = 'weak')$membership</code></td><td></td></tr><tr><td><code>components_weak</code></td><td>igraph (Python)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>python-igraph: g.connected_components(mode="weak").membership</code></td><td></td></tr><tr><td><code>components_weak</code></td><td>NetworKit</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nk.components.WeaklyConnectedComponents(G) (ConnectedComponents when undirected)</code></td><td></td></tr><tr><td><code>components_weak</code></td><td>rustworkx</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>rx.weakly_connected_components(G) (connected_components when undirected)</code></td><td></td></tr><tr><td><code>components_weak</code></td><td>scikit-network</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td>defaults</td><td>abs 0, rel 0</td><td><code>sknetwork.topology.get_connected_components(A, connection = 'weak')</code></td><td>scikit-network rejects an adjacency matrix without entries ('The input matrix is empty').</td></tr><tr><td><code>components_weak</code></td><td>Gephi toolkit</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>Gephi toolkit 0.11.3: ConnectedComponents, node column 'componentnumber'</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [rubinov2010complex](../../references.html#rubinov2010complex), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx), [tool_sknetwork](../../references.html#tool_sknetwork)

## Count components {#cat_component_count}

Measure id: `cat_component_count`. Original family: Components and connectivity.

**Definition.** Count components.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_component_count-igraph">details</a></td><td><code>count_components</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_component_count-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: count\_components.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Kosaraju {#nxo_kosaraju}

Measure id: `nxo_kosaraju`. Original family: Graph theory and combinatorics.

**Definition.** Kosaraju.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nxo_kosaraju</code></td><td>NetworkX</td><td>directed</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges, ties</td><td>abs 0, rel 0</td><td><code>nx.kosaraju_strongly_connected_components(G), components in order</code></td><td>The backend leaves multigraphs to NetworkX (their adjacency order is not the edge order); the reference value's components are the same sets.</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Parallel Connected Components {#cat_component_connected_parallel}

Measure id: `cat_component_connected_parallel`. Original family: Components and connectivity.

**Definition.** Parallel Connected Components.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_component_connected_parallel-networkit">details</a></td><td><code>ParallelConnectedComponents</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_component_connected_parallel-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: ParallelConnectedComponents.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Strong partition {#strong_partition}

Measure id: `strong_partition`. Original family: Components and connectivity.

**Definition.** Strong partition.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>GabowStrongConnectivityInspector; KosarajuStrongConnectivityInspector</code></td><td></td></tr><tr><td><a href="../../tools/boost.html">Boost Graph Library</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>conn_strong_partition</code></td><td>JGraphT</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>JGraphT 1.5.2: new KosarajuStrongConnectivityInspector&lt;&gt;(g).stronglyConnectedSets() on a pseudograph</code></td><td></td></tr><tr><td><code>conn_strong_partition</code></td><td>Boost Graph Library</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>Boost Graph Library strong_components</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht), [siek2002boost](../../references.html#siek2002boost)
{% endraw %}
