---
title: "Burt constraint"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Burt constraint {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Structural holes and brokerage. Concept id: `burt_constraint`. 1 measure.

## Definition {#concept-definition}

Burt constraint. Entries grouped here: Constraint.

## Constraint {#constraint}

Measure id: `constraint`. Original family: Roles and positions.

**Definition.** Constraint.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention | `constraint; local_constraint` |  |
| [igraph (R)](../../tools/igraph.html) | ✓ checked, agrees | `constraint` |  |
| [igraph (Python)](../../tools/pyigraph.html) | ✓ checked, agrees | `constraint` |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `constraint` | published documentation |
| [manynet](../../tools/manynet.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `constraint` | NetworkX | any | differs | loops | self\_loops, ties | abs 1e-12, rel 1e-12 | `nx.constraint(MultiGraph \| MultiDiGraph)` | NetworkX keeps self-loops in the adjacency matrix, so a loop adds to the node's total tie volume and lowers every p\_ij. Burt's measure concerns ties to others; this reference and igraph ignore loops. |
| `constraint` | igraph (R) | any | differs | loops | defaults, self\_loops, ties | abs 1e-12, rel 1e-12 | `igraph::constraint(g) on a copy without the weight attribute` | A node whose only tie is a self-loop has no neighbours, so Burt's constraint is undefined for the reference and the definition oracle; igraph reports 0. |
| `constraint` | igraph (Python) | any | differs | loops | defaults, self\_loops, ties | abs 1e-12, rel 1e-12 | `python-igraph: gu.constraint()` | A node whose only tie is a self-loop has no neighbours, so Burt's constraint is undefined for the reference and the definition oracle; python-igraph reports 0. |
| `constraint` | manynet | any | differs | isolates | defaults, self\_loops, ties | abs 1e-12, rel 1e-12 | `manynet::node_constraint(g) (node_by_constraint in newer versions)` | A node without ties to other nodes (one whose only tie is a self-loop) has undefined constraint for the reference and the definition oracle; manynet reports 0. |
| `constraint_weighted` | NetworkX | any | differs | loops | defaults, self\_loops, ties, weights | abs 1e-12, rel 1e-12 | `nx.constraint(G, weight = 'weight')` | A node whose only tie is a self-loop has no neighbours, so Burt's constraint is undefined for the reference and the definition oracle; NetworkX counts the loop as a tie to itself (4 for one loop of weight 2). |
| `constraint_weighted` | igraph (R) | any | differs | loops | defaults, self\_loops, ties | abs 1e-12, rel 1e-12 | `igraph::constraint(g, weights = E(g)$weight)` | A node whose only tie is a self-loop has no neighbours, so Burt's constraint is undefined for the reference and the definition oracle; igraph reports 0. |
| `constraint_weighted` | igraph (Python) | any | differs | loops | defaults, self\_loops, ties | abs 1e-12, rel 1e-12 | `python-igraph: g.constraint(weights=w)` | A node whose only tie is a self-loop has no neighbours, so Burt's constraint is undefined for the reference and the definition oracle; python-igraph reports 0. |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_manynet](../../references.html#tool_manynet)
{% endraw %}
