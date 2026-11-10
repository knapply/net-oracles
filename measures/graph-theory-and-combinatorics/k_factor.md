---
title: "K-factor"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# K-factor {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Covers and dominating sets. Concept id: `k_factor`. 2 measures.

## Definition {#concept-definition}

K-factor. Entries grouped here: Kfactor; Kfactor edges.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Kfactor](#st_kfactor) | `st_kfactor` | 1 |
| [Kfactor edges](#st_kfactor_edges) | `st_kfactor_edges` | 1 |

## Kfactor {#st_kfactor}

Measure id: `st_kfactor`. Original family: Graph theory and combinatorics.

**Definition.** Kfactor.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `k_factor` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_kfactor` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `for k = 1, 2, 3: the number of edges of nx.k_factor(G, k), -1 if NetworkX finds none` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Kfactor edges {#st_kfactor_edges}

Measure id: `st_kfactor_edges`. Original family: Graph theory and combinatorics.

**Definition.** Kfactor edges.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_kfactor_edges` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `for k = 1, 2: the edges of nx.k_factor(G, k) in order, flat, with their count first (-1 if none)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
