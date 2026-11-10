---
title: "Voronoi"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Voronoi

Family: Communities. Identifier: `voronoi`.

## Definition

Voronoi.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../tools/igraph.html) | ≠ checked, differs by convention |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `voronoi_modularity` | igraph (R) | any | differs | directed, undirected, (no value) loops, (no value) multi\_edges | direction, multi\_edges, self\_loops, ties | abs 1e-14, rel 1e-12 | `set.seed(1); modularity of cluster_voronoi(g, weights = NULL, lengths = NULL, mode = 'out') (igraph 2.3: its internal community_voronoi_impl(g, mode = 'out', radius = -1))` | igraph chooses the radius with Brent's method, a local search, while the reference tries every distinct distance; where they differ the reference value's modularity is the higher. igraph's result also depends on the random number generator (the seed is fixed at 1). Listed for inspection, not expected to match igraph requires a simple network, and on cycle7\_dir its radius search stops with "optimizer did not converge" |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph)
{% endraw %}
