---
title: "Mcb weight"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Mcb weight

Family: Traversal, trees and DAGs. Identifier: `gb_mcb_weight`.

## Definition

Mcb weight.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_mcb_weight` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-09, rel 1e-09 | `total weight of nx.minimum_cycle_basis(G, weight)` | NetworkX's minimum\_cycle\_basis rejects multigraphs. |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
