---
title: "Dedensify and compression"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Dedensify and compression {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Spanners, contraction and reduction. Concept id: `dedensify`. 3 measures.

## Definition {#concept-definition}

Dedensify and compression. Entries grouped here: Dedensify; Quotient internal; Snap groups.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Dedensify](#gb_dedensify) | `gb_dedensify` | 1 |
| [Quotient internal](#gb_quotient_internal) | `gb_quotient_internal` | 1 |
| [Snap groups](#gb_snap_groups) | `gb_snap_groups` | 1 |

## Dedensify {#gb_dedensify}

Measure id: `gb_dedensify`. Original family: Traversal, trees and DAGs.

**Definition.** Dedensify.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `dedensify` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_dedensify` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.dedensify(M, 2)[1])` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Quotient internal {#gb_quotient_internal}

Measure id: `gb_quotient_internal`. Original family: Traversal, trees and DAGs.

**Definition.** Quotient internal.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_quotient_internal` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nedges of each block of nx.quotient_graph(M, parts)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Snap groups {#gb_snap_groups}

Measure id: `gb_snap_groups`. Original family: Traversal, trees and DAGs.

**Definition.** Snap groups.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `snap_aggregation` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_snap_groups` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.snap_aggregation(M, node_attributes=('parity',)).number_of_nodes()` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
