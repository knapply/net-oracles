---
title: "G(n, p) random graph"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# G(n, p) random graph {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Classic random graphs. Concept id: `gnp_random_graph`. 2 measures.

## Definition {#concept-definition}

G(n, p) random graph. Entries grouped here: G(n, p) random graph; Gnp.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [G(n, p) random graph](#gen_gnp) | `gen_gnp` | 9 |
| [Gnp](#cat_gnp) | `cat_gnp` | 1 |

## G(n, p) random graph {#gen_gnp}

Measure id: `gen_gnp`. Original family: Generators and rewiring.

**Definition.** G(n, p) random graph.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `fast_gnp_random_graph; gnp_random_graph` | documentation |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `sample_gnp` | documentation |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Erdos_Renyi` | API listing |
| [sna](../../tools/sna.html) | · reported in docs | `rgraph` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `ErdosRenyiGenerator` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `directed_gnp_random_graph; undirected_gnp_random_graph` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `GnpRandomGraphGenerator` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `erdos_renyi_generator; erdos_renyi_iterator; sorted_erdos_renyi_iterator` | API listing |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `ER; Random matrix generators (Erdos-Renyi, etc.)` | API listing |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)

## Gnp {#cat_gnp}

Measure id: `cat_gnp`. Original family: Generators and rewiring.

**Definition.** Gnp.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `gnp` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
