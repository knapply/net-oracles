---
title: "Strong partition"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Strong partition

Family: Components and connectivity. Identifier: `strong_partition`.

## Definition

Strong partition.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../tools/jgrapht.html) | ✓ checked, agrees | `GabowStrongConnectivityInspector; KosarajuStrongConnectivityInspector` |  |
| [Boost Graph Library](../tools/boost.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_strong_partition` | JGraphT | directed | agrees |  |  | abs 0, rel 0 | `JGraphT 1.5.2: new KosarajuStrongConnectivityInspector<>(g).stronglyConnectedSets() on a pseudograph` |  |
| `conn_strong_partition` | Boost Graph Library | directed | agrees |  |  | abs 0, rel 0 | `Boost Graph Library strong_components` |  |

Tools cited: [michail2020jgrapht](../references.html#michail2020jgrapht), [siek2002boost](../references.html#siek2002boost)
{% endraw %}
