---
title: "Deterministic generators"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Deterministic generators {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Named and deterministic graphs. Concept id: `deterministic_generators`. 1 measure.

## Definition {#concept-definition}

Deterministic generators. Entries grouped here: Deterministic generators.

## Deterministic generators {#deterministic_generators}

Measure id: `deterministic_generators`. Original family: Generators and rewiring.

**Definition.** Deterministic generators.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `balanced_tree; complete_bipartite_graph; complete_graph; cycle_graph; empty_graph; full_rary_tree; hypercube_graph; ladder_graph; null_graph; path_graph; star_graph; trivial_graph` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `empty_graph; make_empty_graph; make_full_bipartite_graph; make_full_graph; make_ring; make_star; make_tree; make_wheel; ring; star; tree; wheel` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Full; Full_Bipartite; Hypercube; Ring; Star; Tree` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `circular_graph; complete_graph` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `complete_graph; cycle_graph; directed_complete_graph; directed_cycle_graph; directed_empty_graph; directed_path_graph; directed_star_graph; empty_graph; full_rary_tree; path_graph; star_graph` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `CompleteBipartiteGraphGenerator; CompleteGraphGenerator; EmptyGraphGenerator; HyperCubeGraphGenerator; LinearGraphGenerator; RingGraphGenerator; StarGraphGenerator; WheelGraphGenerator` | API listing |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `cycle; makeclique; path; star` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `construct_complete` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.complete_graph(n)` |  |
| `construct_complete_bipartite` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.complete_bipartite_graph(n // 2, n - n // 2)` |  |
| `construct_complete_dir` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.complete_graph(n, create_using = nx.DiGraph)` |  |
| `construct_cycle` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.cycle_graph(n)` |  |
| `construct_cycle_dir` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.cycle_graph(n, create_using = nx.DiGraph)` |  |
| `construct_empty` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.empty_graph(n)` |  |
| `construct_hypercube` | NetworkX | any | differs | null\_graph | defaults | abs 0, rel 0 | `nx.hypercube_graph(d) relabelled by the bits of the coordinates, first coordinate most significant` | NetworkX defines the 0-dimensional hypercube as the null graph (nx.hypercube\_graph(0) has no node); the reference and the definition oracle give Q\_0 = K\_1, one node (2^0 nodes joined when their numbers differ in one bit). Convention, on the null graph only. |
| `construct_ladder` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.ladder_graph(n)` |  |
| `construct_lattice` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.grid_2d_graph(3, n) relabelled to r * n + c` |  |
| `construct_path` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.path_graph(n)` |  |
| `construct_path_dir` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.path_graph(n, create_using = nx.DiGraph)` |  |
| `construct_star` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.star_graph(n - 1) (nx.empty_graph(0) for n = 0)` |  |
| `construct_star_dir` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `as star, create_using = nx.DiGraph` |  |
| `construct_tree_binary` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.balanced_tree(2, min(n, 5))` |  |
| `construct_tree_ternary` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.balanced_tree(3, min(n, 4))` |  |
| `construct_wheel` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.wheel_graph(n)` |  |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
