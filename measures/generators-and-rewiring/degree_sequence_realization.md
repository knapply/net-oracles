---
title: "Deterministic degree-sequence realization"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Deterministic degree-sequence realization {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Degree-sequence models. Concept id: `degree_sequence_realization`. 3 measures.

## Definition {#concept-definition}

Deterministic degree-sequence realization. Entries grouped here: Bipartite degree-sequence realization; Deterministic realisation of a degree sequence; Havel Hakimi Generator.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Bipartite degree-sequence realization](#gen_realize_bipartite) | `gen_realize_bipartite` | 2 |
| [Deterministic realisation of a degree sequence](#gen_degree_realization) | `gen_degree_realization` | 3 |
| [Havel Hakimi Generator](#cat_generator_hakimi_havel) | `cat_generator_hakimi_havel` | 1 |

## Bipartite degree-sequence realization {#gen_realize_bipartite}

Measure id: `gen_realize_bipartite`. Original family: Generators and rewiring.

**Definition.** Bipartite degree-sequence realization.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `realize_bipartite_degseq` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Realize_Bipartite_Degree_Sequence` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Deterministic realisation of a degree sequence {#gen_degree_realization}

Measure id: `gen_degree_realization`. Original family: Generators and rewiring.

**Definition.** Deterministic realisation of a degree sequence.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `alternating_havel_hakimi_graph; directed_havel_hakimi_graph; havel_hakimi_graph; reverse_havel_hakimi_graph` | API listing |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `realize_degseq` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Realize_Degree_Sequence` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Havel Hakimi Generator {#cat_generator_hakimi_havel}

Measure id: `cat_generator_hakimi_havel`. Original family: Generators and rewiring.

**Definition.** Havel Hakimi Generator.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | · reported in docs | `HavelHakimiGenerator` | API listing |

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
