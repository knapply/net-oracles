---
title: "Group / betweenness"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Group / betweenness

Family: Centrality. Identifier: `group:betweenness`.

## Definition

Group degree, closeness or betweenness of a set of nodes (Everett and Borgatti).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention | `group_betweenness_centrality` |  |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `digraph_group_betweenness_centrality; graph_group_betweenness_centrality; group_betweenness_centrality` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `group_betweenness` | NetworkX | any | differs | multi\_edges | multi\_edges | abs 1e-14, rel 1e-12 | `nx.group_betweenness_centrality(G, C, normalized = True) on the simple graph` | NetworkX counts parallel edges as one path; the reference counts them as distinct shortest paths, as igraph's betweenness does. NetworkX requires at least two non-members. |
| `group_betweenness_raw` | NetworkX | any | differs | multi\_edges | multi\_edges | abs 1e-14, rel 1e-12 | `nx.group_betweenness_centrality(G, C, normalized = False) on the simple graph` | NetworkX counts parallel edges as one path. NetworkX requires at least two non-members. |
| `group_betweenness_weighted` | NetworkX | any | differs | fractional\_weights, multi\_edges | multi\_edges, weights | abs 1e-12, rel 1e-09 | `nx.group_betweenness_centrality(G, C, normalized = False, weight = 'weight')` | The definition oracle, in exact arithmetic, agrees with the reference. NetworkX compares floating-point path lengths exactly, so paths whose non-integer lengths are equal in exact arithmetic can compare unequal and be dropped (306 against 310 paths on real\_weights\_dir). The definition oracle, in exact arithmetic, agrees with the reference there. (the oracle script skips these fixtures; on other graphs the tag declarations apply) |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F001](../findings.html#f001) | NetworkX | defect | group\_betweenness\_centrality compares float path lengths exactly |
| [F030](../findings.html#f030) | NetworkX | defect | group\_betweenness\_centrality can vary with PYTHONHASHSEED |

## References

[borgatti2006identifying](../references.html#borgatti2006identifying), [brandes2008variants](../references.html#brandes2008variants), [dinic1970algorithm](../references.html#dinic1970algorithm), [everett1999centrality](../references.html#everett1999centrality), [everton2012disrupting](../references.html#everton2012disrupting), [ford1956maximal](../references.html#ford1956maximal), [freeman1991centrality](../references.html#freeman1991centrality), [koschutzki2005centrality](../references.html#koschutzki2005centrality)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
