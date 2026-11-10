---
title: "GML read and write"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# GML read and write

Family: Input and output. Identifier: `io_gml`.

## Definition

GML read and write.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `generate_gml; parse_gml; read_gml; write_gml` | documentation |
| [igraph (R)](../tools/igraph.html) | · reported in docs |  | documentation |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `Read_GML; write_gml` | API listing |
| [NetworKit](../tools/networkit.html) | · reported in docs | `GMLGraphReader; GMLGraphWriter` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `GmlEventDrivenImporter; GmlExporter; GmlImporter` | API listing |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [staudt2016networkit](../references.html#staudt2016networkit)
{% endraw %}
