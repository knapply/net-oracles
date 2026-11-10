---
title: "Nxp katz"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Nxp katz

Family: Centrality. Identifier: `nxp_katz`.

## Definition

NetworkX's Katz centrality iteration, reproduced step for step; reports when it does not converge.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxp_katz` | NetworkX | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-10 | `nx.katz_centrality(G, alpha = 0.05)` | NetworkX does not implement katz\_centrality for multigraphs. |
| `nxp_katz_weighted_raw` | NetworkX | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-10 | `nx.katz_centrality(G, alpha = 0.02, normalized = False, weight = 'weight')` | NetworkX does not implement katz\_centrality for multigraphs. |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
