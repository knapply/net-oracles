---
title: "Clique composites (barbell, lollipop, tadpole, windmill, caveman, ring of cliques)"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Clique composites (barbell, lollipop, tadpole, windmill, caveman, ring of cliques) {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Named and deterministic graphs. Concept id: `clique_composite_graphs`. 10 measures.

## Definition {#concept-definition}

Clique composites (barbell, lollipop, tadpole, windmill, caveman, ring of cliques). Entries grouped here: Barbell graph; Caveman graph; Connected caveman graph; Lollipop graph; Make max clique graph; Relaxed caveman graph; and 4 more.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Barbell graph](#cat_barbell) | `cat_barbell` | 2 |
| [Caveman graph](#cat_caveman) | `cat_caveman` | 1 |
| [Connected caveman graph](#cat_caveman_connected) | `cat_caveman_connected` | 1 |
| [Lollipop graph](#cat_lollipop) | `cat_lollipop` | 2 |
| [Make max clique graph](#cat_clique_make_max) | `cat_clique_make_max` | 1 |
| [Relaxed caveman graph](#cat_caveman_relaxed) | `cat_caveman_relaxed` | 1 |
| [Ring of cliques](#cat_clique_ring) | `cat_clique_ring` | 1 |
| [Tadpole graph](#cat_tadpole) | `cat_tadpole` | 1 |
| [Windmill graph](#cat_windmill) | `cat_windmill` | 1 |
| [Windmill graph generator](#gen_windmill) | `gen_windmill` | 1 |

## Barbell graph {#cat_barbell}

Measure id: `cat_barbell`. Original family: Generators and rewiring.

**Definition.** Barbell graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_barbell-networkx) | `barbell_graph` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_barbell-rustworkx) | `barbell_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_barbell-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: barbell\_graph.
- <a id="why-cat_barbell-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: barbell\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)

## Caveman graph {#cat_caveman}

Measure id: `cat_caveman`. Original family: Generators and rewiring.

**Definition.** Caveman graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_caveman-networkx) | `caveman_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_caveman-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: caveman\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Connected caveman graph {#cat_caveman_connected}

Measure id: `cat_caveman_connected`. Original family: Generators and rewiring.

**Definition.** Connected caveman graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_caveman_connected-networkx) | `connected_caveman_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_caveman_connected-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: connected\_caveman\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Lollipop graph {#cat_lollipop}

Measure id: `cat_lollipop`. Original family: Generators and rewiring.

**Definition.** Lollipop graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_lollipop-networkx) | `lollipop_graph` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_lollipop-rustworkx) | `lollipop_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_lollipop-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: lollipop\_graph.
- <a id="why-cat_lollipop-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: lollipop\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)

## Make max clique graph {#cat_clique_make_max}

Measure id: `cat_clique_make_max`. Original family: Generators and rewiring.

**Definition.** Make max clique graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_clique_make_max-networkx) | `make_max_clique_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_clique_make_max-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: make\_max\_clique\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Relaxed caveman graph {#cat_caveman_relaxed}

Measure id: `cat_caveman_relaxed`. Original family: Generators and rewiring.

**Definition.** Relaxed caveman graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_caveman_relaxed-networkx) | `relaxed_caveman_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_caveman_relaxed-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: relaxed\_caveman\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Ring of cliques {#cat_clique_ring}

Measure id: `cat_clique_ring`. Original family: Generators and rewiring.

**Definition.** Ring of cliques.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_clique_ring-networkx) | `ring_of_cliques` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_clique_ring-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: ring\_of\_cliques.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Tadpole graph {#cat_tadpole}

Measure id: `cat_tadpole`. Original family: Generators and rewiring.

**Definition.** Tadpole graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_tadpole-networkx) | `tadpole_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_tadpole-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: tadpole\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Windmill graph {#cat_windmill}

Measure id: `cat_windmill`. Original family: Generators and rewiring.

**Definition.** Windmill graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_windmill-networkx) | `windmill_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_windmill-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: windmill\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Windmill graph generator {#gen_windmill}

Measure id: `gen_windmill`. Original family: Generators and rewiring.

**Definition.** Windmill graph generator.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_windmill-jgrapht) | `WindmillGraphsGenerator` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_windmill-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: WindmillGraphsGenerator.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
