---
title: "Vf2pp"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Vf2pp

Family: Graph theory and combinatorics. Identifier: `vf2pp`.

## Definition

Vf2pp.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `could_be_isomorphic; fast_could_be_isomorphic; faster_could_be_isomorphic; is_isomorphic; rooted_tree_isomorphism; tree_isomorphism; vf2pp_all_isomorphisms; vf2pp_all_monomorphisms; vf2pp_all_subgraph_isomorphisms; vf2pp_is_isomorphic; vf2pp_is_monomorphic; vf2pp_isomorphism` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `count_isomorphisms; count_subgraph_isomorphisms; is_isomorphic_to; is_subgraph_isomorphic_to; isomorphism_class; isomorphisms; subgraph_isomorphisms` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `count_automorphisms_vf2; count_isomorphisms_vf2; count_subisomorphisms_vf2; get_automorphisms_vf2; get_isomorphisms_vf2; get_subisomorphisms_lad; get_subisomorphisms_vf2; isomorphic; isomorphic_bliss; isomorphic_vf2; subisomorphic_lad; subisomorphic_vf2` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `isomorphism; subgraph_isomorphism` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `digraph_is_isomorphic; digraph_is_subgraph_isomorphic; digraph_vf2_mapping; graph_is_isomorphic; graph_is_subgraph_isomorphic; graph_vf2_mapping; is_isomorphic; is_isomorphic_node_match; is_subgraph_isomorphic; vf2_mapping` | API listing |
| [scikit-network](../tools/sknetwork.html) | · reported in docs | `are_isomorphic` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `AHUForestIsomorphismInspector; AHURootedTreeIsomorphismInspector; AHUUnrootedTreeIsomorphismInspector; ColorRefinementIsomorphismInspector; IsomorphicGraphMapping; IsomorphismInspector; VF2GraphIsomorphismInspector; VF2SubgraphIsomorphismInspector` | API listing |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `isomorphism; vf2_sub_graph_iso` | API listing |
| [nauty](../tools/nauty.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

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

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F071](../findings.html#f071) | nauty | limitation | Parallel edges are not representable |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [mckay2014practical](../references.html#mckay2014practical), [michail2020jgrapht](../references.html#michail2020jgrapht), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [siek2002boost](../references.html#siek2002boost), [tool_rustworkx](../references.html#tool_rustworkx), [tool_sknetwork](../references.html#tool_sknetwork)
{% endraw %}
