---
title: "Counterexample"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Counterexample

Family: Graph theory and combinatorics. Identifier: `st_counterexample`.

## Definition

Counterexample.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_counterexample` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted edges of nx.get_counterexample(G), or [-1] if planar` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
