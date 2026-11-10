---
title: "Regular"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Regular

Family: Graph theory and combinatorics. Identifier: `st_regular`.

## Definition

Regular.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `is_regular` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_regular` | NetworkX | any | agrees |  |  | abs 0, rel 1e-15 | `[nx.is_regular(G), nx.s_metric(G)]` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
