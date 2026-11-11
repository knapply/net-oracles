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

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(y\)</td><td>the network as a matrix of tie indicators \(y_{ij}\in\{0,1\}\) (simple graph, no loops); \(y^{ij+}\) and \(y^{ij-}\) have the tie \((i,j)\) set to 1 and 0</td></tr><tr><td>\(g(y)\)</td><td>vector of network statistics</td></tr><tr><td>\(\theta\)</td><td>coefficient vector</td></tr><tr><td>\(\delta_{ij}(y)\)</td><td>change statistic \(g(y^{ij+})-g(y^{ij-})\)</td></tr><tr><td>\(n\)</td><td>number of nodes</td></tr><tr><td>\(x_i\)</td><td>a nodal attribute</td></tr></tbody></table></div>

## Definition {#concept-definition}

Maximum pseudo-likelihood estimate of an exponential-random-graph model by Newton iterations on the pooled change statistics; returns the coefficients, their standard errors, the iterations, the convergence and the log pseudo-likelihood. The terms are named from the ERGM vocabulary; the node attributes are the columns of the call.

<div class="formula-block"><p class="formula-name"><strong>Exponential random graph model (Frank and Strauss 1986; Holland and Leinhardt 1981)</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\Pr_\theta(Y=y)=\frac{\exp\{\theta^{\top}g(y)\}}{\kappa(\theta)},\qquad \kappa(\theta)=\sum_{y'}\exp\{\theta^{\top}g(y')\}\]</div><p class="formula-where">An exponential family on networks with sufficient statistics \(g\). The normalizing constant sums over all networks of the node set, so it is not computable except for tiny \(n\). Defined for simple graphs; the tool networks used in the comparison hold the simple graph underlying the input (loops dropped, repeated pairs once).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Conditional log-odds of a tie</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\operatorname{logit}\Pr_\theta\bigl(Y_{ij}=1\mid Y_{-ij}=y_{-ij}\bigr)=\theta^{\top}\delta_{ij}(y)\]</div><p class="formula-where">Follows from the model; it is what pseudolikelihood fits and what a toggle in a Markov chain uses.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Maximum pseudolikelihood estimate (Strauss and Ikeda 1990)</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\hat\theta_{\mathrm{MPLE}}=\arg\max_\theta\sum_{i\ne j}\Bigl[y_{ij}\,\theta^{\top}\delta_{ij}(y)-\log\bigl(1+e^{\theta^{\top}\delta_{ij}(y)}\bigr)\Bigr]\]</div><p class="formula-where">A logistic regression of the tie indicators on the change statistics, which ignores the dependence among dyads: the estimate is not the maximum likelihood estimate and its standard errors are not valid. It does not exist when the response is separated by the change statistics (for example an edgeless or complete network with an edge term), where the log pseudolikelihood is monotone.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#ergm_mple">Ergm mple</a></td><td><code>ergm_mple</code></td><td>1</td><td>Coefficients (and their standard errors, iterations and convergence flag) of the logistic regression above, found by Newton iterations on the pooled change statistics. Unique when it exists, because the log pseudolikelihood is concave.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ergm.html">ergm (statnet)</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">The edge coefficient has no finite estimate: the response is constant, the log pseudolikelihood is monotone.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">As for the edgeless network: constant response, no finite estimate for a model with an edge term.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">Fewer dyads than coefficients leave the regression underdetermined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">The model is for simple graphs: parallel edges collapse to one tie before any statistic is computed.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">The model has no loops; loops are dropped.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Directed and undirected networks have different dyad sets and different statistic definitions (below); the same term name can denote different counts.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense).">agrees</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Too few nodes for the formula</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>ergm (statnet)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Self-loops</summary><ul><li><strong>ergm (statnet)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>ergm (statnet)</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## Ergm mple {#ergm_mple}

Measure id: `ergm_mple`. Original family: Statistical fitting.

**Definition.** Maximum pseudo-likelihood estimate of an exponential-random-graph model by Newton iterations on the pooled change statistics; returns the coefficients, their standard errors, the iterations, the convergence and the log pseudo-likelihood. The terms are named from the ERGM vocabulary; the node attributes are the columns of the call.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>ergmMPLE</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ergm_mple_directed</code></td><td>ergm (statnet)</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-10, rel 1e-07</td><td><code>coef(ergm(nw ~ edges + mutual + gwesp(0.5, fixed = TRUE, cutoff = 100) + nodematch("mod3"), estimate = "MPLE"))</code></td><td></td></tr><tr><td><code>ergm_mple_undirected</code></td><td>ergm (statnet)</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-10, rel 1e-07</td><td><code>coef(ergm(nw ~ edges + gwesp(0.5, fixed = TRUE, cutoff = 100) + nodematch("mod3"), estimate = "MPLE"))</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/ergm.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/ergm.yaml); [harness/golden/ergm/](https://github.com/knapply/net-oracles/tree/main/harness/golden/ergm/)

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
