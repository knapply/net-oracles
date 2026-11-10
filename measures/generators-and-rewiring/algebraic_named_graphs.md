---
title: "Algebraic and combinatorial named graphs (Kneser, Paley, Kautz, De Bruijn, LCF, Sudoku)"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Algebraic and combinatorial named graphs (Kneser, Paley, Kautz, De Bruijn, LCF, Sudoku) {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Named and deterministic graphs. Concept id: `algebraic_named_graphs`. 6 measures.

## Definition {#concept-definition}

Algebraic and combinatorial named graphs (Kneser, Paley, Kautz, De Bruijn, LCF, Sudoku). Entries grouped here: De Bruijn graph generator; Kautz graph generator; Kneser graph; LCF notation graph generator; Paley graph; Sudoku graph.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [De Bruijn graph generator](#gen_de_bruijn) | `gen_de_bruijn` | 2 |
| [Kautz graph generator](#gen_kautz) | `gen_kautz` | 2 |
| [Kneser graph](#cat_kneser) | `cat_kneser` | 1 |
| [LCF notation graph generator](#gen_lcf) | `gen_lcf` | 2 |
| [Paley graph](#cat_paley) | `cat_paley` | 1 |
| [Sudoku graph](#cat_sudoku) | `cat_sudoku` | 1 |

## De Bruijn graph generator {#gen_de_bruijn}

Measure id: `gen_de_bruijn`. Original family: Generators and rewiring.

**Definition.** De Bruijn graph generator.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `de_bruijn_graph; make_de_bruijn_graph` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `De_Bruijn` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Kautz graph generator {#gen_kautz}

Measure id: `gen_kautz`. Original family: Generators and rewiring.

**Definition.** Kautz graph generator.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `kautz_graph; make_kautz_graph` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Kautz` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Kneser graph {#cat_kneser}

Measure id: `cat_kneser`. Original family: Generators and rewiring.

**Definition.** Kneser graph.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `kneser_graph` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## LCF notation graph generator {#gen_lcf}

Measure id: `gen_lcf`. Original family: Generators and rewiring.

**Definition.** LCF notation graph generator.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `LCF_graph` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `LCF` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Paley graph {#cat_paley}

Measure id: `cat_paley`. Original family: Generators and rewiring.

**Definition.** Paley graph.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `paley_graph` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Sudoku graph {#cat_sudoku}

Measure id: `cat_sudoku`. Original family: Generators and rewiring.

**Definition.** Sudoku graph.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `sudoku_graph` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
