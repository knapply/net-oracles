---
title: "Local node connectivity"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Local node connectivity {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connectivity numbers. Concept id: `local_node_connectivity`. 4 measures.

## Definition {#concept-definition}

Local node connectivity of every ordered pair, as an n-by-n matrix.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [All pairs node](#all_pairs_node) | `all_pairs_node` | 1 |
| [Ap local connectivity](#ap_local_connectivity) | `ap_local_connectivity` | 1 |
| [Average node](#average_node) | `average_node` | 2 |
| [Local connectivity](#local_connectivity) | `local_connectivity` | 1 |

## References {#concept-references}

[esfahanian1984computing](../../references.html#esfahanian1984computing), [even1975algorithm](../../references.html#even1975algorithm), [even1975network](../../references.html#even1975network), [ford1956maximal](../../references.html#ford1956maximal), [harary1969graph](../../references.html#harary1969graph), [menger1927allgemeinen](../../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../../references.html#schnorr1979bottlenecks)

## All pairs node {#all_pairs_node}

Measure id: `all_pairs_node`. Original family: Components and connectivity.

**Definition.** Local node connectivity of every ordered pair, as an n-by-n matrix.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_all_pairs_node` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.all_pairs_node_connectivity(G), with 0 on the diagonal` |  |

**References:** [esfahanian1984computing](../../references.html#esfahanian1984computing), [even1975algorithm](../../references.html#even1975algorithm), [even1975network](../../references.html#even1975network), [ford1956maximal](../../references.html#ford1956maximal), [harary1969graph](../../references.html#harary1969graph), [menger1927allgemeinen](../../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../../references.html#schnorr1979bottlenecks)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Ap local connectivity {#ap_local_connectivity}

Measure id: `ap_local_connectivity`. Original family: Graph theory and combinatorics.

**Definition.** Ap local connectivity.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_local_connectivity` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `[local_node_connectivity(G_sorted, 0, n - 1), local_node_connectivity(G_sorted, n - 1, 1, cutoff = 2)]` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Average node {#average_node}

Measure id: `average_node`. Original family: Components and connectivity.

**Definition.** Local node connectivity of every ordered pair, as an n-by-n matrix.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `vertex_average` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_average_node` | NetworkX | any | agrees |  |  | abs 0, rel 1e-14 | `nx.average_node_connectivity(G)` |  |

**References:** [esfahanian1984computing](../../references.html#esfahanian1984computing), [even1975algorithm](../../references.html#even1975algorithm), [even1975network](../../references.html#even1975network), [ford1956maximal](../../references.html#ford1956maximal), [harary1969graph](../../references.html#harary1969graph), [menger1927allgemeinen](../../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../../references.html#schnorr1979bottlenecks)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)

## Local connectivity {#local_connectivity}

Measure id: `local_connectivity`. Original family: Components and connectivity.

**Definition.** Local connectivity.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_local_edge` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.connectivity.local_edge_connectivity(G, 0, n - 1)` |  |
| `conn_local_node` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.connectivity.local_node_connectivity(G, 0, n - 1)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
