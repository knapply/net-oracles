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

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(y\)</td><td>the network as a matrix of tie indicators \(y_{ij}\in\{0,1\}\) (simple graph, no loops); \(y^{ij+}\) and \(y^{ij-}\) have the tie \((i,j)\) set to 1 and 0</td></tr><tr><td>\(g(y)\)</td><td>vector of network statistics</td></tr><tr><td>\(\theta\)</td><td>coefficient vector</td></tr><tr><td>\(\delta_{ij}(y)\)</td><td>change statistic \(g(y^{ij+})-g(y^{ij-})\)</td></tr><tr><td>\(n\)</td><td>number of nodes</td></tr><tr><td>\(x_i\)</td><td>a nodal attribute</td></tr><tr><td>\(\eta\)</td><td>the coefficient vector at which the simulation was run</td></tr><tr><td>\(Y_1,\dots,Y_M\)</td><td>draws from \(\Pr_\eta\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Monte Carlo maximum-likelihood estimate of an exponential-random-graph model by Geyer-Thompson rounds of simulation from the current coefficients, started at the pseudo-likelihood estimate or at given coefficients; returns the coefficients, standard errors from the simulated covariance, the rounds, the convergence and the largest t-ratio. The terms are named from the ERGM vocabulary; the node attributes are the columns of the call.

<div class="formula-block"><p class="formula-name"><strong>Exponential random graph model (Frank and Strauss 1986; Holland and Leinhardt 1981)</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\Pr_\theta(Y=y)=\frac{\exp\{\theta^{\top}g(y)\}}{\kappa(\theta)},\qquad \kappa(\theta)=\sum_{y'}\exp\{\theta^{\top}g(y')\}\]</div><p class="formula-where">An exponential family on networks with sufficient statistics \(g\). The normalizing constant sums over all networks of the node set, so it is not computable except for tiny \(n\). Defined for simple graphs; the tool networks used in the comparison hold the simple graph underlying the input (loops dropped, repeated pairs once).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Monte Carlo likelihood approximation (Geyer and Thompson 1992)</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\ell(\theta)-\ell(\eta)\approx(\theta-\eta)^{\top}g(y_{\mathrm{obs}})-\log\Bigl\{\frac1M\sum_{m=1}^{M}\exp\bigl[(\theta-\eta)^{\top}g(Y_m)\bigr]\Bigr\}\]</div><p class="formula-where">The log-likelihood ratio relative to \(\eta\) is estimated from simulated statistics; the approximation maximized in each round replaces the intractable normalizing constant. Rounds repeat with \(\eta\) set to the latest maximizer until the observed statistics are close to the simulated mean; the start is the pseudolikelihood estimate or given values.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Likelihood equations at the maximizer</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\mathbb E_{\hat\theta}\bigl[g(Y)\bigr]=g(y_{\mathrm{obs}})\]</div><p class="formula-where">The maximum likelihood estimate matches the expected statistics to the observed ones; when \(g(y_{\mathrm{obs}})\) lies on the boundary of the convex hull of the attainable statistics the maximum likelihood estimate does not exist.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#ergm_mcmle">Ergm mcmle</a></td><td><code>ergm_mcmle</code></td><td>1</td><td>Monte Carlo estimate of the maximum likelihood coefficients; the result is random (it depends on the seed, the sample size and the number of rounds), so it can only be compared within a Monte Carlo tolerance.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ergm.html">ergm (statnet)</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">The observed statistics are on the boundary of the attainable set: the maximum likelihood estimate does not exist.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">Same as the edgeless network for a model with an edge term.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Equal likelihood values do not arise generically; repeated runs with different seeds give different estimates around the same maximizer.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">The model is for simple graphs: parallel edges collapse to one tie before any statistic is computed.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">The model has no loops; loops are dropped.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Edge weights are not part of the model; the network is binary.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir).">agrees</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>ergm (statnet)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Self-loops</summary><ul><li><strong>ergm (statnet)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Edge weights</summary><ul><li><strong>ergm (statnet)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## Ergm mcmle {#ergm_mcmle}

Measure id: `ergm_mcmle`. Original family: Statistical fitting.

**Definition.** Monte Carlo maximum-likelihood estimate of an exponential-random-graph model by Geyer-Thompson rounds of simulation from the current coefficients, started at the pseudo-likelihood estimate or at given coefficients; returns the coefficients, standard errors from the simulated covariance, the rounds, the convergence and the largest t-ratio. The terms are named from the ERGM vocabulary; the node attributes are the columns of the call.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>ergm</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ergm_mcmle_dyadind</code></td><td>ergm (statnet)</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0.015, rel 0</td><td><code>coef(ergm(nw ~ edges + nodematch("mod3")))</code></td><td></td></tr><tr><td><code>ergm_mcmle_gwesp</code></td><td>ergm (statnet)</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0.02, rel 0</td><td><code>coef(ergm(nw ~ edges + gwesp(0.5, fixed = TRUE, cutoff = 100), control = control.ergm(seed = 1, MCMC.samplesize = 4096)))</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
