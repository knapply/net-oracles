---
title: "St edge cover"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# St edge cover

Family: Graph theory and combinatorics. Identifier: `st_edge_cover`.

## Definition

St edge cover.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_edge_cover` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.min_edge_cover(G)) counting each edge once, -1 with an isolated node` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
