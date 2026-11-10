---
title: "Frontiers"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Frontiers

Family: Traversal, trees and DAGs. Identifier: `frontiers`.

## Definition

Frontiers.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_dominance_frontiers` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.dominance_frontiers(G, 0), one sorted tuple per node, (-1) if unreachable` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
