---
title: "Paths johnson"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Paths johnson

Family: Paths and distances. Identifier: `paths_johnson`.

## Definition

Paths johnson.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `johnson` |  |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `JohnsonShortestPaths` | API listing |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `johnson_all_pairs_shortest_paths` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_johnson_potential` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.johnson(G, weight = 'len'), each path's length summed in order` |  |
| `paths_johnson_shift` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.johnson(G, weight = 'len'); NetworkXUnbounded is a negative cycle` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [siek2002boost](../references.html#siek2002boost)
{% endraw %}
