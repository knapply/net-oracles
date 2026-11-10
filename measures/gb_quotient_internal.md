---
title: "Quotient internal"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Quotient internal

Family: Traversal, trees and DAGs. Identifier: `gb_quotient_internal`.

## Definition

Quotient internal.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_quotient_internal` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nedges of each block of nx.quotient_graph(M, parts)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
