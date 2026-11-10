---
title: "Greedy branching"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Greedy branching

Family: Graph theory and combinatorics. Identifier: `nxs_greedy_branching`.

## Definition

Greedy branching.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `greedy_branching` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_greedy_branching_max` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted(greedy_branching(D, attr = 'weight', kind = 'max').edges())` |  |
| `nxs_greedy_branching_min` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted(greedy_branching(D, attr = 'weight', kind = 'min').edges())` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
