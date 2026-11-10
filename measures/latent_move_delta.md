---
title: "Latent move delta"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Latent move delta

Family: Statistical fitting. Identifier: `latent_move_delta`.

## Definition

Latent move delta.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [latentnet](../tools/latentnet.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `latent_move_delta_d2` | latentnet | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `latentnet ergmm.lpY(model, theta) at the intercept and positions after the move minus before, and ergmm.lpY.grad after` | latentnet needs at least three nodes, and its maximum-likelihood fit (which the oracle uses to build the model object) stops with "non-finite value supplied by optim" on the complete graphs, where the likelihood has no finite maximum. |

Tools cited: [krivitsky2008fitting](../references.html#krivitsky2008fitting)
{% endraw %}
