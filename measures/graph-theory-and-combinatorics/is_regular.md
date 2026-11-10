---
title: "Regular graph tests"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Regular graph tests {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Degree sequences and predicates. Concept id: `is_regular`. 3 measures.

## Definition {#concept-definition}

Regular graph tests. Entries grouped here: Is k regular; Is strongly regular; Regular.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Is k regular](#cat_is_k_regular) | `cat_is_k_regular` | 1 |
| [Is strongly regular](#cat_is_regular_strongly) | `cat_is_regular_strongly` | 1 |
| [Regular](#st_regular) | `st_regular` | 1 |

## Is k regular {#cat_is_k_regular}

Measure id: `cat_is_k_regular`. Original family: Graph theory and combinatorics.

**Definition.** Is k regular.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `is_k_regular` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Is strongly regular {#cat_is_regular_strongly}

Measure id: `cat_is_regular_strongly`. Original family: Graph theory and combinatorics.

**Definition.** Is strongly regular.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `is_strongly_regular` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Regular {#st_regular}

Measure id: `st_regular`. Original family: Graph theory and combinatorics.

**Definition.** Regular.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `is_regular` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_regular` | NetworkX | any | agrees |  |  | abs 0, rel 1e-15 | `[nx.is_regular(G), nx.s_metric(G)]` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
