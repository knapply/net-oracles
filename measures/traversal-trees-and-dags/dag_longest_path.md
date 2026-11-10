---
title: "Longest path in a DAG"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Longest path in a DAG {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `dag_longest_path`. 7 measures.

## Definition {#concept-definition}

A longest path of a DAG and its length, by dynamic programming in topological order.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Dag longest path](#cat_dag_longest_path) | `cat_dag_longest_path` | 1 |
| [Dag longest path length](#cat_dag_length_longest_path) | `cat_dag_length_longest_path` | 1 |
| [Dag weighted longest path](#cat_dag_longest_path_weighted) | `cat_dag_longest_path_weighted` | 1 |
| [Dag weighted longest path length](#cat_dag_length_longest_path_weighted) | `cat_dag_length_longest_path_weighted` | 1 |
| [Longest length](#longest_length) | `longest_length` | 1 |
| [Longest path](#longest_path) | `longest_path` | 1 |
| [Longest path len](#gb_longest_path_len) | `gb_longest_path_len` | 1 |

## References {#concept-references}

[aho1972transitive](../../references.html#aho1972transitive), [aho1976finding](../../references.html#aho1976finding), [bender2005lowest](../../references.html#bender2005lowest), [cooper2001simple](../../references.html#cooper2001simple), [cytron1991efficiently](../../references.html#cytron1991efficiently), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kahn1962topological](../../references.html#kahn1962topological), [knuth1974structured](../../references.html#knuth1974structured)

## Dag longest path {#cat_dag_longest_path}

Measure id: `cat_dag_longest_path`. Original family: Paths and distances.

**Definition.** Dag longest path.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `dag_longest_path` | API listing |

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Dag longest path length {#cat_dag_length_longest_path}

Measure id: `cat_dag_length_longest_path`. Original family: Paths and distances.

**Definition.** Dag longest path length.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `dag_longest_path_length` | API listing |

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Dag weighted longest path {#cat_dag_longest_path_weighted}

Measure id: `cat_dag_longest_path_weighted`. Original family: Paths and distances.

**Definition.** Dag weighted longest path.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `dag_weighted_longest_path` | API listing |

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Dag weighted longest path length {#cat_dag_length_longest_path_weighted}

Measure id: `cat_dag_length_longest_path_weighted`. Original family: Paths and distances.

**Definition.** Dag weighted longest path length.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `dag_weighted_longest_path_length` | API listing |

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Longest length {#longest_length}

Measure id: `longest_length`. Original family: Traversal, trees and DAGs.

**Definition.** A longest path of a DAG and its length, by dynamic programming in topological order.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `dag_longest_path_length` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_longest_length` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.dag_longest_path_length(D)` |  |
| `dag_longest_length_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.dag_longest_path_length(D, weight = 'weight') on the multigraph D` |  |

**References:** [aho1972transitive](../../references.html#aho1972transitive), [aho1976finding](../../references.html#aho1976finding), [bender2005lowest](../../references.html#bender2005lowest), [cooper2001simple](../../references.html#cooper2001simple), [cytron1991efficiently](../../references.html#cytron1991efficiently), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kahn1962topological](../../references.html#kahn1962topological), [knuth1974structured](../../references.html#knuth1974structured)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Longest path {#longest_path}

Measure id: `longest_path`. Original family: Traversal, trees and DAGs.

**Definition.** A longest path of a DAG and its length, by dynamic programming in topological order.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `dag_longest_path` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_longest_path` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.dag_longest_path(D)` |  |
| `dag_longest_path_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.dag_longest_path(D, weight = 'weight') on the multigraph D` |  |

**References:** [aho1972transitive](../../references.html#aho1972transitive), [aho1976finding](../../references.html#aho1976finding), [bender2005lowest](../../references.html#bender2005lowest), [cooper2001simple](../../references.html#cooper2001simple), [cytron1991efficiently](../../references.html#cytron1991efficiently), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kahn1962topological](../../references.html#kahn1962topological), [knuth1974structured](../../references.html#knuth1974structured)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Longest path len {#gb_longest_path_len}

Measure id: `gb_longest_path_len`. Original family: Traversal, trees and DAGs.

**Definition.** Longest path len.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_longest_path_len` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `len(nx.dag_longest_path(M, weight=None)) - 1` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
