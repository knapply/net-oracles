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

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(x\)</td><td>directed network (state)</td></tr><tr><td>\(x^{(ij)}\)</td><td>\(x\) with the tie variable \((i,j)\) toggled; \(x^{(ii)}=x\) means no change</td></tr><tr><td>\(\lambda_i\)</td><td>rate of change opportunities of actor \(i\)</td></tr><tr><td>\(f_i(x)\)</td><td>objective function \(\sum_k\beta_ks_{ik}(x)\)</td></tr><tr><td>\(s_{ik}\)</td><td>effect statistic: outdegree \(\sum_jx_{ij}\), reciprocity \(\sum_jx_{ij}x_{ji}\), ...</td></tr></tbody></table></div>

## Definition {#concept-definition}

Simulates periods of network change under a stochastic actor-oriented model (Snijders): actors take ministeps at a common rate and toggle one tie by a multinomial logit of the objective function; returns, per run, the target statistics followed by the changed ties, the ministeps taken and no networks. The effects are named from the SAOM vocabulary; the covariates are the columns of the call.

<div class="formula-block"><p class="formula-name"><strong>Stochastic actor-oriented model (Snijders 2001; Snijders 1996)</strong> <span class="applies">applies to: any, directed</span></p><div class="formula">\[\Pr(i\text{ toggles }(i,j)\mid x)=\frac{\exp f_i(x^{(ij)})}{\sum_{h}\exp f_i(x^{(ih)})},\qquad \text{waiting time to the next opportunity}\sim\mathrm{Exp}\Bigl(\sum_i\lambda_i\Bigr)\]</div><p class="formula-where">Actors take ministeps at a common rate and change one tie variable by a multinomial logit of the objective function after the change; the sum in the denominator includes the choice of no change. Continuous time runs over a period of length 1 between observations. Simulation starts at the first observed network and the statistics of the final network are averaged over replications, so the mean is random.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Simulated mean</strong> <span class="applies">applies to: any, directed</span></p><div class="formula">\[\bar s_k=\frac1R\sum_{r=1}^{R}s_k\bigl(x^{(r)}_{\mathrm{end}}\bigr)\]</div><p class="formula-where">Mean of the effect statistics over \(R\) simulated end networks; it converges to the model expectation after one period from the start network.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#saom_sim_mean">Saom sim mean</a></td><td><code>saom_sim_mean</code></td><td>1</td><td>Mean statistics of simulated end networks with fixed rate and effect parameters (density, reciprocity); no estimation.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/rsiena.html">RSiena</a></th></tr></thead><tbody><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">Three or more actors are needed by the tool; the definition itself has choices for any \(n\ge2\).</td><td><a class="st st-w st-nov" href="#why-saom_sim_mean-rsiena" title="RSiena needs at least three actors (no value on empty, pair and single_node fixtures).">no value</a></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">A complete start network is a valid state of the model; the definition simulates from it like from any other network, so the mean tie count moves from the start value towards the model's stationary value over the period.</td><td><a class="st st-w st-conv" href="../../findings.html#f085" title="From a complete starting network RSiena returns a mean tie count of about 5.0 (the stationary value, 5.4), where the reference and the exact definition oracle relax from 20 ties to 9.3 within the period; one tie removed gives 8.9 under RSiena, in line with the reference. Cause not identified.">differs</a></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Replications differ by seed; only means over many replications are compared.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Too few nodes for the formula</summary><ul><li><strong>RSiena</strong>: no value. RSiena needs at least three actors (no value on empty, pair and single_node fixtures). <em>(reasons.json saom_sim_mean)</em></li></ul></details><details><summary>Complete graph</summary><ul><li><strong>RSiena</strong>: differs. From a complete starting network RSiena returns a mean tie count of about 5.0 (the stationary value, 5.4), where the reference and the exact definition oracle relax from 20 ties to 9.3 within the period; one tie removed gives 8.9 under RSiena, in line with the reference. Cause not identified. <em>(reasons.json saom_sim_mean)</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details></div>

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
