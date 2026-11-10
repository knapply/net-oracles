---
title: "Mwm pairs"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Mwm pairs

Family: Graph theory and combinatorics. Identifier: `st_mwm_pairs`.

## Definition

Mwm pairs.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_mwm_pairs` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted oriented pairs of max_weight_matching(G), then of (G, True), then of min_weight_matching(G), each list with its length first` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
