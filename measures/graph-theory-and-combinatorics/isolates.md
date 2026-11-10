---
title: "Isolates"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Isolates {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Degree sequences and predicates. Concept id: `isolates`. 2 measures.

## Definition {#concept-definition}

Isolates. Entries grouped here: Is isolate; Isolates.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Is isolate](#cat_is_isolate) | `cat_is_isolate` | 1 |
| [Isolates](#gb_isolates) | `gb_isolates` | 4 |

## Is isolate {#cat_is_isolate}

Measure id: `cat_is_isolate`. Original family: Graph theory and combinatorics.

**Definition.** Is isolate.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_is_isolate-networkx) | `is_isolate` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_is_isolate-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: is\_isolate.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Isolates {#gb_isolates}

Measure id: `gb_isolates`. Original family: Traversal, trees and DAGs.

**Definition.** Isolates.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `isolates; number_of_isolates` |  |
| [sna](../../tools/sna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gb_isolates-sna) | `isolates` | API listing |
| [ergm (statnet)](../../tools/ergm.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gb_isolates-ergm) | `isolates` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gb_isolates-rustworkx) | `digraph_isolates; graph_isolates; isolates` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gb_isolates-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: isolates.
- <a id="why-gb_isolates-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: isolates.
- <a id="why-gb_isolates-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: digraph\_isolates; graph\_isolates; isolates.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_isolates` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `list(nx.isolates(M))` |  |

**Tools cited:** [butts2008sna](../../references.html#butts2008sna), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hunter2008ergm](../../references.html#hunter2008ergm), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
