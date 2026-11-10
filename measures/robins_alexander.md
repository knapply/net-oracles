---
title: "Robins alexander"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Robins alexander

Family: Two-mode and bipartite. Identifier: `robins_alexander`.

## Definition

Robins alexander.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `robins_alexander_clustering` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `robins_alexander` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.bipartite.robins_alexander_clustering(G)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
