---
title: "Overlapping"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Overlapping

Family: Communities. Identifier: `cnx_overlapping`.

## Definition

Overlapping.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `overlapping_modularity` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_overlapping_modularity` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.community.overlapping_modularity(G_simple_undirected, cover)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
