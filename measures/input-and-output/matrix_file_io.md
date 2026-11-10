---
title: "Matrix and spreadsheet formats"
layout: default
parent: "Input and output"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Matrix and spreadsheet formats {#concept-top}

Family: [Input and output](index.html). Subfamily: Matrix and spreadsheet formats. Concept id: `matrix_file_io`. 9 measures.

## Definition {#concept-definition}

Matrix and spreadsheet formats. Entries grouped here: Excel (xlsx) reader and writer; MATLAB read and write; MATRIX read and write; MATRIXMARKET read and write; MTX read and write; Multi-matrix DL, edgelist23, nodelist, ranklist, pilesort, VNA; and 3 more.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Excel (xlsx) reader and writer](#io_xlsx) | `io_xlsx` | 1 |
| [MATLAB read and write](#io_matlab) | `io_matlab` | 1 |
| [MATRIX read and write](#io_matrix) | `io_matrix` | 1 |
| [MATRIXMARKET read and write](#io_matrixmarket) | `io_matrixmarket` | 1 |
| [MTX read and write](#io_mtx) | `io_mtx` | 1 |
| [Multi-matrix DL, edgelist23, nodelist, ranklist, pilesort, VNA](#io_ucinet_multi) | `io_ucinet_multi` | 1 |
| [RB read and write](#io_rb) | `io_rb` | 1 |
| [UCINET binary dataset reader (.##h / .##d)](#io_ucinet_binary) | `io_ucinet_binary` | 1 |
| [UCINET DL text read and write](#io_dl) | `io_dl` | 2 |

## Excel (xlsx) reader and writer {#io_xlsx}

Measure id: `io_xlsx`. Original family: Input and output.

**Definition.** Excel (xlsx) reader and writer.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-io_xlsx-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_xlsx-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## MATLAB read and write {#io_matlab}

Measure id: `io_matlab`. Original family: Input and output.

**Definition.** MATLAB read and write.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-io_matlab-networkit) | `MatReader; MatWriter` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_matlab-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: MatReader; MatWriter.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## MATRIX read and write {#io_matrix}

Measure id: `io_matrix`. Original family: Input and output.

**Definition.** MATRIX read and write.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-io_matrix-jgrapht) | `MatrixExporter` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_matrix-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: MatrixExporter.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## MATRIXMARKET read and write {#io_matrixmarket}

Measure id: `io_matrixmarket`. Original family: Input and output.

**Definition.** MATRIXMARKET read and write.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-io_matrixmarket-rustworkx) | `read_matrix_market; read_matrix_market_file` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_matrixmarket-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: read\_matrix\_market; read\_matrix\_market\_file.

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## MTX read and write {#io_mtx}

Measure id: `io_mtx`. Original family: Input and output.

**Definition.** MTX read and write.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-io_mtx-networkit) | `MTXGraphReader` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_mtx-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: MTXGraphReader.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Multi-matrix DL, edgelist23, nodelist, ranklist, pilesort, VNA {#io_ucinet_multi}

Measure id: `io_ucinet_multi`. Original family: Input and output.

**Definition.** Multi-matrix DL, edgelist23, nodelist, ranklist, pilesort, VNA.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-io_ucinet_multi-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_ucinet_multi-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## RB read and write {#io_rb}

Measure id: `io_rb`. Original family: Input and output.

**Definition.** RB read and write.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-io_rb-networkit) | `RBGraphReader` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_rb-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: RBGraphReader.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## UCINET binary dataset reader (.##h / .##d) {#io_ucinet_binary}

Measure id: `io_ucinet_binary`. Original family: Input and output.

**Definition.** UCINET binary dataset reader (.##h / .##d).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-io_ucinet_binary-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_ucinet_binary-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## UCINET DL text read and write {#io_dl}

Measure id: `io_dl`. Original family: Input and output.

**Definition.** UCINET DL text read and write.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-io_dl-pyigraph) | `Read_DL` | API listing |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-io_dl-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_dl-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Read\_DL.
- <a id="why-io_dl-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
