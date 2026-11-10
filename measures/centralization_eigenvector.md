---
title: "Centralization eigenvector"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Centralization eigenvector

Family: Descriptive statistics. Identifier: `centralization_eigenvector`.

## Definition

Freeman centralization of degree, betweenness, closeness or eigenvector centrality.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../tools/igraph.html) | ≠ checked, differs by convention | `centr_eigen` |  |
| [UCINET](../tools/ucinet.html) | · reported in docs |  | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `centralization_eigenvector` | igraph (R) | any | differs | disconnected, two\_nodes | defaults, normalization | abs 1e-14, rel 1e-12 | `igraph::centr_eigen(g, directed = FALSE, scale = TRUE)$centralization` | On a disconnected graph the leading eigenvalue need not be simple, so the eigenvector (and its centralization) depends on the eigensolver's start; on two nodes the theoretical maximum (n - 2) is 0, so igraph divides by zero (inf) where the reference reports undefined. |

## References

[borgatti2006identifying](../references.html#borgatti2006identifying), [csardi2006igraph](../references.html#csardi2006igraph), [freeman1978centrality](../references.html#freeman1978centrality), [tarjan1972depth](../references.html#tarjan1972depth), [tarjan1975efficiency](../references.html#tarjan1975efficiency), [wasserman1994social](../references.html#wasserman1994social)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph)
{% endraw %}
