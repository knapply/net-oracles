---
title: "Small-world quotient"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Small-world quotient {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Clustering and transitivity. Concept id: `small_world_index`. 2 measures.

## Definition {#concept-definition}

Small-world coefficient omega of a connected undirected network against random and lattice references (Telesford et al.).

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Small world](#small_world) | `small_world` | 1 |
| [Small world observed](#small_world_observed) | `small_world_observed` | 2 |

## References {#concept-references}

[colizza2006detecting](../../references.html#colizza2006detecting), [erdos2010simple](../../references.html#erdos2010simple), [hagberg2008exploring](../../references.html#hagberg2008exploring), [humphries2008network](../../references.html#humphries2008network), [maslov2002specificity](../../references.html#maslov2002specificity), [sporns2004small](../../references.html#sporns2004small), [telesford2011ubiquity](../../references.html#telesford2011ubiquity), [zhou2004rich](../../references.html#zhou2004rich)

## Small world {#small_world}

Measure id: `small_world`. Original family: Generators and rewiring.

**Definition.** Small-world coefficient omega of a connected undirected network against random and lattice references (Telesford et al.).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `omega; sigma` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `small_world_omega` | NetworkX | undirected | no-value-on-some-inputs |  | defaults, normalization | abs 0.05, rel 0 | `mean of nx.omega(G, niter = 2, nrand = 10, seed = s) over s = 0..9; -1 where it raises (disconnected graphs)` | As for small\_world\_sigma; on path10 every clustering coefficient is 0, so NetworkX divides 0 by 0 and raises ZeroDivisionError, where the reference returns NaN. |
| `small_world_sigma` | NetworkX | undirected | no-value-on-some-inputs |  | ties | abs 0.15, rel 0 | `mean of nx.sigma(G, niter = 20, nrand = 20, seed = s) over s = 0..9; -1 where it raises (disconnected graphs)` | The means over random graphs are compared on the small networks only, to keep the NetworkX oracle fast; on a star NetworkX's random\_reference redraws forever (every draw is rejected), where the reference stops each round after 100 (m + 1) rejected draws. |

**References:** [colizza2006detecting](../../references.html#colizza2006detecting), [erdos2010simple](../../references.html#erdos2010simple), [hagberg2008exploring](../../references.html#hagberg2008exploring), [humphries2008network](../../references.html#humphries2008network), [maslov2002specificity](../../references.html#maslov2002specificity), [sporns2004small](../../references.html#sporns2004small), [telesford2011ubiquity](../../references.html#telesford2011ubiquity), [zhou2004rich](../../references.html#zhou2004rich)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Small world observed {#small_world_observed}

Measure id: `small_world_observed`. Original family: Descriptive statistics.

**Definition.** Small world observed.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |
| [igraph (R)](../../tools/igraph.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `small_world_observed` | NetworkX | any | agrees |  |  | abs 1e-15, rel 1e-13 | `nx.transitivity and the mean of nx.shortest_path_length over connected pairs (simple undirected graph)` |  |
| `small_world_observed` | igraph (R) | any | agrees |  |  | abs 1e-15, rel 1e-13 | `igraph::transitivity(type = 'global') and mean_distance(unconnected = TRUE) on simplify(as_undirected(g))` |  |
| `small_world_observed_local` | NetworkX | any | agrees |  |  | abs 1e-15, rel 1e-13 | `nx.average_clustering and the mean of nx.shortest_path_length over connected pairs` |  |
| `small_world_observed_local` | igraph (R) | any | agrees |  |  | abs 1e-15, rel 1e-13 | `igraph::transitivity(type = 'average', isolates = 'zero') and mean_distance(unconnected = TRUE)` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
