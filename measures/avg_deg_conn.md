---
title: "Avg deg conn"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Avg deg conn

Family: Mixing and assortativity. Identifier: `avg_deg_conn`.

## Definition

Avg deg conn.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention | `average_degree_connectivity` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `avg_deg_conn` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_degree_connectivity(G)` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_deg_conn_in_in` | NetworkX | directed | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_degree_connectivity(G, source = 'in', target = 'in')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_deg_conn_out_out` | NetworkX | directed | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_degree_connectivity(G, source = 'out', target = 'out')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_deg_conn_subset` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_degree_connectivity(G, nodes = even nodes)` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_deg_conn_weighted` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_degree_connectivity(G, weight = 'weight')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
