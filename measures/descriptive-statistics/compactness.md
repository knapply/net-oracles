---
title: "Compactness"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Compactness {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Efficiency, compactness and hierarchy. Concept id: `compactness`. 1 measure.

## Definition {#concept-definition}

Compactness. Entries grouped here: Compactness.

## Compactness {#compactness}

Measure id: `compactness`. Original family: Descriptive statistics.

**Definition.** Compactness.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-compactness-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-compactness-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `compactness` | NetworkX | any | agrees |  |  | abs 1e-15, rel 1e-13 | `nx.global_efficiency (undirected), or mean of 1/d from nx.shortest_path_length (directed)` |  |
| `compactness` | igraph (R) | any | agrees |  |  | abs 1e-15, rel 1e-13 | `mean of 1 / igraph::distances(g, mode = 'out', weights = NA) off the diagonal` |  |
| `compactness_weighted` | NetworkX | any | agrees |  |  | abs 1e-15, rel 1e-12 | `mean of 1/d from nx.shortest_path_length(G, weight = 'weight')` |  |
| `compactness_weighted` | igraph (R) | any | agrees |  |  | abs 1e-15, rel 1e-12 | `mean of 1 / igraph::distances(g, mode = 'out', weights = E(g)$weight) off the diagonal` |  |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
