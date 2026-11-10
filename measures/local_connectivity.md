---
title: "Local connectivity"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Local connectivity

Family: Components and connectivity. Identifier: `local_connectivity`.

## Definition

Local connectivity.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_local_edge` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.connectivity.local_edge_connectivity(G, 0, n - 1)` |  |
| `conn_local_node` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.connectivity.local_node_connectivity(G, 0, n - 1)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
