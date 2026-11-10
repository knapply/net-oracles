---
title: "GraphML read and write"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# GraphML read and write

Family: Input and output. Identifier: `io_graphml`.

## Definition

GraphML read and write.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `generate_graphml; parse_graphml; read_graphml; write_graphml_lxml; write_graphml_xml` | documentation |
| [igraph (R)](../tools/igraph.html) | · reported in docs |  | documentation |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `Read_GraphML; Read_GraphMLz; write_graphml; write_graphmlz` | API listing |
| [NetworKit](../tools/networkit.html) | · reported in docs | `GraphMLReader; GraphMLWriter` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `read_graphml` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `GraphMLEventDrivenImporter; GraphMLExporter; GraphMLImporter; SimpleGraphMLEdgeListImporter; SimpleGraphMLEventDrivenImporter; SimpleGraphMLImporter` | API listing |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
