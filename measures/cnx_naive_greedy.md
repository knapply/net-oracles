---
title: "Naive greedy"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Naive greedy

Family: Communities. Identifier: `cnx_naive_greedy`.

## Definition

Naive greedy.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_naive_greedy_modularity` | NetworkX | any | differs | directed, undirected | direction, ties | abs 0, rel 0 | `nx.community.naive_greedy_modularity_communities(G) on the simple undirected graph` | Exactly tied merges: NetworkX compares whole-partition modularities summed in set order, so rounding decides; the reference compares gains and takes the first pair. |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
