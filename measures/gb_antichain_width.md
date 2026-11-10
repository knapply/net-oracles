---
title: "Antichain width"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Antichain width

Family: Traversal, trees and DAGs. Identifier: `gb_antichain_width`.

## Definition

The width of a DAG: the size of a largest antichain (Dilworth), by a maximum matching on the reachability pairs.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_antichain_width` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.algorithms.dag.antichain_width(M)` |  |

## References

[dilworth1950decomposition](../references.html#dilworth1950decomposition), [hopcroft1973n52](../references.html#hopcroft1973n52)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
