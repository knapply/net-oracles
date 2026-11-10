---
title: "Asteroidal"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Asteroidal

Family: Graph theory and combinatorics. Identifier: `st_asteroidal`.

## Definition

Asteroidal.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `find_asteroidal_triple` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_asteroidal` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.find_asteroidal_triple(G): the triple, or [-1]` |  |
| `st_asteroidal_valid` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `1 if nx.find_asteroidal_triple(G) returns a triple, else -1` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
