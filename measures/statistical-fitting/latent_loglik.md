---
title: "Latent space log-likelihood"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Latent space log-likelihood {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `latent_loglik`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(z_i\in\mathbb R^d\)</td><td>latent position of node \(i\)</td></tr><tr><td>\(\alpha\)</td><td>intercept</td></tr><tr><td>\(\eta_{ij}\)</td><td>\(\alpha-\|z_i-z_j\|\)</td></tr><tr><td>\(p_{ij}\)</td><td>\(1/(1+e^{-\eta_{ij}})\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Latent space log-likelihood. Entries grouped here: Latent loglik.

<div class="formula-block"><p class="formula-name"><strong>Latent distance model (Hoff, Raftery and Handcock 2002)</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\operatorname{logit}\Pr(y_{ij}=1\mid z,\alpha)=\alpha-\|z_i-z_j\|,\qquad \ell(\alpha,z)=\sum_{i\ne j}\bigl[y_{ij}\eta_{ij}-\log(1+e^{\eta_{ij}})\bigr]\]</div><p class="formula-where">Ties are independent given the positions. The sum runs over ordered pairs for a directed network and over pairs \(i&lt;j\) for an undirected one. The distance is Euclidean in \(d\) dimensions; positions are identified only up to rotation, reflection and translation.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Gradient</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\frac{\partial\ell}{\partial\alpha}=\sum_{i\ne j}(y_{ij}-p_{ij}),\qquad \frac{\partial\ell}{\partial z_i}=-\sum_{j\ne i}(y_{ij}-p_{ij})\frac{z_i-z_j}{\|z_i-z_j\|}\ \ (\text{counting each pair once per direction})\]</div><p class="formula-where">Undefined where two positions coincide (the unit vector has a zero norm); the log-likelihood itself is still defined there.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#latent_loglik">Latent loglik</a></td><td><code>latent_loglik</code></td><td>1</td><td>The log-likelihood and its gradient at given intercept and positions (no fitting); the dimension \(d\) and \(\alpha\) are inputs.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/latentnet.html">latentnet</a></th></tr></thead><tbody><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">For \(n\le1\) there are no pairs and \(\ell=0\); the formula needs no minimum number of nodes.</td><td><span class="st st-w st-nov" title="latentnet needs at least three nodes.">no value</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">The log-likelihood is defined, but it has no finite maximum over \((\alpha,z)\) because every \(y_{ij}=1\) is improved by increasing \(\alpha\).</td><td><span class="st st-w st-nov" title="The maximum-likelihood fit that builds the model object stops with &#x27;non-finite value supplied by optim&#x27; on the complete graphs, where the likelihood has no finite maximum.">no value</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Loops are not part of the model (sums over \(i\ne j\)).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Binary ties only: repeated edges count once.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Ordered pairs for directed networks, pairs \(i&lt;j\) for undirected; the distance term is symmetric so a directed network is treated as two independent ties per pair.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Too few nodes for the formula</summary><ul><li><strong>latentnet</strong>: no value. latentnet needs at least three nodes. <em>(conventions.json latent_loglik)</em></li></ul></details><details><summary>Complete graph</summary><ul><li><strong>latentnet</strong>: no value. The maximum-likelihood fit that builds the model object stops with 'non-finite value supplied by optim' on the complete graphs, where the likelihood has no finite maximum. <em>(conventions.json latent_loglik)</em></li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details></div>

## Latent loglik {#latent_loglik}

Measure id: `latent_loglik`. Original family: Statistical fitting.

**Definition.** Latent loglik.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/latentnet.html">latentnet</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>latent_loglik_case_control_all</code></td><td>latentnet</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>latentnet ergmm.lpY(model, theta) at the given intercept and positions, with ergmm.lpY.grad</code></td><td>latentnet needs at least three nodes, and its maximum-likelihood fit (which the oracle uses to build the model object) stops with "non-finite value supplied by optim" on the complete graphs, where the likelihood has no finite maximum.</td></tr><tr><td><code>latent_loglik_d1</code></td><td>latentnet</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>latentnet ergmm.lpY(model, theta) at the given intercept and positions, with ergmm.lpY.grad</code></td><td>latentnet needs at least three nodes, and its maximum-likelihood fit (which the oracle uses to build the model object) stops with "non-finite value supplied by optim" on the complete graphs, where the likelihood has no finite maximum.</td></tr><tr><td><code>latent_loglik_d2</code></td><td>latentnet</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>latentnet ergmm.lpY(model, theta) at the given intercept and positions, with ergmm.lpY.grad</code></td><td>latentnet needs at least three nodes, and its maximum-likelihood fit (which the oracle uses to build the model object) stops with "non-finite value supplied by optim" on the complete graphs, where the likelihood has no finite maximum.</td></tr><tr><td><code>latent_loglik_d3</code></td><td>latentnet</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>latentnet ergmm.lpY(model, theta) at the given intercept and positions, with ergmm.lpY.grad</code></td><td>latentnet needs at least three nodes, and its maximum-likelihood fit (which the oracle uses to build the model object) stops with "non-finite value supplied by optim" on the complete graphs, where the likelihood has no finite maximum.</td></tr></tbody></table></div>

**Tools cited:** [krivitsky2008fitting](../../references.html#krivitsky2008fitting)
{% endraw %}
