---
title: "Ap local connectivity"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Ap local connectivity

Family: Graph theory and combinatorics. Identifier: `ap_local_connectivity`.

## Definition

Ap local connectivity.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_local_connectivity` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `[local_node_connectivity(G_sorted, 0, n - 1), local_node_connectivity(G_sorted, n - 1, 1, cutoff = 2)]` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
