---
title: "Leiden"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Leiden

Family: Communities. Identifier: `leiden`.

## Definition

Leiden communities of an undirected network: local moving, refinement into connected groups and aggregation.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `leiden_communities; leiden_partitions` |  |
| [igraph (R)](../tools/igraph.html) | ∅ checked, no value on some inputs | `cluster_leiden` |  |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `community_leiden` | API listing |
| [NetworKit](../tools/networkit.html) | · reported in docs | `ParallelLeiden` | API listing |
| [scikit-network](../tools/sknetwork.html) | · reported in docs | `Leiden` | API listing |
| [UCINET](../tools/ucinet.html) | · reported in docs | `localgreedy` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `leiden_cpm_quality` | igraph (R) | undirected | agrees |  |  | abs 0.015, rel 0 | `mean over set.seed(1..20) of the CPM quality (1/2m) sum_ij (A_ij - 0.1) delta of cluster_leiden(g, objective_function = 'CPM', resolution = 0.1, n_iterations = -1, weights = NA)` |  |
| `leiden_quality` | NetworkX | undirected | differs | edge\_case, loops, multi\_edges | defaults, multi\_edges, self\_loops | abs 0.03, rel 0 | `mean over seeds of modularity(G, leiden_communities(simple graph, metric = 'modularity', seed = s))` | NetworkX runs on the simple graph here, while the reference counts parallel edges with their multiplicity; without edges modularity is undefined (the reference reports -1, NetworkX 0) |
| `leiden_quality` | igraph (R) | undirected | no-value-on-some-inputs |  |  | abs 0.03, rel 0 | `mean over set.seed(1..20) of modularity(g, cluster_leiden(g, objective_function = 'modularity', n_iterations = -1, weights = NA))` | igraph's cluster\_leiden() raises an error for a single node. |

## References

[traag2019louvain](../references.html#traag2019louvain)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [staudt2016networkit](../references.html#staudt2016networkit), [tool_sknetwork](../references.html#tool_sknetwork)
{% endraw %}
