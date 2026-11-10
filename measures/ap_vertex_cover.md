---
title: "Ap vertex cover"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Ap vertex cover

Family: Graph theory and combinatorics. Identifier: `ap_vertex_cover`.

## Definition

Local-ratio vertex cover of least node cost (2-approximation), as node ids.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [NetworKit](../tools/networkit.html) | · reported in docs | `Cover` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_vertex_cover` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted(nx.approximation.min_weighted_vertex_cover(G_sorted, weight = 'w')) with w(v) = v mod 4 + 1` |  |

## References

[baryehuda1985local](../references.html#baryehuda1985local), [bodlaender2010treewidth](../references.html#bodlaender2010treewidth), [boob2020flowless](../references.html#boob2020flowless), [boppana1992approximating](../references.html#boppana1992approximating), [hagberg2008exploring](../references.html#hagberg2008exploring), [vazirani2001approximation](../references.html#vazirani2001approximation), [white2001fast](../references.html#white2001fast)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [staudt2016networkit](../references.html#staudt2016networkit)
{% endraw %}
