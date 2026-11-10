---
title: "Kpp_optimum / distance_reach"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Kpp\_optimum / distance\_reach

Family: Centrality. Identifier: `kpp_optimum:distance_reach`.

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
| `kpp_distance_reach_optimum_k2` | keyplayer | any | no-value-on-some-inputs |  |  | abs 1e-14, rel 1e-12 | `maximum over every pair S of (\|S\| + (n - \|S\|) kpcent(adjacency, S, 'mreach.closeness', M = Inf, method = 'min', binary = TRUE, cmode = 'outdegree')) / n` | no set of two nodes leaves anything to reach (single node), and keyplayer::kpcent fails on a two-node network. |

## References

[borgatti2006identifying](../references.html#borgatti2006identifying), [brandes2008variants](../references.html#brandes2008variants), [dinic1970algorithm](../references.html#dinic1970algorithm), [everett1999centrality](../references.html#everett1999centrality), [everton2012disrupting](../references.html#everton2012disrupting), [ford1956maximal](../references.html#ford1956maximal), [freeman1991centrality](../references.html#freeman1991centrality), [koschutzki2005centrality](../references.html#koschutzki2005centrality)

Tools cited: [an2016keyplayer](../references.html#an2016keyplayer)
{% endraw %}
