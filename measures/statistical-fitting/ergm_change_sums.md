---
title: "ERGM change statistics"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# ERGM change statistics {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `ergm_change_sums`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(y\)</td><td>the network as a matrix of tie indicators \(y_{ij}\in\{0,1\}\) (simple graph, no loops); \(y^{ij+}\) and \(y^{ij-}\) have the tie \((i,j)\) set to 1 and 0</td></tr><tr><td>\(g(y)\)</td><td>vector of network statistics</td></tr><tr><td>\(\theta\)</td><td>coefficient vector</td></tr><tr><td>\(\delta_{ij}(y)\)</td><td>change statistic \(g(y^{ij+})-g(y^{ij-})\)</td></tr><tr><td>\(n\)</td><td>number of nodes</td></tr><tr><td>\(x_i\)</td><td>a nodal attribute</td></tr></tbody></table></div>

## Definition {#concept-definition}

ERGM change statistics. Entries grouped here: Ergm change sums.

<div class="formula-block"><p class="formula-name"><strong>Exponential random graph model (Frank and Strauss 1986; Holland and Leinhardt 1981)</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\Pr_\theta(Y=y)=\frac{\exp\{\theta^{\top}g(y)\}}{\kappa(\theta)},\qquad \kappa(\theta)=\sum_{y'}\exp\{\theta^{\top}g(y')\}\]</div><p class="formula-where">An exponential family on networks with sufficient statistics \(g\). The normalizing constant sums over all networks of the node set, so it is not computable except for tiny \(n\). Defined for simple graphs; the tool networks used in the comparison hold the simple graph underlying the input (loops dropped, repeated pairs once).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Conditional log-odds of a tie</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\operatorname{logit}\Pr_\theta\bigl(Y_{ij}=1\mid Y_{-ij}=y_{-ij}\bigr)=\theta^{\top}\delta_{ij}(y)\]</div><p class="formula-where">Follows from the model; it is what pseudolikelihood fits and what a toggle in a Markov chain uses.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Sum of change statistics</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[c(y)=\sum_{(i,j)}\delta_{ij}(y)\]</div><p class="formula-where">The change statistic of every dyad, added over all dyads of the observed network (the quantity that enters the score of the pseudolikelihood). For a term that is a sum over ties it equals the number of dyads in which the tie can add to the statistic.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#ergm_change_sums">Ergm change sums</a></td><td><code>ergm_change_sums</code></td><td>1</td><td>Column sums of the change-statistic matrix over all dyads for the listed terms, directed or undirected; the terms are those of ergm_statistics.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ergm.html">ergm (statnet)</a></th></tr></thead><tbody><tr><td title="The graph has exactly two nodes."><strong>Two nodes</strong></td><td class="def">Nodefactor has one statistic (see ergm_statistics).</td><td><span class="st st-w st-nov" title="nodefactor() gives one statistic on two nodes.">no value</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">No dyads: every sum is empty, 0, and nodefactor has no level left.</td><td><span class="st st-w st-nov" title="A network of one node has no dyads, and nodefactor() has no level left.">no value</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Directed networks have \(n(n-1)\) dyads, undirected \(n(n-1)/2\); the change statistics of the same term differ accordingly.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">The model is for simple graphs: parallel edges collapse to one tie before any statistic is computed.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">The model has no loops; loops are dropped.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Two nodes</summary><ul><li><strong>ergm (statnet)</strong>: no value. nodefactor() gives one statistic on two nodes. <em>(conventions.json ergm_change_sums)</em></li></ul></details><details><summary>Single node</summary><ul><li><strong>ergm (statnet)</strong>: no value. A network of one node has no dyads, and nodefactor() has no level left. <em>(conventions.json ergm_change_sums)</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details></div>

## Ergm change sums {#ergm_change_sums}

Measure id: `ergm_change_sums`. Original family: Statistical fitting.

**Definition.** Ergm change sums.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ergm_change_sums_directed</code></td><td>ergm (statnet)</td><td>directed</td><td>no-value-on-some-inputs</td><td></td><td>direction, normalization</td><td>abs 1e-14, rel 1e-12</td><td><code>mple &lt;- ergmMPLE(nw ~ &lt;the terms of ergm_stats_directed&gt;, output = "matrix"); colSums(mple$predictor * mple$weights)</code></td><td>nodefactor() gives one statistic on two nodes (see ergm_stats_directed).</td></tr><tr><td><code>ergm_change_sums_undirected</code></td><td>ergm (statnet)</td><td>undirected</td><td>no-value-on-some-inputs</td><td></td><td>direction, normalization</td><td>abs 1e-14, rel 1e-12</td><td><code>mple &lt;- ergmMPLE(nw ~ &lt;the terms of ergm_stats_undirected&gt;, output = "matrix"); colSums(mple$predictor * mple$weights)</code></td><td>A network of one node has no dyads, and nodefactor() has no level left (see ergm_stats_undirected).</td></tr></tbody></table></div>

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
