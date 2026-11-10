---
title: "Tree lca"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Tree lca

Family: Traversal, trees and DAGs. Identifier: `tree_lca`.

## Definition

Tree lca.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `BinaryLiftingLCAFinder; EulerTourRMQLCAFinder; HeavyPathLCAFinder; NaiveLCAFinder; TarjanLCAFinder` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_tree_lca` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.tree_all_pairs_lowest_common_ancestor(T, root = 0, pairs)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht)
{% endraw %}
