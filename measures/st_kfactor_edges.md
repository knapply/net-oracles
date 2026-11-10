---
title: "Kfactor edges"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Kfactor edges

Family: Graph theory and combinatorics. Identifier: `st_kfactor_edges`.

## Definition

Kfactor edges.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_kfactor_edges` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `for k = 1, 2: the edges of nx.k_factor(G, k) in order, flat, with their count first (-1 if none)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
