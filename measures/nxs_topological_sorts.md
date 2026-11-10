---
title: "Topological sorts"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Topological sorts

Family: Graph theory and combinatorics. Identifier: `nxs_topological_sorts`.

## Definition

Topological sorts.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `TopologicalOrderIterator` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_topological_sorts` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `first 2000 of nx.all_topological_sorts(DAG), in its order` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht)
{% endraw %}
