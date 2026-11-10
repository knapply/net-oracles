---
title: "Graph description and exchange formats"
layout: default
parent: "Input and output"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Graph description and exchange formats {#concept-top}

Family: [Input and output](index.html). Subfamily: Graph description formats. Concept id: `graph_markup_io`. 14 measures.

## Definition {#concept-definition}

Graph description and exchange formats. Entries grouped here: DIMACS read and write; GEXF read and write; GML read and write; GRAPH6 read and write; GRAPHDB read and write; GraphML read and write; and 8 more.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [DIMACS read and write](#io_dimacs) | `io_dimacs` | 2 |
| [GEXF read and write](#io_gexf) | `io_gexf` | 4 |
| [GML read and write](#io_gml) | `io_gml` | 5 |
| [GRAPH6 read and write](#io_graph6) | `io_graph6` | 2 |
| [GRAPHDB read and write](#io_graphdb) | `io_graphdb` | 1 |
| [GraphML read and write](#io_graphml) | `io_graphml` | 6 |
| [GRAPHVIZ read and write](#io_graphviz) | `io_graphviz` | 3 |
| [LEDA read and write](#io_leda) | `io_leda` | 2 |
| [LEMON read and write](#io_lemon) | `io_lemon` | 1 |
| [Node-link JSON read and write](#io_json) | `io_json` | 2 |
| [NODELINKJSON read and write](#io_nodelinkjson) | `io_nodelinkjson` | 1 |
| [Pajek .net read and write](#io_pajek) | `io_pajek` | 3 |
| [SVG read and write](#io_svg) | `io_svg` | 1 |
| [TSPLIB read and write](#io_tsplib) | `io_tsplib` | 1 |

## DIMACS read and write {#io_dimacs}

Measure id: `io_dimacs`. Original family: Input and output.

**Definition.** DIMACS read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Read_DIMACS; write_dimacs` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `DIMACSEventDrivenImporter; DIMACSExporter; DIMACSImporter` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [michail2020jgrapht](../../references.html#michail2020jgrapht)

## GEXF read and write {#io_gexf}

Measure id: `io_gexf`. Original family: Input and output.

**Definition.** GEXF read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `generate_gexf; read_gexf; write_gexf` | documentation |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `GEXFReader; GEXFWriter` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `GEXFExporter; SimpleGEXFEventDrivenImporter; SimpleGEXFImporter` | API listing |
| [Gephi toolkit](../../tools/gephi.html) | · reported in docs |  | documentation |

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [staudt2016networkit](../../references.html#staudt2016networkit)

## GML read and write {#io_gml}

Measure id: `io_gml`. Original family: Input and output.

**Definition.** GML read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `generate_gml; parse_gml; read_gml; write_gml` | documentation |
| [igraph (R)](../../tools/igraph.html) | · reported in docs |  | documentation |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Read_GML; write_gml` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `GMLGraphReader; GMLGraphWriter` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `GmlEventDrivenImporter; GmlExporter; GmlImporter` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [staudt2016networkit](../../references.html#staudt2016networkit)

## GRAPH6 read and write {#io_graph6}

Measure id: `io_graph6`. Original family: Input and output.

**Definition.** GRAPH6 read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `from_graph6_bytes; from_sparse6_bytes; read_graph6; read_sparse6; to_graph6_bytes; to_sparse6_bytes; write_graph6; write_sparse6` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `Graph6Sparse6EventDrivenImporter; Graph6Sparse6Exporter; Graph6Sparse6Importer` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht)

## GRAPHDB read and write {#io_graphdb}

Measure id: `io_graphdb`. Original family: Input and output.

**Definition.** GRAPHDB read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Read_GraphDB` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## GraphML read and write {#io_graphml}

Measure id: `io_graphml`. Original family: Input and output.

**Definition.** GraphML read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `generate_graphml; parse_graphml; read_graphml; write_graphml_lxml; write_graphml_xml` | documentation |
| [igraph (R)](../../tools/igraph.html) | · reported in docs |  | documentation |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Read_GraphML; Read_GraphMLz; write_graphml; write_graphmlz` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `GraphMLReader; GraphMLWriter` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `read_graphml` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `GraphMLEventDrivenImporter; GraphMLExporter; GraphMLImporter; SimpleGraphMLEdgeListImporter; SimpleGraphMLEventDrivenImporter; SimpleGraphMLImporter` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)

## GRAPHVIZ read and write {#io_graphviz}

Measure id: `io_graphviz`. Original family: Input and output.

**Definition.** GRAPHVIZ read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `write_dot` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `DotGraphWriter` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `DOTEventDrivenImporter; DOTExporter; DOTImporter` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [michail2020jgrapht](../../references.html#michail2020jgrapht), [staudt2016networkit](../../references.html#staudt2016networkit)

## LEDA read and write {#io_leda}

Measure id: `io_leda`. Original family: Input and output.

**Definition.** LEDA read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `parse_leda; read_leda` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `write_leda` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## LEMON read and write {#io_lemon}

Measure id: `io_lemon`. Original family: Input and output.

**Definition.** LEMON read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `LemonExporter` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Node-link JSON read and write {#io_json}

Measure id: `io_json`. Original family: Input and output.

**Definition.** Node-link JSON read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  | documentation |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `JSONEventDrivenImporter; JSONExporter; JSONImporter` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht)

## NODELINKJSON read and write {#io_nodelinkjson}

Measure id: `io_nodelinkjson`. Original family: Input and output.

**Definition.** NODELINKJSON read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `from_node_link_json_file` | API listing |

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Pajek .net read and write {#io_pajek}

Measure id: `io_pajek`. Original family: Input and output.

**Definition.** Pajek .net read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `generate_pajek; parse_pajek; read_pajek; write_pajek` | documentation |
| [igraph (R)](../../tools/igraph.html) | · reported in docs |  | documentation |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Read_Pajek; write_pajek` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## SVG read and write {#io_svg}

Measure id: `io_svg`. Original family: Input and output.

**Definition.** SVG read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `write_svg` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## TSPLIB read and write {#io_tsplib}

Measure id: `io_tsplib`. Original family: Input and output.

**Definition.** TSPLIB read and write.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `TSPLIBImporter` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
