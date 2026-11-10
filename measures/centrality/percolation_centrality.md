---
title: "Percolation centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Percolation centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Betweenness, load and flow. Concept id: `percolation_centrality`. 1 measure.

## Definition {#concept-definition}

Percolation centrality of every node for given percolation states (Piraveenan, Prokopenko and Hossain 2013).

## References {#concept-references}

[brandes2001faster](../../references.html#brandes2001faster), [brandes2007centrality](../../references.html#brandes2007centrality), [brandes2008variants](../../references.html#brandes2008variants), [goh2001universal](../../references.html#goh2001universal), [piraveenan2013percolation](../../references.html#piraveenan2013percolation)

## Percolation {#cx_percolation}

Measure id: `cx_percolation`. Original family: Centrality.

**Definition.** Percolation centrality of every node for given percolation states (Piraveenan, Prokopenko and Hossain 2013).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `percolation_centrality` |  |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `vertex_percolation` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_percolation` | NetworkX | any | no-value-on-some-inputs | (no value) one\_node | defaults, multi\_edges | abs 1e-12, rel 1e-09 | `nx.percolation_centrality(G, states = {v: ((37 v) mod 11) / 10})` | With one node NetworkX multiplies by 1/(n - 2) = -1 and returns -0; the measure is undefined for n &lt;= 2 and the reference returns NaN (NetworkX raises ZeroDivisionError for n = 2, which the oracle records as undefined). |
| `cx_percolation_weighted` | NetworkX | any | no-value-on-some-inputs | (no value) one\_node | defaults, multi\_edges | abs 1e-12, rel 1e-09 | `nx.percolation_centrality(G, states = ..., weight = 'weight')` | With one node NetworkX multiplies by 1/(n - 2) = -1 and returns -0; the measure is undefined for n &lt;= 2 and the reference returns NaN (NetworkX raises ZeroDivisionError for n = 2, which the oracle records as undefined). |

**References:** [brandes2001faster](../../references.html#brandes2001faster), [brandes2007centrality](../../references.html#brandes2007centrality), [brandes2008variants](../../references.html#brandes2008variants), [goh2001universal](../../references.html#goh2001universal), [piraveenan2013percolation](../../references.html#piraveenan2013percolation)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
