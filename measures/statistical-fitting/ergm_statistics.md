---
title: "ERGM statistics"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# ERGM statistics {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `ergm_statistics`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(y\)</td><td>the network as a matrix of tie indicators \(y_{ij}\in\{0,1\}\) (simple graph, no loops); \(y^{ij+}\) and \(y^{ij-}\) have the tie \((i,j)\) set to 1 and 0</td></tr><tr><td>\(g(y)\)</td><td>vector of network statistics</td></tr><tr><td>\(\theta\)</td><td>coefficient vector</td></tr><tr><td>\(\delta_{ij}(y)\)</td><td>change statistic \(g(y^{ij+})-g(y^{ij-})\)</td></tr><tr><td>\(n\)</td><td>number of nodes</td></tr><tr><td>\(x_i\)</td><td>a nodal attribute</td></tr><tr><td>\(d_i,d^{\mathrm{in}}_i,d^{\mathrm{out}}_i\)</td><td>degree, in-degree, out-degree</td></tr></tbody></table></div>

## Definition {#concept-definition}

ERGM statistics. Entries grouped here: Ergm statistics.

<div class="formula-block"><p class="formula-name"><strong>Exponential random graph model (Frank and Strauss 1986; Holland and Leinhardt 1981)</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\Pr_\theta(Y=y)=\frac{\exp\{\theta^{\top}g(y)\}}{\kappa(\theta)},\qquad \kappa(\theta)=\sum_{y'}\exp\{\theta^{\top}g(y')\}\]</div><p class="formula-where">An exponential family on networks with sufficient statistics \(g\). The normalizing constant sums over all networks of the node set, so it is not computable except for tiny \(n\). Defined for simple graphs; the tool networks used in the comparison hold the simple graph underlying the input (loops dropped, repeated pairs once).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Statistics used in the comparison (Morris, Handcock and Hunter 2008; Hunter 2007)</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\begin{aligned}\text{edges}&amp;=\sum y_{ij},\quad \text{mutual}=\sum_{i&lt;j}y_{ij}y_{ji},\quad \text{isolates}=\#\{i:\deg i=0\},\\ \text{kstar}(k)&amp;=\sum_i\tbinom{d_i}{k},\quad \text{istar}(k)=\sum_i\tbinom{d^{\mathrm{in}}_i}{k},\quad \text{ostar}(k)=\sum_i\tbinom{d^{\mathrm{out}}_i}{k},\\ \text{triangle}&amp;=\sum_{i&lt;j&lt;h}y_{ij}y_{jh}y_{ih},\quad \text{ttriple}=\sum_{(i,j,h)}y_{ij}y_{jh}y_{ih},\quad \text{ctriple}=\tfrac13\sum_{(i,j,h)}y_{ij}y_{jh}y_{hi},\\ \text{nodematch}&amp;=\sum y_{ij}\mathbf 1[x_i{=}x_j],\quad \text{nodecov}=\sum y_{ij}(x_i{+}x_j),\quad \text{nodefactor}_\ell=\sum y_{ij}\bigl(\mathbf 1[x_i{=}\ell]{+}\mathbf 1[x_j{=}\ell]\bigr)\end{aligned}\]</div><p class="formula-where">Sums over ties (or node pairs \(i&lt;j\) in undirected networks); the triple sums run over ordered triples of distinct nodes. One nodefactor statistic exists for every level \(\ell\) of the attribute except the first (the baseline), so the number of statistics depends on the attribute levels present.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Geometrically weighted terms (Hunter 2007)</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\text{gwesp}_\alpha=e^{\alpha}\sum_{k=1}^{n-2}\bigl\{1-(1-e^{-\alpha})^{k}\bigr\}\,\mathrm{ESP}_k,\qquad \text{gwdsp}_\alpha=e^{\alpha}\sum_{k=1}^{n-2}\bigl\{1-(1-e^{-\alpha})^{k}\bigr\}\,\mathrm{DSP}_k,\qquad \text{gwdegree}_\alpha=e^{\alpha}\sum_{k=1}^{n-1}\bigl\{1-(1-e^{-\alpha})^{k}\bigr\}\,D_k\]</div><p class="formula-where">\(\mathrm{ESP}_k\): number of tied pairs with exactly \(k\) shared partners; \(\mathrm{DSP}_k\): number of node pairs (tied or not) with \(k\) shared partners; \(D_k\): number of nodes of degree \(k\). With the decay \(\alpha\) fixed they are ordinary statistics; with \(\alpha\) estimated the model is a curved exponential family. Software truncates the counts at a cutoff; a cutoff above \(n\) loses nothing. In directed networks the direction of the shared-partner two-path (and of the degree) has to be chosen, giving gwidegree and gwodegree for in- and out-degrees.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#ergm_statistics">Ergm statistics</a></td><td><code>ergm_statistics</code></td><td>1</td><td>The value of \(g(y)\) for the listed statistics of an observed network (the sums in the second and third formulas); the attribute-based terms use the node index attributes of the comparison.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ergm.html">ergm (statnet)</a></th></tr></thead><tbody><tr><td title="The graph has exactly two nodes."><strong>Two nodes</strong></td><td class="def">The attribute has at most two levels, so nodefactor has one statistic (the first level is the baseline); the other statistics are defined as usual.</td><td><span class="st st-w st-nov" title="With two nodes mod3 takes only levels 0 and 1, so nodefactor() gives one statistic instead of two.">no value</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">One node has no dyad: every statistic is 0, and nodefactor has no non-baseline level left.</td><td><span class="st st-w st-nov" title="With one node only level 0 of mod3 occurs, so nodefactor() has no statistics left after dropping the first level.">no value</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">All sums over ties are 0; the degree-based terms count nodes of degree 0 (isolates equals \(n\)).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">With no node every sum is empty and every statistic is 0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">The model is for simple graphs: parallel edges collapse to one tie before any statistic is computed.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">The model has no loops; loops are dropped.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Directed and undirected networks have different dyad sets and different statistic definitions (below); the same term name can denote different counts.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Two nodes</summary><ul><li><strong>ergm (statnet)</strong>: no value. With two nodes mod3 takes only levels 0 and 1, so nodefactor() gives one statistic instead of two. <em>(conventions.json ergm_statistics)</em></li></ul></details><details><summary>Single node</summary><ul><li><strong>ergm (statnet)</strong>: no value. With one node only level 0 of mod3 occurs, so nodefactor() has no statistics left after dropping the first level. <em>(conventions.json ergm_statistics)</em></li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details></div>

## Ergm statistics {#ergm_statistics}

Measure id: `ergm_statistics`. Original family: Statistical fitting.

**Definition.** Ergm statistics.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>gwidegree; gwodegree; istar; nodecov; nodefactor; ostar</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ergm_stats_directed</code></td><td>ergm (statnet)</td><td>directed</td><td>no-value-on-some-inputs</td><td></td><td>normalization</td><td>abs 1e-09, rel 1e-12</td><td><code>summary(nw ~ edges + mutual + isolates + istar(2) + ostar(2) + ttriple + ctriple + triangle + gwidegree(0.5, fixed = TRUE, cutoff = 100) + gwodegree(0.5, fixed = TRUE, cutoff = 100) + gwesp(0.5, fixed = TRUE, cutoff = 100) + gwdsp(0.5, fixed = TRUE, cutoff = 100) + nodematch("mod3") + nodefactor("mod3") + nodecov("num7"))</code></td><td>With two nodes mod3 takes only levels 0 and 1, so nodefactor() gives one statistic instead of two.</td></tr><tr><td><code>ergm_stats_undirected</code></td><td>ergm (statnet)</td><td>undirected</td><td>no-value-on-some-inputs</td><td></td><td>normalization</td><td>abs 1e-09, rel 1e-12</td><td><code>summary(nw ~ edges + isolates + kstar(2:3) + triangle + gwdegree(0.5, fixed = TRUE, cutoff = 100) + gwesp(0.5, fixed = TRUE, cutoff = 100) + gwdsp(0.5, fixed = TRUE, cutoff = 100) + nodematch("mod3") + nodefactor("mod3") + nodecov("num7"))</code></td><td>With one node only level 0 of mod3 occurs, so nodefactor() has no statistics left after dropping the first level.</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/ergm.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/ergm.yaml); [harness/golden/ergm/](https://github.com/knapply/net-oracles/tree/main/harness/golden/ergm/)

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
