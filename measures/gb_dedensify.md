---
title: "Dedensify"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Dedensify

Family: Traversal, trees and DAGs. Identifier: `gb_dedensify`.

## Definition

Dedensify.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `dedensify` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_dedensify` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.dedensify(M, 2)[1])` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
