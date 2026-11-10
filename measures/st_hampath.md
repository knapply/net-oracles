---
title: "Hampath"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Hampath

Family: Graph theory and combinatorics. Identifier: `st_hampath`.

## Definition

Hampath.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `hamiltonian_path` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_hampath` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.tournament.hamiltonian_path(G) on the simple digraph` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
