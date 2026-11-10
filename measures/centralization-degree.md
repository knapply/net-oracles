---
title: "Centralization / degree"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Centralization / degree

Family: Descriptive statistics. Identifier: `centralization:degree`.

## Definition

Freeman centralization of degree, betweenness, closeness or eigenvector centrality.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../tools/igraph.html) | ∅ checked, no value on some inputs | `centr_degree` |  |
| [sna](../tools/sna.html) | ✓ checked, agrees |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs |  | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `centralization_degree` | igraph (R) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::centr_degree(g, mode = 'all', loops = TRUE, normalized = TRUE)$centralization` |  |
| `centralization_degree_in` | igraph (R) | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::centr_degree(g, mode = 'in', loops = TRUE, normalized = TRUE)$centralization` |  |
| `centralization_degree_sna` | sna | any | agrees |  |  | abs 1e-14, rel 1e-12 | `sna::centralization(m, sna::degree, mode = gmode, cmode = 'freeman' \| 'indegree')` |  |

## References

[borgatti2006identifying](../references.html#borgatti2006identifying), [csardi2006igraph](../references.html#csardi2006igraph), [freeman1978centrality](../references.html#freeman1978centrality), [tarjan1972depth](../references.html#tarjan1972depth), [tarjan1975efficiency](../references.html#tarjan1975efficiency), [wasserman1994social](../references.html#wasserman1994social)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [butts2008sna](../references.html#butts2008sna), [csardi2006igraph](../references.html#csardi2006igraph)
{% endraw %}
