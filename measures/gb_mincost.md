---
title: "Mincost"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Mincost

Family: Traversal, trees and DAGs. Identifier: `gb_mincost`.

## Definition

Mincost.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_mincost` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.network_simplex(M) with demand -1 at 0 and 1 at n - 1` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
