---
title: "Generalized degree"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Generalized degree {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Degree sequences and predicates. Concept id: `generalized_degree`. 1 measure.

## Definition {#concept-definition}

Generalized degree. Entries grouped here: Generalized degree.

## Generalized degree {#generalized_degree}

Measure id: `generalized_degree`. Original family: Graph theory and combinatorics.

**Definition.** Generalized degree.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `generalized_degree` |  |
| [GraphBLAS algorithms](../../tools/graphblas.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `generalized_degree` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.generalized_degree(G)` |  |
| `generalized_degree` | GraphBLAS algorithms | undirected | differs | multi\_edges | direction, multi\_edges, weights | abs 0, rel 0 | `nx.generalized_degree(G simple, backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. |

**Tools cited:** [davis2019algorithm](../../references.html#davis2019algorithm), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
