---
title: "Bipartite maximum matching"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Bipartite maximum matching {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Matching. Concept id: `bipartite_maximum_matching`. 4 measures.

## Definition {#concept-definition}

A maximum matching of a bipartite graph as each node's mate (-1 if unmatched), by Hopcroft and Karp.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Hopcroft karp](#hopcroft_karp) | `hopcroft_karp` | 5 |
| [Nx eppstein](#nx_eppstein) | `nx_eppstein` | 1 |
| [Nx eppstein size](#nx_eppstein_size) | `nx_eppstein_size` | 1 |
| [Nx hk mates](#nx_hk_mates) | `nx_hk_mates` | 1 |

## References {#concept-references}

[hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [hopcroft1973n52](../../references.html#hopcroft1973n52)

## Hopcroft karp {#hopcroft_karp}

Measure id: `hopcroft_karp`. Original family: Two-mode and bipartite.

**Definition.** A maximum matching of a bipartite graph as each node's mate (-1 if unmatched), by Hopcroft and Karp.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `eppstein_matching; hopcroft_karp_matching` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `max_bipartite_match` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `maximum_bipartite_matching` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `HopcroftKarpMaximumCardinalityBipartiteMatching` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `edmonds_maximum_cardinality_matching` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `hopcroft_karp` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.bipartite.hopcroft_karp_matching(G, top_nodes = top): (size, 1 if nx.is_matching)` |  |

**References:** [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [hopcroft1973n52](../../references.html#hopcroft1973n52)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [siek2002boost](../../references.html#siek2002boost)

## Nx eppstein {#nx_eppstein}

Measure id: `nx_eppstein`. Original family: Two-mode and bipartite.

**Definition.** Nx eppstein.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_eppstein` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.bipartite.eppstein_matching(G, top_nodes = top): the dictionary's (key, value) pairs in order; [-1] if top is not a side` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Nx eppstein size {#nx_eppstein_size}

Measure id: `nx_eppstein_size`. Original family: Two-mode and bipartite.

**Definition.** Nx eppstein size.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_eppstein_size` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `(len(eppstein_matching) / 2, 1 if every pair is an edge matched both ways); [-1] if top is not a side` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Nx hk mates {#nx_hk_mates}

Measure id: `nx_hk_mates`. Original family: Two-mode and bipartite.

**Definition.** Nx hk mates.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_hk_mates` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.bipartite.hopcroft_karp_matching(G, top_nodes = top): each node's mate, -1 if unmatched; [-1] if top is not a side` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
