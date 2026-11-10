---
title: "Antichains and antichain width"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Antichains and antichain width {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `antichains`. 2 measures.

## Definition {#concept-definition}

The width of a DAG: the size of a largest antichain (Dilworth), by a maximum matching on the reachability pairs.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Antichain width](#gb_antichain_width) | `gb_antichain_width` | 1 |
| [Antichains](#cat_antichains) | `cat_antichains` | 1 |

## References {#concept-references}

[dilworth1950decomposition](../../references.html#dilworth1950decomposition), [hopcroft1973n52](../../references.html#hopcroft1973n52)

## Antichain width {#gb_antichain_width}

Measure id: `gb_antichain_width`. Original family: Traversal, trees and DAGs.

**Definition.** The width of a DAG: the size of a largest antichain (Dilworth), by a maximum matching on the reachability pairs.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_antichain_width` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.algorithms.dag.antichain_width(M)` |  |

**References:** [dilworth1950decomposition](../../references.html#dilworth1950decomposition), [hopcroft1973n52](../../references.html#hopcroft1973n52)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Antichains {#cat_antichains}

Measure id: `cat_antichains`. Original family: Graph theory and combinatorics.

**Definition.** Antichains.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `antichains` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
