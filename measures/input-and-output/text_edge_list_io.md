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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-io_adjacency-pyigraph) | `Read_Adjacency` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_adjacency-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Read\_Adjacency.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## CSV read and write {#io_csv}

Measure id: `io_csv`. Original family: Input and output.

**Definition.** CSV read and write.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-io_csv-jgrapht) | `CSVEventDrivenImporter; CSVExporter; CSVImporter; VisioExporter` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_csv-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: CSVEventDrivenImporter; CSVExporter; CSVImporter; VisioExporter.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## EDGELIST read and write {#io_edgelist}

Measure id: `io_edgelist`. Original family: Input and output.

**Definition.** EDGELIST read and write.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-io_edgelist-networkx) | `generate_adjlist; generate_edgelist; parse_adjlist; parse_edgelist; read_adjlist; read_edgelist; write_adjlist; write_edgelist` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-io_edgelist-pyigraph) | `Read_Edgelist; write_edgelist` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-io_edgelist-networkit) | `EdgeListReader; EdgeListWriter` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_edgelist-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: generate\_adjlist; generate\_edgelist; parse\_adjlist; parse\_edgelist; read\_adjlist; read\_edgelist; write\_adjlist; write\_edgelist.
- <a id="why-io_edgelist-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Read\_Edgelist; write\_edgelist.
- <a id="why-io_edgelist-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: EdgeListReader; EdgeListWriter.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [staudt2016networkit](../../references.html#staudt2016networkit)

## Extra file formats: ncol, lgl, dimacs, graphdb, adjacency list {#io_text_formats}

Measure id: `io_text_formats`. Original family: Input and output.

**Definition.** Extra file formats: ncol, lgl, dimacs, graphdb, adjacency list.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's documentation; no comparison set up for this measure yet. [details](#why-io_text_formats-igraph) |  | documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_text_formats-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (R package igraph: exported functions and help titles).

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## KONECT read and write {#io_konect}

Measure id: `io_konect`. Original family: Input and output.

**Definition.** KONECT read and write.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-io_konect-networkit) | `KONECTGraphReader` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_konect-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: KONECTGraphReader.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## LGL read and write {#io_lgl}

Measure id: `io_lgl`. Original family: Input and output.

**Definition.** LGL read and write.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-io_lgl-pyigraph) | `Read_Lgl; write_lgl` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_lgl-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Read\_Lgl; write\_lgl.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## METIS read and write {#io_metis}

Measure id: `io_metis`. Original family: Input and output.

**Definition.** METIS read and write.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-io_metis-networkit) | `METISGraphReader; METISGraphWriter` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_metis-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: METISGraphReader; METISGraphWriter.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## NCOL read and write {#io_ncol}

Measure id: `io_ncol`. Original family: Input and output.

**Definition.** NCOL read and write.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-io_ncol-pyigraph) | `Read_Ncol; write_ncol` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_ncol-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Read\_Ncol; write\_ncol.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## SNAP read and write {#io_snap}

Measure id: `io_snap`. Original family: Input and output.

**Definition.** SNAP read and write.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-io_snap-networkit) | `SNAPGraphReader; SNAPGraphWriter` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_snap-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: SNAPGraphReader; SNAPGraphWriter.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
