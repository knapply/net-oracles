---
title: "Reach and m-reach"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Reach and m-reach {#concept-top}

Family: [Centrality](index.html). Subfamily: Distance-based. Concept id: `reach_centrality`. 3 measures.

## Definition {#concept-definition}

Number (or share) of other nodes within distance k of every node.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Mreach closeness](#cat_closeness_mreach) | `cat_closeness_mreach` | 1 |
| [Mreach degree](#cat_degree_mreach) | `cat_degree_mreach` | 1 |
| [Reach](#reach) | `reach` | 5 |

## References {#concept-references}

[borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2005centrality](../../references.html#brandes2005centrality), [brandes2008variants](../../references.html#brandes2008variants), [butts2008sna](../../references.html#butts2008sna), [freeman1977set](../../references.html#freeman1977set), [girvan2002community](../../references.html#girvan2002community), [hwang2008bridging](../../references.html#hwang2008bridging), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

## Mreach closeness {#cat_closeness_mreach}

Measure id: `cat_closeness_mreach`. Original family: Centrality.

**Definition.** Mreach closeness.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [keyplayer](../../tools/keyplayer.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_closeness_mreach-keyplayer) | `mreach.closeness` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_closeness_mreach-keyplayer"></a>**[keyplayer](../../tools/keyplayer.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. keyplayer 1.0.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package keyplayer: exported functions and help titles); API names: mreach.closeness.

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer)

## Mreach degree {#cat_degree_mreach}

Measure id: `cat_degree_mreach`. Original family: Paths and distances.

**Definition.** Mreach degree.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [keyplayer](../../tools/keyplayer.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_degree_mreach-keyplayer) | `mreach.degree` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_degree_mreach-keyplayer"></a>**[keyplayer](../../tools/keyplayer.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. keyplayer 1.0.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package keyplayer: exported functions and help titles); API names: mreach.degree.

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer)

## Reach {#reach}

Measure id: `reach`. Original family: Centrality.

**Definition.** Number (or share) of other nodes within distance k of every node.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `ancestors; descendants; descendants_at_distance` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `count_reachable` |  |
| [sna](../../tools/sna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-reach-sna) | `reachability` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-reach-rustworkx) | `ancestors; descendants` | API listing |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-reach-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-reach-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: reachability.
- <a id="why-reach-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: ancestors; descendants.
- <a id="why-reach-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `reach_2` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.single_source_shortest_path_length(G, v, cutoff = 2)) - 1` |  |
| `reach_2` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = 2, mode = 'out') - 1` |  |
| `reach_2_all` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `single_source_shortest_path_length on G.to_undirected(), cutoff = 2` |  |
| `reach_2_all` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = 2, mode = 'all') - 1` |  |
| `reach_2_in` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `single_source_shortest_path_length on G.reverse(), cutoff = 2` |  |
| `reach_2_in` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = 2, mode = 'in') - 1` |  |
| `reach_2_normalized` | igraph (R) | any | agrees |  |  | abs 0, rel 1e-14 | `(igraph::ego_size(g, order = 2, mode = 'out') - 1) / (n - 1); undefined for one node` |  |
| `reach_inf` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.single_source_shortest_path_length(G, v)) - 1` |  |
| `reach_inf` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = vcount(g), mode = 'out') - 1` |  |
| `reach_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.single_source_dijkstra_path_length(G, v, weight = 'weight'), lengths <= 3` |  |
| `reach_weighted_strength` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `Dijkstra lengths with edge length 1/weight, <= 1.5` |  |

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2005centrality](../../references.html#brandes2005centrality), [brandes2008variants](../../references.html#brandes2008variants), [butts2008sna](../../references.html#butts2008sna), [freeman1977set](../../references.html#freeman1977set), [girvan2002community](../../references.html#girvan2002community), [hwang2008bridging](../../references.html#hwang2008bridging), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
