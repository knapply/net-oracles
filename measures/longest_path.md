---
title: "Longest path"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Longest path

Family: Traversal, trees and DAGs. Identifier: `longest_path`.

## Definition

A longest path of a DAG and its length, by dynamic programming in topological order.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `dag_longest_path` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_longest_path` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.dag_longest_path(D)` |  |
| `dag_longest_path_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.dag_longest_path(D, weight = 'weight') on the multigraph D` |  |

## References

[aho1972transitive](../references.html#aho1972transitive), [aho1976finding](../references.html#aho1976finding), [bender2005lowest](../references.html#bender2005lowest), [cooper2001simple](../references.html#cooper2001simple), [cytron1991efficiently](../references.html#cytron1991efficiently), [hagberg2008exploring](../references.html#hagberg2008exploring), [kahn1962topological](../references.html#kahn1962topological), [knuth1974structured](../references.html#knuth1974structured)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
