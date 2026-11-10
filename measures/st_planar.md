---
title: "Planar"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Planar

Family: Graph theory and combinatorics. Identifier: `st_planar`.

## Definition

Planar.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `PlanarEmbedding; check_planarity; is_planar` |  |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `is_planar` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `is_planar` | API listing |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `boyer_myrvold_planarity_test` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_planar` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.is_planar(G)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [siek2002boost](../references.html#siek2002boost), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
