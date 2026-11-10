---
title: "Components"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Components

Family: Descriptive statistics. Identifier: `components`.

## Definition

Weak or strong components: a label for every node and the size of each component.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `connected_components; is_biconnected; is_connected; is_strongly_connected; is_weakly_connected; kosaraju_strongly_connected_components; node_connected_component; number_connected_components; number_strongly_connected_components; number_weakly_connected_components; strongly_connected_components; weakly_connected_components` |  |
| [igraph (R)](../tools/igraph.html) | ∅ checked, no value on some inputs | `clusters; component_distribution; components; decompose; is_biconnected; is_connected; largest_component; subcomponent` |  |
| [igraph (Python)](../tools/pyigraph.html) | ✓ checked, agrees | `components; decompose; is_biconnected; is_connected; subcomponent` |  |
| [sna](../tools/sna.html) | · reported in docs | `component.dist; component.largest; component.size.byvertex; components; is.connected` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `extract_largest_component; label_components; label_largest_component; label_out_component` | API listing |
| [NetworKit](../tools/networkit.html) | ✓ checked, agrees | `ConnectedComponents; StronglyConnectedComponents; WeaklyConnectedComponents` |  |
| [rustworkx](../tools/rustworkx.html) | ✓ checked, agrees | `connected_components; connected_subgraphs; is_connected; is_strongly_connected; is_weakly_connected; node_connected_component; number_connected_components; number_strongly_connected_components; number_weakly_connected_components; strongly_connected_components; weakly_connected_components` |  |
| [scikit-network](../tools/sknetwork.html) | ✓ checked, agrees | `get_connected_components; get_largest_connected_component; is_connected` |  |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `ConnectivityInspector` | API listing |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `connected_components; incremental_components; st_connected; strong_components` | API listing |
| [BCT (Octave)](../tools/bct.html) | · reported in docs | `get_components; number_of_components` | API listing |
| [Gephi toolkit](../tools/gephi.html) | ✓ checked, agrees | `ConnectedComponents` |  |
| [UCINET](../tools/ucinet.html) | · reported in docs | `component; numcomp` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

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

Tools cited: [bastian2009gephi](../references.html#bastian2009gephi), [borgatti2002ucinet](../references.html#borgatti2002ucinet), [butts2008sna](../references.html#butts2008sna), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [rubinov2010complex](../references.html#rubinov2010complex), [siek2002boost](../references.html#siek2002boost), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx), [tool_sknetwork](../references.html#tool_sknetwork)
{% endraw %}
