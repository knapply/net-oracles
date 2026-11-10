---
title: "Degree simple"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Degree simple

Family: Centrality. Identifier: `degree_simple`.

## Definition

Degree simple.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [sna](../tools/sna.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `degree_sna` | sna | any | agrees |  |  | abs 0, rel 0 | `sna::degree(m, gmode, cmode = 'freeman' \| 'indegree')` |  |

Tools cited: [butts2008sna](../references.html#butts2008sna)
{% endraw %}
