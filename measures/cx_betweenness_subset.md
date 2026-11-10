---
title: "Betweenness subset"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Betweenness subset

Family: Centrality. Identifier: `cx_betweenness_subset`.

## Definition

Betweenness of nodes and edges for chosen sources and targets (Brandes 2008), which includes betweenness from a sample of sources.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention | `betweenness_centrality_subset; edge_betweenness_centrality_subset` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_bc_all_distinct` | NetworkX | any | differs | multi\_edges | multi\_edges | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality(G, normalized = False)` | NetworkX counts a pair of adjacent nodes once however many parallel edges join them; this variant counts each parallel edge as a distinct shortest path (igraph). |
| `cx_bc_all_distinct_weighted` | NetworkX | any | differs | multi\_edges | multi\_edges | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality(G, normalized = False, weight = 'weight')` | NetworkX counts a pair of adjacent nodes once however many parallel edges join them; this variant counts each parallel edge as a distinct shortest path (igraph). |
| `cx_bc_sampled` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality(G, k = 7, seed = 3)` |  |
| `cx_bc_sampled_endpoints` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality(G, k = 7, endpoints = True, seed = 3)` |  |
| `cx_bc_sampled_raw` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality(G, k = 7, normalized = False, seed = 3)` |  |
| `cx_bc_sampled_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality(G, k = 7, weight = 'weight', seed = 3)` |  |
| `cx_bc_subset_nx` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality_subset(G, even, thirds, normalized = False)` |  |
| `cx_bc_subset_nx_normalized` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality_subset(G, even, thirds, normalized = True)` |  |
| `cx_bc_subset_nx_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality_subset(G, even, thirds, weight = 'weight')` |  |
| `cx_ebc_all_distinct` | NetworkX | any | differs | multi\_edges | multi\_edges | abs 1e-12, rel 1e-09 | `nx.edge_betweenness_centrality(G, normalized = False)` | NetworkX counts parallel edges as one path and shares the pair's value equally among them; this variant gives each parallel edge its own value (igraph). |
| `cx_ebc_sampled` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.edge_betweenness_centrality(G, k = 7, seed = 3)` |  |
| `cx_ebc_subset_nx` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.edge_betweenness_centrality_subset(G, even, thirds, normalized = False)` |  |
| `cx_ebc_subset_nx_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.edge_betweenness_centrality_subset(G, even, thirds, weight = 'weight')` |  |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F024](../findings.html#f024) | NetworkX | defect | edge\_betweenness\_centrality\_subset deviates from its documented formula |

## References

[brandes2001faster](../references.html#brandes2001faster), [brandes2007centrality](../references.html#brandes2007centrality), [brandes2008variants](../references.html#brandes2008variants), [goh2001universal](../references.html#goh2001universal), [piraveenan2013percolation](../references.html#piraveenan2013percolation)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
