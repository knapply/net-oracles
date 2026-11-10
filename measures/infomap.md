---
title: "Infomap"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Infomap

Family: Communities. Identifier: `infomap`.

## Definition

Infomap.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../tools/igraph.html) | ∅ checked, no value on some inputs | `cluster_infomap` |  |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `community_infomap` | API listing |
| [Infomap](../tools/infomap.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `infomap_native` | Infomap | undirected | no-value-on-some-inputs | (no value) loops | self\_loops | abs 1e-09, rel 1e-09 | `Infomap(two_level = True, directed = False, num_trials = 10, seed = 1) on the links without loops; its codelength` | Infomap leaves self-links out unless asked; the reference value's flow counts them |
| `infomap_native_weighted` | Infomap | undirected | no-value-on-some-inputs | (no value) loops | self\_loops | abs 1e-09, rel 1e-09 | `as infomap_native with link weights` | Infomap leaves self-links out unless asked; the reference value's flow counts them |
| `infomap_partition` | Infomap | any | agrees |  |  | abs 1e-09, rel 1e-09 | `map equation (definition oracle, tau = 0.15) of the partition Infomap(two_level = True, num_trials = 10, seed = 1) finds` |  |
| `infomap_partition_weighted` | Infomap | any | agrees |  |  | abs 1e-09, rel 1e-09 | `as infomap_partition with link weights` |  |
| `infomap_quality` | igraph (R) | undirected | differs | edge\_case | defaults, ties | abs 0.02, rel 0 | `mean over set.seed(1..5) of cluster_infomap(g, nb.trials = 10)$codelength` | a network without edges has no random walk; the reference reports -1 (undefined) where igraph may report a codelength of 0 |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [rosvall2008maps](../references.html#rosvall2008maps)
{% endraw %}
