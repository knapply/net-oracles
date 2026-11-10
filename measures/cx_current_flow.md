---
title: "Cx current flow"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Cx current flow

Family: Centrality. Identifier: `cx_current_flow`.

## Definition

Current-flow (random-walk) betweenness of every node and edge, from the grounded inverse of the Laplacian.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `current_flow_betweenness_centrality; edge_current_flow_betweenness_centrality` |  |
| [netrankr](../tools/netrankr.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_cfb` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 1e-14, rel 1e-12 | `nx.current_flow_betweenness_centrality(G)` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |
| `cx_cfb_raw` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 1e-11, rel 1e-12 | `nx.current_flow_betweenness_centrality(G, normalized = False)` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |
| `cx_cfb_raw` | netrankr | undirected | no-value-on-some-inputs | (no value) directed, (no value) disconnected | defaults, direction, weights | abs 1e-11, rel 1e-12 | `aggregate_positions(indirect_relations(g, 'depend_curflow'), 'sum')` | netrankr reads the network as undirected, unweighted and simple and has no value for a single node; its resistance distance (type = "dist\_resist", "depend\_curflow") is defined only for connected graphs and raises an error otherwise. |
| `cx_cfb_weighted` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 5e-14, rel 1e-12 | `nx.current_flow_betweenness_centrality(G, weight = 'weight')` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |
| `cx_ecfb` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 1e-14, rel 1e-12 | `nx.edge_current_flow_betweenness_centrality(G)` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |
| `cx_ecfb_raw` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 1e-14, rel 1e-12 | `nx.edge_current_flow_betweenness_centrality(G, normalized = False)` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |

## References

[brandes2005centrality](../references.html#brandes2005centrality), [ellens2011effective](../references.html#ellens2011effective), [hestenes1952methods](../references.html#hestenes1952methods), [kermarrec2011second](../references.html#kermarrec2011second), [klein1993resistance](../references.html#klein1993resistance), [levene2002kemeny](../references.html#levene2002kemeny), [newman2005measure](../references.html#newman2005measure), [stephenson1989rethinking](../references.html#stephenson1989rethinking)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [schoch2018centrality](../references.html#schoch2018centrality)
{% endraw %}
