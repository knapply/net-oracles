---
title: "Snap groups"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Snap groups

Family: Traversal, trees and DAGs. Identifier: `gb_snap_groups`.

## Definition

Snap groups.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `snap_aggregation` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_snap_groups` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.snap_aggregation(M, node_attributes=('parity',)).number_of_nodes()` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
