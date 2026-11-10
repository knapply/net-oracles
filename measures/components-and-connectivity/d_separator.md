---
title: "D-separators"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# D-separators {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Cuts and separators. Concept id: `d_separator`. 3 measures.

## Definition {#concept-definition}

D-separators. Entries grouped here: D separated; Find minimal d separator; Is minimal d separator.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [D separated](#gb_d_separated) | `gb_d_separated` | 1 |
| [Find minimal d separator](#cat_d_find_minimal_separator) | `cat_d_find_minimal_separator` | 1 |
| [Is minimal d separator](#cat_d_is_minimal_separator) | `cat_d_is_minimal_separator` | 1 |

## D separated {#gb_d_separated}

Measure id: `gb_d_separated`. Original family: Traversal, trees and DAGs.

**Definition.** D separated.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `is_d_separator` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_d_separated` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.is_d_separator(M, 0, n - 1, {1})` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Find minimal d separator {#cat_d_find_minimal_separator}

Measure id: `cat_d_find_minimal_separator`. Original family: Components and connectivity.

**Definition.** Find minimal d separator.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_d_find_minimal_separator-networkx) | `find_minimal_d_separator` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_d_find_minimal_separator-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: find\_minimal\_d\_separator.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Is minimal d separator {#cat_d_is_minimal_separator}

Measure id: `cat_d_is_minimal_separator`. Original family: Components and connectivity.

**Definition.** Is minimal d separator.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_d_is_minimal_separator-networkx) | `is_minimal_d_separator` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_d_is_minimal_separator-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: is\_minimal\_d\_separator.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
