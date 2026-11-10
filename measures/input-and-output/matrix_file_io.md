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

| Tool | State | API names | Source |
|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## MATLAB read and write {#io_matlab}

Measure id: `io_matlab`. Original family: Input and output.

**Definition.** MATLAB read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | · reported in docs | `MatReader; MatWriter` | API listing |

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## MATRIX read and write {#io_matrix}

Measure id: `io_matrix`. Original family: Input and output.

**Definition.** MATRIX read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `MatrixExporter` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## MATRIXMARKET read and write {#io_matrixmarket}

Measure id: `io_matrixmarket`. Original family: Input and output.

**Definition.** MATRIXMARKET read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `read_matrix_market; read_matrix_market_file` | API listing |

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## MTX read and write {#io_mtx}

Measure id: `io_mtx`. Original family: Input and output.

**Definition.** MTX read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | · reported in docs | `MTXGraphReader` | API listing |

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Multi-matrix DL, edgelist23, nodelist, ranklist, pilesort, VNA {#io_ucinet_multi}

Measure id: `io_ucinet_multi`. Original family: Input and output.

**Definition.** Multi-matrix DL, edgelist23, nodelist, ranklist, pilesort, VNA.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## RB read and write {#io_rb}

Measure id: `io_rb`. Original family: Input and output.

**Definition.** RB read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | · reported in docs | `RBGraphReader` | API listing |

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## UCINET binary dataset reader (.##h / .##d) {#io_ucinet_binary}

Measure id: `io_ucinet_binary`. Original family: Input and output.

**Definition.** UCINET binary dataset reader (.##h / .##d).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## UCINET DL text read and write {#io_dl}

Measure id: `io_dl`. Original family: Input and output.

**Definition.** UCINET DL text read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Read_DL` | API listing |
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
