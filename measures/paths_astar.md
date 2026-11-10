---
title: "Paths astar"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Paths astar

Family: Paths and distances. Identifier: `paths_astar`.

## Definition

Paths astar.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `astar_path; astar_path_length` |  |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `get_shortest_path_astar` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `astar_iterator; astar_search` | API listing |
| [NetworKit](../tools/networkit.html) | · reported in docs | `AStar` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `astar_shortest_path; digraph_astar_shortest_path; graph_astar_shortest_path` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `AStarShortestPath; BidirectionalAStarShortestPath` | API listing |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `astar_search` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_astar_exact` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.astar_path_length(G, s, t, heuristic = lambda u, v: d(u, t)) for every pair` |  |
| `paths_astar_half` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.astar_path_length(G, s, t, heuristic = lambda u, v: 0.5 d(u, t), weight = 'weight') for every pair` |  |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [siek2002boost](../references.html#siek2002boost), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
