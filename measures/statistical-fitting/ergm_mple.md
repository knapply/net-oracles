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

*Definition not yet written.*

## Ergm mple {#ergm_mple}

Measure id: `ergm_mple`. Original family: Statistical fitting.

**Definition.** Maximum pseudo-likelihood estimate of an exponential-random-graph model by Newton iterations on the pooled change statistics; returns the coefficients, their standard errors, the iterations, the convergence and the log pseudo-likelihood. The terms are named from the ERGM vocabulary; the node attributes are the columns of the call.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>ergmMPLE</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ergm_mple_directed</code></td><td>ergm (statnet)</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-10, rel 1e-07</td><td><code>coef(ergm(nw ~ edges + mutual + gwesp(0.5, fixed = TRUE, cutoff = 100) + nodematch("mod3"), estimate = "MPLE"))</code></td><td></td></tr><tr><td><code>ergm_mple_undirected</code></td><td>ergm (statnet)</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-10, rel 1e-07</td><td><code>coef(ergm(nw ~ edges + gwesp(0.5, fixed = TRUE, cutoff = 100) + nodematch("mod3"), estimate = "MPLE"))</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
