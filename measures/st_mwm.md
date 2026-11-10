---
title: "Mwm"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Mwm

Family: Graph theory and combinatorics. Identifier: `st_mwm`.

## Definition

Mwm.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_mwm` | NetworkX | any | agrees |  |  | abs 1e-09, rel 1e-09 | `the same totals and sizes from nx.max_weight_matching(G), (G, True), nx.min_weight_matching(G)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
