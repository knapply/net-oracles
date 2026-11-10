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

## References {#concept-references}

[staudt2016networkit](../../references.html#staudt2016networkit)

## Ego size {#ego_size}

Measure id: `ego_size`. Original family: Descriptive statistics.

**Definition.** Number of nodes within a range of steps from each node (ego included when the range starts at 0).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |
| [igraph (R)](../../tools/igraph.html) | ✓ checked, agrees | `ego_size` |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `Ego network density, size, ties, ego betweenness, ego composition (egocomp, 6.845), alter heterogeneity (IQV, Blau, Shannon; option to ignore ego's category, 6.` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ego_size` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.ego_graph(G, v, radius = 1, undirected = True))` |  |
| `ego_size` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = 1, mode = 'all', mindist = 0)` |  |
| `ego_size_in` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `len(nx.ego_graph(G.reverse(), v, radius = 1))` |  |
| `ego_size_in` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = 1, mode = 'in')` |  |
| `ego_size_order2` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.ego_graph(G, v, radius = 2, undirected = True))` |  |
| `ego_size_order2` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = 2, mode = 'all')` |  |
| `ego_size_out` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `len(nx.ego_graph(G, v, radius = 1)) (successors)` |  |
| `ego_size_out` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = 1, mode = 'out')` |  |

**References:** [staudt2016networkit](../../references.html#staudt2016networkit)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
