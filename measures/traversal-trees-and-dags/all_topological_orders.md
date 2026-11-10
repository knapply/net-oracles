---
title: "All topological orders"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# All topological orders {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `all_topological_orders`. 2 measures.

## Definition {#concept-definition}

Every topological order of a DAG, in the sequence of Knuth and Szwarcfiter's algorithm.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [All topological](#all_topological) | `all_topological` | 1 |
| [Topological sorts](#nxs_topological_sorts) | `nxs_topological_sorts` | 2 |

## References {#concept-references}

[knuth1974structured](../../references.html#knuth1974structured)

## All topological {#all_topological}

Measure id: `all_topological`. Original family: Traversal, trees and DAGs.

**Definition.** Every topological order of a DAG, in the sequence of Knuth and Szwarcfiter's algorithm.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `all_topological_sorts` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_all_topological` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `the first 50 orders of nx.all_topological_sorts(D), in its sequence` |  |

**References:** [knuth1974structured](../../references.html#knuth1974structured)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Topological sorts {#nxs_topological_sorts}

Measure id: `nxs_topological_sorts`. Original family: Graph theory and combinatorics.

**Definition.** Topological sorts.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-nxs_topological_sorts-jgrapht) | `TopologicalOrderIterator` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-nxs_topological_sorts-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: TopologicalOrderIterator.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_topological_sorts` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `first 2000 of nx.all_topological_sorts(DAG), in its order` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
