---
title: "ERGM statistics"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# ERGM statistics {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `ergm_statistics`. 1 measure.

## Definition {#concept-definition}

ERGM statistics. Entries grouped here: Ergm statistics.

## Ergm statistics {#ergm_statistics}

Measure id: `ergm_statistics`. Original family: Statistical fitting.

**Definition.** Ergm statistics.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [ergm (statnet)](../../tools/ergm.html) | ✓ checked, agrees | `gwidegree; gwodegree; istar; nodecov; nodefactor; ostar` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ergm_stats_directed` | ergm (statnet) | directed | no-value-on-some-inputs |  | normalization | abs 1e-09, rel 1e-12 | `summary(nw ~ edges + mutual + isolates + istar(2) + ostar(2) + ttriple + ctriple + triangle + gwidegree(0.5, fixed = TRUE, cutoff = 100) + gwodegree(0.5, fixed = TRUE, cutoff = 100) + gwesp(0.5, fixed = TRUE, cutoff = 100) + gwdsp(0.5, fixed = TRUE, cutoff = 100) + nodematch("mod3") + nodefactor("mod3") + nodecov("num7"))` | With two nodes mod3 takes only levels 0 and 1, so nodefactor() gives one statistic instead of two. |
| `ergm_stats_undirected` | ergm (statnet) | undirected | no-value-on-some-inputs |  | normalization | abs 1e-09, rel 1e-12 | `summary(nw ~ edges + isolates + kstar(2:3) + triangle + gwdegree(0.5, fixed = TRUE, cutoff = 100) + gwesp(0.5, fixed = TRUE, cutoff = 100) + gwdsp(0.5, fixed = TRUE, cutoff = 100) + nodematch("mod3") + nodefactor("mod3") + nodecov("num7"))` | With one node only level 0 of mod3 occurs, so nodefactor() has no statistics left after dropping the first level. |

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
