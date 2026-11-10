---
title: "Gb disjoint paths"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Gb disjoint paths

Family: Traversal, trees and DAGs. Identifier: `gb_disjoint_paths`.

## Definition

Gb disjoint paths.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_edge_disjoint` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(list(nx.edge_disjoint_paths(M, 0, n - 1)))` |  |
| `gb_node_disjoint` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(list(nx.node_disjoint_paths(M, 0, n - 1)))` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
