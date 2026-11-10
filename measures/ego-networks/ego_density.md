---
title: "Ego network density"
layout: default
parent: "Ego networks"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Ego network density {#concept-top}

Family: [Ego networks](index.html). Subfamily: Ego measures. Concept id: `ego_density`. 1 measure.

## Definition {#concept-definition}

Ego network density. Entries grouped here: Ego\_summary / density.

*Definition not yet written.*

## Ego\_summary / density {#ego_summary-density}

Measure id: `ego_summary:density`. Original family: Two-mode and bipartite.

**Definition.** Ego\_summary / density.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-ego_summary-density-ucinet">details</a></td><td><code>egodensity</code></td><td>published documentation</td></tr><tr><td><a href="../../tools/egor.html">egor</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-ego_summary-density-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ego_density</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-14</td><td><code>nx.density(nx.ego_graph(simple G, v, undirected = True, center = False)); undefined below two alters</code></td><td></td></tr><tr><td><code>ego_density</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-14</td><td><code>igraph::edge_density(induced_subgraph(simplify(g), ego(g, 1, v, 'all', mindist = 1)))</code></td><td></td></tr><tr><td><code>ego_density</code></td><td>egor</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-14</td><td><code>egor::ego_density(egor object, directed = 'directed' | 'undirected')</code></td><td></td></tr><tr><td><code>ego_density_out</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-14</td><td><code>nx.density(nx.ego_graph(simple G, v, center = False)); undefined below two alters</code></td><td></td></tr><tr><td><code>ego_density_out</code></td><td>igraph (R)</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-14</td><td><code>igraph::edge_density(induced_subgraph(simplify(g), ego(g, 1, v, 'out', mindist = 1)))</code></td><td></td></tr><tr><td><code>ego_density_out</code></td><td>egor</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-14</td><td><code>egor::ego_density(egor object of out-neighbours, directed = 'directed')</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_egor](../../references.html#tool_egor)
{% endraw %}
