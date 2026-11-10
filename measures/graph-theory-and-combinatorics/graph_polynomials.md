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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_chromatic_polynomial-networkx) | `chromatic_polynomial` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_chromatic_polynomial-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: chromatic\_polynomial.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Polynomials {#st_polynomials}

Measure id: `st_polynomials`. Original family: Graph theory and combinatorics.

**Definition.** Polynomials.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `tutte_polynomial` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_polynomials` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `coefficients of sympy.Poly(nx.chromatic_polynomial(G), x) and of nx.tutte_polynomial(G) in x, y` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
