---
title: "Find a cycle"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Find a cycle {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Cycles. Concept id: `find_cycle`. 2 measures.

## Definition {#concept-definition}

Find a cycle. Entries grouped here: Find cycle; Nxs find cycle.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Find cycle](#find_cycle) | `find_cycle` | 5 |
| [Nxs find cycle](#nxs_find_cycle) | `nxs_find_cycle` | 1 |

## Find cycle {#find_cycle}

Measure id: `find_cycle`. Original family: Graph theory and combinatorics.

**Definition.** Find cycle.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `find_cycle` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-find_cycle-igraph) | `find_cycle` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-find_cycle-rustworkx) | `digraph_find_cycle` | API listing |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-find_cycle-sknetwork) | `get_cycles` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-find_cycle-jgrapht) | `CycleDetector` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-find_cycle-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: find\_cycle.
- <a id="why-find_cycle-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: digraph\_find\_cycle.
- <a id="why-find_cycle-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: get\_cycles.
- <a id="why-find_cycle-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: CycleDetector.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cyc_find_cycle` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(M) as (key, 0) pairs, nothing on NetworkXNoCycle` |  |
| `cyc_find_cycle_ignore` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(M, orientation = 'ignore') as (key, reversed) pairs` |  |
| `cyc_find_cycle_reverse` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(M, orientation = 'reverse') as (key, reversed) pairs` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [tool_rustworkx](../../references.html#tool_rustworkx), [tool_sknetwork](../../references.html#tool_sknetwork)

## Nxs find cycle {#nxs_find_cycle}

Measure id: `nxs_find_cycle`. Original family: Graph theory and combinatorics.

**Definition.** Nxs find cycle.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_find_cycle_ignore` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(D, orientation = 'ignore'), with 1 for an edge reported 'reverse'` |  |
| `nxs_find_cycle_ignore_source` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(D, source = n // 2, orientation = 'ignore')` |  |
| `nxs_find_cycle_none` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(G) on the simple graph with loops (the cycle's edges; (-1, -1) if none)` |  |
| `nxs_find_cycle_none_source` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(G, source = n // 2)` |  |
| `nxs_find_cycle_original` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(D, orientation = 'original')` |  |
| `nxs_find_cycle_reverse` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(D, orientation = 'reverse'), with 1 for an edge reported 'reverse'` |  |
| `nxs_find_cycle_reverse_source` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(D, source = n // 2, orientation = 'reverse')` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
