---
title: "Effective size"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Effective size {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Structural holes and brokerage. Concept id: `effective_size`. 1 measure.

## Definition {#concept-definition}

Effective size. Entries grouped here: Effective size.

## Effective size {#effective_size}

Measure id: `effective_size`. Original family: Roles and positions.

**Definition.** Effective size.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention | `effective_size` |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `structuralholes` | published documentation |
| [manynet](../../tools/manynet.html) | ≠ checked, differs by convention |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `effective_size` | NetworkX | any | differs | loops | self\_loops, ties | abs 1e-12, rel 1e-12 | `nx.effective_size(MultiGraph \| MultiDiGraph)` | NetworkX keeps self-loops in the adjacency matrix, so a loop adds to the node's tie volume and can be its strongest tie. This reference ignores loops. |
| `effective_size` | manynet | any | differs | directed, edge\_case, loops, multi\_edges | defaults, direction, multi\_edges, normalization, self\_loops, ties | abs 1e-12, rel 1e-12 | `manynet::node_effsize(g) (node_by_effsize in newer versions)` | manynet (netrics) returns a different value from the reference on directed networks, on multigraphs with loops, and on the two-node network (about half the reference value's on a directed cycle and on directed random graphs); the cause was not traced. Simple undirected networks agree. |
| `effective_size_weighted` | NetworkX | any | differs | loops | self\_loops, weights | abs 1e-12, rel 1e-12 | `nx.effective_size(G, weight = 'weight')` | Burt's effective size counts a node's neighbours; NetworkX's weighted formula also counts a neighbour's self-loop as redundancy (0.5 for node 0 of 1-0 plus a loop at 1, against 1). |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F025](../../findings.html#f025) | NetworkX | defect | effective\_size is wrong for weighted or directed graphs on its vectorized path |
| [F082](../../findings.html#f082) | manynet | defect | Effective size and efficiency differ on directed networks and multigraphs with loops |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_manynet](../../references.html#tool_manynet)
{% endraw %}
