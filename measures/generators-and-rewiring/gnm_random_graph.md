---
title: "G(n, m) random graph"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# G(n, m) random graph {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Classic random graphs. Concept id: `gnm_random_graph`. 2 measures.

## Definition {#concept-definition}

G(n, m) random graph. Entries grouped here: G(n, m) random graph; Gnm.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [G(n, m) random graph](#gen_gnm) | `gen_gnm` | 5 |
| [Gnm](#cat_gnm) | `cat_gnm` | 1 |

## G(n, m) random graph {#gen_gnm}

Measure id: `gen_gnm`. Original family: Generators and rewiring.

**Definition.** G(n, m) random graph.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `dense_gnm_random_graph; gnm_random_graph; gnmk_random_graph` | documentation |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `sample_gnm` | documentation |
| [sna](../../tools/sna.html) | · reported in docs | `rgnm` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `directed_gnm_random_graph; undirected_gnm_random_graph` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `GnmRandomGraphGenerator` | API listing |

**Tools cited:** [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [tool_rustworkx](../../references.html#tool_rustworkx)

## Gnm {#cat_gnm}

Measure id: `cat_gnm`. Original family: Generators and rewiring.

**Definition.** Gnm.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `gnm` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
