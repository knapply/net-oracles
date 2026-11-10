---
title: "Greedy modularity"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Greedy modularity

Family: Communities. Identifier: `cnx_greedy_modularity`.

## Definition

Greedy modularity.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `GreedyModularityAlgorithm` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_greedy_modularity` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.community.greedy_modularity_communities(G) on the simple undirected graph` |  |
| `nx_greedy_modularity_res` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.community.greedy_modularity_communities(G, resolution = 0.6) on the simple undirected graph` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht)
{% endraw %}
