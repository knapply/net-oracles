---
title: "Ego network ties"
layout: default
parent: "Ego networks"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Ego network ties {#concept-top}

Family: [Ego networks](index.html). Subfamily: Ego measures. Concept id: `ego_ties`. 1 measure.

## Definition {#concept-definition}

Ego network ties. Entries grouped here: Ego\_summary / ties.

## Ego\_summary / ties {#ego_summary-ties}

Measure id: `ego_summary:ties`. Original family: Two-mode and bipartite.

**Definition.** Ego\_summary / ties.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |
| [igraph (R)](../../tools/igraph.html) | ✓ checked, agrees |  |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ego_ties` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.ego_graph(simple G, v, undirected = True, center = False).number_of_edges()` |  |
| `ego_ties` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::ecount(induced_subgraph(simplify(g), ego(g, 1, v, 'all', mindist = 1)))` |  |
| `ego_ties_order2` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.ego_graph(simple G, v, radius = 2, undirected = True, center = False).number_of_edges()` |  |
| `ego_ties_order2` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::ecount(induced_subgraph(simplify(g), ego(g, 2, v, 'all', mindist = 1)))` |  |
| `ego_ties_out` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.ego_graph(simple G, v, center = False).number_of_edges()` |  |
| `ego_ties_out` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::ecount(induced_subgraph(simplify(g), ego(g, 1, v, 'out', mindist = 1)))` |  |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
