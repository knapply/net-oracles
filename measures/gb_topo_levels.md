---
title: "Topo levels"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Topo levels

Family: Traversal, trees and DAGs. Identifier: `gb_topo_levels`.

## Definition

Topo levels.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_topo_levels` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.topological_generations(M)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
