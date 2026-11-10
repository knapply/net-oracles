---
title: "Basis"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Basis

Family: Graph theory and combinatorics. Identifier: `basis`.

## Definition

Basis.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cyc_basis_check` | NetworkX | undirected | differs | multi\_edges | multi\_edges | abs 0, rel 0 | `the count and the cycle/independence tests of nx.cycle_basis(G)` | as for cyc\_basis |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
