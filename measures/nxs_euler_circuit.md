---
title: "Euler circuit"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Euler circuit

Family: Graph theory and combinatorics. Identifier: `nxs_euler_circuit`.

## Definition

Euler circuit.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_euler_circuit` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `list(nx.eulerian_circuit(G, source = 0, keys = True))` | NetworkX refuses a graph that is not connected (or has no node) |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
