---
title: "Ego_summary / betweenness"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Ego\_summary / betweenness

Family: Two-mode and bipartite. Identifier: `ego_summary:betweenness`.

## Definition

Ego\_summary / betweenness.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs |  | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ego_betweenness` | NetworkX | any | agrees |  |  | abs 1e-09, rel 1e-09 | `nx.betweenness_centrality(nx.ego_graph(simple G, v, undirected = True), normalized = False)[v]` |  |
| `ego_betweenness` | igraph (R) | any | agrees |  |  | abs 1e-09, rel 1e-09 | `igraph::betweenness(make_ego_graph(simplify(g), 1, v, 'all')[[1]], ego)` |  |
| `ego_betweenness_order2` | NetworkX | any | agrees |  |  | abs 1e-09, rel 1e-09 | `nx.betweenness_centrality(nx.ego_graph(simple G, v, radius = 2, undirected = True), normalized = False)[v]` |  |
| `ego_betweenness_out` | NetworkX | directed | agrees |  |  | abs 1e-09, rel 1e-09 | `nx.betweenness_centrality(nx.ego_graph(simple G, v), normalized = False)[v]` |  |
| `ego_betweenness_out` | igraph (R) | directed | agrees |  |  | abs 1e-09, rel 1e-09 | `igraph::betweenness(make_ego_graph(simplify(g), 1, v, 'out')[[1]], ego, directed = TRUE)` |  |

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
