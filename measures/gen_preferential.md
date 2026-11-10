---
title: "Preferential attachment generator"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Preferential attachment generator

Family: Generators and rewiring. Identifier: `gen_preferential`.

## Definition

Preferential attachment generator.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | · reported in docs | `barabasi_albert_graph; dual_barabasi_albert_graph; extended_barabasi_albert_graph; scale_free_graph` | documentation |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `sample_pa; sample_pa_age` | documentation |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `Barabasi; Recent_Degree` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `price_network` | API listing |
| [NetworKit](../tools/networkit.html) | · reported in docs | `BarabasiAlbertGenerator` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `barabasi_albert_graph; directed_barabasi_albert_graph` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `BarabasiAlbertForestGenerator; BarabasiAlbertGraphGenerator; DirectedScaleFreeGraphGenerator; ScaleFreeGraphGenerator` | API listing |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
