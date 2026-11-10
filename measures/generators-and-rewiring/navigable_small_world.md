---
title: "Navigable small-world graph"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Navigable small-world graph {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Small-world, lattice and geometric models. Concept id: `navigable_small_world`. 2 measures.

## Definition {#concept-definition}

Navigable small-world graph. Entries grouped here: Navigable small world graph; Navigable small-world generator.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Navigable small world graph](#cat_navigable_small_world) | `cat_navigable_small_world` | 1 |
| [Navigable small-world generator](#gen_navigable_small_world) | `gen_navigable_small_world` | 1 |

## Navigable small world graph {#cat_navigable_small_world}

Measure id: `cat_navigable_small_world`. Original family: Generators and rewiring.

**Definition.** Navigable small world graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_navigable_small_world-networkx) | `navigable_small_world_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_navigable_small_world-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: navigable\_small\_world\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Navigable small-world generator {#gen_navigable_small_world}

Measure id: `gen_navigable_small_world`. Original family: Generators and rewiring.

**Definition.** Navigable small-world generator.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_navigable_small_world-jgrapht) | `KleinbergSmallWorldGraphGenerator` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_navigable_small_world-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: KleinbergSmallWorldGraphGenerator.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
