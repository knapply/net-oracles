---
title: "Node connectivity"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Node connectivity

Family: Graph theory and combinatorics. Identifier: `ap_node_connectivity`.

## Definition

Approximate node connectivity of the whole network by greedy node-disjoint shortest paths.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_node_connectivity` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.approximation.node_connectivity(G_sorted)` |  |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F031](../findings.html#f031) | NetworkX | defect | approximation.node\_connectivity starts from a bound that can exceed the connectivity |

## References

[baryehuda1985local](../references.html#baryehuda1985local), [bodlaender2010treewidth](../references.html#bodlaender2010treewidth), [boob2020flowless](../references.html#boob2020flowless), [boppana1992approximating](../references.html#boppana1992approximating), [hagberg2008exploring](../references.html#hagberg2008exploring), [vazirani2001approximation](../references.html#vazirani2001approximation), [white2001fast](../references.html#white2001fast)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
