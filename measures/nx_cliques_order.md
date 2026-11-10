---
title: "Nx cliques order"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Nx cliques order

Family: Cohesion and subgroups. Identifier: `nx_cliques_order`.

## Definition

Nx cliques order.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_cliques_order` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `list(nx.find_cliques(G)) then list(nx.find_cliques_recursive(G)), each clique in order` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
