---
title: "Relational event model fit"
layout: default
parent: "Temporal and events"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Relational event model fit {#concept-top}

Family: [Temporal and events](index.html). Subfamily: Relational event models. Concept id: `rem_fit`. 1 measure.

## Definition {#concept-definition}

Relational event model fit. Entries grouped here: Rem fit.

## Rem fit {#rem_fit}

Measure id: `rem_fit`. Original family: Temporal and events.

**Definition.** Rem fit.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [remstats / remify](../../tools/remstats.html) | ≠ checked, differs by convention |  |  |
| [goldfish](../../tools/goldfish.html) | · reported in docs | `estimate` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `rem_fit_activity` | remstats / remify | any | differs |  | ties | abs 0.0001, rel 0.001 | `remstimate::remstimate(reh, remstats::remstats(reh, tie_effects = ~ inertia() + outdegreeSender() + outdegreeReceiver() + osp(), memory = "full"), method = "MLE")` | remstimate's coefficients differ by up to a few percent on these fixtures, while the reference agrees with the definition oracle's Newton iteration to 1e-11 there (tolerance 1e-9); the difference is in remstimate's optimizer. On pair, remify rejects a stream this short. On the others the maximum partial likelihood estimate does not exist (the likelihood is monotone; the reference and the definition oracle report it as -999) and remstimate returns its last iterate. |
| `rem_fit_basic` | remstats / remify | any | differs |  | ties | abs 0.0001, rel 0.001 | `remstimate::remstimate(reh, remstats::remstats(reh, tie_effects = ~ inertia() + reciprocity() + indegreeReceiver() + otp(), memory = "full"), method = "MLE")` | remstimate's coefficients differ by up to a few percent on these fixtures, while the reference agrees with the definition oracle's Newton iteration to 1e-11 there (tolerance 1e-9); the difference is in remstimate's optimizer. On pair, remify rejects a stream this short. On the others the maximum partial likelihood estimate does not exist (the likelihood is monotone; the reference and the definition oracle report it as -999) and remstimate returns its last iterate. |
| `rem_fit_closure` | remstats / remify | any | differs |  | ties | abs 0.0001, rel 0.001 | `remstimate::remstimate(reh, remstats::remstats(reh, tie_effects = ~ reciprocity() + otp() + itp() + isp(), memory = "full"), method = "MLE")` | remstimate's coefficients differ by up to a few percent on these fixtures, while the reference agrees with the definition oracle's Newton iteration to 1e-11 there (tolerance 1e-9); the difference is in remstimate's optimizer. On pair, remify rejects a stream this short. On the others the maximum partial likelihood estimate does not exist (the likelihood is monotone; the reference and the definition oracle report it as -999) and remstimate returns its last iterate. |
| `rem_fit_decay` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 0.0001, rel 0.001 | `remstimate::remstimate(reh, remstats::remstats(reh, tie_effects = ~ inertia() + reciprocity() + otp(), memory = "decay", memory_value = 5), method = "MLE"), coefficients divided by c = (ln 2 / 5) 2^(-1/5)` | On pair, remify rejects a stream this short. On the others the maximum partial likelihood estimate does not exist (the likelihood is monotone; the reference and the definition oracle report it as -999) and remstimate returns its last iterate. |
| `rem_fit_recency` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 0.0001, rel 0.001 | `remstimate::remstimate(reh, remstats::remstats(reh, tie_effects = ~ recencyContinue() + reciprocity() + recencyReceiveReceiver(), memory = "full"), method = "MLE")` | remify rejects a stream this short (one edge). |
| `rem_fit_window` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 0.0001, rel 0.001 | `remstimate::remstimate(reh, remstats::remstats(reh, tie_effects = ~ inertia() + reciprocity() + indegreeReceiver(), memory = "window", memory_value = 6), method = "MLE")` | On pair, remify rejects a stream this short. On the others the maximum partial likelihood estimate does not exist (the likelihood is monotone; the reference and the definition oracle report it as -999) and remstimate returns its last iterate. |

**Tools cited:** [arena2026remstats](../../references.html#arena2026remstats), [tool_goldfish](../../references.html#tool_goldfish)
{% endraw %}
