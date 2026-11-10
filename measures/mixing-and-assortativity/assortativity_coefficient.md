---
title: "Assortativity coefficient"
layout: default
parent: "Mixing and assortativity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Assortativity coefficient {#concept-top}

Family: [Mixing and assortativity](index.html). Subfamily: Assortativity. Concept id: `assortativity_coefficient`. 4 measures.

## Definition {#concept-definition}

Assortativity coefficient. Entries grouped here: Assort; Assortativity degree; Assortativity nominal; Assortativity values.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Assort](#assort) | `assort` | 3 |
| [Assortativity degree](#assortativity_degree) | `assortativity_degree` | 4 |
| [Assortativity nominal](#assortativity_nominal) | `assortativity_nominal` | 4 |
| [Assortativity values](#assortativity_values) | `assortativity_values` | 6 |

## Assort {#assort}

Measure id: `assort`. Original family: Mixing and assortativity.

**Definition.** Assort.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `degree_pearson_correlation_coefficient` |  |
| [bctpy](../../tools/bctpy.html) | ≠ checked, differs by convention |  |  |
| [netseg](../../tools/netseg.html) | · reported in docs | `assort` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `assort_attribute` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.attribute_assortativity_coefficient(G, 'label')` |  |
| `assort_attribute_subset` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.attribute_assortativity_coefficient(G, 'label', nodes = even nodes)` |  |
| `assort_degree` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-08 | `nx.degree_assortativity_coefficient(G)` |  |
| `assort_degree` | bctpy | any | differs | multi\_edges, (no value) directed | direction, multi\_edges | abs 1e-12, rel 1e-09 | `bct.assortativity_bin(A binary, flag = 0)` | BCT works on the binary matrix, so parallel edges collapse and degrees count distinct neighbours; NetworkX and the reference count every edge. assortativity\_bin(flag = 0) is the undirected coefficient; directed fixtures are left to the definition and NetworkX oracles. |
| `assort_degree_in_in` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-08 | `nx.degree_assortativity_coefficient(G, x = 'in', y = 'in')` |  |
| `assort_degree_out_out` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-08 | `nx.degree_assortativity_coefficient(G, x = 'out', y = 'out')` |  |
| `assort_degree_pearson` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.degree_pearson_correlation_coefficient(G)` |  |
| `assort_degree_subset` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-08 | `nx.degree_assortativity_coefficient(G, nodes = even nodes)` |  |
| `assort_degree_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-08 | `nx.degree_assortativity_coefficient(G, weight = 'weight')` |  |
| `assort_degree_weighted` | bctpy | any | no-value-on-some-inputs | (no value) directed | direction | abs 1e-12, rel 1e-09 | `bct.assortativity_wei(W summed, flag = 0)` | assortativity\_wei(flag = 0) is the undirected coefficient; directed fixtures are not passed to it. |
| `assort_numeric` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.numeric_assortativity_coefficient(G, 'value')` |  |
| `assort_numeric_subset` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.numeric_assortativity_coefficient(G, 'value', nodes = even nodes)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [rubinov2010complex](../../references.html#rubinov2010complex), [tool_netseg](../../references.html#tool_netseg)

## Assortativity degree {#assortativity_degree}

Measure id: `assortativity_degree`. Original family: Mixing and assortativity.

**Definition.** Assortativity degree.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |
| [igraph (R)](../../tools/igraph.html) | ∅ checked, no value on some inputs |  |  |
| [igraph (Python)](../../tools/pyigraph.html) | ✓ checked, agrees |  |  |
| [BCT (Octave)](../../tools/bct.html) | ≠ checked, differs by convention |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `assortativity_degree` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-08 | `igraph::assortativity_degree(g, directed = TRUE)` |  |
| `assortativity_degree` | igraph (Python) | any | agrees |  |  | abs 1e-12, rel 1e-08 | `python-igraph: [g.assortativity_degree(directed=True)]` |  |
| `assortativity_degree` | BCT (Octave) | any | differs |  | defaults, direction, multi\_edges, self\_loops, ties, weights | abs 1e-12, rel 1e-10 | `Brain Connectivity Toolbox 2019-03-03 in Octave: assortativity_bin(A, 0 \| 1), on the binary adjacency matrix without loops or parallel edges` | BCT returns NaN where the degree variance is zero (regular networks, a single node); the reference returns no value there, so both are undefined. On directed networks BCT's assortativity\_bin(A, 1) is close to but not equal to the Pearson correlation of out-degree at the source and in-degree at the target over the arcs (differences of 0.1% to 14% on the four directed random/weighted fixtures; cause not identified), and it cannot count loops or parallel edges. |
| `assortativity_degree_networkx` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-08 | `nx.degree_assortativity_coefficient(MultiGraph/MultiDiGraph)` |  |
| `assortativity_degree_undirected` | igraph (R) | directed | agrees |  |  | abs 1e-12, rel 1e-08 | `igraph::assortativity_degree(g, directed = FALSE)` |  |
| `assortativity_degree_undirected` | igraph (Python) | directed | agrees |  |  | abs 1e-12, rel 1e-08 | `python-igraph: [g.assortativity_degree(directed=False)]` |  |
| `assortativity_degree_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-08 | `nx.degree_assortativity_coefficient(G, weight = 'weight')` |  |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F058](../../findings.html#f058) | BCT (Octave) | convention | Degree assortativity is NaN for regular networks; the directed variant differs from the Pearson correlation of out-degree at the source and in-degree at the target |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [rubinov2010complex](../../references.html#rubinov2010complex)

## Assortativity nominal {#assortativity_nominal}

Measure id: `assortativity_nominal`. Original family: Mixing and assortativity.

**Definition.** Assortativity nominal.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention |  |  |
| [igraph (R)](../../tools/igraph.html) | ∅ checked, no value on some inputs |  |  |
| [igraph (Python)](../../tools/pyigraph.html) | ✓ checked, agrees |  |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `categonethomophily; homophily` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `assortativity_modularity` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `igraph::assortativity_nominal(g, types, directed = TRUE, normalized = FALSE)` |  |
| `assortativity_nominal` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `igraph::assortativity_nominal(g, types = (0:(n - 1)) %% 3 + 1, directed = TRUE)` |  |
| `assortativity_nominal` | igraph (Python) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `python-igraph: [g.assortativity_nominal( [v % 3 for v in v0], directed=True)]` |  |
| `assortativity_nominal_networkx` | NetworkX | any | differs | edge\_case | defaults | abs 1e-12, rel 1e-10 | `nx.attribute_assortativity_coefficient(MultiGraph/MultiDiGraph, 'group')` | Without edges the mixing matrix is empty and the coefficient is 0 / 0; |
| `assortativity_nominal_undirected` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `igraph::assortativity_nominal(g, types, directed = FALSE)` |  |
| `assortativity_nominal_undirected` | igraph (Python) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `python-igraph: [g.assortativity_nominal( [v % 3 for v in v0], directed=False)]` |  |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F074](../../findings.html#f074) | igraph (Python) | limitation | assortativity\_nominal(normalized=False) raises SystemError; eigenvector\_centrality(directed=False) on a directed graph raises Invalid mode |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Assortativity values {#assortativity_values}

Measure id: `assortativity_values`. Original family: Mixing and assortativity.

**Definition.** Assortativity values.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `attribute_assortativity_coefficient; degree_assortativity_coefficient; numeric_assortativity_coefficient` |  |
| [igraph (R)](../../tools/igraph.html) | ∅ checked, no value on some inputs | `assortativity; assortativity_degree; assortativity_nominal` |  |
| [igraph (Python)](../../tools/pyigraph.html) | ✓ checked, agrees | `assortativity; assortativity_degree; assortativity_nominal` |  |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `assortativity; scalar_assortativity` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `Assortativity` | API listing |
| [BCT (Octave)](../../tools/bct.html) | · reported in docs | `assortativity_bin; assortativity_wei` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `assortativity_covariance` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `igraph::assortativity(g, values, directed = TRUE, normalized = FALSE)` |  |
| `assortativity_covariance` | igraph (Python) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `python-igraph: [g.assortativity( [(7 * v) % 11 for v in v0], directed=True, normalized=False)],` |  |
| `assortativity_values` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `igraph::assortativity(g, values = (7 * (0:(n - 1))) %% 11, directed = TRUE)` |  |
| `assortativity_values` | igraph (Python) | any | agrees |  |  | abs 1e-12, rel 1e-10 | `python-igraph: [g.assortativity([(7 * v) % 11 for v in v0], directed=True)]` |  |
| `assortativity_values_in` | igraph (R) | directed | agrees |  |  | abs 1e-12, rel 1e-10 | `igraph::assortativity(g, values = 7v mod 11, values.in = 3v mod 5, directed = TRUE)` |  |
| `assortativity_values_in` | igraph (Python) | directed | agrees |  |  | abs 1e-12, rel 1e-10 | `python-igraph: [g.assortativity( [(7 * v) % 11 for v in v0], [(3 * v) % 5 for v in v0], directed=True)]` |  |
| `assortativity_values_networkx` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-10 | `nx.numeric_assortativity_coefficient(MultiGraph/MultiDiGraph, 'value')` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [rubinov2010complex](../../references.html#rubinov2010complex), [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
