---
title: "Hopcroft karp"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Hopcroft karp

Family: Two-mode and bipartite. Identifier: `hopcroft_karp`.

## Definition

A maximum matching of a bipartite graph as each node's mate (-1 if unmatched), by Hopcroft and Karp.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `eppstein_matching; hopcroft_karp_matching` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `max_bipartite_match` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `maximum_bipartite_matching` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `HopcroftKarpMaximumCardinalityBipartiteMatching` | API listing |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `edmonds_maximum_cardinality_matching` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `hopcroft_karp` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.bipartite.hopcroft_karp_matching(G, top_nodes = top): (size, 1 if nx.is_matching)` |  |

## References

[hopcroft1973algorithm](../references.html#hopcroft1973algorithm), [hopcroft1973n52](../references.html#hopcroft1973n52)

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [siek2002boost](../references.html#siek2002boost)
{% endraw %}
