---
title: "Distance-regular intersection array"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Distance-regular intersection array {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Chordal, perfect and special graph classes. Concept id: `intersection_array`. 1 measure.

## Definition {#concept-definition}

Distance-regular intersection array. Entries grouped here: Intersection.

## Intersection {#st_intersection}

Measure id: `st_intersection`. Original family: Graph theory and combinatorics.

**Definition.** Intersection.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `intersection_array` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_intersection` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.intersection_array(G) (-1 where it raises)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
