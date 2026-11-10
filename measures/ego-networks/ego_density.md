---
title: "Ego network density"
layout: default
parent: "Ego networks"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Ego network density {#concept-top}

Family: [Ego networks](index.html). Subfamily: Ego measures. Concept id: `ego_density`. 1 measure.

## Definition {#concept-definition}

Ego network density. Entries grouped here: Ego\_summary / density.

## Ego\_summary / density {#ego_summary-density}

Measure id: `ego_summary:density`. Original family: Two-mode and bipartite.

**Definition.** Ego\_summary / density.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-ego_summary-density-ucinet) | `egodensity` | published documentation |
| [egor](../../tools/egor.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-ego_summary-density-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ego_density` | NetworkX | any | agrees |  |  | abs 0, rel 1e-14 | `nx.density(nx.ego_graph(simple G, v, undirected = True, center = False)); undefined below two alters` |  |
| `ego_density` | igraph (R) | any | agrees |  |  | abs 0, rel 1e-14 | `igraph::edge_density(induced_subgraph(simplify(g), ego(g, 1, v, 'all', mindist = 1)))` |  |
| `ego_density` | egor | any | agrees |  |  | abs 0, rel 1e-14 | `egor::ego_density(egor object, directed = 'directed' \| 'undirected')` |  |
| `ego_density_out` | NetworkX | directed | agrees |  |  | abs 0, rel 1e-14 | `nx.density(nx.ego_graph(simple G, v, center = False)); undefined below two alters` |  |
| `ego_density_out` | igraph (R) | directed | agrees |  |  | abs 0, rel 1e-14 | `igraph::edge_density(induced_subgraph(simplify(g), ego(g, 1, v, 'out', mindist = 1)))` |  |
| `ego_density_out` | egor | directed | agrees |  |  | abs 0, rel 1e-14 | `egor::ego_density(egor object of out-neighbours, directed = 'directed')` |  |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_egor](../../references.html#tool_egor)
{% endraw %}
