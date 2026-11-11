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

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(y\)</td><td>the network as a matrix of tie indicators \(y_{ij}\in\{0,1\}\) (simple graph, no loops); \(y^{ij+}\) and \(y^{ij-}\) have the tie \((i,j)\) set to 1 and 0</td></tr><tr><td>\(g(y)\)</td><td>vector of network statistics</td></tr><tr><td>\(\theta\)</td><td>coefficient vector</td></tr><tr><td>\(\delta_{ij}(y)\)</td><td>change statistic \(g(y^{ij+})-g(y^{ij-})\)</td></tr><tr><td>\(n\)</td><td>number of nodes</td></tr><tr><td>\(x_i\)</td><td>a nodal attribute</td></tr><tr><td>\(B\)</td><td>burn-in steps</td></tr><tr><td>\(s\)</td><td>interval between kept draws</td></tr><tr><td>\(T\)</td><td>number of draws</td></tr></tbody></table></div>

## Definition {#concept-definition}

Draws from an exponential-random-graph model by Metropolis-Hastings toggles started at the given network; returns the statistics of every draw (chain by chain) and the acceptance rate of each chain. The terms are named from the ERGM vocabulary; the node attributes are the columns of the call.

<div class="formula-block"><p class="formula-name"><strong>Exponential random graph model (Frank and Strauss 1986; Holland and Leinhardt 1981)</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\Pr_\theta(Y=y)=\frac{\exp\{\theta^{\top}g(y)\}}{\kappa(\theta)},\qquad \kappa(\theta)=\sum_{y'}\exp\{\theta^{\top}g(y')\}\]</div><p class="formula-where">An exponential family on networks with sufficient statistics \(g\). The normalizing constant sums over all networks of the node set, so it is not computable except for tiny \(n\). Defined for simple graphs; the tool networks used in the comparison hold the simple graph underlying the input (loops dropped, repeated pairs once).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Metropolis-Hastings toggle step (Hastings 1970; Snijders 2002)</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\Pr(\text{accept toggle of }(i,j))=\min\Bigl\{1,\ \exp\bigl(\theta^{\top}[g(y')-g(y)]\bigr)\cdot\frac{q(y\mid y')}{q(y'\mid y)}\Bigr\}\]</div><p class="formula-where">\(y'\) is \(y\) with one dyad toggled and \(q\) is the proposal distribution of the dyad to toggle; the proposal rule changes the chain but not its stationary distribution \(\Pr_\theta\). With a symmetric proposal the ratio is 1. For a toggle that adds a tie, \(g(y')-g(y)=\delta_{ij}\).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Simulated mean statistics</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\bar g=\frac1T\sum_{t=1}^{T}g(Y_{B+ts})\]</div><p class="formula-where">The Monte Carlo mean over \(T\) draws kept after \(B\) burn-in steps at spacing \(s\) converges to \(\mathbb E_\theta g(Y)\) as the chain mixes; it is random (seed, \(B\), \(s\), \(T\)). Mixing may be extremely slow for models near degeneracy.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#ergm_sim_mean">Ergm sim mean</a></td><td><code>ergm_sim_mean</code></td><td>1</td><td>Mean of the statistics over draws from the model at fixed coefficients, started at the given network; compared against another tool within a tolerance of several standard errors. The acceptance rate per chain is also returned.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ergm.html">ergm (statnet)</a></th></tr></thead><tbody><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">A complete start network is a valid state; the chain moves away from it when removing ties has positive probability.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Different seeds give different draws; only the means over many draws agree.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Directed and undirected dyad sets differ (see ergm_statistics).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense).">agrees</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Simple graphs only: the start network is the simple graph underlying the input.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>ergm (statnet)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>ergm (statnet)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## Ergm sim mean {#ergm_sim_mean}

Measure id: `ergm_sim_mean`. Original family: Statistical fitting.

**Definition.** Draws from an exponential-random-graph model by Metropolis-Hastings toggles started at the given network; returns the statistics of every draw (chain by chain) and the acceptance rate of each chain. The terms are named from the ERGM vocabulary; the node attributes are the columns of the call.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>gwdegree; nodematch</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ergm_sim_directed</code></td><td>ergm (statnet)</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0.1, rel 0.02</td><td><code>colMeans(simulate(nw ~ edges + mutual + gwesp(0.5, fixed = TRUE, cutoff = 100) + ctriple + gwdsp(0.5, fixed = TRUE, cutoff = 100), coef = c(-2.5, 1, 0.3, 0, -0.05), nsim = 4000, output = "stats", seed = 1, control = control.simulate.formula(MCMC.burnin = 50000, MCMC.interval = 2000)))</code></td><td></td></tr><tr><td><code>ergm_sim_dyadind_directed</code></td><td>ergm (statnet)</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0.05, rel 0.01</td><td><code>colMeans(simulate(nw ~ edges + mutual + nodematch("mod3"), coef = c(-2, 1.5, 0.5), nsim = 4000, output = "stats", seed = 1, control = control.simulate.formula(MCMC.burnin = 20000, MCMC.interval = 1000)))</code></td><td></td></tr><tr><td><code>ergm_sim_dyadind_undirected</code></td><td>ergm (statnet)</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0.05, rel 0.01</td><td><code>colMeans(simulate(nw ~ edges + nodematch("mod3") + nodecov("num7"), coef = c(-2, 1, 0.1), nsim = 4000, output = "stats", seed = 1, control = control.simulate.formula(MCMC.burnin = 20000, MCMC.interval = 1000)))</code></td><td></td></tr><tr><td><code>ergm_sim_undirected</code></td><td>ergm (statnet)</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0.1, rel 0.02</td><td><code>colMeans(simulate(nw ~ edges + gwesp(0.5, fixed = TRUE, cutoff = 100) + triangle + gwdegree(0.5, fixed = TRUE, cutoff = 100), coef = c(-2.5, 0.4, 0, -0.3), nsim = 4000, output = "stats", seed = 1, control = control.simulate.formula(MCMC.burnin = 50000, MCMC.interval = 2000)))</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/ergm.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/ergm.yaml); [harness/golden/ergm/](https://github.com/knapply/net-oracles/tree/main/harness/golden/ergm/)

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
