---
title: "Tree centroid"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Tree centroid

Family: Graph theory and combinatorics. Identifier: `nxs_tree_centroid`.

## Definition

Tree centroid.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `centroid` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_tree_centroid` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted(nx.centroid(T))` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
