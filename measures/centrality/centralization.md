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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-cat_centralization-ucinet) | `centralization` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_centralization-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## Centralization / betweenness {#centralization-betweenness}

Measure id: `centralization:betweenness`. Original family: Descriptive statistics.

**Definition.** Freeman centralization of degree, betweenness, closeness or eigenvector centrality.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `centr_betw` |  |
| [sna](../../tools/sna.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges): sna collapses parallel edges, which changes shortest-path counts. [details](#why-centralization-betweenness-sna) | `centralization` |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-centralization-betweenness-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-centralization-betweenness-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> sna 2.8 was run and its value differs from the reference value by convention (multi-edges) on inputs tagged multi\_edges. sna collapses parallel edges, which changes shortest-path counts. Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 1e-12, rel 1e-10 on all 2 comparisons where the difference occurs. Tolerance before mapping: abs 1e-12, rel 1e-10 (0 means exact equality). 4 comparisons differ and 32 agree.
- <a id="why-centralization-betweenness-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `centr_clo` |  |
| [sna](../../tools/sna.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-centralization-closeness-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-centralization-closeness-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `centr_degree` |  |
| [sna](../../tools/sna.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-centralization-degree-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-centralization-degree-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults and normalization): On a disconnected graph the leading eigenvalue need not be simple, so the eigenvector (and its centralization) depends on the eigensolver's start. [details](#why-centralization_eigenvector-igraph) | `centr_eigen` |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-centralization_eigenvector-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-centralization_eigenvector-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (R) 2.3.4 was run and its value differs from the reference value by convention (defaults and normalization) on inputs tagged disconnected and two\_nodes. On a disconnected graph the leading eigenvalue need not be simple, so the eigenvector (and its centralization) depends on the eigensolver's start; on two nodes the theoretical maximum (n - 2) is 0, so igraph divides by zero (inf) where the reference reports undefined. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 1 comparisons differ and 27 agree.
- <a id="why-centralization_eigenvector-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-centralization_tmax-igraph) | `centr_betw_tmax; centr_clo_tmax; centr_degree_tmax; centr_eigen_tmax` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-centralization_tmax-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: centr\_betw\_tmax; centr\_clo\_tmax; centr\_degree\_tmax; centr\_eigen\_tmax.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
