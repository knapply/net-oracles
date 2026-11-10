---
title: "Nx ramsey"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Nx ramsey

Family: Graph theory and combinatorics. Identifier: `ap_nx_ramsey`.

## Definition

Nx ramsey.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `ramsey_R2` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_nx_ramsey` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `ramsey_R2, clique_removal, max_clique, maximum_independent_set, large_clique_size on G_sorted: each set sorted with its size first` |  |
| `ap_nx_ramsey_valid` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's results` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
