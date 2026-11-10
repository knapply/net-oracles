---
title: "Dfs events"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Dfs events

Family: Traversal, trees and DAGs. Identifier: `trav_dfs_events`.

## Definition

Dfs events.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `dfs_labeled_edges` |  |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `DepthFirstIterator` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `trav_dfs_events` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.dfs_labeled_edges(M)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht)
{% endraw %}
