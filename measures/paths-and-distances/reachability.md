---
title: "Reachability"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Reachability {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Efficiency and reachability. Concept id: `reachability`. 3 measures.

## Definition {#concept-definition}

Reachability. Entries grouped here: Reachability; Reachable Nodes; Reachdist.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Reachability](#reachability) | `reachability` | 5 |
| [Reachable Nodes](#cat_reachable) | `cat_reachable` | 1 |
| [Reachdist](#cat_reachdist) | `cat_reachdist` | 1 |

## Reachability {#reachability}

Measure id: `reachability`. Original family: Paths and distances.

**Definition.** Reachability.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `has_path; is_reachable` |  |
| [igraph (R)](../../tools/igraph.html) | ✓ checked, agrees |  |  |
| [igraph (Python)](../../tools/pyigraph.html) | ✓ checked, agrees | `neighborhood_size` |  |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `digraph_has_path; graph_has_path; has_path` | API listing |
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `reachability` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.descendants(G, v)), or len(nx.node_connected_component(G, v)) - 1 if undirected` |  |
| `reachability` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = vcount(g), mode = 'out') - 1` |  |
| `reachability` | igraph (Python) | any | agrees |  |  | abs 0, rel 0 | `python-igraph: [x - 1 for x in gu.neighborhood_size(order=everything, mode="out")]` |  |
| `reachability_all` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `len(nx.node_connected_component(G.to_undirected(), v)) - 1` |  |
| `reachability_all` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = vcount(g), mode = 'all') - 1` |  |
| `reachability_all` | igraph (Python) | directed | agrees |  |  | abs 0, rel 0 | `python-igraph: [x - 1 for x in gu.neighborhood_size(order=everything, mode="all")]` |  |
| `reachability_in` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `len(nx.ancestors(G, v))` |  |
| `reachability_in` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = vcount(g), mode = 'in') - 1` |  |
| `reachability_in` | igraph (Python) | directed | agrees |  |  | abs 0, rel 0 | `python-igraph: [x - 1 for x in gu.neighborhood_size(order=everything, mode="in")]` |  |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)

## Reachable Nodes {#cat_reachable}

Measure id: `cat_reachable`. Original family: Paths and distances.

**Definition.** Reachable Nodes.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | · reported in docs | `ReachableNodes` | API listing |

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Reachdist {#cat_reachdist}

Measure id: `cat_reachdist`. Original family: Paths and distances.

**Definition.** Reachdist.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [BCT (Octave)](../../tools/bct.html) | · reported in docs | `reachdist` | API listing |

**Tools cited:** [rubinov2010complex](../../references.html#rubinov2010complex)
{% endraw %}
