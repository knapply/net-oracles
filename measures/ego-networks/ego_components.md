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

## Ego\_summary / components {#ego_summary-components}

Measure id: `ego_summary:components`. Original family: Two-mode and bipartite.

**Definition.** Ego\_summary / components.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ego_components` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.number_weakly_connected_components / number_connected_components of the ego graph without its center` |  |
| `ego_components` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::count_components(induced_subgraph(g, ego(g, 1, v, 'all', mindist = 1)), mode = 'weak')` |  |
| `ego_components_in` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.number_weakly_connected_components(nx.ego_graph(G.reverse(), v, center = False))` |  |
| `ego_components_in` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::count_components(induced_subgraph(g, ego(g, 1, v, 'in', mindist = 1)), mode = 'weak')` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
