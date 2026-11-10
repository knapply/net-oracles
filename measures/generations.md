---
title: "Generations"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Generations

Family: Traversal, trees and DAGs. Identifier: `generations`.

## Definition

Topological generations of a DAG: the roots, then the nodes all of whose parents are in earlier generations.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_generations` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `generation index of each node in nx.topological_generations(D)` |  |

## References

[aho1972transitive](../references.html#aho1972transitive), [aho1976finding](../references.html#aho1976finding), [bender2005lowest](../references.html#bender2005lowest), [cooper2001simple](../references.html#cooper2001simple), [cytron1991efficiently](../references.html#cytron1991efficiently), [hagberg2008exploring](../references.html#hagberg2008exploring), [kahn1962topological](../references.html#kahn1962topological), [knuth1974structured](../references.html#knuth1974structured)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
