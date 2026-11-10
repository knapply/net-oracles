---
title: "Kpp_optimum / distance_fragmentation"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Kpp\_optimum / distance\_fragmentation

Family: Centrality. Identifier: `kpp_optimum:distance_fragmentation`.

## Definition

The set of k key players that best satisfies a key player criterion (Borgatti's greedy swap search or exact enumeration), with its score.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [keyplayer](../tools/keyplayer.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `kpp_distance_fragmentation_optimum_k2` | keyplayer | any | no-value-on-some-inputs | (no value) directed | direction | abs 1e-14, rel 1e-12 | `maximum over every pair S of keyplayer::fragment(adjacency, S, binary = TRUE)` | single\_node has fewer nodes than the set size, so there is no set to score; keyplayer's fragmentation is not directional, so it is compared on undirected networks only. |

## References

[borgatti2006identifying](../references.html#borgatti2006identifying), [brandes2008variants](../references.html#brandes2008variants), [dinic1970algorithm](../references.html#dinic1970algorithm), [everett1999centrality](../references.html#everett1999centrality), [everton2012disrupting](../references.html#everton2012disrupting), [ford1956maximal](../references.html#ford1956maximal), [freeman1991centrality](../references.html#freeman1991centrality), [koschutzki2005centrality](../references.html#koschutzki2005centrality)

Tools cited: [an2016keyplayer](../references.html#an2016keyplayer)
{% endraw %}
