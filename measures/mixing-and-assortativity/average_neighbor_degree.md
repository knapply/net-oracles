---
title: "Average neighbor degree and degree connectivity"
layout: default
parent: "Mixing and assortativity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Average neighbor degree and degree connectivity {#concept-top}

Family: [Mixing and assortativity](index.html). Subfamily: Assortativity. Concept id: `average_neighbor_degree`. 3 measures.

## Definition {#concept-definition}

Average neighbor degree and degree connectivity. Entries grouped here: Avg deg conn; Avg nbr deg; Knn.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Avg deg conn](#avg_deg_conn) | `avg_deg_conn` | 1 |
| [Avg nbr deg](#avg_nbr_deg) | `avg_nbr_deg` | 1 |
| [Knn](#cat_knn) | `cat_knn` | 2 |

## Avg deg conn {#avg_deg_conn}

Measure id: `avg_deg_conn`. Original family: Mixing and assortativity.

**Definition.** Avg deg conn.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention | `average_degree_connectivity` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `avg_deg_conn` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_degree_connectivity(G)` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_deg_conn_in_in` | NetworkX | directed | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_degree_connectivity(G, source = 'in', target = 'in')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_deg_conn_out_out` | NetworkX | directed | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_degree_connectivity(G, source = 'out', target = 'out')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_deg_conn_subset` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_degree_connectivity(G, nodes = even nodes)` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_deg_conn_weighted` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_degree_connectivity(G, weight = 'weight')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Avg nbr deg {#avg_nbr_deg}

Measure id: `avg_nbr_deg`. Original family: Mixing and assortativity.

**Definition.** Avg nbr deg.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention | `average_neighbor_degree` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `avg_nbr_deg` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G)` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_nbr_deg_in_in` | NetworkX | directed | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G, source = 'in', target = 'in')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_nbr_deg_out_in` | NetworkX | directed | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G, source = 'out', target = 'in')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_nbr_deg_subset` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G, nodes = even nodes)` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_nbr_deg_total` | NetworkX | directed | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G, source = 'in+out', target = 'in+out')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_nbr_deg_weighted` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G, weight = 'weight')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Knn {#cat_knn}

Measure id: `cat_knn`. Original family: Descriptive statistics.

**Definition.** Knn.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `knn` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `knn` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
