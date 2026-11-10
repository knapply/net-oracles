---
title: "Compactness"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Compactness {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Efficiency, compactness and hierarchy. Concept id: `compactness`. 1 measure.

## Definition {#concept-definition}

Compactness. Entries grouped here: Compactness.

## Compactness {#compactness}

Measure id: `compactness`. Original family: Descriptive statistics.

**Definition.** Compactness.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |
| [igraph (R)](../../tools/igraph.html) | ✓ checked, agrees |  |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `compactness` | NetworkX | any | agrees |  |  | abs 1e-15, rel 1e-13 | `nx.global_efficiency (undirected), or mean of 1/d from nx.shortest_path_length (directed)` |  |
| `compactness` | igraph (R) | any | agrees |  |  | abs 1e-15, rel 1e-13 | `mean of 1 / igraph::distances(g, mode = 'out', weights = NA) off the diagonal` |  |
| `compactness_weighted` | NetworkX | any | agrees |  |  | abs 1e-15, rel 1e-12 | `mean of 1/d from nx.shortest_path_length(G, weight = 'weight')` |  |
| `compactness_weighted` | igraph (R) | any | agrees |  |  | abs 1e-15, rel 1e-12 | `mean of 1 / igraph::distances(g, mode = 'out', weights = E(g)$weight) off the diagonal` |  |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
