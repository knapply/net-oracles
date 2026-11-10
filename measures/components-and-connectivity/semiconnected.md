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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `is_semiconnected` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_semiconnected` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.is_semiconnected(G)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Is semi connected {#cat_connected_is_semi}

Measure id: `cat_connected_is_semi`. Original family: Components and connectivity.

**Definition.** Is semi connected.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_connected_is_semi-rustworkx) | `is_semi_connected` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_connected_is_semi-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: is\_semi\_connected.

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
