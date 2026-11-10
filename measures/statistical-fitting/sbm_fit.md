---
title: "Stochastic block model fit"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Stochastic block model fit {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `sbm_fit`. 1 measure.

## Definition {#concept-definition}

Stochastic block model fit by minimum description length: agglomerative start, annealed and Markov chain refinement, best of several restarts; returns the blocks, their number and the description length with its parts.

## Sbm fit {#sbm_fit}

Measure id: `sbm_fit`. Original family: Statistical fitting.

**Definition.** Stochastic block model fit by minimum description length: agglomerative start, annealed and Markov chain refinement, best of several restarts; returns the blocks, their number and the description length with its parts.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `minimize_blockmodel_dl` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `sbm_fit_dc_vs_graphtool` | graph-tool | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 |  | The oracle script does not run graph-tool on a network with fewer than two nodes or without edges. |
| `sbm_fit_vs_graphtool` | graph-tool | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 |  | The oracle script does not run graph-tool on a network with fewer than two nodes or without edges. |

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
