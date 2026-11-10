---
title: "Spanning tree"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Spanning tree

Family: Traversal, trees and DAGs. Identifier: `spanning_tree`.

## Definition

Minimum or maximum spanning forest of an undirected network, as input edge positions and total weight.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `maximum_spanning_edges; maximum_spanning_tree; minimum_spanning_edges; minimum_spanning_tree` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `mst` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `spanning_tree` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `min_spanning_tree` | API listing |
| [NetworKit](../tools/networkit.html) | · reported in docs | `KruskalMSF; PrimMSF; SpanningForest` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `minimum_spanning_edges; minimum_spanning_tree` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `BoruvkaMinimumSpanningTree; KruskalMinimumSpanningTree; PrimMinimumSpanningTree` | API listing |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `kruskal_minimum_spanning_tree; prim_minimum_spanning_tree` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `tree_maxst_edges_kruskal` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.maximum_spanning_edges(M, algorithm = 'kruskal', keys = True) as (u, v, weight)` |  |
| `tree_mst_edges_boruvka` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.minimum_spanning_edges(M, algorithm = 'kruskal', keys = True)` |  |
| `tree_mst_edges_kruskal` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.minimum_spanning_edges(M, algorithm = 'kruskal', keys = True) as (u, v, weight); the reference is given the edges in M.edges() order` |  |
| `tree_mst_edges_prim` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.minimum_spanning_edges(M, algorithm = 'kruskal', keys = True): every algorithm of the reference returns Kruskal's forest` |  |

## References

[boruvka1926jistem](../references.html#boruvka1926jistem), [camerini1979note](../references.html#camerini1979note), [chu1965shortest](../references.html#chu1965shortest), [edmonds1967optimum](../references.html#edmonds1967optimum), [gabow1986efficient](../references.html#gabow1986efficient), [hagberg2008exploring](../references.html#hagberg2008exploring), [kruskal1956shortest](../references.html#kruskal1956shortest), [prim1957shortest](../references.html#prim1957shortest)

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [siek2002boost](../references.html#siek2002boost), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
