---
title: "Path counts"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Path counts {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Path enumeration and counting. Concept id: `path_counts`. 1 measure.

## Definition {#concept-definition}

Path counts. Entries grouped here: Paths count.

## Paths count {#paths_count}

Measure id: `paths_count`. Original family: Paths and distances.

**Definition.** Paths count.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_count-graphtool) | `count_shortest_paths` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-paths_count-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: count\_shortest\_paths.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_count_unweighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(list(nx.all_shortest_paths(G, 0, t))) for every t (0 without a path)` |  |
| `paths_count_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(list(nx.all_shortest_paths(G, 0, t, weight = 'weight'))) for every t` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
