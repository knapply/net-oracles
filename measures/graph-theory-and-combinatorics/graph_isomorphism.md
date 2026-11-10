---
title: "Graph isomorphism"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Graph isomorphism {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Isomorphism and subgraph matching. Concept id: `graph_isomorphism`. 7 measures.

## Definition {#concept-definition}

Graph isomorphism. Entries grouped here: Could be iso; Di Graph Matcher; Graph Matcher; Match vertices; Multi Di Graph Matcher; Multi Graph Matcher; and 1 more.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Could be iso](#could_be_iso) | `could_be_iso` | 1 |
| [Di Graph Matcher](#cat_di_matcher) | `cat_di_matcher` | 1 |
| [Graph Matcher](#cat_matcher) | `cat_matcher` | 1 |
| [Match vertices](#cat_match) | `cat_match` | 1 |
| [Multi Di Graph Matcher](#cat_di_matcher_multi) | `cat_di_matcher_multi` | 1 |
| [Multi Graph Matcher](#cat_matcher_multi) | `cat_matcher_multi` | 1 |
| [Vf2pp](#vf2pp) | `vf2pp` | 9 |

## Could be iso {#could_be_iso}

Measure id: `could_be_iso`. Original family: Graph theory and combinatorics.

**Definition.** Could be iso.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `could_be_iso_d_perturbed` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.could_be_isomorphic(G, perturbed(G), properties = 'd')` |  |
| `could_be_iso_d_rev` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.could_be_isomorphic(G, rev(G), properties = 'd')` |  |
| `could_be_iso_dt_perturbed` | NetworkX | any | no-value-on-some-inputs | (no value) directed | direction | abs 0, rel 0 | `nx.could_be_isomorphic(G, perturbed(G), properties = 'dt')` | NetworkX counts triangles and maximal cliques of undirected graphs only (it raises NetworkXNotImplemented) |
| `could_be_iso_dt_rev` | NetworkX | any | no-value-on-some-inputs | (no value) directed | direction | abs 0, rel 0 | `nx.could_be_isomorphic(G, rev(G), properties = 'dt')` | NetworkX counts triangles and maximal cliques of undirected graphs only (it raises NetworkXNotImplemented) |
| `could_be_iso_dtc_perturbed` | NetworkX | any | no-value-on-some-inputs | (no value) directed | direction | abs 0, rel 0 | `nx.could_be_isomorphic(G, perturbed(G), properties = 'dtc')` | NetworkX counts triangles and maximal cliques of undirected graphs only (it raises NetworkXNotImplemented) |
| `could_be_iso_dtc_rev` | NetworkX | any | no-value-on-some-inputs | (no value) directed | direction | abs 0, rel 0 | `nx.could_be_isomorphic(G, rev(G), properties = 'dtc')` | NetworkX counts triangles and maximal cliques of undirected graphs only (it raises NetworkXNotImplemented) |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Di Graph Matcher {#cat_di_matcher}

Measure id: `cat_di_matcher`. Original family: Graph theory and combinatorics.

**Definition.** Di Graph Matcher.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_di_matcher-networkx) | `DiGraphMatcher` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_di_matcher-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: DiGraphMatcher.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Graph Matcher {#cat_matcher}

Measure id: `cat_matcher`. Original family: Graph theory and combinatorics.

**Definition.** Graph Matcher.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_matcher-networkx) | `GraphMatcher` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_matcher-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: GraphMatcher.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Match vertices {#cat_match}

Measure id: `cat_match`. Original family: Graph theory and combinatorics.

**Definition.** Match vertices.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_match-igraph) | `match_vertices` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_match-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: match\_vertices.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Multi Di Graph Matcher {#cat_di_matcher_multi}

Measure id: `cat_di_matcher_multi`. Original family: Graph theory and combinatorics.

**Definition.** Multi Di Graph Matcher.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_di_matcher_multi-networkx) | `MultiDiGraphMatcher` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_di_matcher_multi-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: MultiDiGraphMatcher.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Multi Graph Matcher {#cat_matcher_multi}

Measure id: `cat_matcher_multi`. Original family: Graph theory and combinatorics.

**Definition.** Multi Graph Matcher.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_matcher_multi-networkx) | `MultiGraphMatcher` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_matcher_multi-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: MultiGraphMatcher.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Vf2pp {#vf2pp}

Measure id: `vf2pp`. Original family: Graph theory and combinatorics.

**Definition.** Vf2pp.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `could_be_isomorphic; fast_could_be_isomorphic; faster_could_be_isomorphic; is_isomorphic; rooted_tree_isomorphism; tree_isomorphism; vf2pp_all_isomorphisms; vf2pp_all_monomorphisms; vf2pp_all_subgraph_isomorphisms; vf2pp_is_isomorphic; vf2pp_is_monomorphic; vf2pp_isomorphism` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-vf2pp-igraph) | `count_isomorphisms; count_subgraph_isomorphisms; is_isomorphic_to; is_subgraph_isomorphic_to; isomorphism_class; isomorphisms; subgraph_isomorphisms` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-vf2pp-pyigraph) | `count_automorphisms_vf2; count_isomorphisms_vf2; count_subisomorphisms_vf2; get_automorphisms_vf2; get_isomorphisms_vf2; get_subisomorphisms_lad; get_subisomorphisms_vf2; isomorphic; isomorphic_bliss; isomorphic_vf2; subisomorphic_lad; subisomorphic_vf2` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-vf2pp-graphtool) | `isomorphism; subgraph_isomorphism` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-vf2pp-rustworkx) | `digraph_is_isomorphic; digraph_is_subgraph_isomorphic; digraph_vf2_mapping; graph_is_isomorphic; graph_is_subgraph_isomorphic; graph_vf2_mapping; is_isomorphic; is_isomorphic_node_match; is_subgraph_isomorphic; vf2_mapping` | API listing |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-vf2pp-sknetwork) | `are_isomorphic` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-vf2pp-jgrapht) | `AHUForestIsomorphismInspector; AHURootedTreeIsomorphismInspector; AHUUnrootedTreeIsomorphismInspector; ColorRefinementIsomorphismInspector; IsomorphicGraphMapping; IsomorphismInspector; VF2GraphIsomorphismInspector; VF2SubgraphIsomorphismInspector` | API listing |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-vf2pp-boost) | `isomorphism; vf2_sub_graph_iso` | API listing |
| [nauty](../../tools/nauty.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-vf2pp-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: count\_isomorphisms; count\_subgraph\_isomorphisms; is\_isomorphic\_to; is\_subgraph\_isomorphic\_to; isomorphism\_class; isomorphisms; subgraph\_isomorphisms.
- <a id="why-vf2pp-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: count\_automorphisms\_vf2; count\_isomorphisms\_vf2; count\_subisomorphisms\_vf2; get\_automorphisms\_vf2; get\_isomorphisms\_vf2; get\_subisomorphisms\_lad; get\_subisomorphisms\_vf2; isomorphic; isomorphic\_bliss; isomorphic\_vf2; subisomorphic\_lad; subisomorphic\_vf2.
- <a id="why-vf2pp-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: isomorphism; subgraph\_isomorphism.
- <a id="why-vf2pp-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: digraph\_is\_isomorphic; digraph\_is\_subgraph\_isomorphic; digraph\_vf2\_mapping; graph\_is\_isomorphic; graph\_is\_subgraph\_isomorphic; graph\_vf2\_mapping; is\_isomorphic; is\_isomorphic\_node\_match; is\_subgraph\_isomorphic; vf2\_mapping.
- <a id="why-vf2pp-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: are\_isomorphic.
- <a id="why-vf2pp-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: AHUForestIsomorphismInspector; AHURootedTreeIsomorphismInspector; AHUUnrootedTreeIsomorphismInspector; ColorRefinementIsomorphismInspector; IsomorphicGraphMapping; IsomorphismInspector; VF2GraphIsomorphismInspector; VF2SubgraphIsomorphismInspector.
- <a id="why-vf2pp-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: isomorphism; vf2\_sub\_graph\_iso.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `vf2pp_induced_cycle4` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `min(len(list(nx.vf2pp_all_subgraph_isomorphisms(G, cycle4))), 5000)` |  |
| `vf2pp_induced_feedforward` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `min(len(list(nx.vf2pp_all_subgraph_isomorphisms(G, feedforward))), 5000)` |  |
| `vf2pp_induced_path3` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `min(len(list(nx.vf2pp_all_subgraph_isomorphisms(G, path3))), 5000)` |  |
| `vf2pp_induced_path3_labels` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `min(len(list(nx.vf2pp_all_subgraph_isomorphisms(G, path3, node_label = 'label'))), 5000)` |  |
| `vf2pp_induced_star3` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `min(len(list(nx.vf2pp_all_subgraph_isomorphisms(G, star3))), 5000)` |  |
| `vf2pp_induced_triangle` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `min(len(list(nx.vf2pp_all_subgraph_isomorphisms(G, triangle))), 5000)` |  |
| `vf2pp_iso` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `min(len(list(nx.vf2pp_all_isomorphisms(G, rev(G)))), 5000)` |  |
| `vf2pp_iso` | nauty | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 0, rel 0 | `pynauty.autgrp group order when the network is isomorphic to its node-reversed copy, capped at 5000` | nauty graphs are simple: parallel edges (edge multiplicities, which the reference and the definition oracle respect) cannot be represented. |
| `vf2pp_iso_labels` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `min(len(list(nx.vf2pp_all_isomorphisms(G, rev(G), node_label = 'label'))), 5000)` |  |
| `vf2pp_iso_labels` | nauty | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 0, rel 0 | `as vf2pp_iso with vertex colours v mod 2 (pynauty vertex_coloring), capped at 5000` | nauty graphs are simple: parallel edges (edge multiplicities, which the reference and the definition oracle respect) cannot be represented. |
| `vf2pp_mono_cycle4` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `min(len(list(nx.vf2pp_all_monomorphisms(G, cycle4))), 5000)` |  |
| `vf2pp_mono_feedforward` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `min(len(list(nx.vf2pp_all_monomorphisms(G, feedforward))), 5000)` |  |
| `vf2pp_mono_path3` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `min(len(list(nx.vf2pp_all_monomorphisms(G, path3))), 5000)` |  |
| `vf2pp_mono_star3` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `min(len(list(nx.vf2pp_all_monomorphisms(G, star3))), 5000)` |  |
| `vf2pp_mono_star3_labels` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `min(len(list(nx.vf2pp_all_monomorphisms(G, star3, node_label = 'label'))), 5000)` |  |
| `vf2pp_mono_triangle` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `min(len(list(nx.vf2pp_all_monomorphisms(G, triangle))), 5000)` |  |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F071](../../findings.html#f071) | nauty | limitation | Parallel edges are not representable |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [mckay2014practical](../../references.html#mckay2014practical), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx), [tool_sknetwork](../../references.html#tool_sknetwork)
{% endraw %}
