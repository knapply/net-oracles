---
title: "Polynomials"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Polynomials

Family: Graph theory and combinatorics. Identifier: `st_polynomials`.

## Definition

Polynomials.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `tutte_polynomial` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_polynomials` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `coefficients of sympy.Poly(nx.chromatic_polynomial(G), x) and of nx.tutte_polynomial(G) in x, y` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
