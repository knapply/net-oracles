---
title: "Group / degree"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Group / degree

Family: Centrality. Identifier: `group:degree`.

## Definition

Group degree, closeness or betweenness of a set of nodes (Everett and Borgatti).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `group_degree_centrality; group_in_degree_centrality` |  |
| [NetworKit](../tools/networkit.html) | ✓ checked, agrees | `GroupDegree` |  |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `digraph_group_degree_centrality; graph_group_degree_centrality; group_degree_centrality` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `group_degree` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-14 | `nx.group_degree_centrality(G, C) (out-neighbours in directed graphs: nx.group_out_degree_centrality)` | The group is the only node, so there are no non-members (division by zero). |
| `group_degree` | NetworKit | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-14 | `nk.centrality.GroupDegree(G, k = 3, countGroupNodes = False).scoreOfGroup(S) / (n - \|S\|)` |  |
| `group_degree_all` | NetworkX | directed | agrees |  |  | abs 0, rel 1e-14 | `nx.group_degree_centrality(G.to_undirected(), C)` |  |
| `group_degree_in` | NetworkX | directed | agrees |  |  | abs 0, rel 1e-14 | `nx.group_in_degree_centrality(G, C)` |  |
| `group_degree_in` | NetworKit | directed | no-value-on-some-inputs |  |  | abs 0, rel 1e-14 | `nk.centrality.GroupDegree(reversed G, k = 3, countGroupNodes = False).scoreOfGroup(S) / (n - \|S\|)` |  |

## References

[borgatti2006identifying](../references.html#borgatti2006identifying), [brandes2008variants](../references.html#brandes2008variants), [dinic1970algorithm](../references.html#dinic1970algorithm), [everett1999centrality](../references.html#everett1999centrality), [everton2012disrupting](../references.html#everton2012disrupting), [ford1956maximal](../references.html#ford1956maximal), [freeman1991centrality](../references.html#freeman1991centrality), [koschutzki2005centrality](../references.html#koschutzki2005centrality)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
