---
title: "St edge cut"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# St edge cut

Family: Components and connectivity. Identifier: `st_edge_cut`.

## Definition

St edge cut.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_st_edge_cut` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.connectivity.minimum_st_edge_cut(G, 0, n - 1), as pairs (u, v)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
