---
title: "Cds"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Cds

Family: Graph theory and combinatorics. Identifier: `st_cds`.

## Definition

Cds.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_cds` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `sorted(nx.connected_dominating_set(G_sorted)) (-1 if disconnected)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
