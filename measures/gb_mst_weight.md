---
title: "Mst weight"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Mst weight

Family: Traversal, trees and DAGs. Identifier: `gb_mst_weight`.

## Definition

Mst weight.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_mst_weight` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `sum of weights over nx.minimum_spanning_edges(M)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
