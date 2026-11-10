---
title: "Intersection"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Intersection

Family: Graph theory and combinatorics. Identifier: `st_intersection`.

## Definition

Intersection.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `intersection_array` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_intersection` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.intersection_array(G) (-1 where it raises)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
