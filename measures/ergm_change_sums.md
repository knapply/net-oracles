---
title: "Ergm change sums"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Ergm change sums

Family: Statistical fitting. Identifier: `ergm_change_sums`.

## Definition

Ergm change sums.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [ergm (statnet)](../tools/ergm.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ergm_change_sums_directed` | ergm (statnet) | directed | no-value-on-some-inputs |  | direction, normalization | abs 1e-14, rel 1e-12 | `mple <- ergmMPLE(nw ~ <the terms of ergm_stats_directed>, output = "matrix"); colSums(mple$predictor * mple$weights)` | nodefactor() gives one statistic on two nodes (see ergm\_stats\_directed). |
| `ergm_change_sums_undirected` | ergm (statnet) | undirected | no-value-on-some-inputs |  | direction, normalization | abs 1e-14, rel 1e-12 | `mple <- ergmMPLE(nw ~ <the terms of ergm_stats_undirected>, output = "matrix"); colSums(mple$predictor * mple$weights)` | A network of one node has no dyads, and nodefactor() has no level left (see ergm\_stats\_undirected). |

Tools cited: [hunter2008ergm](../references.html#hunter2008ergm)
{% endraw %}
