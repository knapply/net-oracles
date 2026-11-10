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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `degree_pearson_correlation_coefficient` |  |
| [bctpy](../../tools/bctpy.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction and multi-edges): BCT works on the binary matrix, so parallel edges collapse and degrees count distinct neighbours. [details](#why-assort-bctpy) |  |  |
| [netseg](../../tools/netseg.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: netseg is documented-only in this survey; listed in its documentation. [details](#why-assort-netseg) | `assort` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-assort-bctpy"></a>**[bctpy](../../tools/bctpy.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> bctpy 0.6.1 was run and its value differs from the reference value by convention (direction and multi-edges) on inputs tagged multi\_edges. BCT works on the binary matrix, so parallel edges collapse and degrees count distinct neighbours; NetworkX and the reference count every edge. Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 1e-12, rel 1e-09 on all 1 comparison where the difference occurs. Tolerance before mapping: abs 1e-12, rel 1e-09 (0 means exact equality). No value (assort\_degree\_weighted) on inputs tagged directed: assortativity\_wei(flag = 0) is the undirected coefficient; directed fixtures are not passed to it. 1 comparisons differ and 23 agree.
- <a id="why-assort-netseg"></a>**[netseg](../../tools/netseg.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. netseg (1.0-3) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of netseg 1.0-3: help topics.

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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction, multi-edges, self-loops, ties and weights): BCT returns NaN where the degree variance is zero (regular networks, a single node). *(reason incomplete)* [details](#why-assortativity_degree-bct) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-assortativity_degree-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> BCT (Octave) 2019-03-03 was run and its value differs from the reference value by convention (defaults, direction, multi-edges, self-loops, ties and weights) on the fixtures complete5\_dir, complete6, cycle7\_dir, empty, gnp\_dir\_dense, gnp\_dir\_sparse, multi\_loops\_dir, multi\_loops\_und, pair, real\_weights\_dir, single\_node, two\_triangles\_isolate, weighted\_dir. BCT returns NaN where the degree variance is zero (regular networks, a single node); the reference returns no value there, so both are undefined. On directed networks BCT's assortativity\_bin(A, 1) is close to but not equal to the Pearson correlation of out-degree at the source and in-degree at the target over the arcs (differences of 0.1% to 14% on the four directed random/weighted fixtures; cause not identified), and it cannot count loops or parallel edges. Relation to the reference value: Directed input, zero variance: NaN for regular networks (the reference returns no value); the directed variant is close to but not equal to the Pearson correlation of out-degree at the source and in-degree at the target (0.1% to 14%, cause not identified). Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 1e-12, rel 1e-10 on all 1 comparison where the difference occurs. Tolerance before mapping: abs 1e-12, rel 1e-10 (0 means exact equality). 13 comparisons differ and 15 agree. Finding F058 (convention): Degree assortativity is NaN for regular networks; the directed variant differs from the Pearson correlation of out-degree at the source and in-degree at the target. Findings: [F058](../../findings.html#f058). **Reason incomplete:** the cause of the difference is stated in the sources as not identified.

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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults): Without edges the mixing matrix is empty and the coefficient is 0 / 0. [details](#why-assortativity_nominal-networkx) |  |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-assortativity_nominal-ucinet) | `categonethomophily; homophily` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-assortativity_nominal-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (defaults) on inputs tagged edge\_case. Without edges the mixing matrix is empty and the coefficient is 0 / 0; NetworkX returns 0, the reference and igraph return NaN. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-10 (0 means exact equality). 2 comparisons differ and 42 agree.
- <a id="why-assortativity_nominal-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `attribute_assortativity_coefficient; degree_assortativity_coefficient; numeric_assortativity_coefficient` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `assortativity; assortativity_degree; assortativity_nominal` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `assortativity; assortativity_degree; assortativity_nominal` |  |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-assortativity_values-graphtool) | `assortativity; scalar_assortativity` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-assortativity_values-networkit) | `Assortativity` | API listing |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-assortativity_values-bct) | `assortativity_bin; assortativity_wei` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-assortativity_values-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: assortativity; scalar\_assortativity.
- <a id="why-assortativity_values-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: Assortativity.
- <a id="why-assortativity_values-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: assortativity\_bin; assortativity\_wei.

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
