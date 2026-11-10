---
title: "Spanner ok"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Spanner ok

Family: Traversal, trees and DAGs. Identifier: `gb_spanner_ok`.

## Definition

Spanner ok.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `spanner` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_spanner_ok` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 0, rel 0 | `stretch check of nx.spanner(nx.Graph(M), 3, seed=1)` | NetworkX's spanner rejects multigraphs. |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
