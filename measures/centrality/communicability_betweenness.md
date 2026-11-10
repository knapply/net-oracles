---
title: "Communicability betweenness"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Communicability betweenness {#concept-top}

Family: [Centrality](index.html). Subfamily: Betweenness, load and flow. Concept id: `communicability_betweenness`. 1 measure.

## Definition {#concept-definition}

Communicability betweenness of every node: the loss of communicability when the node's edges are removed (Estrada, Higham and Hatano 2009).

## References {#concept-references}

[estrada2009communicability](../../references.html#estrada2009communicability)

## Communicability betweenness {#cx_communicability_betweenness}

Measure id: `cx_communicability_betweenness`. Original family: Centrality.

**Definition.** Communicability betweenness of every node: the loss of communicability when the node's edges are removed (Estrada, Higham and Hatano 2009).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `communicability_betweenness_centrality` |  |
| [centiserve](../../tools/centiserve.html) | ✓ checked, agrees | `communibet` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_cbc` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization | abs 1e-11, rel 5e-09 | `nx.communicability_betweenness_centrality(G)` | NetworkX defines this measure for connected simple graphs and raises an error otherwise (the reference, like the definition oracle, sums over the pairs joined by a walk, G\_pq &gt; 0); on a single node NetworkX divides by (n - 1)(n - 2) = 0. |
| `cx_cbc` | centiserve | undirected | differs | loops, multi\_edges, (no value) disconnected | defaults, multi\_edges, self\_loops | abs 2e-14, rel 2e-10 | `centiserve::communibet(g, normalized = TRUE)` | communibet() builds e^A from igraph's adjacency matrix, where parallel edges and self-loops enter differently from the reference value's reading (the definition oracle's); networks without them agree. On a disconnected network communibet() returns NaN for every node: a pair p, q in different components has G\_pq = (e^A)\_pq = 0, the denominator of its term. the reference and the definition oracle leave such pairs out (Estrada, Higham and Hatano 2009 define the measure on connected networks). On a single node it writes no value. |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F013](../../findings.html#f013) | centiserve | defect | communibet() cannot find an installed expm |

**References:** [estrada2009communicability](../../references.html#estrada2009communicability)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [jalili2015centiserver](../../references.html#jalili2015centiserver)
{% endraw %}
