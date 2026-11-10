---
title: "Cycle count"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Cycle count

Family: Traversal, trees and DAGs. Identifier: `gb_cycle_count`.

## Definition

Cycle count.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [ergm (statnet)](../tools/ergm.html) | ✓ checked, agrees | `cycle; sum` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_cycle_count` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(list(nx.simple_cycles(M)))` |  |
| `gb_cycle_count` | ergm (statnet) | any | agrees |  |  | abs 0, rel 0 | `sum(summary(nw ~ cycle(2:n))) directed, cycle(3:n) undirected` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [hunter2008ergm](../references.html#hunter2008ergm)
{% endraw %}
