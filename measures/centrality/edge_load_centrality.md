---
title: "Edge load centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Edge load centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Betweenness, load and flow. Concept id: `edge_load_centrality`. 1 measure.

## Definition {#concept-definition}

Load on every edge: NetworkX's edge load centrality, over ordered pairs of adjacent nodes.

## References {#concept-references}

[brandes2001faster](../../references.html#brandes2001faster), [brandes2007centrality](../../references.html#brandes2007centrality), [brandes2008variants](../../references.html#brandes2008variants), [goh2001universal](../../references.html#goh2001universal), [piraveenan2013percolation](../../references.html#piraveenan2013percolation)

## Edge load {#cx_edge_load}

Measure id: `cx_edge_load`. Original family: Centrality.

**Definition.** Load on every edge: NetworkX's edge load centrality, over ordered pairs of adjacent nodes.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `edge_load_centrality` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_edge_load` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.edge_load_centrality(G), values for (u, v) and (v, u) of every edge` |  |
| `cx_edge_load_cutoff` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.edge_load_centrality(G, cutoff = 2)` |  |

**References:** [brandes2001faster](../../references.html#brandes2001faster), [brandes2007centrality](../../references.html#brandes2007centrality), [brandes2008variants](../../references.html#brandes2008variants), [goh2001universal](../../references.html#goh2001universal), [piraveenan2013percolation](../../references.html#piraveenan2013percolation)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
