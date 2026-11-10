---
title: "Projection"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Projection

Family: Two-mode and bipartite. Identifier: `projection`.

## Definition

Projection.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `graph_projection` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `projection_count` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nx.bipartite.weighted_projected_graph(G, top)` | NetworkX raises when no node lies outside `top` |
| `projection_jaccard` | NetworkX | any | agrees |  |  | abs 0, rel 1e-15 | `nx.bipartite.overlap_weighted_projected_graph(G, top)` |  |
| `projection_min` | NetworkX | any | agrees |  |  | abs 0, rel 1e-15 | `nx.bipartite.overlap_weighted_projected_graph(G, top, jaccard = False)` |  |
| `projection_newman` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.bipartite.collaboration_weighted_projected_graph(G, top)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [peixoto2014graphtool](../references.html#peixoto2014graphtool)
{% endraw %}
