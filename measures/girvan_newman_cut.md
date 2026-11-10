---
title: "Girvan newman cut"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Girvan newman cut

Family: Communities. Identifier: `girvan_newman_cut`.

## Definition

Girvan newman cut.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `girvan_newman_cut3` | igraph (R) | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) edge\_case, (no value) loops, (no value) multi\_edges | defaults, multi\_edges, self\_loops | abs 0, rel 0 | `cut_at(cluster_edge_betweenness(simplify(g), weights = NULL), no = 3)` | the R oracle simplifies the network, so multigraphs and networks with loops are not comparable; disconnected and trivial networks give dendrograms that cannot be cut at 3 groups in one tool or the other |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph)
{% endraw %}
