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

## Latent move delta {#latent_move_delta}

Measure id: `latent_move_delta`. Original family: Statistical fitting.

**Definition.** Latent move delta.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [latentnet](../../tools/latentnet.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `latent_move_delta_d2` | latentnet | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `latentnet ergmm.lpY(model, theta) at the intercept and positions after the move minus before, and ergmm.lpY.grad after` | latentnet needs at least three nodes, and its maximum-likelihood fit (which the oracle uses to build the model object) stops with "non-finite value supplied by optim" on the complete graphs, where the likelihood has no finite maximum. |

**Tools cited:** [krivitsky2008fitting](../../references.html#krivitsky2008fitting)
{% endraw %}
