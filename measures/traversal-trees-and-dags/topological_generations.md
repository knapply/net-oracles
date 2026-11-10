---
title: "Topological generations"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Topological generations {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `topological_generations`. 2 measures.

## Definition {#concept-definition}

Topological generations of a DAG: the roots, then the nodes all of whose parents are in earlier generations.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Generations](#generations) | `generations` | 1 |
| [Topo levels](#gb_topo_levels) | `gb_topo_levels` | 1 |

## References {#concept-references}

[aho1972transitive](../../references.html#aho1972transitive), [aho1976finding](../../references.html#aho1976finding), [bender2005lowest](../../references.html#bender2005lowest), [cooper2001simple](../../references.html#cooper2001simple), [cytron1991efficiently](../../references.html#cytron1991efficiently), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kahn1962topological](../../references.html#kahn1962topological), [knuth1974structured](../../references.html#knuth1974structured)

## Generations {#generations}

Measure id: `generations`. Original family: Traversal, trees and DAGs.

**Definition.** Topological generations of a DAG: the roots, then the nodes all of whose parents are in earlier generations.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_generations` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `generation index of each node in nx.topological_generations(D)` |  |

**References:** [aho1972transitive](../../references.html#aho1972transitive), [aho1976finding](../../references.html#aho1976finding), [bender2005lowest](../../references.html#bender2005lowest), [cooper2001simple](../../references.html#cooper2001simple), [cytron1991efficiently](../../references.html#cytron1991efficiently), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kahn1962topological](../../references.html#kahn1962topological), [knuth1974structured](../../references.html#knuth1974structured)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Topo levels {#gb_topo_levels}

Measure id: `gb_topo_levels`. Original family: Traversal, trees and DAGs.

**Definition.** Topo levels.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_topo_levels` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.topological_generations(M)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
