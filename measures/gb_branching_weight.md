---
title: "Branching weight"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Branching weight

Family: Traversal, trees and DAGs. Identifier: `gb_branching_weight`.

## Definition

Branching weight.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `branching_weight` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_branching_weight` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.maximum_branching(M, preserve_attrs=True)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
