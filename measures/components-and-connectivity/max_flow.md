---
title: "Maximum flow"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Maximum flow {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Flows and flow trees. Concept id: `max_flow`. 2 measures.

## Definition {#concept-definition}

Maximum flow from a set of sources to a set of sinks (Dinic), with the flow on every edge.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Max flow](#max_flow) | `max_flow` | 7 |
| [Maxflow](#gb_maxflow) | `gb_maxflow` | 1 |

## References {#concept-references}

[dinic1970algorithm](../../references.html#dinic1970algorithm), [ford1956maximal](../../references.html#ford1956maximal), [ford1962flows](../../references.html#ford1962flows), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Max flow {#max_flow}

Measure id: `max_flow`. Original family: Components and connectivity.

**Definition.** Maximum flow from a set of sources to a set of sinks (Dinic), with the flow on every edge.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `boykov_kolmogorov; capacity_scaling; dinitz; edmonds_karp; maximum_flow; maximum_flow_value; preflow_push; shortest_augmenting_path` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-max_flow-igraph) | `max_flow` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-max_flow-pyigraph) | `maxflow; maxflow_value` | API listing |
| [sna](../../tools/sna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-max_flow-sna) | `maxflow` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-max_flow-graphtool) | `boykov_kolmogorov_max_flow; edmonds_karp_max_flow; push_relabel_max_flow` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-max_flow-networkit) | `EdmondsKarp` | API listing |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-max_flow-boost) | `boykov_kolmogorov_max_flow; edmonds_karp_max_flow; push_relabel_max_flow` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-max_flow-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: max\_flow.
- <a id="why-max_flow-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: maxflow; maxflow\_value.
- <a id="why-max_flow-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: maxflow.
- <a id="why-max_flow-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: boykov\_kolmogorov\_max\_flow; edmonds\_karp\_max\_flow; push\_relabel\_max\_flow.
- <a id="why-max_flow-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: EdmondsKarp.
- <a id="why-max_flow-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: boykov\_kolmogorov\_max\_flow; edmonds\_karp\_max\_flow; push\_relabel\_max\_flow.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `flow_max_flow_valid` | NetworkX | any | agrees |  |  | abs 1e-09, rel 1e-09 | `[nx.maximum_flow_value(G, 0, n - 1), 1]: the reference value's edge flows must respect capacities, conserve flow, and carry the maximum value` |  |
| `flow_max_flow_valid_multi` | NetworkX | any | agrees |  |  | abs 1e-09, rel 1e-09 | `[nx.maximum_flow_value(H, 'S', 'T'), 1] with H as for flow_max_value_multi` |  |
| `flow_max_value` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.maximum_flow_value(G, 0, n - 1, capacity = 'capacity')` |  |
| `flow_max_value_multi` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.maximum_flow_value(H, 'S', 'T'), H = G plus arcs S -> 0, S -> 1, n - 2 -> T, n - 1 -> T without a capacity (infinite)` |  |

**References:** [dinic1970algorithm](../../references.html#dinic1970algorithm), [ford1956maximal](../../references.html#ford1956maximal), [ford1962flows](../../references.html#ford1962flows), [hagberg2008exploring](../../references.html#hagberg2008exploring)

**Tools cited:** [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit)

## Maxflow {#gb_maxflow}

Measure id: `gb_maxflow`. Original family: Traversal, trees and DAGs.

**Definition.** Maxflow.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_maxflow` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.maximum_flow_value(D, 0, n - 1, flow_func=edmonds_karp), D the simple graph with capacity = weight` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
