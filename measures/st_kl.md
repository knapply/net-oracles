---
title: "Kl"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Kl

Family: Graph theory and combinatorics. Identifier: `st_kl`.

## Definition

Kl.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `kl_connected_subgraph` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_kl` | NetworkX | any | no-value-on-some-inputs |  | direction | abs 0, rel 0 | `per edge: 1 if kept by nx.kl_connected_subgraph(G_sorted, 2, l), l = 2, 3` | NetworkX deep-copies the graph once per edge; the 784-arc fixture is skipped for time |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
