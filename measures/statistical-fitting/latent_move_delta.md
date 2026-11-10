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

## Definition {#concept-definition}

Latent space move delta. Entries grouped here: Latent move delta.

*Definition not yet written.*

## Latent move delta {#latent_move_delta}

Measure id: `latent_move_delta`. Original family: Statistical fitting.

**Definition.** Latent move delta.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/latentnet.html">latentnet</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>latent_move_delta_d2</code></td><td>latentnet</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>latentnet ergmm.lpY(model, theta) at the intercept and positions after the move minus before, and ergmm.lpY.grad after</code></td><td>latentnet needs at least three nodes, and its maximum-likelihood fit (which the oracle uses to build the model object) stops with "non-finite value supplied by optim" on the complete graphs, where the likelihood has no finite maximum.</td></tr></tbody></table></div>

**Tools cited:** [krivitsky2008fitting](../../references.html#krivitsky2008fitting)
{% endraw %}
