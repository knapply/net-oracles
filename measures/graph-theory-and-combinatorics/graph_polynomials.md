---
title: "Chromatic and Tutte polynomials"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Chromatic and Tutte polynomials {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Coloring. Concept id: `graph_polynomials`. 2 measures.

## Definition {#concept-definition}

Chromatic and Tutte polynomials. Entries grouped here: Chromatic polynomial; Polynomials.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Chromatic polynomial](#cat_chromatic_polynomial) | `cat_chromatic_polynomial` | 1 |
| [Polynomials](#st_polynomials) | `st_polynomials` | 1 |

## Chromatic polynomial {#cat_chromatic_polynomial}

Measure id: `cat_chromatic_polynomial`. Original family: Graph theory and combinatorics.

**Definition.** Chromatic polynomial.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `chromatic_polynomial` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Polynomials {#st_polynomials}

Measure id: `st_polynomials`. Original family: Graph theory and combinatorics.

**Definition.** Polynomials.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `tutte_polynomial` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_polynomials` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `coefficients of sympy.Poly(nx.chromatic_polynomial(G), x) and of nx.tutte_polynomial(G) in x, y` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
