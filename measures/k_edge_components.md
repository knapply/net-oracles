---
title: "K edge components"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# K edge components

Family: Components and connectivity. Identifier: `k_edge_components`.

## Definition

K edge components.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `k_edge_components` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_k_edge_components_2` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.k_edge_components(G, k = 2)` |  |
| `conn_k_edge_components_3` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.k_edge_components(G, k = 3)` |  |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F028](../findings.html#f028) | NetworkX | limitation | k\_edge\_components hits the recursion limit near n = 1000 |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
