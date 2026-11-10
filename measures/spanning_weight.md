---
title: "Spanning weight"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Spanning weight

Family: Traversal, trees and DAGs. Identifier: `spanning_weight`.

## Definition

Minimum or maximum spanning forest of an undirected network, as input edge positions and total weight.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [NetworKit](../tools/networkit.html) | ✓ checked, agrees |  |  |
| [rustworkx](../tools/rustworkx.html) | ✓ checked, agrees |  |  |
| [JGraphT](../tools/jgrapht.html) | ✓ checked, agrees |  |  |
| [Boost Graph Library](../tools/boost.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `tree_maxst_weight_weighted` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.maximum_spanning_tree(M, weight = 'weight').size(weight = 'weight')` |  |
| `tree_mst_weight` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.minimum_spanning_tree(M).size(weight = 'weight') on the multigraph` |  |
| `tree_mst_weight` | NetworKit | undirected | agrees |  |  | abs 0, rel 0 | `nk.graph.KruskalMSF(G with unit weights).getTotalWeight()` |  |
| `tree_mst_weight` | rustworkx | undirected | agrees |  |  | abs 0, rel 0 | `rx.minimum_spanning_edges(G, weight_fn = 1)` |  |
| `tree_mst_weight` | JGraphT | undirected | agrees |  |  | abs 0, rel 0 | `JGraphT 1.5.2: new KruskalMinimumSpanningTree<>(g).getSpanningTree().getWeight() on a pseudograph` |  |
| `tree_mst_weight` | Boost Graph Library | undirected | agrees |  |  | abs 0, rel 0 | `Boost Graph Library kruskal_minimum_spanning_tree (unit weights: tree edge count)` |  |
| `tree_mst_weight_weighted` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.minimum_spanning_tree(M, weight = 'weight').size(weight = 'weight')` |  |
| `tree_mst_weight_weighted` | NetworKit | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `nk.graph.KruskalMSF(G_weighted).getTotalWeight()` |  |
| `tree_mst_weight_weighted` | rustworkx | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `rx.minimum_spanning_edges(G, weight_fn = float)` |  |
| `tree_mst_weight_weighted` | JGraphT | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `JGraphT 1.5.2: new KruskalMinimumSpanningTree<>(g_weighted).getSpanningTree().getWeight() on a pseudograph` |  |
| `tree_mst_weight_weighted` | Boost Graph Library | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `Boost Graph Library kruskal_minimum_spanning_tree` |  |

## References

[boruvka1926jistem](../references.html#boruvka1926jistem), [camerini1979note](../references.html#camerini1979note), [chu1965shortest](../references.html#chu1965shortest), [edmonds1967optimum](../references.html#edmonds1967optimum), [gabow1986efficient](../references.html#gabow1986efficient), [hagberg2008exploring](../references.html#hagberg2008exploring), [kruskal1956shortest](../references.html#kruskal1956shortest), [prim1957shortest](../references.html#prim1957shortest)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [siek2002boost](../references.html#siek2002boost), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
