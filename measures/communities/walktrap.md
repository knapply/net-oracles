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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, multi-edges, self-loops, ties and weights): exact ties between pairs of groups occur during the merges, which the reference breaks by group names and igraph by an undocumented rule. [details](#why-walktrap-igraph) | `cluster_walktrap` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-walktrap-pyigraph) | `community_walktrap` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-walktrap-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (R) 2.3.4 was run and its value differs from the reference value by convention (defaults, multi-edges, self-loops, ties and weights) on inputs tagged symmetric\_nodes and the fixtures mid\_dense\_und\_1000, mid\_gnm\_und\_2000, mid\_gnm\_und\_int\_2500, mid\_sbm\_und\_4000, twomode\_weighted, weighted\_und. walktrap, walktrap\_cut2, walktrap\_membership and walktrap\_weighted: exact ties between pairs of groups occur during the merges, which the reference breaks by group names and igraph by an undocumented rule; on the seeded mid-size random networks listed by name igraph merges pairs that do not have the smallest delta sigma, which leads to a different best level. walktrap\_merges: exact ties between pairs of groups (symmetric positions) occur during the merges, which the reference breaks by group names and igraph by an undocumented rule; on weighted\_und igraph merges a pair that does not have the smallest delta sigma, an igraph exception listed by name; the same on the mid-size random networks listed by name. walktrap\_steps2: as for walktrap\_merges: ties broken differently, and on twomode\_weighted igraph merges pairs that do not have the smallest delta sigma, which leads to a different best level; the same on the mid-size random networks listed by name. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12; abs 0, rel 0 (0 means exact equality). 53 comparisons differ and 76 agree. Finding F010 (defect): Walktrap skips minimal merge pairs on mid-size random networks. Findings: [F010](../../findings.html#f010).
- <a id="why-walktrap-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_walktrap.

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
