---
title: "Nxs tree lca"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Nxs tree lca

Family: Graph theory and combinatorics. Identifier: `nxs_tree_lca`.

## Definition

Nxs tree lca.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_tree_lca` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `[(u, v, a) for (u, v), a in nx.tree_all_pairs_lowest_common_ancestor(T, root = 0)], in its order` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
