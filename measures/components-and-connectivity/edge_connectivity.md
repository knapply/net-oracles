---
title: "Edge connectivity"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Edge connectivity {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connectivity numbers. Concept id: `edge_connectivity`. 1 measure.

## Definition {#concept-definition}

Global edge connectivity: the fewest edges whose removal disconnects the network.

## References {#concept-references}

[esfahanian1984computing](../../references.html#esfahanian1984computing), [even1975algorithm](../../references.html#even1975algorithm), [even1975network](../../references.html#even1975network), [ford1956maximal](../../references.html#ford1956maximal), [harary1969graph](../../references.html#harary1969graph), [menger1927allgemeinen](../../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../../references.html#schnorr1979bottlenecks)

## Connectivity {#connectivity}

Measure id: `connectivity`. Original family: Components and connectivity.

**Definition.** Global edge connectivity: the fewest edges whose removal disconnects the network.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `average_node_connectivity; edge_connectivity; is_k_edge_connected; local_edge_connectivity; local_node_connectivity; node_connectivity` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-connectivity-igraph) | `adhesion; cohesion; edge_connectivity; vertex_connectivity` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-connectivity-pyigraph) | `adhesion; cohesion` | API listing |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-connectivity-boost) | `edge_connectivity` | API listing |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-connectivity-ucinet) | `cohesion` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-connectivity-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: adhesion; cohesion; edge\_connectivity; vertex\_connectivity.
- <a id="why-connectivity-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: adhesion; cohesion.
- <a id="why-connectivity-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: edge\_connectivity.
- <a id="why-connectivity-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_edge` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.edge_connectivity(G)` |  |
| `conn_node` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.node_connectivity(G)` |  |

**References:** [esfahanian1984computing](../../references.html#esfahanian1984computing), [even1975algorithm](../../references.html#even1975algorithm), [even1975network](../../references.html#even1975network), [ford1956maximal](../../references.html#ford1956maximal), [harary1969graph](../../references.html#harary1969graph), [menger1927allgemeinen](../../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../../references.html#schnorr1979bottlenecks)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [siek2002boost](../../references.html#siek2002boost)
{% endraw %}
