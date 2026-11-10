---
title: "Beam"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Beam

Family: Traversal, trees and DAGs. Identifier: `trav_beam`.

## Definition

Beam.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `bfs_beam_edges` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `trav_beam` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.bfs_beam_edges(M, 0, lambda v: (v * 7) % 5, 2)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
