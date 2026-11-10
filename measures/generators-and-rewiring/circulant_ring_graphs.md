---
title: "Circulant and ring graphs (ladder, chordal, Petersen, Harary)"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Circulant and ring graphs (ladder, chordal, Petersen, Harary) {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Named and deterministic graphs. Concept id: `circulant_ring_graphs`. 9 measures.

## Definition {#concept-definition}

Circulant and ring graphs (ladder, chordal, Petersen, Harary). Entries grouped here: Chordal cycle graph; Chordal ring generator; Circulant graph generator; Circular ladder graph; Generalized petersen graph; Generalized Petersen graph generator; and 3 more.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Chordal cycle graph](#cat_chordal_cycle) | `cat_chordal_cycle` | 1 |
| [Chordal ring generator](#gen_chordal_ring) | `gen_chordal_ring` | 1 |
| [Circulant graph generator](#gen_circulant) | `gen_circulant` | 2 |
| [Circular ladder graph](#cat_circular_ladder) | `cat_circular_ladder` | 1 |
| [Generalized petersen graph](#cat_generalized_petersen) | `cat_generalized_petersen` | 2 |
| [Generalized Petersen graph generator](#gen_generalized_petersen) | `gen_generalized_petersen` | 1 |
| [Hkn harary graph](#cat_harary_hkn) | `cat_harary_hkn` | 1 |
| [Hnm harary graph](#cat_harary_hnm) | `cat_harary_hnm` | 1 |
| [Implicit family](#implicit_family) | `implicit_family` | 1 |

## Chordal cycle graph {#cat_chordal_cycle}

Measure id: `cat_chordal_cycle`. Original family: Generators and rewiring.

**Definition.** Chordal cycle graph.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `chordal_cycle_graph` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Chordal ring generator {#gen_chordal_ring}

Measure id: `gen_chordal_ring`. Original family: Generators and rewiring.

**Definition.** Chordal ring generator.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `chordal_ring; make_chordal_ring` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Circulant graph generator {#gen_circulant}

Measure id: `gen_circulant`. Original family: Generators and rewiring.

**Definition.** Circulant graph generator.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `circulant_graph` | API listing |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `circulant; make_circulant` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Circular ladder graph {#cat_circular_ladder}

Measure id: `cat_circular_ladder`. Original family: Generators and rewiring.

**Definition.** Circular ladder graph.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `circular_ladder_graph` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Generalized petersen graph {#cat_generalized_petersen}

Measure id: `cat_generalized_petersen`. Original family: Generators and rewiring.

**Definition.** Generalized petersen graph.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `generalized_petersen_graph` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `generalized_petersen_graph` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)

## Generalized Petersen graph generator {#gen_generalized_petersen}

Measure id: `gen_generalized_petersen`. Original family: Generators and rewiring.

**Definition.** Generalized Petersen graph generator.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `GeneralizedPetersenGraphGenerator` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Hkn harary graph {#cat_harary_hkn}

Measure id: `cat_harary_hkn`. Original family: Generators and rewiring.

**Definition.** Hkn harary graph.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `hkn_harary_graph` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Hnm harary graph {#cat_harary_hnm}

Measure id: `cat_harary_hnm`. Original family: Generators and rewiring.

**Definition.** Hnm harary graph.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `hnm_harary_graph` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Implicit family {#implicit_family}

Measure id: `implicit_family`. Original family: Graph theory and combinatorics.

**Definition.** Implicit family.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ∅ checked, no value on some inputs |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `implicit_circulant` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.circulant_graph(n, offsets)` |  |
| `implicit_complete_bipartite` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.complete_bipartite_graph(a, b)` |  |
| `implicit_complete_bipartite_dir` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.complete_bipartite_graph(a, b), oriented from the first part` |  |
| `implicit_complete_multipartite` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.complete_multipartite_graph(*sizes)` |  |
| `implicit_de_bruijn` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `iterated nx.line_graph of the complete digraph with loops` |  |
| `implicit_hypercube` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.hypercube_graph(d), tuple read as an integer` |  |
| `implicit_kautz` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `iterated nx.line_graph of the complete digraph` |  |
| `implicit_path` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.path_graph(n)` |  |
| `implicit_path_dir` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.path_graph(n, create_using=nx.DiGraph)` |  |
| `implicit_star` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.star_graph(n)` |  |
| `implicit_wheel` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.wheel_graph(n)` |  |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F034](../../findings.html#f034) | NetworkX | convention | hypercube\_graph nodes are bit tuples; dimension 0 is the null graph |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
