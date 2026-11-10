---
title: "Transitive closure"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Transitive closure {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `transitive_closure`. 1 measure.

## Definition {#concept-definition}

The pairs (u, v) of the transitive closure, sorted by source then target.

## References {#concept-references}

[aho1972transitive](../../references.html#aho1972transitive), [aho1976finding](../../references.html#aho1976finding), [bender2005lowest](../../references.html#bender2005lowest), [cooper2001simple](../../references.html#cooper2001simple), [cytron1991efficiently](../../references.html#cytron1991efficiently), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kahn1962topological](../../references.html#kahn1962topological), [knuth1974structured](../../references.html#knuth1974structured)

## Closure {#closure}

Measure id: `closure`. Original family: Traversal, trees and DAGs.

**Definition.** The pairs (u, v) of the transitive closure, sorted by source then target.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `transitive_closure; transitive_closure_dag` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `transitive_closure` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `transitive_closure` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `TransitiveClosure` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `transitive_closure` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_closure_always` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.transitive_closure(G, reflexive = True).edges()` |  |
| `dag_closure_cycles` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.transitive_closure(G, reflexive = False).edges()` |  |
| `dag_closure_never` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.transitive_closure(G, reflexive = None).edges()` |  |

**References:** [aho1972transitive](../../references.html#aho1972transitive), [aho1976finding](../../references.html#aho1976finding), [bender2005lowest](../../references.html#bender2005lowest), [cooper2001simple](../../references.html#cooper2001simple), [cytron1991efficiently](../../references.html#cytron1991efficiently), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kahn1962topological](../../references.html#kahn1962topological), [knuth1974structured](../../references.html#knuth1974structured)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost)
{% endraw %}
