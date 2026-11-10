---
title: "Greedy color"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Greedy color

Family: Graph theory and combinatorics. Identifier: `greedy_color`.

## Definition

A greedy colouring: the colour of every node, from 0, by one of seven node-order strategies.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention | `color; equitable_color; greedy_color; strategy_connected_sequential; strategy_connected_sequential_bfs; strategy_connected_sequential_dfs; strategy_independent_set; strategy_largest_first; strategy_random_sequential; strategy_saturation_largest_first; strategy_smallest_last` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `greedy_vertex_coloring` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `vertex_coloring_greedy` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `sequential_vertex_coloring` | API listing |
| [NetworKit](../tools/networkit.html) | · reported in docs | `SpectralColoring` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `graph_greedy_color` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `BrownBacktrackColoring; ChordalGraphColoring; GreedyColoring; LargestDegreeFirstColoring; RandomGreedyColoring; SaturationDegreeColoring; SmallestDegreeLastColoring` | API listing |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `edge_coloring; sequential_vertex_coloring; smallest_last_ordering` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `color_connected_sequential_bfs` | NetworkX | undirected | differs | disconnected, unsorted\_edges | defaults, ties | abs 0, rel 0 | `nx.greedy_color(G, strategy = 'connected_sequential_bfs')` | NetworkX visits the neighbours of a node in the order its edges were added, and starts each component from the first node of its Python set (not the smallest when the component's nodes are large numbers); the reference visits neighbours in increasing node order and starts from the smallest node (the order used by the definition oracle). The two agree on connected graphs with a sorted edge list. |
| `color_connected_sequential_dfs` | NetworkX | undirected | differs | disconnected, unsorted\_edges | defaults, ties | abs 0, rel 0 | `nx.greedy_color(G, strategy = 'connected_sequential_dfs')` | NetworkX visits the neighbours of a node in the order its edges were added, and starts each component from the first node of its Python set (not the smallest when the component's nodes are large numbers); the reference visits neighbours in increasing node order and starts from the smallest node (the order used by the definition oracle). The two agree on connected graphs with a sorted edge list. |
| `color_independent_set_valid` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `the same two tests on nx.greedy_color(G, strategy = 'independent_set') of the loop-free simple graph` |  |
| `color_largest_first` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.greedy_color(G, strategy = 'largest_first')` |  |
| `color_saturation_largest_first` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.greedy_color(G, strategy = 'saturation_largest_first')` |  |
| `color_smallest_last_valid` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `the same two tests on nx.greedy_color(G, strategy = 'smallest_last') of the loop-free simple graph` |  |

## References

[brelaz1979new](../references.html#brelaz1979new), [hagberg2008exploring](../references.html#hagberg2008exploring), [kosowski2004classical](../references.html#kosowski2004classical), [matula1983smallest](../references.html#matula1983smallest), [welsh1967upper](../references.html#welsh1967upper)

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [siek2002boost](../references.html#siek2002boost), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
