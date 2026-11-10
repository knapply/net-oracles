---
title: "Reachability"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Reachability {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Efficiency and reachability. Concept id: `reachability`. 3 measures.

## Definition {#concept-definition}

Reachability. Entries grouped here: Reachability; Reachable Nodes; Reachdist.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#reachability">Reachability</a></td><td><code>reachability</code></td><td>5</td></tr><tr><td><a href="#cat_reachable">Reachable Nodes</a></td><td><code>cat_reachable</code></td><td>1</td></tr><tr><td><a href="#cat_reachdist">Reachdist</a></td><td><code>cat_reachdist</code></td><td>1</td></tr></tbody></table></div>

## Reachability {#reachability}

Measure id: `reachability`. Original family: Paths and distances.

**Definition.** Reachability.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>has_path; is_reachable</code></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>neighborhood_size</code></td><td></td></tr><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-reachability-rustworkx">details</a></td><td><code>digraph_has_path; graph_has_path; has_path</code></td><td>API listing</td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-reachability-ucinet">details</a></td><td></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-reachability-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: digraph\_has\_path; graph\_has\_path; has\_path.
- <a id="why-reachability-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>reachability</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>len(nx.descendants(G, v)), or len(nx.node_connected_component(G, v)) - 1 if undirected</code></td><td></td></tr><tr><td><code>reachability</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>igraph::ego_size(g, order = vcount(g), mode = 'out') - 1</code></td><td></td></tr><tr><td><code>reachability</code></td><td>igraph (Python)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>python-igraph: [x - 1 for x in gu.neighborhood_size(order=everything, mode="out")]</code></td><td></td></tr><tr><td><code>reachability_all</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>len(nx.node_connected_component(G.to_undirected(), v)) - 1</code></td><td></td></tr><tr><td><code>reachability_all</code></td><td>igraph (R)</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>igraph::ego_size(g, order = vcount(g), mode = 'all') - 1</code></td><td></td></tr><tr><td><code>reachability_all</code></td><td>igraph (Python)</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>python-igraph: [x - 1 for x in gu.neighborhood_size(order=everything, mode="all")]</code></td><td></td></tr><tr><td><code>reachability_in</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>len(nx.ancestors(G, v))</code></td><td></td></tr><tr><td><code>reachability_in</code></td><td>igraph (R)</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>igraph::ego_size(g, order = vcount(g), mode = 'in') - 1</code></td><td></td></tr><tr><td><code>reachability_in</code></td><td>igraph (Python)</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>python-igraph: [x - 1 for x in gu.neighborhood_size(order=everything, mode="in")]</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)

## Reachable Nodes {#cat_reachable}

Measure id: `cat_reachable`. Original family: Paths and distances.

**Definition.** Reachable Nodes.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_reachable-networkit">details</a></td><td><code>ReachableNodes</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_reachable-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: ReachableNodes.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Reachdist {#cat_reachdist}

Measure id: `cat_reachdist`. Original family: Paths and distances.

**Definition.** Reachdist.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/bct.html">BCT (Octave)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_reachdist-bct">details</a></td><td><code>reachdist</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_reachdist-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: reachdist.

**Tools cited:** [rubinov2010complex](../../references.html#rubinov2010complex)
{% endraw %}
