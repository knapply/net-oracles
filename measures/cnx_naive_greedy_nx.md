---
title: "Naive greedy nx"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Naive greedy nx

Family: Communities. Identifier: `cnx_naive_greedy_nx`.

## Definition

Naive greedy nx.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_naive_greedy_exact` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.community.naive_greedy_modularity_communities(G) on the simple undirected graph: community index per node in NetworkX's order; -1 without edges` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
