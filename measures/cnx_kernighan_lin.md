---
title: "Kernighan lin"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Kernighan lin

Family: Communities. Identifier: `cnx_kernighan_lin`.

## Definition

Kernighan lin.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `kernighan_lin_bisection` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_kernighan_lin` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.community.kernighan_lin_bisection(G_sorted, (first half, rest), max_iter = 10, weight = 'weight' if weighted)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
