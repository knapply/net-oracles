---
title: "Gm aperiodic"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Gm aperiodic

Family: Matrices and spectra. Identifier: `gm_aperiodic`.

## Definition

Gm aperiodic.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gm_aperiodic` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.is_aperiodic(G) on strongly connected graphs` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
