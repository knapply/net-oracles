---
title: "Edge-list and adjacency-list text formats"
layout: default
parent: "Input and output"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Edge-list and adjacency-list text formats {#concept-top}

Family: [Input and output](index.html). Subfamily: Edge-list and adjacency-list formats. Concept id: `text_edge_list_io`. 9 measures.

## Definition {#concept-definition}

Edge-list and adjacency-list text formats. Entries grouped here: ADJACENCY read and write; CSV read and write; EDGELIST read and write; Extra file formats: ncol, lgl, dimacs, graphdb, adjacency list; KONECT read and write; LGL read and write; and 3 more.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [ADJACENCY read and write](#io_adjacency) | `io_adjacency` | 1 |
| [CSV read and write](#io_csv) | `io_csv` | 1 |
| [EDGELIST read and write](#io_edgelist) | `io_edgelist` | 3 |
| [Extra file formats: ncol, lgl, dimacs, graphdb, adjacency list](#io_text_formats) | `io_text_formats` | 1 |
| [KONECT read and write](#io_konect) | `io_konect` | 1 |
| [LGL read and write](#io_lgl) | `io_lgl` | 1 |
| [METIS read and write](#io_metis) | `io_metis` | 1 |
| [NCOL read and write](#io_ncol) | `io_ncol` | 1 |
| [SNAP read and write](#io_snap) | `io_snap` | 1 |

## ADJACENCY read and write {#io_adjacency}

Measure id: `io_adjacency`. Original family: Input and output.

**Definition.** ADJACENCY read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Read_Adjacency` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## CSV read and write {#io_csv}

Measure id: `io_csv`. Original family: Input and output.

**Definition.** CSV read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `CSVEventDrivenImporter; CSVExporter; CSVImporter; VisioExporter` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## EDGELIST read and write {#io_edgelist}

Measure id: `io_edgelist`. Original family: Input and output.

**Definition.** EDGELIST read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `generate_adjlist; generate_edgelist; parse_adjlist; parse_edgelist; read_adjlist; read_edgelist; write_adjlist; write_edgelist` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Read_Edgelist; write_edgelist` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `EdgeListReader; EdgeListWriter` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [staudt2016networkit](../../references.html#staudt2016networkit)

## Extra file formats: ncol, lgl, dimacs, graphdb, adjacency list {#io_text_formats}

Measure id: `io_text_formats`. Original family: Input and output.

**Definition.** Extra file formats: ncol, lgl, dimacs, graphdb, adjacency list.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs |  | documentation |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## KONECT read and write {#io_konect}

Measure id: `io_konect`. Original family: Input and output.

**Definition.** KONECT read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | · reported in docs | `KONECTGraphReader` | API listing |

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## LGL read and write {#io_lgl}

Measure id: `io_lgl`. Original family: Input and output.

**Definition.** LGL read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Read_Lgl; write_lgl` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## METIS read and write {#io_metis}

Measure id: `io_metis`. Original family: Input and output.

**Definition.** METIS read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | · reported in docs | `METISGraphReader; METISGraphWriter` | API listing |

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## NCOL read and write {#io_ncol}

Measure id: `io_ncol`. Original family: Input and output.

**Definition.** NCOL read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Read_Ncol; write_ncol` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## SNAP read and write {#io_snap}

Measure id: `io_snap`. Original family: Input and output.

**Definition.** SNAP read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | · reported in docs | `SNAPGraphReader; SNAPGraphWriter` | API listing |

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
