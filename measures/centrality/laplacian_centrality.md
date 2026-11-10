---
title: "Laplacian centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Laplacian centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `laplacian_centrality`. 1 measure.

## Definition {#concept-definition}

Laplacian centrality. Entries grouped here: Cx laplacian.

## Cx laplacian {#cx_laplacian}

Measure id: `cx_laplacian`. Original family: Centrality.

**Definition.** Cx laplacian.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `laplacian_centrality` |  |
| [NetworKit](../../tools/networkit.html) | ✓ checked, agrees | `LaplacianCentrality` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_laplacian` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.laplacian_centrality(G, weight = None)` |  |
| `cx_laplacian` | NetworKit | undirected | no-value-on-some-inputs |  |  | abs 1e-12, rel 1e-09 | `nk.centrality.LaplacianCentrality(G, normalized = True)` |  |
| `cx_laplacian_raw` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.laplacian_centrality(G, normalized = False, weight = None)` |  |
| `cx_laplacian_raw` | NetworKit | undirected | no-value-on-some-inputs |  |  | abs 1e-12, rel 1e-09 | `nk.centrality.LaplacianCentrality(G, normalized = False)` |  |
| `cx_laplacian_weighted` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.laplacian_centrality(G, weight = 'weight')` |  |
| `cx_laplacian_weighted` | NetworKit | undirected | no-value-on-some-inputs |  |  | abs 1e-12, rel 1e-09 | `nk.centrality.LaplacianCentrality(G_weighted, normalized = True)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
