---
title: "Incidence matrix"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Incidence matrix {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Graph matrices. Concept id: `incidence_matrix`. 1 measure.

## Definition {#concept-definition}

Incidence matrix. Entries grouped here: Incidence.

## Incidence {#gm_incidence}

Measure id: `gm_incidence`. Original family: Matrices and spectra.

**Definition.** Incidence.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `biadjacency_matrix; incidence_matrix` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `as_biadjacency_matrix; as_incidence_matrix` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `get_biadjacency` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `incidence` | API listing |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `bipartite` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gm_incidence` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.incidence_matrix(G, edgelist = the fixture's edges in order).toarray()` |  |
| `gm_incidence_oriented_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.incidence_matrix(G, edgelist = the fixture's edges, oriented = True, weight = 'weight').toarray()` |  |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
