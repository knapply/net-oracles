---
title: "Stochastic block model generator"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Stochastic block model generator {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Block models. Concept id: `sbm_generator`. 2 measures.

## Definition {#concept-definition}

Stochastic block model generator. Entries grouped here: Sbm random graph; Stochastic block model generator.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Sbm random graph](#cat_random_sbm) | `cat_random_sbm` | 1 |
| [Stochastic block model generator](#gen_sbm) | `gen_sbm` | 8 |

## Sbm random graph {#cat_random_sbm}

Measure id: `cat_random_sbm`. Original family: Generators and rewiring.

**Definition.** Sbm random graph.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `directed_sbm_random_graph` | API listing |

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Stochastic block model generator {#gen_sbm}

Measure id: `gen_sbm`. Original family: Generators and rewiring.

**Definition.** Stochastic block model generator.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `LFR_benchmark_graph; gaussian_random_partition_graph; planted_partition_graph; random_partition_graph; stochastic_block_model` | documentation |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `hierarchical_sbm; sample_hierarchical_sbm; sample_sbm; sbm` | documentation |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `SBM` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `generate_maxent_sbm; generate_sbm; solve_sbm_fugacities` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `ClusteredRandomGraphGenerator` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `undirected_sbm_random_graph` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `PlantedPartitionGraphGenerator` | API listing |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `makeclumpy` | API listing |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
