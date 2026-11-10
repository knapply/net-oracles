---
title: "Girvan-Newman edge removal"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Girvan-Newman edge removal {#concept-top}

Family: [Communities](index.html). Subfamily: Other detection algorithms. Concept id: `girvan_newman`. 5 measures.

## Definition {#concept-definition}

Girvan-Newman clustering by removing the edge of highest betweenness one at a time; returns the best level, its modularity, the removal order and the modularity path.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Girvan newman](#girvan_newman) | `girvan_newman` | 5 |
| [Cnx current flow](#cnx_current_flow) | `cnx_current_flow` | 1 |
| [Cnx edge betweenness](#cnx_edge_betweenness) | `cnx_edge_betweenness` | 1 |
| [Cnx girvan newman](#cnx_girvan_newman) | `cnx_girvan_newman` | 1 |
| [Girvan newman cut](#girvan_newman_cut) | `girvan_newman_cut` | 1 |

## References {#concept-references}

[girvan2002community](../../references.html#girvan2002community), [brandes2005centrality](../../references.html#brandes2005centrality), [brandes2001faster](../../references.html#brandes2001faster), [chen2014extension](../../references.html#chen2014extension), [clauset2004finding](../../references.html#clauset2004finding), [cordasco2010community](../../references.html#cordasco2010community), [fortunato2010community](../../references.html#fortunato2010community), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kernighan1970efficient](../../references.html#kernighan1970efficient)

## Girvan newman {#girvan_newman}

Measure id: `girvan_newman`. Original family: Communities.

**Definition.** Girvan-Newman clustering by removing the edge of highest betweenness one at a time; returns the best level, its modularity, the removal order and the modularity path.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `edge_betweenness_partition; girvan_newman` |  |
| [igraph (R)](../../tools/igraph.html) | ✓ checked, agrees | `cluster_edge_betweenness` |  |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `community_edge_betweenness` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `GirvanNewmanClustering` | API listing |
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `girvan_newman` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `max of nx.community.modularity over nx.community.girvan_newman(simple graph)` |  |
| `girvan_newman` | igraph (R) | undirected | differs | symmetric\_nodes | ties | abs 1e-14, rel 1e-12 | `max(modularity(cluster_edge_betweenness(simplify(g), weights = NULL)))` | Edges of exactly equal betweenness (symmetric positions) are removed in a different order, igraph by its own rule, the reference by edge index, so the dendrograms and their best levels can differ. |
| `girvan_newman_membership` | NetworkX | undirected | differs | edgeless | defaults | abs 0, rel 0 | `the first partition of highest modularity among the components and the partitions of nx.community.girvan_newman(simple graph)` | Without edges: the reference returns no membership level for the null graph and the singletons otherwise, the NetworkX oracle one value for the empty level. |

**References:** [girvan2002community](../../references.html#girvan2002community)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Cnx current flow {#cnx_current_flow}

Measure id: `cnx_current_flow`. Original family: Communities.

**Definition.** Component labels after removing the edges of largest current-flow betweenness until at least k components exist (NetworkX's edge current-flow partition).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention | `edge_current_flow_betweenness_partition` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_edge_current_flow_partition` | NetworkX | any | differs | symmetric\_nodes | ties | abs 0, rel 0 | `nx.community.edge_current_flow_betweenness_partition(G, 3) on the simple undirected graph (-1 when n < 3)` | Edges whose current-flow betweenness ties in exact arithmetic (symmetric positions) differ in the last digits; NetworkX removes the one its rounding and dict order rank first, the reference the first in edge order. |

**References:** [brandes2005centrality](../../references.html#brandes2005centrality)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Cnx edge betweenness {#cnx_edge_betweenness}

Measure id: `cnx_edge_betweenness`. Original family: Communities.

**Definition.** Component labels after removing the most central edges one at a time until at least k components exist (NetworkX's edge betweenness partition).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_edge_betweenness_partition` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.community.edge_betweenness_partition(G, 3) on the simple undirected graph (-1 when n < 3)` |  |

**References:** [brandes2001faster](../../references.html#brandes2001faster), [chen2014extension](../../references.html#chen2014extension), [clauset2004finding](../../references.html#clauset2004finding), [cordasco2010community](../../references.html#cordasco2010community), [fortunato2010community](../../references.html#fortunato2010community), [girvan2002community](../../references.html#girvan2002community), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kernighan1970efficient](../../references.html#kernighan1970efficient)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Cnx girvan newman {#cnx_girvan_newman}

Measure id: `cnx_girvan_newman`. Original family: Communities.

**Definition.** Cnx girvan newman.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_girvan_newman` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `itertools.islice(nx.community.girvan_newman(G), 3)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Girvan newman cut {#girvan_newman_cut}

Measure id: `girvan_newman_cut`. Original family: Communities.

**Definition.** Girvan newman cut.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `girvan_newman_cut3` | igraph (R) | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) edge\_case, (no value) loops, (no value) multi\_edges | defaults, multi\_edges, self\_loops | abs 0, rel 0 | `cut_at(cluster_edge_betweenness(simplify(g), weights = NULL), no = 3)` | the R oracle simplifies the network, so multigraphs and networks with loops are not comparable; disconnected and trivial networks give dendrograms that cannot be cut at 3 groups in one tool or the other |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
