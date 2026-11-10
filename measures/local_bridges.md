---
title: "Local bridges"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Local bridges

Family: Components and connectivity. Identifier: `local_bridges`.

## Definition

Local bridges.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_local_bridges` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.local_bridges(G, with_span = True), mapped to the fixture's edges` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
