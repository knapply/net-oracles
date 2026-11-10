---
title: "Vertex cover"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Vertex cover

Family: Two-mode and bipartite. Identifier: `vertex_cover`.

## Definition

Vertex cover.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `min_weighted_vertex_cover; to_vertex_cover` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `vertex_cover` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.bipartite.to_vertex_cover(G, nx.bipartite.hopcroft_karp_matching(G, top), top_nodes = top): (size, 1 if it covers every edge)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
