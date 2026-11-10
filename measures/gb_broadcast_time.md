---
title: "Broadcast time"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Broadcast time

Family: Traversal, trees and DAGs. Identifier: `gb_broadcast_time`.

## Definition

Broadcast time.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `tree_broadcast_time` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_broadcast_time` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.tree_broadcast_time(nx.Graph(M))` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
