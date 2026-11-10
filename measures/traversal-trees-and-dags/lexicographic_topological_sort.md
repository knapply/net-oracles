---
title: "Lexicographic topological sort"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Lexicographic topological sort {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `lexicographic_topological_sort`. 2 measures.

## Definition {#concept-definition}

Lexicographic topological sort. Entries grouped here: Lex topo; Lexicographic.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Lex topo](#gb_lex_topo) | `gb_lex_topo` | 1 |
| [Lexicographic](#lexicographic) | `lexicographic` | 1 |

## Lex topo {#gb_lex_topo}

Measure id: `gb_lex_topo`. Original family: Traversal, trees and DAGs.

**Definition.** Lex topo.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_lex_topo` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.lexicographical_topological_sort(M)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Lexicographic {#lexicographic}

Measure id: `lexicographic`. Original family: Traversal, trees and DAGs.

**Definition.** Lexicographic.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_lexicographic` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `list(nx.lexicographical_topological_sort(D))` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
