---
title: "Large clique size"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Large clique size

Family: Graph theory and combinatorics. Identifier: `ap_large_clique_size`.

## Definition

Large clique size.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention | `large_clique_size` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_large_clique_size` | NetworkX | any | differs | directed, undirected | direction, ties | abs 0, rel 0 | `nx.approximation.large_clique_size(G_sorted)` | NetworkX picks the candidate of largest degree from a Python set, so ties go to a different node than the reference value's first in node order, on any graph with tied degrees. |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
