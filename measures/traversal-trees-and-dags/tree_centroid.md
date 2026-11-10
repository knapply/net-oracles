---
title: "Tree centroid"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Tree centroid {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Tree structure and enumeration. Concept id: `tree_centroid`. 1 measure.

## Definition {#concept-definition}

Tree centroid. Entries grouped here: Tree centroid.

## Tree centroid {#nxs_tree_centroid}

Measure id: `nxs_tree_centroid`. Original family: Graph theory and combinatorics.

**Definition.** Tree centroid.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `centroid` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_tree_centroid` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted(nx.centroid(T))` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
