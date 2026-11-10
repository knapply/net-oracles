---
title: "Group betweenness centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Group betweenness centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Betweenness, load and flow. Concept id: `group_betweenness`. 1 measure.

## Definition {#concept-definition}

Group degree, closeness or betweenness of a set of nodes (Everett and Borgatti).

## References {#concept-references}

[borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

## Group / betweenness {#group-betweenness}

Measure id: `group:betweenness`. Original family: Centrality.

**Definition.** Group degree, closeness or betweenness of a set of nodes (Everett and Borgatti).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges and weights): NetworkX counts parallel edges as one path. [details](#why-group-betweenness-networkx) | `group_betweenness_centrality` |  |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-group-betweenness-rustworkx) | `digraph_group_betweenness_centrality; graph_group_betweenness_centrality; group_betweenness_centrality` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-group-betweenness-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (multi-edges and weights) on inputs tagged fractional\_weights and multi\_edges. group\_betweenness: NetworkX counts parallel edges as one path; the reference counts them as distinct shortest paths, as igraph's betweenness does. group\_betweenness\_raw: NetworkX counts parallel edges as one path. group\_betweenness\_weighted: NetworkX keeps one edge per pair of nodes; and it compares floating- point path lengths exactly, so with non-integer weights a path can be counted or dropped by rounding (306 against 310 paths on real\_weights\_dir; 7 against 6 on an 8-node digraph, where integer weights scaled by 1e6 give 6: a NetworkX defect). The definition oracle, in exact arithmetic, agrees with the reference. Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 1e-14, rel 1e-12 on all 4 comparisons where the difference occurs. Tolerance before mapping: abs 1e-14, rel 1e-12; abs 1e-12, rel 1e-09 (0 means exact equality). 4 comparisons differ and 53 agree. Finding F001 (defect): group\_betweenness\_centrality compares float path lengths exactly. Finding F030 (defect): group\_betweenness\_centrality can vary with PYTHONHASHSEED. Findings: [F001](../../findings.html#f001), [F030](../../findings.html#f030).
- <a id="why-group-betweenness-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: digraph\_group\_betweenness\_centrality; graph\_group\_betweenness\_centrality; group\_betweenness\_centrality.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `group_betweenness` | NetworkX | any | differs | multi\_edges | multi\_edges | abs 1e-14, rel 1e-12 | `nx.group_betweenness_centrality(G, C, normalized = True) on the simple graph` | NetworkX counts parallel edges as one path; the reference counts them as distinct shortest paths, as igraph's betweenness does. NetworkX requires at least two non-members. |
| `group_betweenness_raw` | NetworkX | any | differs | multi\_edges | multi\_edges | abs 1e-14, rel 1e-12 | `nx.group_betweenness_centrality(G, C, normalized = False) on the simple graph` | NetworkX counts parallel edges as one path. NetworkX requires at least two non-members. |
| `group_betweenness_weighted` | NetworkX | any | differs | fractional\_weights, multi\_edges | multi\_edges, weights | abs 1e-12, rel 1e-09 | `nx.group_betweenness_centrality(G, C, normalized = False, weight = 'weight')` | The definition oracle, in exact arithmetic, agrees with the reference. NetworkX compares floating-point path lengths exactly, so paths whose non-integer lengths are equal in exact arithmetic can compare unequal and be dropped (306 against 310 paths on real\_weights\_dir). The definition oracle, in exact arithmetic, agrees with the reference there. (the oracle script skips these fixtures; on other graphs the tag declarations apply) |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F001](../../findings.html#f001) | NetworkX | defect | group\_betweenness\_centrality compares float path lengths exactly |
| [F030](../../findings.html#f030) | NetworkX | defect | group\_betweenness\_centrality can vary with PYTHONHASHSEED |

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
