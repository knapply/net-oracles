---
title: "Bellman ford"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Bellman ford

Family: Traversal, trees and DAGs. Identifier: `ord_bellman_ford`.

## Definition

Bellman ford.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `bellman_ford_path; bellman_ford_path_length; bellman_ford_predecessor_and_distance; single_source_bellman_ford; single_source_bellman_ford_path; single_source_bellman_ford_path_length` |  |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `bellman_ford_search` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `bellman_ford_shortest_path_lengths; bellman_ford_shortest_paths; digraph_bellman_ford_shortest_path_lengths; digraph_bellman_ford_shortest_paths; graph_bellman_ford_shortest_path_lengths; graph_bellman_ford_shortest_paths` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `BellmanFordShortestPath` | API listing |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `bellman_ford_shortest_paths` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ord_bellman_ford` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.bellman_ford_predecessor_and_distance(M, 0)` |  |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F004](../findings.html#f004) | NetworkX | defect | goldberg\_radzik raises NetworkXUnbounded for any negative self-loop |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [siek2002boost](../references.html#siek2002boost), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
