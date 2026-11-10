---
title: "Ego network components"
layout: default
parent: "Ego networks"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Ego network components {#concept-top}

Family: [Ego networks](index.html). Subfamily: Ego measures. Concept id: `ego_components`. 1 measure.

## Definition {#concept-definition}

Ego network components. Entries grouped here: Ego\_summary / components.

*Definition not yet written.*

## Ego\_summary / components {#ego_summary-components}

Measure id: `ego_summary:components`. Original family: Two-mode and bipartite.

**Definition.** Ego\_summary / components.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ego_components</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.number_weakly_connected_components / number_connected_components of the ego graph without its center</code></td><td></td></tr><tr><td><code>ego_components</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>igraph::count_components(induced_subgraph(g, ego(g, 1, v, 'all', mindist = 1)), mode = 'weak')</code></td><td></td></tr><tr><td><code>ego_components_in</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.number_weakly_connected_components(nx.ego_graph(G.reverse(), v, center = False))</code></td><td></td></tr><tr><td><code>ego_components_in</code></td><td>igraph (R)</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>igraph::count_components(induced_subgraph(g, ego(g, 1, v, 'in', mindist = 1)), mode = 'weak')</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
