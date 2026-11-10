---
title: "Ego network members"
layout: default
parent: "Ego networks"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Ego network members {#concept-top}

Family: [Ego networks](index.html). Subfamily: Ego measures. Concept id: `ego_members`. 1 measure.

## Definition {#concept-definition}

Ego network members. Entries grouped here: Ego members.

## Ego members {#ego_members}

Measure id: `ego_members`. Original family: Two-mode and bipartite.

**Definition.** Ego members.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `ego_graph` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `ego; make_ego_graph` |  |
| [sna](../../tools/sna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-ego_members-sna) | `ego.extract` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-ego_members-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: ego.extract.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ego_alters` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.ego_graph(G, v, undirected = True, center = False).nodes` |  |
| `ego_alters` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::ego(g, order = 1, mode = 'all', mindist = 1)` |  |
| `ego_alters_order2_out` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.ego_graph(G, v, radius = 2, center = False).nodes` |  |
| `ego_alters_order2_out` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::ego(g, order = 2, mode = 'out', mindist = 1)` |  |

**Tools cited:** [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
