---
title: "Connected components"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Connected components {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connected components. Concept id: `connected_components`. 5 measures.

## Definition {#concept-definition}

Weak or strong components: a label for every node and the size of each component.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Components](#components) | `components` | 13 |
| [Count components](#cat_component_count) | `cat_component_count` | 1 |
| [Kosaraju](#nxo_kosaraju) | `nxo_kosaraju` | 1 |
| [Parallel Connected Components](#cat_component_connected_parallel) | `cat_component_connected_parallel` | 1 |
| [Strong partition](#strong_partition) | `strong_partition` | 2 |

## Components {#components}

Measure id: `components`. Original family: Descriptive statistics.

**Definition.** Weak or strong components: a label for every node and the size of each component.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `connected_components; is_biconnected; is_connected; is_strongly_connected; is_weakly_connected; kosaraju_strongly_connected_components; node_connected_component; number_connected_components; number_strongly_connected_components; number_weakly_connected_components; strongly_connected_components; weakly_connected_components` |  |
| [igraph (R)](../../tools/igraph.html) | ∅ checked, no value on some inputs | `clusters; component_distribution; components; decompose; is_biconnected; is_connected; largest_component; subcomponent` |  |
| [igraph (Python)](../../tools/pyigraph.html) | ✓ checked, agrees | `components; decompose; is_biconnected; is_connected; subcomponent` |  |
| [sna](../../tools/sna.html) | · reported in docs | `component.dist; component.largest; component.size.byvertex; components; is.connected` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `extract_largest_component; label_components; label_largest_component; label_out_component` | API listing |
| [NetworKit](../../tools/networkit.html) | ✓ checked, agrees | `ConnectedComponents; StronglyConnectedComponents; WeaklyConnectedComponents` |  |
| [rustworkx](../../tools/rustworkx.html) | ✓ checked, agrees | `connected_components; connected_subgraphs; is_connected; is_strongly_connected; is_weakly_connected; node_connected_component; number_connected_components; number_strongly_connected_components; number_weakly_connected_components; strongly_connected_components; weakly_connected_components` |  |
| [scikit-network](../../tools/sknetwork.html) | ✓ checked, agrees | `get_connected_components; get_largest_connected_component; is_connected` |  |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `ConnectivityInspector` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `connected_components; incremental_components; st_connected; strong_components` | API listing |
| [BCT (Octave)](../../tools/bct.html) | · reported in docs | `get_components; number_of_components` | API listing |
| [Gephi toolkit](../../tools/gephi.html) | ✓ checked, agrees | `ConnectedComponents` |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `component; numcomp` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `components_strong` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.strongly_connected_components / nx.connected_components` |  |
| `components_strong` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::components(g, mode = 'strong')$membership` |  |
| `components_strong` | igraph (Python) | any | agrees |  |  | abs 0, rel 0 | `python-igraph: g.connected_components(mode="strong").membership` |  |
| `components_strong` | NetworKit | any | agrees |  |  | abs 0, rel 0 | `nk.components.StronglyConnectedComponents(G) (ConnectedComponents when undirected)` |  |
| `components_strong` | rustworkx | any | agrees |  |  | abs 0, rel 0 | `rx.strongly_connected_components(G) (connected_components when undirected)` |  |
| `components_strong` | scikit-network | any | no-value-on-some-inputs |  | defaults | abs 0, rel 0 | `sknetwork.topology.get_connected_components(A, connection = 'strong')` | scikit-network rejects an adjacency matrix without entries ('The input matrix is empty'). |
| `components_strong` | Gephi toolkit | any | agrees |  |  | abs 0, rel 0 | `Gephi toolkit 0.11.3: ConnectedComponents, node column 'strongcompnum' (directed networks; 'componentnumber' for undirected)` |  |
| `components_weak` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.weakly_connected_components / nx.connected_components` |  |
| `components_weak` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::components(g, mode = 'weak')$membership` |  |
| `components_weak` | igraph (Python) | any | agrees |  |  | abs 0, rel 0 | `python-igraph: g.connected_components(mode="weak").membership` |  |
| `components_weak` | NetworKit | any | agrees |  |  | abs 0, rel 0 | `nk.components.WeaklyConnectedComponents(G) (ConnectedComponents when undirected)` |  |
| `components_weak` | rustworkx | any | agrees |  |  | abs 0, rel 0 | `rx.weakly_connected_components(G) (connected_components when undirected)` |  |
| `components_weak` | scikit-network | any | no-value-on-some-inputs |  | defaults | abs 0, rel 0 | `sknetwork.topology.get_connected_components(A, connection = 'weak')` | scikit-network rejects an adjacency matrix without entries ('The input matrix is empty'). |
| `components_weak` | Gephi toolkit | any | agrees |  |  | abs 0, rel 0 | `Gephi toolkit 0.11.3: ConnectedComponents, node column 'componentnumber'` |  |

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [rubinov2010complex](../../references.html#rubinov2010complex), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx), [tool_sknetwork](../../references.html#tool_sknetwork)

## Count components {#cat_component_count}

Measure id: `cat_component_count`. Original family: Components and connectivity.

**Definition.** Count components.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `count_components` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Kosaraju {#nxo_kosaraju}

Measure id: `nxo_kosaraju`. Original family: Graph theory and combinatorics.

**Definition.** Kosaraju.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxo_kosaraju` | NetworkX | directed | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges, ties | abs 0, rel 0 | `nx.kosaraju_strongly_connected_components(G), components in order` | The backend leaves multigraphs to NetworkX (their adjacency order is not the edge order); the reference value's components are the same sets. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Parallel Connected Components {#cat_component_connected_parallel}

Measure id: `cat_component_connected_parallel`. Original family: Components and connectivity.

**Definition.** Parallel Connected Components.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | · reported in docs | `ParallelConnectedComponents` | API listing |

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Strong partition {#strong_partition}

Measure id: `strong_partition`. Original family: Components and connectivity.

**Definition.** Strong partition.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | ✓ checked, agrees | `GabowStrongConnectivityInspector; KosarajuStrongConnectivityInspector` |  |
| [Boost Graph Library](../../tools/boost.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_strong_partition` | JGraphT | directed | agrees |  |  | abs 0, rel 0 | `JGraphT 1.5.2: new KosarajuStrongConnectivityInspector<>(g).stronglyConnectedSets() on a pseudograph` |  |
| `conn_strong_partition` | Boost Graph Library | directed | agrees |  |  | abs 0, rel 0 | `Boost Graph Library strong_components` |  |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht), [siek2002boost](../../references.html#siek2002boost)
{% endraw %}
