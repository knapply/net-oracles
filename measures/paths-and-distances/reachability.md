---
title: "Reachability"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Reachability {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Efficiency and reachability. Concept id: `reachability`. 3 measures.

## Definition {#concept-definition}

Reachability. Entries grouped here: Reachability; Reachable Nodes; Reachdist.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Reachability](#reachability) | `reachability` | 5 |
| [Reachable Nodes](#cat_reachable) | `cat_reachable` | 1 |
| [Reachdist](#cat_reachdist) | `cat_reachdist` | 1 |

## Reachability {#reachability}

Measure id: `reachability`. Original family: Paths and distances.

**Definition.** Reachability.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `has_path; is_reachable` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `neighborhood_size` |  |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-reachability-rustworkx) | `digraph_has_path; graph_has_path; has_path` | API listing |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-reachability-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-reachability-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: digraph\_has\_path; graph\_has\_path; has\_path.
- <a id="why-reachability-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `reachability` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.descendants(G, v)), or len(nx.node_connected_component(G, v)) - 1 if undirected` |  |
| `reachability` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = vcount(g), mode = 'out') - 1` |  |
| `reachability` | igraph (Python) | any | agrees |  |  | abs 0, rel 0 | `python-igraph: [x - 1 for x in gu.neighborhood_size(order=everything, mode="out")]` |  |
| `reachability_all` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `len(nx.node_connected_component(G.to_undirected(), v)) - 1` |  |
| `reachability_all` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = vcount(g), mode = 'all') - 1` |  |
| `reachability_all` | igraph (Python) | directed | agrees |  |  | abs 0, rel 0 | `python-igraph: [x - 1 for x in gu.neighborhood_size(order=everything, mode="all")]` |  |
| `reachability_in` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `len(nx.ancestors(G, v))` |  |
| `reachability_in` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = vcount(g), mode = 'in') - 1` |  |
| `reachability_in` | igraph (Python) | directed | agrees |  |  | abs 0, rel 0 | `python-igraph: [x - 1 for x in gu.neighborhood_size(order=everything, mode="in")]` |  |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)

## Reachable Nodes {#cat_reachable}

Measure id: `cat_reachable`. Original family: Paths and distances.

**Definition.** Reachable Nodes.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_reachable-networkit) | `ReachableNodes` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_reachable-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: ReachableNodes.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Reachdist {#cat_reachdist}

Measure id: `cat_reachdist`. Original family: Paths and distances.

**Definition.** Reachdist.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_reachdist-bct) | `reachdist` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_reachdist-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: reachdist.

**Tools cited:** [rubinov2010complex](../../references.html#rubinov2010complex)
{% endraw %}
