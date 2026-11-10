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

*Definition not yet written.* The sources list edge-list, adjacency-list, CSV, KONECT, LGL, METIS, NCOL and SNAP text readers and writers by name only (documented tools, never run); no specification of any of these formats is among the sources.

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#io_adjacency">ADJACENCY read and write</a></td><td><code>io_adjacency</code></td><td>1</td></tr><tr><td><a href="#io_csv">CSV read and write</a></td><td><code>io_csv</code></td><td>1</td></tr><tr><td><a href="#io_edgelist">EDGELIST read and write</a></td><td><code>io_edgelist</code></td><td>3</td></tr><tr><td><a href="#io_text_formats">Extra file formats: ncol, lgl, dimacs, graphdb, adjacency list</a></td><td><code>io_text_formats</code></td><td>1</td></tr><tr><td><a href="#io_konect">KONECT read and write</a></td><td><code>io_konect</code></td><td>1</td></tr><tr><td><a href="#io_lgl">LGL read and write</a></td><td><code>io_lgl</code></td><td>1</td></tr><tr><td><a href="#io_metis">METIS read and write</a></td><td><code>io_metis</code></td><td>1</td></tr><tr><td><a href="#io_ncol">NCOL read and write</a></td><td><code>io_ncol</code></td><td>1</td></tr><tr><td><a href="#io_snap">SNAP read and write</a></td><td><code>io_snap</code></td><td>1</td></tr></tbody></table></div>

## ADJACENCY read and write {#io_adjacency}

Measure id: `io_adjacency`. Original family: Input and output.

**Definition.** ADJACENCY read and write.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-io_adjacency-pyigraph">details</a></td><td><code>Read_Adjacency</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_adjacency-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Read\_Adjacency.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## CSV read and write {#io_csv}

Measure id: `io_csv`. Original family: Input and output.

**Definition.** CSV read and write.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-io_csv-jgrapht">details</a></td><td><code>CSVEventDrivenImporter; CSVExporter; CSVImporter; VisioExporter</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_csv-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: CSVEventDrivenImporter; CSVExporter; CSVImporter; VisioExporter.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## EDGELIST read and write {#io_edgelist}

Measure id: `io_edgelist`. Original family: Input and output.

**Definition.** EDGELIST read and write.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-io_edgelist-networkx">details</a></td><td><code>generate_adjlist; generate_edgelist; parse_adjlist; parse_edgelist; read_adjlist; read_edgelist; write_adjlist; write_edgelist</code></td><td>API listing</td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-io_edgelist-pyigraph">details</a></td><td><code>Read_Edgelist; write_edgelist</code></td><td>API listing</td></tr><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-io_edgelist-networkit">details</a></td><td><code>EdgeListReader; EdgeListWriter</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_edgelist-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: generate\_adjlist; generate\_edgelist; parse\_adjlist; parse\_edgelist; read\_adjlist; read\_edgelist; write\_adjlist; write\_edgelist.
- <a id="why-io_edgelist-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Read\_Edgelist; write\_edgelist.
- <a id="why-io_edgelist-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: EdgeListReader; EdgeListWriter.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [staudt2016networkit](../../references.html#staudt2016networkit)

## Extra file formats: ncol, lgl, dimacs, graphdb, adjacency list {#io_text_formats}

Measure id: `io_text_formats`. Original family: Input and output.

**Definition.** Extra file formats: ncol, lgl, dimacs, graphdb, adjacency list.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's documentation; no comparison set up for this measure yet. <a href="#why-io_text_formats-igraph">details</a></td><td></td><td>documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_text_formats-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (R package igraph: exported functions and help titles).

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## KONECT read and write {#io_konect}

Measure id: `io_konect`. Original family: Input and output.

**Definition.** KONECT read and write.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-io_konect-networkit">details</a></td><td><code>KONECTGraphReader</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_konect-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: KONECTGraphReader.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## LGL read and write {#io_lgl}

Measure id: `io_lgl`. Original family: Input and output.

**Definition.** LGL read and write.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-io_lgl-pyigraph">details</a></td><td><code>Read_Lgl; write_lgl</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_lgl-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Read\_Lgl; write\_lgl.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## METIS read and write {#io_metis}

Measure id: `io_metis`. Original family: Input and output.

**Definition.** METIS read and write.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-io_metis-networkit">details</a></td><td><code>METISGraphReader; METISGraphWriter</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_metis-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: METISGraphReader; METISGraphWriter.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## NCOL read and write {#io_ncol}

Measure id: `io_ncol`. Original family: Input and output.

**Definition.** NCOL read and write.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-io_ncol-pyigraph">details</a></td><td><code>Read_Ncol; write_ncol</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_ncol-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Read\_Ncol; write\_ncol.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## SNAP read and write {#io_snap}

Measure id: `io_snap`. Original family: Input and output.

**Definition.** SNAP read and write.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-io_snap-networkit">details</a></td><td><code>SNAPGraphReader; SNAPGraphWriter</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_snap-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: SNAPGraphReader; SNAPGraphWriter.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
