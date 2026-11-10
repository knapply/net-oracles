---
title: "Cycle basis"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Cycle basis

Family: Graph theory and combinatorics. Identifier: `cycle_basis`.

## Definition

Cycle basis.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention | `cycle_basis` |  |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `cycle_basis` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `PatonCycleBase; QueueBFSFundamentalCycleBasis; StackBFSFundamentalCycleBasis` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cyc_basis` | NetworkX | undirected | differs | multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.cycle_basis(G), cycle for cycle, in order` | NetworkX's simple graph merges parallel edges and repeated loops, whose cycles the reference lists after NetworkX's basis (the basis of the multigraph has m - n + c cycles). |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
