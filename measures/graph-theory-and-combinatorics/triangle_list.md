---
title: "Triangle listing"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Triangle listing {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Triangles and local counts. Concept id: `triangle_list`. 1 measure.

## Definition {#concept-definition}

Triangle listing. Entries grouped here: Triangle list.

## Triangle list {#nxs_triangle_list}

Measure id: `nxs_triangle_list`. Original family: Graph theory and combinatorics.

**Definition.** Triangle list.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_triangle_list` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `sorted(nx.all_triangles(G)) (NetworkX's order follows Python set order and is not compared)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
