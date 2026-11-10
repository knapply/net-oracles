---
title: "Dominators and dominance frontiers"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Dominators and dominance frontiers {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Dominators. Concept id: `dominators`. 3 measures.

## Definition {#concept-definition}

Immediate dominator of every node reachable from the start node (the start's is itself); unreachable nodes get the none mark u32::MAX.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Dominator](#cat_dominator) | `cat_dominator` | 1 |
| [Frontiers](#frontiers) | `frontiers` | 1 |
| [Idom](#idom) | `idom` | 5 |

## References {#concept-references}

[cooper2001simple](../../references.html#cooper2001simple)

## Dominator {#cat_dominator}

Measure id: `cat_dominator`. Original family: Components and connectivity.

**Definition.** Dominator.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `dominator` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Frontiers {#frontiers}

Measure id: `frontiers`. Original family: Traversal, trees and DAGs.

**Definition.** Frontiers.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_dominance_frontiers` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.dominance_frontiers(G, 0), one sorted tuple per node, (-1) if unreachable` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Idom {#idom}

Measure id: `idom`. Original family: Traversal, trees and DAGs.

**Definition.** Immediate dominator of every node reachable from the start node (the start's is itself); unreachable nodes get the none mark u32::MAX.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `dominance_frontiers; immediate_dominators` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `dominator_tree` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `dominator_tree` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `dominance_frontiers; immediate_dominators` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `lengauer_tarjan_dominator_tree` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_immediate_dominators` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.immediate_dominators(G, 0), with 0 for the start and -1 for unreachable nodes` |  |

**References:** [cooper2001simple](../../references.html#cooper2001simple)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
