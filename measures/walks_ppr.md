---
title: "Walks ppr"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Walks ppr

Family: Centrality. Identifier: `walks_ppr`.

## Definition

Personalized PageRank by the local push of Andersen, Chung and Lang: estimates below the exact value by at most the residual.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `walks_ppr_exact` | NetworkX | any | no-value-on-some-inputs | (no value) loops | direction, normalization, self\_loops | abs 2e-13, rel 1e-10 | `nx.pagerank(G, alpha = 0.85, personalization = {0: 2, n - 1: 1}, tol = 1e-14, max_iter = 100000, weight = None)` | NetworkX counts an undirected self-loop once, the reference twice. |
| `walks_ppr_push` | NetworkX | any | no-value-on-some-inputs | (no value) loops | direction, normalization, self\_loops | abs 5e-13, rel 5e-10 | `nx.pagerank(G, alpha = 0.85, personalization = {0: 2, n - 1: 1}, tol = 1e-14, max_iter = 100000, weight = None)` | NetworkX counts an undirected self-loop once, the reference twice. |
| `walks_ppr_push_weighted` | NetworkX | any | no-value-on-some-inputs | (no value) loops | direction, normalization, self\_loops | abs 5e-12, rel 2e-09 | `nx.pagerank(G, alpha = 0.7, personalization = {0: 2, n - 1: 1}, tol = 1e-14, max_iter = 100000, weight = 'weight')` | NetworkX counts an undirected self-loop once, the reference twice. |

## References

[andersen2006local](../references.html#andersen2006local), [brin1998anatomy](../references.html#brin1998anatomy), [grover2016node2vec](../references.html#grover2016node2vec), [tong2006fast](../references.html#tong2006fast), [vose1991linear](../references.html#vose1991linear), [walker1977new](../references.html#walker1977new)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
