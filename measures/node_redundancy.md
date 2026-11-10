---
title: "Node redundancy"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Node redundancy

Family: Two-mode and bipartite. Identifier: `node_redundancy`.

## Definition

Node redundancy.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `node_redundancy` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `node_redundancy` | NetworkX | any | agrees |  |  | abs 0, rel 1e-14 | `nx.bipartite.node_redundancy(G, nodes with at least two neighbours)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
