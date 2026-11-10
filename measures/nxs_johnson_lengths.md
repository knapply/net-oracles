---
title: "Johnson lengths"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Johnson lengths

Family: Paths and distances. Identifier: `nxs_johnson_lengths`.

## Definition

Johnson lengths.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_johnson_lengths` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `the same from nx.single_source_bellman_ford_path_length on the graph with a zero-length source arc to every node` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
