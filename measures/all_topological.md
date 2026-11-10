---
title: "All topological"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# All topological

Family: Traversal, trees and DAGs. Identifier: `all_topological`.

## Definition

Every topological order of a DAG, in the sequence of Knuth and Szwarcfiter's algorithm.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `all_topological_sorts` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_all_topological` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `the first 50 orders of nx.all_topological_sorts(D), in its sequence` |  |

## References

[knuth1974structured](../references.html#knuth1974structured)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
