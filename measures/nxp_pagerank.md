---
title: "Nxp pagerank"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Nxp pagerank

Family: Centrality. Identifier: `nxp_pagerank`.

## Definition

NetworkX's PageRank iteration, reproduced step for step; reports when it does not converge.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [BCT (Octave)](../tools/bct.html) | · reported in docs | `pagerank_centrality` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxp_pagerank` | NetworkX | any | agrees |  |  | abs 1e-13, rel 1e-10 | `nx.pagerank(G, weight = None)` |  |
| `nxp_pagerank_personalized_weighted` | NetworkX | any | no-value-on-some-inputs | (no value) one\_node | defaults, weights | abs 1e-13, rel 1e-10 | `nx.pagerank(G, alpha = 0.7, personalization = {v: v % 3}, weight = 'weight')` | The personalization v % 3 gives node 0 weight 0, so on one node it sums to zero; the reference rejects it. |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [rubinov2010complex](../references.html#rubinov2010complex)
{% endraw %}
