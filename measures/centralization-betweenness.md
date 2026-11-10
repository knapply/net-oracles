---
title: "Centralization / betweenness"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Centralization / betweenness

Family: Descriptive statistics. Identifier: `centralization:betweenness`.

## Definition

Freeman centralization of degree, betweenness, closeness or eigenvector centrality.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees | `centr_betw` |  |
| [sna](../tools/sna.html) | ≠ checked, differs by convention | `centralization` |  |
| [UCINET](../tools/ucinet.html) | · reported in docs |  | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `centralization_betweenness` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `igraph::centr_betw(g, directed = TRUE, normalized = TRUE)$centralization` |  |
| `centralization_betweenness` | sna | any | differs | multi\_edges | multi\_edges | abs 1e-12, rel 1e-10 | `sna::centralization(m, sna::betweenness, mode = gmode)` | sna collapses parallel edges, which changes shortest-path counts. |

## References

[borgatti2006identifying](../references.html#borgatti2006identifying), [csardi2006igraph](../references.html#csardi2006igraph), [freeman1978centrality](../references.html#freeman1978centrality), [tarjan1972depth](../references.html#tarjan1972depth), [tarjan1975efficiency](../references.html#tarjan1975efficiency), [wasserman1994social](../references.html#wasserman1994social)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [butts2008sna](../references.html#butts2008sna), [csardi2006igraph](../references.html#csardi2006igraph)
{% endraw %}
