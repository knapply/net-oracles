---
title: "Modularity matrix"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Modularity matrix {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Graph matrices. Concept id: `modularity_matrix`. 1 measure.

## Definition {#concept-definition}

Modularity matrix. Entries grouped here: Gm modularity.

## Gm modularity {#gm_modularity}

Measure id: `gm_modularity`. Original family: Matrices and spectra.

**Definition.** Gm modularity.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `directed_modularity_matrix; modularity_matrix` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `modularity_matrix` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `modularity_matrix` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `modularity_matrix` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gm_modularity` | NetworkX | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `nx.modularity_matrix(G) or nx.directed_modularity_matrix(G)` | NetworkX does not implement the modularity matrices for multigraphs. |
| `gm_modularity_weighted` | NetworkX | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `nx.modularity_matrix(G, weight = 'weight') or the directed version` | NetworkX does not implement the modularity matrices for multigraphs. |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
