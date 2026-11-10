---
title: "Paths k shortest"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Paths k shortest

Family: Paths and distances. Identifier: `paths_k_shortest`.

## Definition

Paths k shortest.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `shortest_simple_paths` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `k_shortest_paths` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `get_k_shortest_paths` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `digraph_k_shortest_path_lengths; graph_k_shortest_path_lengths; k_shortest_path_lengths` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `EppsteinKShortestPath; EppsteinShortestPathIterator; YenKShortestPath; YenShortestPathIterator` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_k_shortest_unweighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `lengths of the first 10 paths of nx.shortest_simple_paths(H, 0, n - 1), H the simple graph` |  |
| `paths_k_shortest_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.path_weight of the first 10 paths of nx.shortest_simple_paths(H, 0, n - 1, weight = 'weight'), H the simple graph keeping the lightest parallel edge` |  |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
