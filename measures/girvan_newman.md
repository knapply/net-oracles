---
title: "Girvan newman"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Girvan newman

Family: Communities. Identifier: `girvan_newman`.

## Definition

Girvan-Newman clustering by removing the edge of highest betweenness one at a time; returns the best level, its modularity, the removal order and the modularity path.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `edge_betweenness_partition; girvan_newman` |  |
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees | `cluster_edge_betweenness` |  |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `community_edge_betweenness` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `GirvanNewmanClustering` | API listing |
| [UCINET](../tools/ucinet.html) | · reported in docs |  | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `girvan_newman` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `max of nx.community.modularity over nx.community.girvan_newman(simple graph)` |  |
| `girvan_newman` | igraph (R) | undirected | differs | symmetric\_nodes | ties | abs 1e-14, rel 1e-12 | `max(modularity(cluster_edge_betweenness(simplify(g), weights = NULL)))` | Edges of exactly equal betweenness (symmetric positions) are removed in a different order, igraph by its own rule, the reference by edge index, so the dendrograms and their best levels can differ. |
| `girvan_newman_membership` | NetworkX | undirected | differs | edgeless | defaults | abs 0, rel 0 | `the first partition of highest modularity among the components and the partitions of nx.community.girvan_newman(simple graph)` | Without edges: the reference returns no membership level for the null graph and the singletons otherwise, the NetworkX oracle one value for the empty level. |

## References

[girvan2002community](../references.html#girvan2002community)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht)
{% endraw %}
