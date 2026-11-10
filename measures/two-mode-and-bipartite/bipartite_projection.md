---
title: "Bipartite projection"
layout: default
parent: "Two-mode and bipartite"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Bipartite projection {#concept-top}

Family: [Two-mode and bipartite](index.html). Subfamily: Projection. Concept id: `bipartite_projection`. 3 measures.

## Definition {#concept-definition}

One-mode projection of a two-mode network onto either mode, with count, Newman or product weights.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Project](#project) | `project` | 6 |
| [Projection](#projection) | `projection` | 2 |
| [Two-mode projection weights (covariance, correlation, Jaccard, Bonacich, cosine)](#projection_weights) | `projection_weights` | 2 |

## References {#concept-references}

[bonacich1972factoring](../../references.html#bonacich1972factoring), [bonacich1987power](../../references.html#bonacich1987power), [borgatti1997network](../../references.html#borgatti1997network), [borgatti2011analyzing](../../references.html#borgatti2011analyzing), [breiger1974duality](../../references.html#breiger1974duality), [collatz1942einschliessungssatz](../../references.html#collatz1942einschliessungssatz), [daniel1976reorthogonalization](../../references.html#daniel1976reorthogonalization), [everett2013dual](../../references.html#everett2013dual)

## Project {#project}

Measure id: `project`. Original family: Two-mode and bipartite.

**Definition.** One-mode projection of a two-mode network onto either mode, with count, Newman or product weights.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ∅ checked, no value on some inputs | `collaboration_weighted_projected_graph; generic_weighted_projected_graph; overlap_weighted_projected_graph; projected_graph; weighted_projected_graph` |  |
| [igraph (R)](../../tools/igraph.html) | ∅ checked, no value on some inputs | `bipartite_projection; bipartite_projection_size` |  |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `bipartite_projection; bipartite_projection_size` | API listing |
| [ergm (statnet)](../../tools/ergm.html) | · reported in docs | `Project` | API listing |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `Affiliations (2-mode to 1-mode): co-membership values 0-4; cosine similarity (6.833); old routine "to avoid"; bprod; bxtx; bxxt; xtx; xxt` | published documentation |
| [tnet](../../tools/tnet.html) | ✓ checked, agrees | `projecting_tm` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `project_first` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nx.bipartite.weighted_projected_graph(G, first_mode_nodes)` | one-mode fixture (no node types) |
| `project_first` | igraph (R) | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `igraph::bipartite_projection(g, types, multiplicity = TRUE)$proj1` | one-mode fixture (no node types) |
| `project_first` | tnet | any | agrees |  |  | abs 0, rel 0 | `tnet::projecting_tm(two-mode list, method = 'sum')` |  |
| `project_first_newman` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-12 | `nx.bipartite.collaboration_weighted_projected_graph(G, first_mode_nodes)` | one-mode fixture (no node types) |
| `project_first_newman` | tnet | any | agrees |  |  | abs 0, rel 1e-12 | `tnet::projecting_tm(two-mode list, method = 'Newman')` |  |
| `project_first_product` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-12 | `nx.bipartite.generic_weighted_projected_graph(G, first_mode_nodes, sum of w_ue w_ve)` | one-mode fixture (no node types) |
| `project_second` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nx.bipartite.weighted_projected_graph(G, second_mode_nodes)` | one-mode fixture (no node types) |
| `project_second` | igraph (R) | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `igraph::bipartite_projection(g, types, multiplicity = TRUE)$proj2` | one-mode fixture (no node types) |
| `project_second` | tnet | any | agrees |  |  | abs 0, rel 0 | `tnet::projecting_tm(two-mode list, method = 'sum')` |  |
| `project_second_newman` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-12 | `nx.bipartite.collaboration_weighted_projected_graph(G, second_mode_nodes)` | one-mode fixture (no node types) |
| `project_second_newman` | tnet | any | agrees |  |  | abs 0, rel 1e-12 | `tnet::projecting_tm(two-mode list, method = 'Newman')` |  |

**References:** [bonacich1972factoring](../../references.html#bonacich1972factoring), [bonacich1987power](../../references.html#bonacich1987power), [borgatti1997network](../../references.html#borgatti1997network), [borgatti2011analyzing](../../references.html#borgatti2011analyzing), [breiger1974duality](../../references.html#breiger1974duality), [collatz1942einschliessungssatz](../../references.html#collatz1942einschliessungssatz), [daniel1976reorthogonalization](../../references.html#daniel1976reorthogonalization), [everett2013dual](../../references.html#everett2013dual)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hunter2008ergm](../../references.html#hunter2008ergm), [opsahl2010node](../../references.html#opsahl2010node)

## Projection {#projection}

Measure id: `projection`. Original family: Two-mode and bipartite.

**Definition.** Projection.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `graph_projection` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `projection_count` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nx.bipartite.weighted_projected_graph(G, top)` | NetworkX raises when no node lies outside `top` |
| `projection_jaccard` | NetworkX | any | agrees |  |  | abs 0, rel 1e-15 | `nx.bipartite.overlap_weighted_projected_graph(G, top)` |  |
| `projection_min` | NetworkX | any | agrees |  |  | abs 0, rel 1e-15 | `nx.bipartite.overlap_weighted_projected_graph(G, top, jaccard = False)` |  |
| `projection_newman` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.bipartite.collaboration_weighted_projected_graph(G, top)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)

## Two-mode projection weights (covariance, correlation, Jaccard, Bonacich, cosine) {#projection_weights}

Measure id: `projection_weights`. Original family: Two-mode and bipartite.

**Definition.** Two-mode projection weights (covariance, correlation, Jaccard, Bonacich, cosine).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |
| [tnet](../../tools/tnet.html) | · reported in docs |  | documentation |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [opsahl2010node](../../references.html#opsahl2010node)
{% endraw %}
