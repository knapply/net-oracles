---
title: "Centralization"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Centralization {#concept-top}

Family: [Centrality](index.html). Subfamily: Centralization and tables. Concept id: `centralization`. 6 measures.

## Definition {#concept-definition}

Freeman centralization of degree, betweenness, closeness or eigenvector centrality.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Centralization](#cat_centralization) | `cat_centralization` | 1 |
| [Centralization / betweenness](#centralization-betweenness) | `centralization:betweenness` | 3 |
| [Centralization / closeness](#centralization-closeness) | `centralization:closeness` | 3 |
| [Centralization / degree](#centralization-degree) | `centralization:degree` | 3 |
| [Centralization eigenvector](#centralization_eigenvector) | `centralization_eigenvector` | 2 |
| [Theoretical maximum of centralization](#centralization_tmax) | `centralization_tmax` | 1 |

## References {#concept-references}

[borgatti2006identifying](../../references.html#borgatti2006identifying), [csardi2006igraph](../../references.html#csardi2006igraph), [freeman1978centrality](../../references.html#freeman1978centrality), [tarjan1972depth](../../references.html#tarjan1972depth), [tarjan1975efficiency](../../references.html#tarjan1975efficiency), [wasserman1994social](../../references.html#wasserman1994social)

## Centralization {#cat_centralization}

Measure id: `cat_centralization`. Original family: Centrality.

**Definition.** Centralization.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | · reported in docs | `centralization` | API listing |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## Centralization / betweenness {#centralization-betweenness}

Measure id: `centralization:betweenness`. Original family: Descriptive statistics.

**Definition.** Freeman centralization of degree, betweenness, closeness or eigenvector centrality.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | ✓ checked, agrees | `centr_betw` |  |
| [sna](../../tools/sna.html) | ≠ checked, differs by convention | `centralization` |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `centralization_betweenness` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `igraph::centr_betw(g, directed = TRUE, normalized = TRUE)$centralization` |  |
| `centralization_betweenness` | sna | any | differs | multi\_edges | multi\_edges | abs 1e-12, rel 1e-10 | `sna::centralization(m, sna::betweenness, mode = gmode)` | sna collapses parallel edges, which changes shortest-path counts. |

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [csardi2006igraph](../../references.html#csardi2006igraph), [freeman1978centrality](../../references.html#freeman1978centrality), [tarjan1972depth](../../references.html#tarjan1972depth), [tarjan1975efficiency](../../references.html#tarjan1975efficiency), [wasserman1994social](../../references.html#wasserman1994social)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph)

## Centralization / closeness {#centralization-closeness}

Measure id: `centralization:closeness`. Original family: Descriptive statistics.

**Definition.** Freeman centralization of degree, betweenness, closeness or eigenvector centrality.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | ✓ checked, agrees | `centr_clo` |  |
| [sna](../../tools/sna.html) | ✓ checked, agrees |  |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `centralization_closeness` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `igraph::centr_clo(g, mode = 'out', normalized = TRUE)$centralization` |  |
| `centralization_closeness_sna` | sna | any | agrees |  |  | abs 1e-12, rel 1e-10 | `sna::centralization(m, sna::closeness, mode = gmode)` |  |

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [csardi2006igraph](../../references.html#csardi2006igraph), [freeman1978centrality](../../references.html#freeman1978centrality), [tarjan1972depth](../../references.html#tarjan1972depth), [tarjan1975efficiency](../../references.html#tarjan1975efficiency), [wasserman1994social](../../references.html#wasserman1994social)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph)

## Centralization / degree {#centralization-degree}

Measure id: `centralization:degree`. Original family: Descriptive statistics.

**Definition.** Freeman centralization of degree, betweenness, closeness or eigenvector centrality.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | ∅ checked, no value on some inputs | `centr_degree` |  |
| [sna](../../tools/sna.html) | ✓ checked, agrees |  |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `centralization_degree` | igraph (R) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::centr_degree(g, mode = 'all', loops = TRUE, normalized = TRUE)$centralization` |  |
| `centralization_degree_in` | igraph (R) | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::centr_degree(g, mode = 'in', loops = TRUE, normalized = TRUE)$centralization` |  |
| `centralization_degree_sna` | sna | any | agrees |  |  | abs 1e-14, rel 1e-12 | `sna::centralization(m, sna::degree, mode = gmode, cmode = 'freeman' \| 'indegree')` |  |

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [csardi2006igraph](../../references.html#csardi2006igraph), [freeman1978centrality](../../references.html#freeman1978centrality), [tarjan1972depth](../../references.html#tarjan1972depth), [tarjan1975efficiency](../../references.html#tarjan1975efficiency), [wasserman1994social](../../references.html#wasserman1994social)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph)

## Centralization eigenvector {#centralization_eigenvector}

Measure id: `centralization_eigenvector`. Original family: Descriptive statistics.

**Definition.** Freeman centralization of degree, betweenness, closeness or eigenvector centrality.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | ≠ checked, differs by convention | `centr_eigen` |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `centralization_eigenvector` | igraph (R) | any | differs | disconnected, two\_nodes | defaults, normalization | abs 1e-14, rel 1e-12 | `igraph::centr_eigen(g, directed = FALSE, scale = TRUE)$centralization` | On a disconnected graph the leading eigenvalue need not be simple, so the eigenvector (and its centralization) depends on the eigensolver's start; on two nodes the theoretical maximum (n - 2) is 0, so igraph divides by zero (inf) where the reference reports undefined. |

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [csardi2006igraph](../../references.html#csardi2006igraph), [freeman1978centrality](../../references.html#freeman1978centrality), [tarjan1972depth](../../references.html#tarjan1972depth), [tarjan1975efficiency](../../references.html#tarjan1975efficiency), [wasserman1994social](../../references.html#wasserman1994social)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph)

## Theoretical maximum of centralization {#centralization_tmax}

Measure id: `centralization_tmax`. Original family: Centrality.

**Definition.** Theoretical maximum of centralization.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `centr_betw_tmax; centr_clo_tmax; centr_degree_tmax; centr_eigen_tmax` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
