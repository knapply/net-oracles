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

*Definition not yet written.*

## Ergm mcmle {#ergm_mcmle}

Measure id: `ergm_mcmle`. Original family: Statistical fitting.

**Definition.** Monte Carlo maximum-likelihood estimate of an exponential-random-graph model by Geyer-Thompson rounds of simulation from the current coefficients, started at the pseudo-likelihood estimate or at given coefficients; returns the coefficients, standard errors from the simulated covariance, the rounds, the convergence and the largest t-ratio. The terms are named from the ERGM vocabulary; the node attributes are the columns of the call.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>ergm</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ergm_mcmle_dyadind</code></td><td>ergm (statnet)</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0.015, rel 0</td><td><code>coef(ergm(nw ~ edges + nodematch("mod3")))</code></td><td></td></tr><tr><td><code>ergm_mcmle_gwesp</code></td><td>ergm (statnet)</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0.02, rel 0</td><td><code>coef(ergm(nw ~ edges + gwesp(0.5, fixed = TRUE, cutoff = 100), control = control.ergm(seed = 1, MCMC.samplesize = 4096)))</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
