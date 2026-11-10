---
title: "Ego_summary / density"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Ego\_summary / density

Family: Two-mode and bipartite. Identifier: `ego_summary:density`.

## Definition

Ego\_summary / density.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs | `egodensity` | published documentation |
| [egor](../tools/egor.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ego_density` | NetworkX | any | agrees |  |  | abs 0, rel 1e-14 | `nx.density(nx.ego_graph(simple G, v, undirected = True, center = False)); undefined below two alters` |  |
| `ego_density` | igraph (R) | any | agrees |  |  | abs 0, rel 1e-14 | `igraph::edge_density(induced_subgraph(simplify(g), ego(g, 1, v, 'all', mindist = 1)))` |  |
| `ego_density` | egor | any | agrees |  |  | abs 0, rel 1e-14 | `egor::ego_density(egor object, directed = 'directed' \| 'undirected')` |  |
| `ego_density_out` | NetworkX | directed | agrees |  |  | abs 0, rel 1e-14 | `nx.density(nx.ego_graph(simple G, v, center = False)); undefined below two alters` |  |
| `ego_density_out` | igraph (R) | directed | agrees |  |  | abs 0, rel 1e-14 | `igraph::edge_density(induced_subgraph(simplify(g), ego(g, 1, v, 'out', mindist = 1)))` |  |
| `ego_density_out` | egor | directed | agrees |  |  | abs 0, rel 1e-14 | `egor::ego_density(egor object of out-neighbours, directed = 'directed')` |  |

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [tool_egor](../references.html#tool_egor)
{% endraw %}
