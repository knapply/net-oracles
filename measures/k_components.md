---
title: "K components"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# K components

Family: Components and connectivity. Identifier: `k_components`.

## Definition

K components.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `k_components` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_k_components` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.k_components(G), each component of k as k * 1000 + node` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
