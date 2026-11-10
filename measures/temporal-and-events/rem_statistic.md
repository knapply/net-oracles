---
title: "Relational event statistics"
layout: default
parent: "Temporal and events"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Relational event statistics {#concept-top}

Family: [Temporal and events](index.html). Subfamily: Relational event models. Concept id: `rem_statistic`. 1 measure.

## Definition {#concept-definition}

Relational event statistics. Entries grouped here: Rem statistic.

## Rem statistic {#rem_statistic}

Measure id: `rem_statistic`. Original family: Temporal and events.

**Definition.** Rem statistic.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [remstats / remify](../../tools/remstats.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `rem_cyclic` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ itp(), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_cyclic_binary` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ itp(unique = TRUE), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_inertia` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ inertia(), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_inertia_decay` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `c * remstats::remstats(reh, tie_effects = ~ inertia(), memory = "decay", memory_value = 5), c = (ln 2 / 5) 2^(-1/5)` | remify rejects a stream this short (one edge). |
| `rem_inertia_window` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ inertia(), memory = "window", memory_value = 6)` | remify rejects a stream this short (one edge). |
| `rem_receiver_in` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ indegreeReceiver(), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_receiver_in_decay` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `c * remstats::remstats(reh, tie_effects = ~ indegreeReceiver(), memory = "decay", memory_value = 5), c = (ln 2 / 5) 2^(-1/5)` | remify rejects a stream this short (one edge). |
| `rem_receiver_in_window` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ indegreeReceiver(), memory = "window", memory_value = 6)` | remify rejects a stream this short (one edge). |
| `rem_receiver_out` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ outdegreeReceiver(), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_recency_dyad` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ recencyContinue(), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_recency_receiver_in` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ recencyReceiveReceiver(), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_recency_receiver_out` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ recencySendReceiver(), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_recency_sender_in` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ recencyReceiveSender(), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_recency_sender_out` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ recencySendSender(), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_reciprocity` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ reciprocity(), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_reciprocity_window` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ reciprocity(), memory = "window", memory_value = 6)` | remify rejects a stream this short (one edge). |
| `rem_sender_in` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ indegreeSender(), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_sender_out` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ outdegreeSender(), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_sender_out_decay` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `c * remstats::remstats(reh, tie_effects = ~ outdegreeSender(), memory = "decay", memory_value = 5), c = (ln 2 / 5) 2^(-1/5)` | remify rejects a stream this short (one edge). |
| `rem_shared_in` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ isp(), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_shared_in_binary` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ isp(unique = TRUE), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_shared_in_window` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ isp(), memory = "window", memory_value = 6)` | remify rejects a stream this short (one edge). |
| `rem_shared_out` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ osp(), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_shared_out_binary` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ osp(unique = TRUE), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_shared_out_decay` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `c * remstats::remstats(reh, tie_effects = ~ osp(), memory = "decay", memory_value = 5), c = (ln 2 / 5) 2^(-1/5)` | remify rejects a stream this short (one edge). |
| `rem_transitive` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ otp(), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_transitive_binary` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ otp(unique = TRUE), memory = "full")` | remify rejects a stream this short (one edge). |
| `rem_transitive_decay` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `c * remstats::remstats(reh, tie_effects = ~ otp(), memory = "decay", memory_value = 5), c = (ln 2 / 5) 2^(-1/5)` | remify rejects a stream this short (one edge). |
| `rem_transitive_window` | remstats / remify | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `remstats::remstats(reh, tie_effects = ~ otp(), memory = "window", memory_value = 6)` | remify rejects a stream this short (one edge). |

**Tools cited:** [arena2026remstats](../../references.html#arena2026remstats)
{% endraw %}
