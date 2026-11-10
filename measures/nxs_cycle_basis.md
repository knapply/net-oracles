---
title: "Nxs cycle basis"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Nxs cycle basis

Family: Graph theory and combinatorics. Identifier: `nxs_cycle_basis`.

## Definition

Nxs cycle basis.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_cycle_basis` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.cycle_basis(G) on the simple graph, in its order` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
