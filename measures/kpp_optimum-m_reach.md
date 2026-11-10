---
title: "Kpp_optimum / m_reach"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Kpp\_optimum / m\_reach

Family: Centrality. Identifier: `kpp_optimum:m_reach`.

## Definition

The set of k key players that best satisfies a key player criterion (Borgatti's greedy swap search or exact enumeration), with its score.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [keyplayer](../tools/keyplayer.html) | ✓ checked, agrees | `kpcent` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `kpp_m_reach_optimum_k3` | keyplayer | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `maximum over every set S of three nodes of keyplayer::kpcent(adjacency, S, 'mreach.degree', M = 1, method = 'min', binary = TRUE, cmode = 'outdegree')` | fewer nodes than the set size, so there is no set to score. |

## References

[borgatti2006identifying](../references.html#borgatti2006identifying), [brandes2008variants](../references.html#brandes2008variants), [dinic1970algorithm](../references.html#dinic1970algorithm), [everett1999centrality](../references.html#everett1999centrality), [everton2012disrupting](../references.html#everton2012disrupting), [ford1956maximal](../references.html#ford1956maximal), [freeman1991centrality](../references.html#freeman1991centrality), [koschutzki2005centrality](../references.html#koschutzki2005centrality)

Tools cited: [an2016keyplayer](../references.html#an2016keyplayer)
{% endraw %}
