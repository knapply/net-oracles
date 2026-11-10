---
title: "Ego members"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Ego members

Family: Two-mode and bipartite. Identifier: `ego_members`.

## Definition

Ego members.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `ego_graph` |  |
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees | `ego; make_ego_graph` |  |
| [sna](../tools/sna.html) | · reported in docs | `ego.extract` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ego_alters` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.ego_graph(G, v, undirected = True, center = False).nodes` |  |
| `ego_alters` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::ego(g, order = 1, mode = 'all', mindist = 1)` |  |
| `ego_alters_order2_out` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.ego_graph(G, v, radius = 2, center = False).nodes` |  |
| `ego_alters_order2_out` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::ego(g, order = 2, mode = 'out', mindist = 1)` |  |

Tools cited: [butts2008sna](../references.html#butts2008sna), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
