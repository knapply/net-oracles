---
title: "Transitive reduction"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Transitive reduction {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `transitive_reduction`. 1 measure.

## Definition {#concept-definition}

The arcs of the transitive reduction of a DAG, sorted by source then target.

## References {#concept-references}

[aho1972transitive](../../references.html#aho1972transitive), [aho1976finding](../../references.html#aho1976finding), [bender2005lowest](../../references.html#bender2005lowest), [cooper2001simple](../../references.html#cooper2001simple), [cytron1991efficiently](../../references.html#cytron1991efficiently), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kahn1962topological](../../references.html#kahn1962topological), [knuth1974structured](../../references.html#knuth1974structured)

## Reduction {#reduction}

Measure id: `reduction`. Original family: Traversal, trees and DAGs.

**Definition.** The arcs of the transitive reduction of a DAG, sorted by source then target.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `transitive_reduction` |  |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `transitive_reduction` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `TransitiveReduction` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `transitive_reduction` | API listing |
| [netrankr](../../tools/netrankr.html) | · reported in docs | `transitive_reduction` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_reduction` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.transitive_reduction(D).edges()` |  |

**References:** [aho1972transitive](../../references.html#aho1972transitive), [aho1976finding](../../references.html#aho1976finding), [bender2005lowest](../../references.html#bender2005lowest), [cooper2001simple](../../references.html#cooper2001simple), [cytron1991efficiently](../../references.html#cytron1991efficiently), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kahn1962topological](../../references.html#kahn1962topological), [knuth1974structured](../../references.html#knuth1974structured)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [schoch2018centrality](../../references.html#schoch2018centrality), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
