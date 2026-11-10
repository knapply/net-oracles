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

## Ergm sim mean {#ergm_sim_mean}

Measure id: `ergm_sim_mean`. Original family: Statistical fitting.

**Definition.** Draws from an exponential-random-graph model by Metropolis-Hastings toggles started at the given network; returns the statistics of every draw (chain by chain) and the acceptance rate of each chain. The terms are named from the ERGM vocabulary; the node attributes are the columns of the call.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [ergm (statnet)](../../tools/ergm.html) | ✓ checked, agrees | `gwdegree; nodematch` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ergm_sim_directed` | ergm (statnet) | directed | agrees |  |  | abs 0.1, rel 0.02 | `colMeans(simulate(nw ~ edges + mutual + gwesp(0.5, fixed = TRUE, cutoff = 100) + ctriple + gwdsp(0.5, fixed = TRUE, cutoff = 100), coef = c(-2.5, 1, 0.3, 0, -0.05), nsim = 4000, output = "stats", seed = 1, control = control.simulate.formula(MCMC.burnin = 50000, MCMC.interval = 2000)))` |  |
| `ergm_sim_dyadind_directed` | ergm (statnet) | directed | agrees |  |  | abs 0.05, rel 0.01 | `colMeans(simulate(nw ~ edges + mutual + nodematch("mod3"), coef = c(-2, 1.5, 0.5), nsim = 4000, output = "stats", seed = 1, control = control.simulate.formula(MCMC.burnin = 20000, MCMC.interval = 1000)))` |  |
| `ergm_sim_dyadind_undirected` | ergm (statnet) | undirected | agrees |  |  | abs 0.05, rel 0.01 | `colMeans(simulate(nw ~ edges + nodematch("mod3") + nodecov("num7"), coef = c(-2, 1, 0.1), nsim = 4000, output = "stats", seed = 1, control = control.simulate.formula(MCMC.burnin = 20000, MCMC.interval = 1000)))` |  |
| `ergm_sim_undirected` | ergm (statnet) | undirected | agrees |  |  | abs 0.1, rel 0.02 | `colMeans(simulate(nw ~ edges + gwesp(0.5, fixed = TRUE, cutoff = 100) + triangle + gwdegree(0.5, fixed = TRUE, cutoff = 100), coef = c(-2.5, 0.4, 0, -0.3), nsim = 4000, output = "stats", seed = 1, control = control.simulate.formula(MCMC.burnin = 50000, MCMC.interval = 2000)))` |  |

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
