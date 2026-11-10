---
title: "All cliques"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# All cliques

Family: Cohesion and subgroups. Identifier: `all_cliques`.

## Definition

All cliques.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `all_cliques` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `list(nx.enumerate_all_cliques(G))` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
