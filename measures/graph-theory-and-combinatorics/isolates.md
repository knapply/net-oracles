---
title: "Isolates"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Isolates {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Degree sequences and predicates. Concept id: `isolates`. 2 measures.

## Definition {#concept-definition}

Isolates. Entries grouped here: Is isolate; Isolates.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Is isolate](#cat_is_isolate) | `cat_is_isolate` | 1 |
| [Isolates](#gb_isolates) | `gb_isolates` | 4 |

## Is isolate {#cat_is_isolate}

Measure id: `cat_is_isolate`. Original family: Graph theory and combinatorics.

**Definition.** Is isolate.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `is_isolate` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Isolates {#gb_isolates}

Measure id: `gb_isolates`. Original family: Traversal, trees and DAGs.

**Definition.** Isolates.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `isolates; number_of_isolates` |  |
| [sna](../../tools/sna.html) | · reported in docs | `isolates` | API listing |
| [ergm (statnet)](../../tools/ergm.html) | · reported in docs | `isolates` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `digraph_isolates; graph_isolates; isolates` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_isolates` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `list(nx.isolates(M))` |  |

**Tools cited:** [butts2008sna](../../references.html#butts2008sna), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hunter2008ergm](../../references.html#hunter2008ergm), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
