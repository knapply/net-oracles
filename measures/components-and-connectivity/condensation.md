---
title: "Condensation of strong components"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Condensation of strong components {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connected components. Concept id: `condensation`. 1 measure.

## Definition {#concept-definition}

Condensation of strong components. Entries grouped here: Condensation.

## Condensation {#condensation}

Measure id: `condensation`. Original family: Components and connectivity.

**Definition.** Condensation.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `condensation` |  |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `condensation_graph` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `condensation; digraph_condensation; graph_condensation` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `create_condensation_graph` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_condensation_input` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.condensation(G).graph['mapping']` |  |
| `conn_condensation_sorted` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.condensation(H).graph['mapping'], H built from the edges in increasing order` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
