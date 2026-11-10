---
title: "Kosaraju"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Kosaraju

Family: Graph theory and combinatorics. Identifier: `nxo_kosaraju`.

## Definition

Kosaraju.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxo_kosaraju` | NetworkX | directed | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges, ties | abs 0, rel 0 | `nx.kosaraju_strongly_connected_components(G), components in order` | The backend leaves multigraphs to NetworkX (their adjacency order is not the edge order); the reference value's components are the same sets. |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
