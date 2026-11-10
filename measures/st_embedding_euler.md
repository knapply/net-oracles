---
title: "Embedding euler"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Embedding euler

Family: Graph theory and combinatorics. Identifier: `st_embedding_euler`.

## Definition

Embedding euler.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_embedding_euler` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `1 if the faces of check_planarity(G)[1] satisfy V - E + F = 1 + C, -1 if not planar` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
