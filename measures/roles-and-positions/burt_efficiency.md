---
title: "Burt efficiency"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Burt efficiency {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Structural holes and brokerage. Concept id: `burt_efficiency`. 1 measure.

## Definition {#concept-definition}

Burt efficiency. Entries grouped here: Efficiency.

## Efficiency {#efficiency}

Measure id: `efficiency`. Original family: Roles and positions.

**Definition.** Efficiency.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention |  |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |
| [manynet](../../tools/manynet.html) | ≠ checked, differs by convention |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `efficiency` | NetworkX | any | differs | loops | self\_loops | abs 1e-12, rel 1e-12 | `nx.effective_size(G) / number of distinct neighbours other than the node` | NetworkX keeps self-loops in the effective size (see effective\_size). |
| `efficiency` | manynet | any | differs | directed, edge\_case, loops, multi\_edges | defaults, direction, multi\_edges, normalization, self\_loops, ties | abs 1e-12, rel 1e-12 | `manynet::node_efficiency(g) (node_by_efficiency in newer versions)` | manynet (netrics) returns a different value from the reference on directed networks, on multigraphs with loops, and on the two-node network (about half the reference value's on a directed cycle and on directed random graphs); the cause was not traced. Simple undirected networks agree. |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_manynet](../../references.html#tool_manynet)
{% endraw %}
