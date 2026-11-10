---
title: "Gb aperiodic"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Gb aperiodic

Family: Traversal, trees and DAGs. Identifier: `gb_aperiodic`.

## Definition

Gb aperiodic.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `is_aperiodic` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_aperiodic` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.is_aperiodic(M)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
