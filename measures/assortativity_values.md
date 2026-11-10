---
title: "Assortativity values"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Assortativity values

Family: Mixing and assortativity. Identifier: `assortativity_values`.

## Definition

Assortativity values.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `attribute_assortativity_coefficient; degree_assortativity_coefficient; numeric_assortativity_coefficient` |  |
| [igraph (R)](../tools/igraph.html) | ∅ checked, no value on some inputs | `assortativity; assortativity_degree; assortativity_nominal` |  |
| [igraph (Python)](../tools/pyigraph.html) | ✓ checked, agrees | `assortativity; assortativity_degree; assortativity_nominal` |  |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `assortativity; scalar_assortativity` | API listing |
| [NetworKit](../tools/networkit.html) | · reported in docs | `Assortativity` | API listing |
| [BCT (Octave)](../tools/bct.html) | · reported in docs | `assortativity_bin; assortativity_wei` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `assortativity_covariance` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `igraph::assortativity(g, values, directed = TRUE, normalized = FALSE)` |  |
| `assortativity_covariance` | igraph (Python) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `python-igraph: [g.assortativity( [(7 * v) % 11 for v in v0], directed=True, normalized=False)],` |  |
| `assortativity_values` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `igraph::assortativity(g, values = (7 * (0:(n - 1))) %% 11, directed = TRUE)` |  |
| `assortativity_values` | igraph (Python) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `python-igraph: [g.assortativity([(7 * v) % 11 for v in v0], directed=True)]` |  |
| `assortativity_values_in` | igraph (R) | directed | agrees |  |  | abs 1e-12, rel 1e-10 | `igraph::assortativity(g, values = 7v mod 11, values.in = 3v mod 5, directed = TRUE)` |  |
| `assortativity_values_in` | igraph (Python) | directed | agrees |  |  | abs 1e-12, rel 1e-10 | `python-igraph: [g.assortativity( [(7 * v) % 11 for v in v0], [(3 * v) % 5 for v in v0], directed=True)]` |  |
| `assortativity_values_networkx` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-10 | `nx.numeric_assortativity_coefficient(MultiGraph/MultiDiGraph, 'value')` |  |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [rubinov2010complex](../references.html#rubinov2010complex), [staudt2016networkit](../references.html#staudt2016networkit)
{% endraw %}
