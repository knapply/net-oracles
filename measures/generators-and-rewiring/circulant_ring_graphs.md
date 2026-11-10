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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_chordal_cycle-networkx) | `chordal_cycle_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_chordal_cycle-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: chordal\_cycle\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Chordal ring generator {#gen_chordal_ring}

Measure id: `gen_chordal_ring`. Original family: Generators and rewiring.

**Definition.** Chordal ring generator.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_chordal_ring-igraph) | `chordal_ring; make_chordal_ring` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_chordal_ring-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: chordal\_ring; make\_chordal\_ring.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Circulant graph generator {#gen_circulant}

Measure id: `gen_circulant`. Original family: Generators and rewiring.

**Definition.** Circulant graph generator.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_circulant-networkx) | `circulant_graph` | API listing |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_circulant-igraph) | `circulant; make_circulant` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_circulant-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: circulant\_graph.
- <a id="why-gen_circulant-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: circulant; make\_circulant.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Circular ladder graph {#cat_circular_ladder}

Measure id: `cat_circular_ladder`. Original family: Generators and rewiring.

**Definition.** Circular ladder graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_circular_ladder-networkx) | `circular_ladder_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_circular_ladder-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: circular\_ladder\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Generalized petersen graph {#cat_generalized_petersen}

Measure id: `cat_generalized_petersen`. Original family: Generators and rewiring.

**Definition.** Generalized petersen graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_generalized_petersen-networkx) | `generalized_petersen_graph` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_generalized_petersen-rustworkx) | `generalized_petersen_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_generalized_petersen-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: generalized\_petersen\_graph.
- <a id="why-cat_generalized_petersen-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: generalized\_petersen\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)

## Generalized Petersen graph generator {#gen_generalized_petersen}

Measure id: `gen_generalized_petersen`. Original family: Generators and rewiring.

**Definition.** Generalized Petersen graph generator.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_generalized_petersen-jgrapht) | `GeneralizedPetersenGraphGenerator` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_generalized_petersen-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: GeneralizedPetersenGraphGenerator.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Hkn harary graph {#cat_harary_hkn}

Measure id: `cat_harary_hkn`. Original family: Generators and rewiring.

**Definition.** Hkn harary graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_harary_hkn-networkx) | `hkn_harary_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_harary_hkn-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: hkn\_harary\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Hnm harary graph {#cat_harary_hnm}

Measure id: `cat_harary_hnm`. Original family: Generators and rewiring.

**Definition.** Hnm harary graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_harary_hnm-networkx) | `hnm_harary_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_harary_hnm-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: hnm\_harary\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Implicit family {#implicit_family}

Measure id: `implicit_family`. Original family: Graph theory and combinatorics.

**Definition.** Implicit family.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-nov" href="../../method.html#state-checked-no-value"><span class="g" aria-hidden="true">∅</span>checked, no value on some inputs</a> | Checked, no comparison counts recorded for this entry. *(reason incomplete)* [details](#why-implicit_family-networkx) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-implicit_family-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-nov" href="../../method.html#state-checked-no-value"><span class="g" aria-hidden="true">∅</span>checked, no value on some inputs</a> NetworkX 3.7 was run for this measure, but the survey's comparison report records no comparison counts (neither agreeing nor differing) for the entry, so the inputs on which the tool gives no value, and why, cannot be stated from the sources. What the sources do say: the cases are fixed and do not use the fixture graph; one fixture carries them. The comparison is restricted to the fixture(s): pair. Findings: [F034](../../findings.html#f034). **Reason incomplete:** The sources record no comparison counts (agreeing or differing) for this entry, so the inputs on which the tool gives no value, and why, cannot be stated.

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
