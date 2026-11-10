---
title: "Kpp_single / distance_reach"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Kpp\_single / distance\_reach

Family: Centrality. Identifier: `kpp_single:distance_reach`.

## Definition

Key player criterion (fragmentation, distance-weighted fragmentation, m-reach or distance-weighted reach) of a given set of nodes.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [keyplayer](../tools/keyplayer.html) | ≠ checked, differs by convention |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `kpp_distance_reach_single` | keyplayer | any | no-value-on-some-inputs | (no value) edgeless | defaults | abs 1e-14, rel 1e-12 | `(1 + (n - 1) * keyplayer::mreach.closeness(adjacency, v, M = Inf, binary = TRUE, cmode = 'outdegree')) / n; keyplayer divides the sum of 1/d by n - 1, Borgatti's DR by n` | keyplayer returns -1 for a network without edges (and for one node), where Borgatti's measures are defined. |
| `kpp_distance_reach_single_in` | keyplayer | directed | no-value-on-some-inputs | (no value) edgeless | defaults | abs 1e-14, rel 1e-12 | `as kpp_distance_reach_single with cmode = 'indegree'` | keyplayer returns -1 for a network without edges (and for one node), where Borgatti's measures are defined. |
| `kpp_distance_reach_single_weighted` | keyplayer | any | differs | (no value) edgeless | defaults, weights | abs 1e-14, rel 1e-12 | `as kpp_distance_reach_single on the weighted adjacency matrix with binary = FALSE (edge values read as distances)` | keyplayer's weighted distances are not the Dijkstra shortest-path lengths: on a probe graph its closeness-based reach lies 2 to 5 percent below the value from igraph Dijkstra distances with edge values as lengths, and its weighted fragmentation 3 to 14 percent above. the reference equals the definition oracle (exact shortest paths). |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F012](../findings.html#f012) | keyplayer | defect | Weighted distances (binary = FALSE) are not shortest-path lengths |

## References

[borgatti2006identifying](../references.html#borgatti2006identifying), [brandes2008variants](../references.html#brandes2008variants), [dinic1970algorithm](../references.html#dinic1970algorithm), [everett1999centrality](../references.html#everett1999centrality), [everton2012disrupting](../references.html#everton2012disrupting), [ford1956maximal](../references.html#ford1956maximal), [freeman1991centrality](../references.html#freeman1991centrality), [koschutzki2005centrality](../references.html#koschutzki2005centrality)

Tools cited: [an2016keyplayer](../references.html#an2016keyplayer)
{% endraw %}
