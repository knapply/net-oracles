---
title: "Latent loglik"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Latent loglik

Family: Statistical fitting. Identifier: `latent_loglik`.

## Definition

Latent loglik.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [latentnet](../tools/latentnet.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `latent_loglik_case_control_all` | latentnet | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `latentnet ergmm.lpY(model, theta) at the given intercept and positions, with ergmm.lpY.grad` | latentnet needs at least three nodes, and its maximum-likelihood fit (which the oracle uses to build the model object) stops with "non-finite value supplied by optim" on the complete graphs, where the likelihood has no finite maximum. |
| `latent_loglik_d1` | latentnet | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `latentnet ergmm.lpY(model, theta) at the given intercept and positions, with ergmm.lpY.grad` | latentnet needs at least three nodes, and its maximum-likelihood fit (which the oracle uses to build the model object) stops with "non-finite value supplied by optim" on the complete graphs, where the likelihood has no finite maximum. |
| `latent_loglik_d2` | latentnet | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `latentnet ergmm.lpY(model, theta) at the given intercept and positions, with ergmm.lpY.grad` | latentnet needs at least three nodes, and its maximum-likelihood fit (which the oracle uses to build the model object) stops with "non-finite value supplied by optim" on the complete graphs, where the likelihood has no finite maximum. |
| `latent_loglik_d3` | latentnet | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `latentnet ergmm.lpY(model, theta) at the given intercept and positions, with ergmm.lpY.grad` | latentnet needs at least three nodes, and its maximum-likelihood fit (which the oracle uses to build the model object) stops with "non-finite value supplied by optim" on the complete graphs, where the likelihood has no finite maximum. |

Tools cited: [krivitsky2008fitting](../references.html#krivitsky2008fitting)
{% endraw %}
