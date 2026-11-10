---
title: "Lukes"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Lukes

Family: Communities. Identifier: `cnx_lukes`.

## Definition

Lukes.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `lukes_partitioning` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_lukes_partitioning` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nx.community.lukes_partitioning(G, 3): (edges inside clusters, 1 if every cluster has at most 3 nodes); -1 if not a tree` | NetworkX 3.7 fails with a KeyError on a tree of one node |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
