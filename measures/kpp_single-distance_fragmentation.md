---
title: "Kpp_single / distance_fragmentation"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Kpp\_single / distance\_fragmentation

Family: Centrality. Identifier: `kpp_single:distance_fragmentation`.

## Definition

Key player criterion (fragmentation, distance-weighted fragmentation, m-reach or distance-weighted reach) of a given set of nodes.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [keyplayer](../tools/keyplayer.html) | ≠ checked, differs by convention | `fragment` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `kpp_distance_fragmentation_single` | keyplayer | any | no-value-on-some-inputs | (no value) directed, (no value) edgeless | defaults, direction, normalization, ties | abs 1e-14, rel 1e-12 | `keyplayer::fragment(adjacency, v, binary = TRUE) for each node v: 1 - sum_{j,k != v} 1/d_jk / (d (n - 1)(n - 2)), d the largest 1/d_jk (An and Liu 2016, eq. 7)` | keyplayer's fragmentation is not directional, so it is compared on undirected networks only. Its formula divides by the largest inverse distance in the residual network (1 on a binary network with any tie left, which makes it Borgatti's DF), so it is undefined when removing a node leaves no ties (the centre of star8) or no pairs (one node). |
| `kpp_distance_fragmentation_single_weighted` | keyplayer | any | differs | (no value) directed, (no value) edgeless | defaults, direction, weights | abs 1e-14, rel 1e-12 | `keyplayer::fragment(weighted adjacency, v, binary = FALSE) for each node v (edge values read as distances)` | keyplayer's weighted distances are not the Dijkstra shortest-path lengths: on a probe graph its closeness-based reach lies 2 to 5 percent below the value from igraph Dijkstra distances with edge values as lengths, and its weighted fragmentation 3 to 14 percent above. the reference equals the definition oracle (exact shortest paths). |

## References

[borgatti2006identifying](../references.html#borgatti2006identifying), [brandes2008variants](../references.html#brandes2008variants), [dinic1970algorithm](../references.html#dinic1970algorithm), [everett1999centrality](../references.html#everett1999centrality), [everton2012disrupting](../references.html#everton2012disrupting), [ford1956maximal](../references.html#ford1956maximal), [freeman1991centrality](../references.html#freeman1991centrality), [koschutzki2005centrality](../references.html#koschutzki2005centrality)

Tools cited: [an2016keyplayer](../references.html#an2016keyplayer)
{% endraw %}
