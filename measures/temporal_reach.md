---
title: "Temporal reach"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Temporal reach

Family: Temporal and events. Identifier: `temporal_reach`.

## Definition

Temporal reach.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [tsna / networkDynamic](../tools/tsna.html) | ✓ checked, agrees | `forward.reachable; tReach` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `temporal_reach_out_instantaneous` | tsna / networkDynamic | any | agrees |  |  | abs 0, rel 0 | `sum(is.finite(tPath(nd, v, 'fwd', 'earliest.arrive', ...)$tdist)) - 1` |  |

Tools cited: [handcock2008statnet](../references.html#handcock2008statnet)
{% endraw %}
