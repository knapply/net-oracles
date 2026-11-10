---
title: "Assortativity nominal"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Assortativity nominal

Family: Mixing and assortativity. Identifier: `assortativity_nominal`.

## Definition

Assortativity nominal.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention |  |  |
| [igraph (R)](../tools/igraph.html) | ∅ checked, no value on some inputs |  |  |
| [igraph (Python)](../tools/pyigraph.html) | ✓ checked, agrees |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs | `categonethomophily; homophily` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `assortativity_modularity` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `igraph::assortativity_nominal(g, types, directed = TRUE, normalized = FALSE)` |  |
| `assortativity_nominal` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `igraph::assortativity_nominal(g, types = (0:(n - 1)) %% 3 + 1, directed = TRUE)` |  |
| `assortativity_nominal` | igraph (Python) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `python-igraph: [g.assortativity_nominal( [v % 3 for v in v0], directed=True)]` |  |
| `assortativity_nominal_networkx` | NetworkX | any | differs | edge\_case | defaults | abs 1e-12, rel 1e-10 | `nx.attribute_assortativity_coefficient(MultiGraph/MultiDiGraph, 'group')` | Without edges the mixing matrix is empty and the coefficient is 0 / 0; |
| `assortativity_nominal_undirected` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `igraph::assortativity_nominal(g, types, directed = FALSE)` |  |
| `assortativity_nominal_undirected` | igraph (Python) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `python-igraph: [g.assortativity_nominal( [v % 3 for v in v0], directed=False)]` |  |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F074](../findings.html#f074) | igraph (Python) | limitation | assortativity\_nominal(normalized=False) raises SystemError; eigenvector\_centrality(directed=False) on a directed graph raises Invalid mode |

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
