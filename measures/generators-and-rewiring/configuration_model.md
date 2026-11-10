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

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `configuration_model; directed_configuration_model; random_degree_sequence_graph` | documentation |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `sample_degseq` | documentation |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Degree_Sequence` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Degseq {#cat_degseq}

Measure id: `cat_degseq`. Original family: Graph theory and combinatorics.

**Definition.** Degseq.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `degseq` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
