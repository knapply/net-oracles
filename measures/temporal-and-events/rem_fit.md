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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [remstats / remify](../../tools/remstats.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (ties): remstimate's coefficients differ by up to a few percent on these fixtures, while the reference agrees with the definition oracle's Newton iteration... [details](#why-rem_fit-remstats) |  |  |
| [goldfish](../../tools/goldfish.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: goldfish is documented-only in this survey; listed in its documentation. [details](#why-rem_fit-goldfish) | `estimate` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-rem_fit-remstats"></a>**[remstats / remify](../../tools/remstats.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> remstats / remify remstats 4.1.0, remstimate 3.1.0, remify 4.1.0 was run and its value differs from the reference value by convention (ties) on the fixtures complete5\_dir, gnp\_dir\_dense. remstimate's coefficients differ by up to a few percent on these fixtures, while the reference agrees with the definition oracle's Newton iteration to 1e-11 there (tolerance 1e-9); the difference is in remstimate's optimizer. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0.0001, rel 0.001 (0 means exact equality). No value (rem\_fit\_decay) on the fixtures cycle7\_dir, davis\_twomode, florentine, pair, path10, southern\_women, star8, twomode\_random, twomode\_weighted: On pair, remify rejects a stream this short. On the others the maximum partial likelihood estimate does not exist (the likelihood is monotone; the reference value and the definition oracle report it as -999) and remstimate returns its last iterate. No value (rem\_fit\_recency) on the fixtures pair: remify rejects a stream this short (one edge). No value (rem\_fit\_window) on the fixtures davis\_twomode, gnp\_dir\_sparse, gnp\_und\_dense, gnp\_und\_sparse, karate, les\_miserables, pair, real\_weights\_dir, real\_weights\_und, southern\_women, twomode\_random, twomode\_weighted, uniform\_weights, weighted\_dir, weighted\_und: On pair, remify rejects a stream this short. On the others the maximum partial likelihood estimate does not exist (the likelihood is monotone; the reference value and the definition oracle report it as -999) and remstimate returns its last iterate. 5 comparisons differ and 112 agree.
- <a id="why-rem_fit-goldfish"></a>**[goldfish](../../tools/goldfish.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. goldfish (1.6.12) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: R package goldfish: exported functions and help titles.

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
