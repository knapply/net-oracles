---
title: "Latent space move delta"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Latent space move delta {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `latent_move_delta`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(z_i\in\mathbb R^d\)</td><td>latent position of node \(i\)</td></tr><tr><td>\(\alpha\)</td><td>intercept</td></tr><tr><td>\(\eta_{ij}\)</td><td>\(\alpha-\|z_i-z_j\|\)</td></tr><tr><td>\(p_{ij}\)</td><td>\(1/(1+e^{-\eta_{ij}})\)</td></tr><tr><td>\(z_i'\)</td><td>new position of the moved node \(i\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Latent space move delta. Entries grouped here: Latent move delta.

<div class="formula-block"><p class="formula-name"><strong>Latent distance model (Hoff, Raftery and Handcock 2002)</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\operatorname{logit}\Pr(y_{ij}=1\mid z,\alpha)=\alpha-\|z_i-z_j\|,\qquad \ell(\alpha,z)=\sum_{i\ne j}\bigl[y_{ij}\eta_{ij}-\log(1+e^{\eta_{ij}})\bigr]\]</div><p class="formula-where">Ties are independent given the positions. The sum runs over ordered pairs for a directed network and over pairs \(i&lt;j\) for an undirected one. The distance is Euclidean in \(d\) dimensions; positions are identified only up to rotation, reflection and translation.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Change in log-likelihood from moving one node</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\Delta=\ell(\alpha,z')-\ell(\alpha,z)=\sum_{j\ne i}\Bigl[\ell_{ij}(\alpha,z_i',z_j)-\ell_{ij}(\alpha,z_i,z_j)\Bigr]\quad(\times2\text{ pairs per }j\text{ if directed})\]</div><p class="formula-where">Only pairs that contain the moved node \(i\) change, so the update costs \(n-1\) terms, not \(n^2\). \(\ell_{ij}\) is the term of the pair in the sum above.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#latent_move_delta">Latent move delta</a></td><td><code>latent_move_delta</code></td><td>1</td><td>The difference of the log-likelihood after and before a one-node move (and the gradient after it).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/latentnet.html">latentnet</a></th></tr></thead><tbody><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">For \(n=1\) the sum is empty and \(\Delta=0\).</td><td><span class="st st-w st-nov" title="latentnet needs at least three nodes.">no value</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">Defined for any positions; the lack of a finite maximum does not matter for a difference.</td><td><span class="st st-w st-nov" title="The maximum-likelihood fit that builds the model object stops with &#x27;non-finite value supplied by optim&#x27; on the complete graphs, where the likelihood has no finite maximum.">no value</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Too few nodes for the formula</summary><ul><li><strong>latentnet</strong>: no value. latentnet needs at least three nodes. <em>(conventions.json latent_move_delta)</em></li></ul></details><details><summary>Complete graph</summary><ul><li><strong>latentnet</strong>: no value. The maximum-likelihood fit that builds the model object stops with 'non-finite value supplied by optim' on the complete graphs, where the likelihood has no finite maximum. <em>(conventions.json latent_move_delta)</em></li></ul></details></div>

## Latent move delta {#latent_move_delta}

Measure id: `latent_move_delta`. Original family: Statistical fitting.

**Definition.** Latent move delta.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/latentnet.html">latentnet</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>latent_move_delta_d2</code></td><td>latentnet</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>latentnet ergmm.lpY(model, theta) at the intercept and positions after the move minus before, and ergmm.lpY.grad after</code></td><td>latentnet needs at least three nodes, and its maximum-likelihood fit (which the oracle uses to build the model object) stops with "non-finite value supplied by optim" on the complete graphs, where the likelihood has no finite maximum.</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/latent_space.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/latent_space.yaml); [harness/golden/latentnet/](https://github.com/knapply/net-oracles/tree/main/harness/golden/latentnet/)

**Tools cited:** [krivitsky2008fitting](../../references.html#krivitsky2008fitting)
{% endraw %}
