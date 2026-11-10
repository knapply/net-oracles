---
title: "ERGM simulated mean statistics"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# ERGM simulated mean statistics {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `ergm_sim_mean`. 1 measure.

## Definition {#concept-definition}

Draws from an exponential-random-graph model by Metropolis-Hastings toggles started at the given network; returns the statistics of every draw (chain by chain) and the acceptance rate of each chain. The terms are named from the ERGM vocabulary; the node attributes are the columns of the call.

*Definition not yet written.*

## Ergm sim mean {#ergm_sim_mean}

Measure id: `ergm_sim_mean`. Original family: Statistical fitting.

**Definition.** Draws from an exponential-random-graph model by Metropolis-Hastings toggles started at the given network; returns the statistics of every draw (chain by chain) and the acceptance rate of each chain. The terms are named from the ERGM vocabulary; the node attributes are the columns of the call.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>gwdegree; nodematch</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ergm_sim_directed</code></td><td>ergm (statnet)</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0.1, rel 0.02</td><td><code>colMeans(simulate(nw ~ edges + mutual + gwesp(0.5, fixed = TRUE, cutoff = 100) + ctriple + gwdsp(0.5, fixed = TRUE, cutoff = 100), coef = c(-2.5, 1, 0.3, 0, -0.05), nsim = 4000, output = "stats", seed = 1, control = control.simulate.formula(MCMC.burnin = 50000, MCMC.interval = 2000)))</code></td><td></td></tr><tr><td><code>ergm_sim_dyadind_directed</code></td><td>ergm (statnet)</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0.05, rel 0.01</td><td><code>colMeans(simulate(nw ~ edges + mutual + nodematch("mod3"), coef = c(-2, 1.5, 0.5), nsim = 4000, output = "stats", seed = 1, control = control.simulate.formula(MCMC.burnin = 20000, MCMC.interval = 1000)))</code></td><td></td></tr><tr><td><code>ergm_sim_dyadind_undirected</code></td><td>ergm (statnet)</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0.05, rel 0.01</td><td><code>colMeans(simulate(nw ~ edges + nodematch("mod3") + nodecov("num7"), coef = c(-2, 1, 0.1), nsim = 4000, output = "stats", seed = 1, control = control.simulate.formula(MCMC.burnin = 20000, MCMC.interval = 1000)))</code></td><td></td></tr><tr><td><code>ergm_sim_undirected</code></td><td>ergm (statnet)</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0.1, rel 0.02</td><td><code>colMeans(simulate(nw ~ edges + gwesp(0.5, fixed = TRUE, cutoff = 100) + triangle + gwdegree(0.5, fixed = TRUE, cutoff = 100), coef = c(-2.5, 0.4, 0, -0.3), nsim = 4000, output = "stats", seed = 1, control = control.simulate.formula(MCMC.burnin = 50000, MCMC.interval = 2000)))</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
