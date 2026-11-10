---
title: "Semiconnected graphs"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Semiconnected graphs {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connected components. Concept id: `semiconnected`. 2 measures.

## Definition {#concept-definition}

Semiconnected graphs. Entries grouped here: Semiconnected; Is semi connected.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Semiconnected](#semiconnected) | `semiconnected` | 1 |
| [Is semi connected](#cat_connected_is_semi) | `cat_connected_is_semi` | 1 |

## Semiconnected {#semiconnected}

Measure id: `semiconnected`. Original family: Components and connectivity.

**Definition.** Semiconnected.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `is_semiconnected` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_semiconnected` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.is_semiconnected(G)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Is semi connected {#cat_connected_is_semi}

Measure id: `cat_connected_is_semi`. Original family: Components and connectivity.

**Definition.** Is semi connected.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `is_semi_connected` | API listing |

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
