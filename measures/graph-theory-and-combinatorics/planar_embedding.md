---
title: "Planar embedding"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Planar embedding {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Planarity. Concept id: `planar_embedding`. 2 measures.

## Definition {#concept-definition}

Planar embedding. Entries grouped here: Embedding; Embedding euler.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Embedding](#st_embedding) | `st_embedding` | 1 |
| [Embedding euler](#st_embedding_euler) | `st_embedding_euler` | 1 |

## Embedding {#st_embedding}

Measure id: `st_embedding`. Original family: Graph theory and combinatorics.

**Definition.** Embedding.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_embedding` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `check_planarity(G)[1].get_data(): each node's neighbours clockwise, flat with a count first; [-1] if not planar` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Embedding euler {#st_embedding_euler}

Measure id: `st_embedding_euler`. Original family: Graph theory and combinatorics.

**Definition.** Embedding euler.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_embedding_euler` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `1 if the faces of check_planarity(G)[1] satisfy V - E + F = 1 + C, -1 if not planar` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
