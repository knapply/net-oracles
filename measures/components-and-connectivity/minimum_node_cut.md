---
title: "Minimum node cut"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Minimum node cut {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Cuts and separators. Concept id: `minimum_node_cut`. 3 measures.

## Definition {#concept-definition}

A smallest set of nodes whose removal disconnects the network.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Min node cut](#min_node_cut) | `min_node_cut` | 1 |
| [Node cut](#node_cut) | `node_cut` | 3 |
| [St node cut](#st_node_cut) | `st_node_cut` | 1 |

## References {#concept-references}

[esfahanian1984computing](../../references.html#esfahanian1984computing), [even1975algorithm](../../references.html#even1975algorithm), [even1975network](../../references.html#even1975network), [ford1956maximal](../../references.html#ford1956maximal), [hagberg2008exploring](../../references.html#hagberg2008exploring), [menger1927allgemeinen](../../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../../references.html#schnorr1979bottlenecks)

## Min node cut {#min_node_cut}

Measure id: `min_node_cut`. Original family: Components and connectivity.

**Definition.** Min node cut.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `flow_min_node_cut` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.connectivity.minimum_st_node_cut(G, 0, n - 1)) on the simple graph; -1 if G.has_edge(0, n - 1)` |  |
| `flow_min_node_cut_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.minimum_cut_value(H, '0B', '(n-1)A') on the split digraph H: arcs vA -> vB of capacity (v mod 3) + 1 and uB -> vA for each arc u -> v without a capacity (infinite)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Node cut {#node_cut}

Measure id: `node_cut`. Original family: Components and connectivity.

**Definition.** A smallest set of nodes whose removal disconnects the network.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `minimum_edge_cut; minimum_node_cut; minimum_st_edge_cut; minimum_st_node_cut` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `is_min_separator; is_separator; min_separators; min_st_separators; stCuts; st_cuts; st_min_cuts` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `all_minimal_st_separators; all_st_cuts; all_st_mincuts; is_minimal_separator; is_separator; minimum_size_separators` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_node_cut` | NetworkX | any | no-value-on-some-inputs | (no value) disconnected | defaults | abs 0, rel 0 | `[len(nx.minimum_node_cut(G)), 1]` | NetworkX raises an error for a network that is not connected; the reference returns the empty cut. |
| `conn_node_cut_networkx` | NetworkX | any | no-value-on-some-inputs | (no value) disconnected | defaults | abs 0, rel 0 | `[len(nx.minimum_node_cut(G)), 1]` | as for conn\_node\_cut |

**References:** [esfahanian1984computing](../../references.html#esfahanian1984computing), [even1975algorithm](../../references.html#even1975algorithm), [even1975network](../../references.html#even1975network), [ford1956maximal](../../references.html#ford1956maximal), [hagberg2008exploring](../../references.html#hagberg2008exploring), [menger1927allgemeinen](../../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../../references.html#schnorr1979bottlenecks)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## St node cut {#st_node_cut}

Measure id: `st_node_cut`. Original family: Components and connectivity.

**Definition.** St node cut.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_st_node_cut` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `[len(nx.connectivity.minimum_st_node_cut(G, 0, n - 1)), 1]; -1 if G.has_edge(0, n - 1)` |  |
| `conn_st_node_cut_networkx` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted(nx.connectivity.minimum_st_node_cut(G, 0, n - 1))` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
