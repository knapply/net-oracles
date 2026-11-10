---
title: "Isolates"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Isolates

Family: Traversal, trees and DAGs. Identifier: `gb_isolates`.

## Definition

Isolates.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `isolates; number_of_isolates` |  |
| [sna](../tools/sna.html) | · reported in docs | `isolates` | API listing |
| [ergm (statnet)](../tools/ergm.html) | · reported in docs | `isolates` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `digraph_isolates; graph_isolates; isolates` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_isolates` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `list(nx.isolates(M))` |  |

Tools cited: [butts2008sna](../references.html#butts2008sna), [hagberg2008exploring](../references.html#hagberg2008exploring), [hunter2008ergm](../references.html#hunter2008ergm), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
