---
title: "Avg nbr deg"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Avg nbr deg

Family: Mixing and assortativity. Identifier: `avg_nbr_deg`.

## Definition

Avg nbr deg.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention | `average_neighbor_degree` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `avg_nbr_deg` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G)` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_nbr_deg_in_in` | NetworkX | directed | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G, source = 'in', target = 'in')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_nbr_deg_out_in` | NetworkX | directed | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G, source = 'out', target = 'in')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_nbr_deg_subset` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G, nodes = even nodes)` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_nbr_deg_total` | NetworkX | directed | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G, source = 'in+out', target = 'in+out')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_nbr_deg_weighted` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G, weight = 'weight')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
