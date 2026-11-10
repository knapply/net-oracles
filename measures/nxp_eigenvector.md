---
title: "Nxp eigenvector"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Nxp eigenvector

Family: Centrality. Identifier: `nxp_eigenvector`.

## Definition

NetworkX's power-iteration eigenvector centrality, reproduced step for step; reports when it does not converge.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxp_eigenvector` | NetworkX | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-10 | `nx.eigenvector_centrality(G)` | NetworkX does not implement eigenvector\_centrality for multigraphs. |
| `nxp_eigenvector_weighted_capped` | NetworkX | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-10 | `nx.eigenvector_centrality(G, max_iter = 8, weight = 'weight')` | NetworkX does not implement eigenvector\_centrality for multigraphs. |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
