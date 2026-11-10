---
title: "At free"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# At free

Family: Graph theory and combinatorics. Identifier: `st_at_free`.

## Definition

At free.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `is_at_free` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_at_free` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.is_at_free(G)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
