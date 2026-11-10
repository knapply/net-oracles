---
title: "Cnx edge betweenness"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Cnx edge betweenness

Family: Communities. Identifier: `cnx_edge_betweenness`.

## Definition

Component labels after removing the most central edges one at a time until at least k components exist (NetworkX's edge betweenness partition).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_edge_betweenness_partition` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.community.edge_betweenness_partition(G, 3) on the simple undirected graph (-1 when n < 3)` |  |

## References

[brandes2001faster](../references.html#brandes2001faster), [chen2014extension](../references.html#chen2014extension), [clauset2004finding](../references.html#clauset2004finding), [cordasco2010community](../references.html#cordasco2010community), [fortunato2010community](../references.html#fortunato2010community), [girvan2002community](../references.html#girvan2002community), [hagberg2008exploring](../references.html#hagberg2008exploring), [kernighan1970efficient](../references.html#kernighan1970efficient)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
