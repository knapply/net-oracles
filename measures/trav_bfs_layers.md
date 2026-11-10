---
title: "Bfs layers"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Bfs layers

Family: Traversal, trees and DAGs. Identifier: `trav_bfs_layers`.

## Definition

Levels, parents and counts of a breadth-first search from one node (direction-optimizing).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `bfs_layers` |  |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `bfs_layers; digraph_bfs_layers; graph_bfs_layers` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `trav_bfs_layers` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.bfs_layers(M, [0])` |  |

## References

[luby1986simple](../references.html#luby1986simple), [magnien2009fast](../references.html#magnien2009fast), [schank2005approximating](../references.html#schank2005approximating), [staudt2016networkit](../references.html#staudt2016networkit)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
