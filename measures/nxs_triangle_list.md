---
title: "Triangle list"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Triangle list

Family: Graph theory and combinatorics. Identifier: `nxs_triangle_list`.

## Definition

Triangle list.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_triangle_list` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `sorted(nx.all_triangles(G)) (NetworkX's order follows Python set order and is not compared)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
