---
title: "Louvain modularity"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Louvain modularity

Family: Communities. Identifier: `louvain_modularity`.

## Definition

Louvain communities of an undirected network by greedy modularity moves and aggregation.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention | `louvain_communities; louvain_partitions` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `cluster_louvain` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `community_multilevel` | API listing |
| [NetworKit](../tools/networkit.html) | · reported in docs | `LouvainMapEquation; PLM` | API listing |
| [scikit-network](../tools/sknetwork.html) | · reported in docs | `Louvain` | API listing |
| [BCT (Octave)](../tools/bct.html) | · reported in docs | `community_louvain; modularity_finetune_dir; modularity_finetune_und; modularity_finetune_und_sign; modularity_louvain_dir; modularity_louvain_und; modularity_louvain_und_sign; modularity_probtune_und_sign` | API listing |
| [UCINET](../tools/ucinet.html) | · reported in docs |  | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `louvain_modularity` | NetworkX | undirected | differs | edge\_case | defaults | abs 1e-14, rel 1e-12 | `nx.community.modularity(G, reference partition, weight = None)` | NetworkX returns 0 for a network without edges; this reference returns NaN. |
| `louvain_modularity_resolution` | NetworkX | undirected | differs | edge\_case | defaults | abs 1e-14, rel 1e-12 | `nx.community.modularity(G, reference partition, resolution = 0.5)` | NetworkX returns 0 for a network without edges; this reference returns NaN. |
| `louvain_modularity_weighted` | NetworkX | undirected | differs | edgeless | defaults | abs 1e-14, rel 1e-12 | `nx.community.modularity(G, reference partition, weight = 'weight')` | Without edges modularity is 0 / 0; NetworkX returns 0, the reference NaN. |

## References

[blondel2008fast](../references.html#blondel2008fast), [dugue2015directed](../references.html#dugue2015directed), [leicht2008community](../references.html#leicht2008community), [newman2004analysis](../references.html#newman2004analysis), [newman2004finding](../references.html#newman2004finding), [newman2006modularity](../references.html#newman2006modularity), [reichardt2006statistical](../references.html#reichardt2006statistical), [traag2019louvain](../references.html#traag2019louvain)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [rubinov2010complex](../references.html#rubinov2010complex), [staudt2016networkit](../references.html#staudt2016networkit), [tool_sknetwork](../references.html#tool_sknetwork)
{% endraw %}
