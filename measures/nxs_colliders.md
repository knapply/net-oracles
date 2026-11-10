---
title: "Colliders"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Colliders

Family: Graph theory and combinatorics. Identifier: `nxs_colliders`.

## Definition

Colliders.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_colliders_order` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `list(nx.dag.colliders(D)), in its order` |  |
| `nxs_v_structures_order` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `list(nx.dag.v_structures(D)), in its order` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
