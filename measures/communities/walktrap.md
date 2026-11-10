---
title: "Walktrap"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Walktrap {#concept-top}

Family: [Communities](index.html). Subfamily: Other detection algorithms. Concept id: `walktrap`. 1 measure.

## Definition {#concept-definition}

Walktrap communities by merging nodes whose random-walk distributions are close; returns the best level, its modularity, the mergers and the modularity path.

## References {#concept-references}

[pons2006computing](../../references.html#pons2006computing)

## Walktrap {#walktrap}

Measure id: `walktrap`. Original family: Communities.

**Definition.** Walktrap communities by merging nodes whose random-walk distributions are close; returns the best level, its modularity, the mergers and the modularity path.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | ≠ checked, differs by convention | `cluster_walktrap` |  |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `community_walktrap` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `walktrap` | igraph (R) | undirected | differs | symmetric\_nodes, (no value) loops, (no value) multi\_edges | multi\_edges, self\_loops, ties | abs 1e-14, rel 1e-12 | `max(modularity(cluster_walktrap(g, weights = NULL, steps = 4)))` | exact ties between pairs of groups occur during the merges, which the reference breaks by group names and igraph by an undocumented rule; on the seeded mid-size random networks listed by name igraph merges pairs that do not have the smallest delta sigma (finding F-SIZES-1), which leads to a different best level igraph's treatment of parallel edges and self-loops in the walk is not documented |
| `walktrap_cut2` | igraph (R) | undirected | differs | symmetric\_nodes, (no value) disconnected, (no value) loops, (no value) multi\_edges | defaults, multi\_edges, self\_loops, ties | abs 0, rel 0 | `cut_at(cluster_walktrap(g, weights = NULL, steps = 4), no = 2)` | exact ties between pairs of groups occur during the merges, which the reference breaks by group names and igraph by an undocumented rule; on the seeded mid-size random networks listed by name igraph merges pairs that do not have the smallest delta sigma (finding F-SIZES-1), which leads to a different best level as for walktrap\_merges; igraph's cut\_at() raises an error when asked for two groups of a single node |
| `walktrap_membership` | igraph (R) | undirected | differs | symmetric\_nodes, (no value) loops, (no value) multi\_edges | multi\_edges, self\_loops, ties | abs 0, rel 0 | `membership(cluster_walktrap(g, weights = NULL, steps = 4))` | exact ties between pairs of groups occur during the merges, which the reference breaks by group names and igraph by an undocumented rule; on the seeded mid-size random networks listed by name igraph merges pairs that do not have the smallest delta sigma (finding F-SIZES-1), which leads to a different best level as for walktrap |
| `walktrap_merges` | igraph (R) | undirected | differs | symmetric\_nodes, (no value) disconnected, (no value) loops, (no value) multi\_edges | defaults, multi\_edges, self\_loops, ties, weights | abs 0, rel 0 | `cluster_walktrap(g, weights = NULL, steps = 4)$merges - 1` | exact ties between pairs of groups (symmetric positions) occur during the merges, which the reference breaks by group names and igraph by an undocumented rule; on weighted\_und igraph merges a pair that does not have the smallest delta sigma (see the note above the Walktrap entries), an igraph exception listed by name; the same on the mid-size random networks listed by name (finding F-SIZES-1) loops and parallel edges as for walktrap; on disconnected networks igraph completes the dendrogram by joining components, which the reference (like the paper) does not |
| `walktrap_steps2` | igraph (R) | undirected | differs | symmetric\_nodes, (no value) loops, (no value) multi\_edges | multi\_edges, self\_loops, ties, weights | abs 1e-14, rel 1e-12 | `max(modularity(cluster_walktrap(g, weights = NULL, steps = 2)))` | as for walktrap\_merges: ties broken differently, and on twomode\_weighted igraph merges pairs that do not have the smallest delta sigma, which leads to a different best level; the same on the mid-size random networks listed by name (finding F-SIZES-1) as for walktrap |
| `walktrap_weighted` | igraph (R) | undirected | differs | symmetric\_nodes, (no value) loops, (no value) multi\_edges | multi\_edges, self\_loops, ties | abs 1e-14, rel 1e-12 | `max(modularity(cluster_walktrap(g, weights = E(g)$weight, steps = 4)))` | exact ties between pairs of groups occur during the merges, which the reference breaks by group names and igraph by an undocumented rule; on the seeded mid-size random networks listed by name igraph merges pairs that do not have the smallest delta sigma (finding F-SIZES-1), which leads to a different best level as for walktrap |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F010](../../findings.html#f010) | igraph (R) | defect | Walktrap skips minimal merge pairs on mid-size random networks |

**References:** [pons2006computing](../../references.html#pons2006computing)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
