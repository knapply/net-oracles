---
title: "Label spreading"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Label spreading

Family: Communities. Identifier: `nxo_label_spreading`.

## Definition

NetworkX's label spreading (harmonic function or local and global consistency): best class of every node and whether it ties.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `harmonic_function; local_and_global_consistency` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxo_harmonic_function` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.node_classification.harmonic_function(G), labels (v // 4) % 3 on nodes v % 4 == 0 (graph without weights)` |  |
| `nxo_local_global_weighted` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.node_classification.local_and_global_consistency(G, alpha = 0.9, max_iter = 12)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
