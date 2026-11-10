---
title: "Local reaching centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Local reaching centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `local_reaching_centrality`. 1 measure.

## Definition {#concept-definition}

Global reaching centrality of a network (Mones et al.): the mean gap between the largest local reaching centrality and every node's, divided by n - 1.

## References {#concept-references}

[johnson2014trophic](../../references.html#johnson2014trophic), [levine1980several](../../references.html#levine1980several), [mones2012hierarchy](../../references.html#mones2012hierarchy), [tarjan1972depth](../../references.html#tarjan1972depth)

## Reaching {#cx_reaching}

Measure id: `cx_reaching`. Original family: Centrality.

**Definition.** Global reaching centrality of a network (Mones et al.): the mean gap between the largest local reaching centrality and every node's, divided by n - 1.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention | `global_reaching_centrality; local_reaching_centrality` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_reaching_global` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.global_reaching_centrality(G)` |  |
| `cx_reaching_global_weighted` | NetworkX | any | differs | integer\_weights, multi\_edges | direction, multi\_edges, normalization, ties, weights | abs 1e-12, rel 1e-09 | `nx.global_reaching_centrality(G, weight = 'weight')` | With integer weights some nodes have several shortest paths (lengths W/w) whose edges have different mean weights, and each tool averages the path its search finds first: NetworkX settles ties in insertion order, the reference by node index (weighted\_dir has two such pairs from node 3, checked with nx.all\_shortest\_paths). The NetworkX oracle builds a simple graph (the last parallel weight wins), while the reference keeps every edge, so the mean edge weight that normalizes the measure counts parallel edges (two parallel edges of weights 1 and 9: 1.8 against 1.0). |
| `cx_reaching_local` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.local_reaching_centrality(G, v) for every v (an error is undefined)` |  |
| `cx_reaching_local_weighted` | NetworkX | any | differs | integer\_weights, multi\_edges | direction, multi\_edges, normalization, ties, weights | abs 1e-12, rel 1e-09 | `nx.local_reaching_centrality(G, v, weight = 'weight')` | With integer weights some nodes have several shortest paths (lengths W/w) whose edges have different mean weights, and each tool averages the path its search finds first: NetworkX settles ties in insertion order, the reference by node index (weighted\_dir has two such pairs from node 3, checked with nx.all\_shortest\_paths). The NetworkX oracle builds a simple graph (the last parallel weight wins), while the reference keeps every edge, so the mean edge weight that normalizes the measure counts parallel edges (two parallel edges of weights 1 and 9: 1.8 against 1.0). |

**References:** [johnson2014trophic](../../references.html#johnson2014trophic), [levine1980several](../../references.html#levine1980several), [mones2012hierarchy](../../references.html#mones2012hierarchy), [tarjan1972depth](../../references.html#tarjan1972depth)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
