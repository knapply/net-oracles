---
title: "Recursive cycles"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Recursive cycles

Family: Graph theory and combinatorics. Identifier: `nxs_recursive_cycles`.

## Definition

Recursive cycles.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_recursive_cycles` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `list(nx.recursive_simple_cycles(D)) on the simple digraph with loops, in its order and rotation` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
