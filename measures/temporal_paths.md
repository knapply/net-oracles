---
title: "Temporal paths"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Temporal paths

Family: Temporal and events. Identifier: `temporal_paths`.

## Definition

Temporal paths.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [tsna / networkDynamic](../tools/tsna.html) | ✓ checked, agrees | `tPath` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `temporal_earliest_arrival_instantaneous` | tsna / networkDynamic | any | agrees |  |  | abs 0, rel 0 | `start + tPath(nd, v, 'fwd', 'earliest.arrive', start, end, graph.step.time = 0)$tdist for every v` |  |

Tools cited: [handcock2008statnet](../references.html#handcock2008statnet)
{% endraw %}
