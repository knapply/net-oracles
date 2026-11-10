---
title: "Group closeness centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Group closeness centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Distance-based. Concept id: `group_closeness`. 1 measure.

## Definition {#concept-definition}

Group degree, closeness or betweenness of a set of nodes (Everett and Borgatti).

## References {#concept-references}

[borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

## Group / closeness {#group-closeness}

Measure id: `group:closeness`. Original family: Centrality.

**Definition.** Group degree, closeness or betweenness of a set of nodes (Everett and Borgatti).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `group_closeness_centrality` |  |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `GroupCloseness` |  |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-group-closeness-rustworkx) | `digraph_group_closeness_centrality; graph_group_closeness_centrality; group_closeness_centrality` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-group-closeness-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: digraph\_group\_closeness\_centrality; graph\_group\_closeness\_centrality; group\_closeness\_centrality.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `group_closeness` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.group_closeness_centrality(G.reverse(), C) for directed graphs (NetworkX measures distances to the group)` |  |
| `group_closeness` | NetworKit | any | agrees |  |  | abs 0, rel 1e-12 | `nk.centrality.GroupCloseness(G, k = 3).scoreOfGroup(S)` |  |
| `group_closeness_in` | NetworkX | directed | agrees |  |  | abs 0, rel 1e-12 | `nx.group_closeness_centrality(G, C)` |  |
| `group_closeness_in` | NetworKit | directed | agrees |  |  | abs 0, rel 1e-12 | `nk.centrality.GroupCloseness(reversed G, k = 3).scoreOfGroup(S)` |  |
| `group_closeness_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.group_closeness_centrality(G (reversed if directed), C, weight = 'weight')` |  |
| `group_closeness_weighted` | NetworKit | any | agrees |  |  | abs 0, rel 1e-12 | `nk.centrality.GroupCloseness(G_weighted, k = 3).scoreOfGroup(S)` |  |

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
