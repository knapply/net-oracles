---
title: "Maximal matching"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Maximal matching {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Matching. Concept id: `maximal_matching`. 2 measures.

## Definition {#concept-definition}

Maximal matching. Entries grouped here: Maximal matching; Min maximal matching (approximate).

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Maximal matching](#maximal_matching) | `maximal_matching` | 1 |
| [Min maximal matching (approximate)](#cat_matching_maximal_min-approximate) | `cat_matching_maximal_min@approximate` | 1 |

## Maximal matching {#maximal_matching}

Measure id: `maximal_matching`. Original family: Graph theory and combinatorics.

**Definition.** Maximal matching.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `maximal_matching` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `matching_maximal` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.maximal_matching(G)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Min maximal matching (approximate) {#cat_matching_maximal_min-approximate}

Measure id: `cat_matching_maximal_min@approximate`. Original family: Graph theory and combinatorics.

**Definition.** Min maximal matching (approximate).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `min_maximal_matching` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
