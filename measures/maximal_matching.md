---
title: "Maximal matching"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Maximal matching

Family: Graph theory and combinatorics. Identifier: `maximal_matching`.

## Definition

Maximal matching.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `maximal_matching` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `matching_maximal` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.maximal_matching(G)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
