---
title: "Node clique number"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Node clique number

Family: Cohesion and subgroups. Identifier: `node_clique_number`.

## Definition

Node clique number.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `node_clique_number` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.node_clique_number(G)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
