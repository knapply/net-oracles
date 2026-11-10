---
title: "SAOM simulated mean statistics"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# SAOM simulated mean statistics {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: SAOM effects. Concept id: `saom_simulated_mean`. 1 measure.

## Definition {#concept-definition}

Simulates periods of network change under a stochastic actor-oriented model (Snijders): actors take ministeps at a common rate and toggle one tie by a multinomial logit of the objective function; returns, per run, the target statistics followed by the changed ties, the ministeps taken and no networks. The effects are named from the SAOM vocabulary; the covariates are the columns of the call.

*Definition not yet written.*

## Saom sim mean {#saom_sim_mean}

Measure id: `saom_sim_mean`. Original family: Statistical fitting.

**Definition.** Simulates periods of network change under a stochastic actor-oriented model (Snijders): actors take ministeps at a common rate and toggle one tie by a multinomial logit of the objective function; returns, per run, the target statistics followed by the changed ties, the ministeps taken and no networks. The effects are named from the SAOM vocabulary; the covariates are the columns of the call.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/rsiena.html">RSiena</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (ties): From a complete starting network RSiena returns a mean tie count of about 5.0 (the stationary value of the model, 5.4), where the reference value... <em>(reason incomplete)</em> <a href="#why-saom_sim_mean-rsiena">details</a></td><td><code>siena07</code></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-saom_sim_mean-rsiena"></a>**[RSiena](../../tools/rsiena.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> RSiena 1.6.6 was run and its value differs from the reference value by convention (ties) on the fixtures complete5\_dir. From a complete starting network RSiena returns a mean tie count of about 5.0 (the stationary value of the model, 5.4), where the reference value and the exact definition oracle relax from 20 ties to 9.3 within the period. The same network with one tie removed gives 8.9 under RSiena (tools/probe\_rsiena.R), in line with the reference, so RSiena treats an all-ones first wave differently; the cause is not identified. Relation to the reference value: Complete first wave: from a complete network the mean tie count is the stationary value (5.0) instead of relaxing to 9.3; one tie removed agrees with the reference; cause not identified. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0.5, rel 0.02 (0 means exact equality). 2 comparisons differ and 12 agree. Finding F085 (defect): From a complete first wave the mean tie count stays at 5.0. Findings: [F085](../../findings.html#f085). **Reason incomplete:** the cause of the difference is stated in the sources as not identified.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>saom_sim_density</code></td><td>RSiena</td><td>directed</td><td>differs</td><td></td><td>ties</td><td>abs 0.5, rel 0.02</td><td><code>RSiena siena07(simOnly = TRUE, returnDeps = TRUE, cond = FALSE, n3 = 8000) with density = -1 and basic rate 3, both fixed; the statistics are computed from the simulated networks</code></td><td>From a complete starting network RSiena returns a mean tie count of about 5.0 (the stationary value of the model, 5.4), where the reference and the exact definition oracle relax from 20 ties to 9.3 within the period. The same network with one tie removed gives 8.9 under RSiena (tools/probe_rsiena.R), in line with the reference, so RSiena treats an all-ones first wave differently; the cause is not identified. RSiena needs at least three actors.</td></tr><tr><td><code>saom_sim_reciprocity</code></td><td>RSiena</td><td>directed</td><td>differs</td><td></td><td>ties</td><td>abs 0.5, rel 0.02</td><td><code>RSiena siena07(simOnly = TRUE, returnDeps = TRUE, cond = FALSE, n3 = 8000) with density = -1, reciprocity = 1 and basic rate 3, all fixed; the statistics are computed from the simulated networks</code></td><td>From a complete starting network RSiena returns a mean tie count of about 5.0 (the stationary value of the model, 5.4), where the reference and the exact definition oracle relax from 20 ties to 9.3 within the period. The same network with one tie removed gives 8.9 under RSiena (tools/probe_rsiena.R), in line with the reference, so RSiena treats an all-ones first wave differently; the cause is not identified. RSiena needs at least three actors.</td></tr></tbody></table></div>

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f085">F085</a></td><td>RSiena</td><td>defect</td><td>From a complete first wave the mean tie count stays at 5.0</td></tr></tbody></table></div>

**Tools cited:** [ripley2026manual](../../references.html#ripley2026manual)
{% endraw %}
