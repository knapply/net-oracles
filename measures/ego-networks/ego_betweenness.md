---
title: "Ego betweenness"
layout: default
parent: "Ego networks"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Ego betweenness {#concept-top}

Family: [Ego networks](index.html). Subfamily: Ego measures. Concept id: `ego_betweenness`. 1 measure.

## Definition {#concept-definition}

Ego betweenness. Entries grouped here: Ego\_summary / betweenness.

*Definition not yet written.*

## Ego\_summary / betweenness {#ego_summary-betweenness}

Measure id: `ego_summary:betweenness`. Original family: Two-mode and bipartite.

**Definition.** Ego\_summary / betweenness.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-ego_summary-betweenness-ucinet">details</a></td><td></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-ego_summary-betweenness-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ego_betweenness</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>nx.betweenness_centrality(nx.ego_graph(simple G, v, undirected = True), normalized = False)[v]</code></td><td></td></tr><tr><td><code>ego_betweenness</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>igraph::betweenness(make_ego_graph(simplify(g), 1, v, 'all')[[1]], ego)</code></td><td></td></tr><tr><td><code>ego_betweenness_order2</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>nx.betweenness_centrality(nx.ego_graph(simple G, v, radius = 2, undirected = True), normalized = False)[v]</code></td><td></td></tr><tr><td><code>ego_betweenness_out</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>nx.betweenness_centrality(nx.ego_graph(simple G, v), normalized = False)[v]</code></td><td></td></tr><tr><td><code>ego_betweenness_out</code></td><td>igraph (R)</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>igraph::betweenness(make_ego_graph(simplify(g), 1, v, 'out')[[1]], ego, directed = TRUE)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
