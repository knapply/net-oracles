---
title: "Configuration model"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Configuration model {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Degree-sequence models. Concept id: `configuration_model`. 2 measures.

## Definition {#concept-definition}

Configuration model. Entries grouped here: Configuration model; Degseq.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Configuration model](#gen_configuration) | `gen_configuration` | 3 |
| [Degseq](#cat_degseq) | `cat_degseq` | 1 |

## Configuration model {#gen_configuration}

Measure id: `gen_configuration`. Original family: Generators and rewiring.

**Definition.** Configuration model.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's documentation; no comparison set up for this measure yet. [details](#why-gen_configuration-networkx) | `configuration_model; directed_configuration_model; random_degree_sequence_graph` | documentation |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's documentation; no comparison set up for this measure yet. [details](#why-gen_configuration-igraph) | `sample_degseq` | documentation |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_configuration-pyigraph) | `Degree_Sequence` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_configuration-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (networkx public API (algorithms, generators, linalg, readwrite)); API names: configuration\_model; directed\_configuration\_model; random\_degree\_sequence\_graph.
- <a id="why-gen_configuration-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (R package igraph: exported functions and help titles); API names: sample\_degseq.
- <a id="why-gen_configuration-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Degree\_Sequence.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Degseq {#cat_degseq}

Measure id: `cat_degseq`. Original family: Graph theory and combinatorics.

**Definition.** Degseq.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_degseq-igraph) | `degseq` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_degseq-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: degseq.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
