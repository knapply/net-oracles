---
title: "Fw tree"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Fw tree

Family: Graph theory and combinatorics. Identifier: `nxs_fw_tree`.

## Definition

Fw tree.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_fw_tree_dist` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.floyd_warshall_tree(G): finite distances, sorted` |  |
| `nxs_fw_tree_dist_negative` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.floyd_warshall_tree(DAG): finite distances, sorted` |  |
| `nxs_fw_tree_pred` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.floyd_warshall_tree(G): predecessor entries, sorted` |  |
| `nxs_fw_tree_pred_negative` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.floyd_warshall_tree(DAG): predecessor entries, sorted` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
