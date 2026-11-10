---
title: "ERGM pseudolikelihood estimation"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# ERGM pseudolikelihood estimation {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `ergm_mple`. 1 measure.

## Definition {#concept-definition}

Maximum pseudo-likelihood estimate of an exponential-random-graph model by Newton iterations on the pooled change statistics; returns the coefficients, their standard errors, the iterations, the convergence and the log pseudo-likelihood. The terms are named from the ERGM vocabulary; the node attributes are the columns of the call.

## Ergm mple {#ergm_mple}

Measure id: `ergm_mple`. Original family: Statistical fitting.

**Definition.** Maximum pseudo-likelihood estimate of an exponential-random-graph model by Newton iterations on the pooled change statistics; returns the coefficients, their standard errors, the iterations, the convergence and the log pseudo-likelihood. The terms are named from the ERGM vocabulary; the node attributes are the columns of the call.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [ergm (statnet)](../../tools/ergm.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `ergmMPLE` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ergm_mple_directed` | ergm (statnet) | directed | agrees |  |  | abs 1e-10, rel 1e-07 | `coef(ergm(nw ~ edges + mutual + gwesp(0.5, fixed = TRUE, cutoff = 100) + nodematch("mod3"), estimate = "MPLE"))` |  |
| `ergm_mple_undirected` | ergm (statnet) | undirected | agrees |  |  | abs 1e-10, rel 1e-07 | `coef(ergm(nw ~ edges + gwesp(0.5, fixed = TRUE, cutoff = 100) + nodematch("mod3"), estimate = "MPLE"))` |  |

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
