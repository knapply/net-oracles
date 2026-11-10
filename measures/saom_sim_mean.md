---
title: "Saom sim mean"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Saom sim mean

Family: Statistical fitting. Identifier: `saom_sim_mean`.

## Definition

Simulates periods of network change under a stochastic actor-oriented model (Snijders): actors take ministeps at a common rate and toggle one tie by a multinomial logit of the objective function; returns, per run, the target statistics followed by the changed ties, the ministeps taken and no networks. The effects are named from the SAOM vocabulary; the covariates are the columns of the call.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [RSiena](../tools/rsiena.html) | ≠ checked, differs by convention | `siena07` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `saom_sim_density` | RSiena | directed | differs |  | ties | abs 0.5, rel 0.02 | `RSiena siena07(simOnly = TRUE, returnDeps = TRUE, cond = FALSE, n3 = 8000) with density = -1 and basic rate 3, both fixed; the statistics are computed from the simulated networks` | From a complete starting network RSiena returns a mean tie count of about 5.0 (the stationary value of the model, 5.4), where the reference and the exact definition oracle relax from 20 ties to 9.3 within the period. The same network with one tie removed gives 8.9 under RSiena (tools/probe\_rsiena.R), in line with the reference, so RSiena treats an all-ones first wave differently; the cause is not identified. RSiena needs at least three actors. |
| `saom_sim_reciprocity` | RSiena | directed | differs |  | ties | abs 0.5, rel 0.02 | `RSiena siena07(simOnly = TRUE, returnDeps = TRUE, cond = FALSE, n3 = 8000) with density = -1, reciprocity = 1 and basic rate 3, all fixed; the statistics are computed from the simulated networks` | From a complete starting network RSiena returns a mean tie count of about 5.0 (the stationary value of the model, 5.4), where the reference and the exact definition oracle relax from 20 ties to 9.3 within the period. The same network with one tie removed gives 8.9 under RSiena (tools/probe\_rsiena.R), in line with the reference, so RSiena treats an all-ones first wave differently; the cause is not identified. RSiena needs at least three actors. |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F085](../findings.html#f085) | RSiena | defect | From a complete first wave the mean tie count stays at 5.0 |

Tools cited: [ripley2026manual](../references.html#ripley2026manual)
{% endraw %}
