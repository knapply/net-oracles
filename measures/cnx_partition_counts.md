---
title: "Partition counts"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Partition counts

Family: Communities. Identifier: `cnx_partition_counts`.

## Definition

Partition counts.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_partition_counts` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `(quality.intra_community_edges, quality.inter_community_edges, quality.inter_community_non_edges) of blocks on G_natural` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
