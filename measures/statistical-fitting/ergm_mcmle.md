---
title: "ERGM Monte Carlo maximum likelihood"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# ERGM Monte Carlo maximum likelihood {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `ergm_mcmle`. 1 measure.

## Definition {#concept-definition}

Monte Carlo maximum-likelihood estimate of an exponential-random-graph model by Geyer-Thompson rounds of simulation from the current coefficients, started at the pseudo-likelihood estimate or at given coefficients; returns the coefficients, standard errors from the simulated covariance, the rounds, the convergence and the largest t-ratio. The terms are named from the ERGM vocabulary; the node attributes are the columns of the call.

## Ergm mcmle {#ergm_mcmle}

Measure id: `ergm_mcmle`. Original family: Statistical fitting.

**Definition.** Monte Carlo maximum-likelihood estimate of an exponential-random-graph model by Geyer-Thompson rounds of simulation from the current coefficients, started at the pseudo-likelihood estimate or at given coefficients; returns the coefficients, standard errors from the simulated covariance, the rounds, the convergence and the largest t-ratio. The terms are named from the ERGM vocabulary; the node attributes are the columns of the call.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [ergm (statnet)](../../tools/ergm.html) | ✓ checked, agrees | `ergm` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ergm_mcmle_dyadind` | ergm (statnet) | undirected | agrees |  |  | abs 0.015, rel 0 | `coef(ergm(nw ~ edges + nodematch("mod3")))` |  |
| `ergm_mcmle_gwesp` | ergm (statnet) | undirected | agrees |  |  | abs 0.02, rel 0 | `coef(ergm(nw ~ edges + gwesp(0.5, fixed = TRUE, cutoff = 100), control = control.ergm(seed = 1, MCMC.samplesize = 4096)))` |  |

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
