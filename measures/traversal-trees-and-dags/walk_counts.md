---
title: "Walk counts"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Walk counts {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Traversal and orderings. Concept id: `walk_counts`. 1 measure.

## Definition {#concept-definition}

Walk counts. Entries grouped here: Walks.

## Walks {#gb_walks}

Measure id: `gb_walks`. Original family: Traversal, trees and DAGs.

**Definition.** Walks.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `number_of_walks` |  |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gb_walks-networkit) | `walk` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gb_walks-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: walk.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_walks` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.number_of_walks(M, 2)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
