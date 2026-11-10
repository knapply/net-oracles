---
title: "Ego size"
layout: default
parent: "Ego networks"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Ego size {#concept-top}

Family: [Ego networks](index.html). Subfamily: Ego measures. Concept id: `ego_size`. 1 measure.

## Definition {#concept-definition}

Number of nodes within a range of steps from each node (ego included when the range starts at 0).

*Definition not yet written.*

## References {#concept-references}

[staudt2016networkit](../../references.html#staudt2016networkit)

## Ego size {#ego_size}

Measure id: `ego_size`. Original family: Descriptive statistics.

**Definition.** Number of nodes within a range of steps from each node (ego included when the range starts at 0).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>ego_size</code></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-ego_size-ucinet">details</a></td><td><code>Ego network density, size, ties, ego betweenness, ego composition (egocomp, 6.845), alter heterogeneity (IQV, Blau, Shannon; option to ignore ego's category, 6.</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-ego_size-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ego_size</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>len(nx.ego_graph(G, v, radius = 1, undirected = True))</code></td><td></td></tr><tr><td><code>ego_size</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>igraph::ego_size(g, order = 1, mode = 'all', mindist = 0)</code></td><td></td></tr><tr><td><code>ego_size_in</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>len(nx.ego_graph(G.reverse(), v, radius = 1))</code></td><td></td></tr><tr><td><code>ego_size_in</code></td><td>igraph (R)</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>igraph::ego_size(g, order = 1, mode = 'in')</code></td><td></td></tr><tr><td><code>ego_size_order2</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>len(nx.ego_graph(G, v, radius = 2, undirected = True))</code></td><td></td></tr><tr><td><code>ego_size_order2</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>igraph::ego_size(g, order = 2, mode = 'all')</code></td><td></td></tr><tr><td><code>ego_size_out</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>len(nx.ego_graph(G, v, radius = 1)) (successors)</code></td><td></td></tr><tr><td><code>ego_size_out</code></td><td>igraph (R)</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>igraph::ego_size(g, order = 1, mode = 'out')</code></td><td></td></tr></tbody></table></div>

**References:** [staudt2016networkit](../../references.html#staudt2016networkit)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
