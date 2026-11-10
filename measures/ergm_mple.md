---
title: "Ergm mple"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Ergm mple

Family: Statistical fitting. Identifier: `ergm_mple`.

## Definition

Maximum pseudo-likelihood estimate of an exponential-random-graph model by Newton iterations on the pooled change statistics; returns the coefficients, their standard errors, the iterations, the convergence and the log pseudo-likelihood. The terms are named from the ERGM vocabulary; the node attributes are the columns of the call.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [ergm (statnet)](../tools/ergm.html) | ✓ checked, agrees | `ergmMPLE` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ergm_mple_directed` | ergm (statnet) | directed | agrees |  |  | abs 1e-10, rel 1e-07 | `coef(ergm(nw ~ edges + mutual + gwesp(0.5, fixed = TRUE, cutoff = 100) + nodematch("mod3"), estimate = "MPLE"))` |  |
| `ergm_mple_undirected` | ergm (statnet) | undirected | agrees |  |  | abs 1e-10, rel 1e-07 | `coef(ergm(nw ~ edges + gwesp(0.5, fixed = TRUE, cutoff = 100) + nodematch("mod3"), estimate = "MPLE"))` |  |

Tools cited: [hunter2008ergm](../references.html#hunter2008ergm)
{% endraw %}
