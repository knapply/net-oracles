---
title: "Spanning trees"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Spanning trees

Family: Traversal, trees and DAGs. Identifier: `gb_spanning_trees`.

## Definition

Number of spanning trees (arborescences rooted at the root for a directed network) by the matrix-tree theorem.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `number_of_spanning_trees` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_spanning_trees` | NetworkX | undirected | agrees |  |  | abs 1e-09, rel 1e-09 | `nx.number_of_spanning_trees(M)` |  |

## References

[kirchhoff1847ueber](../references.html#kirchhoff1847ueber), [tutte1948dissection](../references.html#tutte1948dissection)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
