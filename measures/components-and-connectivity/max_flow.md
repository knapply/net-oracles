---
title: "Maximum flow"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Maximum flow {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Flows and flow trees. Concept id: `max_flow`. 2 measures.

## Definition {#concept-definition}

Maximum flow from a set of sources to a set of sinks (Dinic), with the flow on every edge.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Max flow](#max_flow) | `max_flow` | 7 |
| [Maxflow](#gb_maxflow) | `gb_maxflow` | 1 |

## References {#concept-references}

[dinic1970algorithm](../../references.html#dinic1970algorithm), [ford1956maximal](../../references.html#ford1956maximal), [ford1962flows](../../references.html#ford1962flows), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Max flow {#max_flow}

Measure id: `max_flow`. Original family: Components and connectivity.

**Definition.** Maximum flow from a set of sources to a set of sinks (Dinic), with the flow on every edge.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `boykov_kolmogorov; capacity_scaling; dinitz; edmonds_karp; maximum_flow; maximum_flow_value; preflow_push; shortest_augmenting_path` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `max_flow` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `maxflow; maxflow_value` | API listing |
| [sna](../../tools/sna.html) | · reported in docs | `maxflow` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `boykov_kolmogorov_max_flow; edmonds_karp_max_flow; push_relabel_max_flow` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `EdmondsKarp` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `boykov_kolmogorov_max_flow; edmonds_karp_max_flow; push_relabel_max_flow` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `flow_max_flow_valid` | NetworkX | any | agrees |  |  | abs 1e-09, rel 1e-09 | `[nx.maximum_flow_value(G, 0, n - 1), 1]: the reference value's edge flows must respect capacities, conserve flow, and carry the maximum value` |  |
| `flow_max_flow_valid_multi` | NetworkX | any | agrees |  |  | abs 1e-09, rel 1e-09 | `[nx.maximum_flow_value(H, 'S', 'T'), 1] with H as for flow_max_value_multi` |  |
| `flow_max_value` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.maximum_flow_value(G, 0, n - 1, capacity = 'capacity')` |  |
| `flow_max_value_multi` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.maximum_flow_value(H, 'S', 'T'), H = G plus arcs S -> 0, S -> 1, n - 2 -> T, n - 1 -> T without a capacity (infinite)` |  |

**References:** [dinic1970algorithm](../../references.html#dinic1970algorithm), [ford1956maximal](../../references.html#ford1956maximal), [ford1962flows](../../references.html#ford1962flows), [hagberg2008exploring](../../references.html#hagberg2008exploring)

**Tools cited:** [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit)

## Maxflow {#gb_maxflow}

Measure id: `gb_maxflow`. Original family: Traversal, trees and DAGs.

**Definition.** Maxflow.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_maxflow` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.maximum_flow_value(D, 0, n - 1, flow_func=edmonds_karp), D the simple graph with capacity = weight` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
