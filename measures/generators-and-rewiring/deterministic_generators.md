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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `balanced_tree; complete_bipartite_graph; complete_graph; cycle_graph; empty_graph; full_rary_tree; hypercube_graph; ladder_graph; null_graph; path_graph; star_graph; trivial_graph` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-deterministic_generators-igraph) | `empty_graph; make_empty_graph; make_full_bipartite_graph; make_full_graph; make_ring; make_star; make_tree; make_wheel; ring; star; tree; wheel` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-deterministic_generators-pyigraph) | `Full; Full_Bipartite; Hypercube; Ring; Star; Tree` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-deterministic_generators-graphtool) | `circular_graph; complete_graph` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-deterministic_generators-rustworkx) | `complete_graph; cycle_graph; directed_complete_graph; directed_cycle_graph; directed_empty_graph; directed_path_graph; directed_star_graph; empty_graph; full_rary_tree; path_graph; star_graph` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-deterministic_generators-jgrapht) | `CompleteBipartiteGraphGenerator; CompleteGraphGenerator; EmptyGraphGenerator; HyperCubeGraphGenerator; LinearGraphGenerator; RingGraphGenerator; StarGraphGenerator; WheelGraphGenerator` | API listing |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-deterministic_generators-ucinet) | `cycle; makeclique; path; star` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-deterministic_generators-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: empty\_graph; make\_empty\_graph; make\_full\_bipartite\_graph; make\_full\_graph; make\_ring; make\_star; make\_tree; make\_wheel; ring; star; tree; wheel.
- <a id="why-deterministic_generators-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Full; Full\_Bipartite; Hypercube; Ring; Star; Tree.
- <a id="why-deterministic_generators-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: circular\_graph; complete\_graph.
- <a id="why-deterministic_generators-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: complete\_graph; cycle\_graph; directed\_complete\_graph; directed\_cycle\_graph; directed\_empty\_graph; directed\_path\_graph; directed\_star\_graph; empty\_graph; full\_rary\_tree; path\_graph; star\_graph.
- <a id="why-deterministic_generators-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: CompleteBipartiteGraphGenerator; CompleteGraphGenerator; EmptyGraphGenerator; HyperCubeGraphGenerator; LinearGraphGenerator; RingGraphGenerator; StarGraphGenerator; WheelGraphGenerator.
- <a id="why-deterministic_generators-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

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
