---
title: "Biconnected components"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Biconnected components {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Articulation points, bridges and biconnected components. Concept id: `biconnected_components`. 2 measures.

## Definition {#concept-definition}

Biconnected components. Entries grouped here: Bicomponents; Biconnected.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Bicomponents](#bicomponents) | `bicomponents` | 10 |
| [Biconnected](#nxo_biconnected) | `nxo_biconnected` | 1 |

## Bicomponents {#bicomponents}

Measure id: `bicomponents`. Original family: Components and connectivity.

**Definition.** Bicomponents.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `biconnected_component_edges; biconnected_components` |  |
| [igraph (R)](../../tools/igraph.html) | ✓ checked, agrees | `biconnected_components` |  |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `biconnected_components` | API listing |
| [sna](../../tools/sna.html) | · reported in docs | `bicomponent.dist` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `label_biconnected_components` | API listing |
| [NetworKit](../../tools/networkit.html) | ∅ checked, no value on some inputs | `BiconnectedComponents` |  |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `biconnected_components` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `BiconnectivityInspector; BlockCutpointGraph` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `biconnected_components` | API listing |
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `bicomponents` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.biconnected_components(simple undirected graph)` |  |
| `bicomponents` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::biconnected_components(simplify(as_undirected(g)))$components` |  |
| `bicomponents` | NetworKit | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nk.components.BiconnectedComponents(G simple).getComponents()` |  |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)

## Biconnected {#nxo_biconnected}

Measure id: `nxo_biconnected`. Original family: Components and connectivity.

**Definition.** Biconnected.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxo_biconnected` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges, ties | abs 0, rel 0 | `nx.biconnected_component_edges(G), components in order, (parent, child) edges` | The backend leaves multigraphs to NetworkX (their adjacency order is not the edge order). |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
