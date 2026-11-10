---
title: "Attracting components"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Attracting components {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connected components. Concept id: `attracting_components`. 4 measures.

## Definition {#concept-definition}

Attracting components. Entries grouped here: Attracting; Attracting flags; Is attracting component; Number attracting components.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Attracting](#attracting) | `attracting` | 1 |
| [Attracting flags](#attracting_flags) | `attracting_flags` | 1 |
| [Is attracting component](#cat_attracting_component_is) | `cat_attracting_component_is` | 1 |
| [Number attracting components](#cat_attracting_component) | `cat_attracting_component` | 1 |

## Attracting {#attracting}

Measure id: `attracting`. Original family: Components and connectivity.

**Definition.** Attracting.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `attracting_components` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_attracting` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.attracting_components(G), labelled by nx.condensation(G).graph['mapping'], -1 elsewhere` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Attracting flags {#attracting_flags}

Measure id: `attracting_flags`. Original family: Components and connectivity.

**Definition.** Attracting flags.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_attracting_flags` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `1 if v is in a component of nx.attracting_components(G)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Is attracting component {#cat_attracting_component_is}

Measure id: `cat_attracting_component_is`. Original family: Components and connectivity.

**Definition.** Is attracting component.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_attracting_component_is-networkx) | `is_attracting_component` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_attracting_component_is-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: is\_attracting\_component.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Number attracting components {#cat_attracting_component}

Measure id: `cat_attracting_component`. Original family: Components and connectivity.

**Definition.** Number attracting components.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_attracting_component-networkx) | `number_attracting_components` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_attracting_component-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: number\_attracting\_components.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
