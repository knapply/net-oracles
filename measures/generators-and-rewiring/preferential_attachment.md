---
title: "Preferential attachment"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Preferential attachment {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Growth and attachment models. Concept id: `preferential_attachment`. 4 measures.

## Definition {#concept-definition}

Preferential attachment. Entries grouped here: Pa; Pa age; Preferential attachment generator; Preferential attachment graph (bipartite).

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Pa](#cat_pa) | `cat_pa` | 1 |
| [Pa age](#cat_age_pa) | `cat_age_pa` | 1 |
| [Preferential attachment generator](#gen_preferential) | `gen_preferential` | 7 |
| [Preferential attachment graph (bipartite)](#cat_attachment_preferential-bipartite) | `cat_attachment_preferential@bipartite` | 1 |

## Pa {#cat_pa}

Measure id: `cat_pa`. Original family: Graph theory and combinatorics.

**Definition.** Pa.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `pa` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Pa age {#cat_age_pa}

Measure id: `cat_age_pa`. Original family: Graph theory and combinatorics.

**Definition.** Pa age.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `pa_age` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Preferential attachment generator {#gen_preferential}

Measure id: `gen_preferential`. Original family: Generators and rewiring.

**Definition.** Preferential attachment generator.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `barabasi_albert_graph; dual_barabasi_albert_graph; extended_barabasi_albert_graph; scale_free_graph` | documentation |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `sample_pa; sample_pa_age` | documentation |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Barabasi; Recent_Degree` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `price_network` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `BarabasiAlbertGenerator` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `barabasi_albert_graph; directed_barabasi_albert_graph` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `BarabasiAlbertForestGenerator; BarabasiAlbertGraphGenerator; DirectedScaleFreeGraphGenerator; ScaleFreeGraphGenerator` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)

## Preferential attachment graph (bipartite) {#cat_attachment_preferential-bipartite}

Measure id: `cat_attachment_preferential@bipartite`. Original family: Generators and rewiring.

**Definition.** Preferential attachment graph (bipartite).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `preferential_attachment_graph` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
