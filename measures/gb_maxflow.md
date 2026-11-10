---
title: "Maxflow"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Maxflow

Family: Traversal, trees and DAGs. Identifier: `gb_maxflow`.

## Definition

Maxflow.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_maxflow` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.maximum_flow_value(D, 0, n - 1, flow_func=edmonds_karp), D the simple graph with capacity = weight` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
