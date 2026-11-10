---
title: "Disjoint paths"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Disjoint paths {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connectivity numbers. Concept id: `disjoint_paths`. 2 measures.

## Definition {#concept-definition}

Disjoint paths. Entries grouped here: Disjoint paths; Gb disjoint paths.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Disjoint paths](#disjoint_paths) | `disjoint_paths` | 3 |
| [Gb disjoint paths](#gb_disjoint_paths) | `gb_disjoint_paths` | 1 |

## Disjoint paths {#disjoint_paths}

Measure id: `disjoint_paths`. Original family: Components and connectivity.

**Definition.** Disjoint paths.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `edge_disjoint_paths; node_disjoint_paths` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-disjoint_paths-igraph) | `edge_disjoint_paths; vertex_disjoint_paths` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-disjoint_paths-jgrapht) | `BhandariKDisjointShortestPaths; SuurballeKDisjointShortestPaths` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-disjoint_paths-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: edge\_disjoint\_paths; vertex\_disjoint\_paths.
- <a id="why-disjoint_paths-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: BhandariKDisjointShortestPaths; SuurballeKDisjointShortestPaths.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_edge_disjoint_paths` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `[len(list(nx.edge_disjoint_paths(G, 0, n - 1))), 1], 0 paths on NetworkXNoPath` |  |
| `conn_node_disjoint_paths` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `[len(list(nx.node_disjoint_paths(G, 0, n - 1))), 1], 0 paths on NetworkXNoPath` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Gb disjoint paths {#gb_disjoint_paths}

Measure id: `gb_disjoint_paths`. Original family: Traversal, trees and DAGs.

**Definition.** Gb disjoint paths.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_edge_disjoint` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(list(nx.edge_disjoint_paths(M, 0, n - 1)))` |  |
| `gb_node_disjoint` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(list(nx.node_disjoint_paths(M, 0, n - 1)))` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
