---
title: "Ego betweenness"
layout: default
parent: "Ego networks"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Ego betweenness {#concept-top}

Family: [Ego networks](index.html). Subfamily: Ego measures. Concept id: `ego_betweenness`. 1 measure.

## Definition {#concept-definition}

Ego betweenness. Entries grouped here: Ego\_summary / betweenness.

## Ego\_summary / betweenness {#ego_summary-betweenness}

Measure id: `ego_summary:betweenness`. Original family: Two-mode and bipartite.

**Definition.** Ego\_summary / betweenness.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-ego_summary-betweenness-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-ego_summary-betweenness-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ego_betweenness` | NetworkX | any | agrees |  |  | abs 1e-09, rel 1e-09 | `nx.betweenness_centrality(nx.ego_graph(simple G, v, undirected = True), normalized = False)[v]` |  |
| `ego_betweenness` | igraph (R) | any | agrees |  |  | abs 1e-09, rel 1e-09 | `igraph::betweenness(make_ego_graph(simplify(g), 1, v, 'all')[[1]], ego)` |  |
| `ego_betweenness_order2` | NetworkX | any | agrees |  |  | abs 1e-09, rel 1e-09 | `nx.betweenness_centrality(nx.ego_graph(simple G, v, radius = 2, undirected = True), normalized = False)[v]` |  |
| `ego_betweenness_out` | NetworkX | directed | agrees |  |  | abs 1e-09, rel 1e-09 | `nx.betweenness_centrality(nx.ego_graph(simple G, v), normalized = False)[v]` |  |
| `ego_betweenness_out` | igraph (R) | directed | agrees |  |  | abs 1e-09, rel 1e-09 | `igraph::betweenness(make_ego_graph(simplify(g), 1, v, 'out')[[1]], ego, directed = TRUE)` |  |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
