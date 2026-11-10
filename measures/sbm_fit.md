---
title: "Sbm fit"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Sbm fit

Family: Statistical fitting. Identifier: `sbm_fit`.

## Definition

Stochastic block model fit by minimum description length: agglomerative start, annealed and Markov chain refinement, best of several restarts; returns the blocks, their number and the description length with its parts.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [graph-tool](../tools/graphtool.html) | ✓ checked, agrees | `minimize_blockmodel_dl` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `sbm_fit_dc_vs_graphtool` | graph-tool | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 |  | The oracle script does not run graph-tool on a network with fewer than two nodes or without edges. |
| `sbm_fit_vs_graphtool` | graph-tool | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 |  | The oracle script does not run graph-tool on a network with fewer than two nodes or without edges. |

Tools cited: [peixoto2014graphtool](../references.html#peixoto2014graphtool)
{% endraw %}
