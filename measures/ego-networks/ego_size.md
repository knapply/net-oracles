---
title: "Ego size"
layout: default
parent: "Ego networks"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Ego size {#concept-top}

Family: [Ego networks](index.html). Subfamily: Ego measures. Concept id: `ego_size`. 1 measure.

## Definition {#concept-definition}

Number of nodes within a range of steps from each node (ego included when the range starts at 0).

## References {#concept-references}

[staudt2016networkit](../../references.html#staudt2016networkit)

## Ego size {#ego_size}

Measure id: `ego_size`. Original family: Descriptive statistics.

**Definition.** Number of nodes within a range of steps from each node (ego included when the range starts at 0).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `ego_size` |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-ego_size-ucinet) | `Ego network density, size, ties, ego betweenness, ego composition (egocomp, 6.845), alter heterogeneity (IQV, Blau, Shannon; option to ignore ego's category, 6.` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-ego_size-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ego_size` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.ego_graph(G, v, radius = 1, undirected = True))` |  |
| `ego_size` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = 1, mode = 'all', mindist = 0)` |  |
| `ego_size_in` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `len(nx.ego_graph(G.reverse(), v, radius = 1))` |  |
| `ego_size_in` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = 1, mode = 'in')` |  |
| `ego_size_order2` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.ego_graph(G, v, radius = 2, undirected = True))` |  |
| `ego_size_order2` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = 2, mode = 'all')` |  |
| `ego_size_out` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `len(nx.ego_graph(G, v, radius = 1)) (successors)` |  |
| `ego_size_out` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = 1, mode = 'out')` |  |

**References:** [staudt2016networkit](../../references.html#staudt2016networkit)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
