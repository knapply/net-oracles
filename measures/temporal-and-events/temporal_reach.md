---
title: "Temporal reach"
layout: default
parent: "Temporal and events"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Temporal reach {#concept-top}

Family: [Temporal and events](index.html). Subfamily: Temporal descriptives. Concept id: `temporal_reach`. 1 measure.

## Definition {#concept-definition}

Temporal reach. Entries grouped here: Temporal reach.

## Temporal reach {#temporal_reach}

Measure id: `temporal_reach`. Original family: Temporal and events.

**Definition.** Temporal reach.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [tsna / networkDynamic](../../tools/tsna.html) | ✓ checked, agrees | `forward.reachable; tReach` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `temporal_reach_out_instantaneous` | tsna / networkDynamic | any | agrees |  |  | abs 0, rel 0 | `sum(is.finite(tPath(nd, v, 'fwd', 'earliest.arrive', ...)$tdist)) - 1` |  |

**Tools cited:** [handcock2008statnet](../../references.html#handcock2008statnet)
{% endraw %}
