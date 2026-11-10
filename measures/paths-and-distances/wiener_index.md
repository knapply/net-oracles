---
title: "Wiener index"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Wiener index {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Distance summaries. Concept id: `wiener_index`. 1 measure.

## Definition {#concept-definition}

Sum of the distances over unordered pairs (ordered pairs in a directed network); infinite unless connected.

## References {#concept-references}

[gutman1994selected](../../references.html#gutman1994selected), [hage1995eccentricity](../../references.html#hage1995eccentricity), [klein1995hyper](../../references.html#klein1995hyper), [koschutzki2005centrality](../../references.html#koschutzki2005centrality), [latora2001efficient](../../references.html#latora2001efficient), [marchiori2000harmony](../../references.html#marchiori2000harmony), [randic1993novel](../../references.html#randic1993novel), [schultz1989topological](../../references.html#schultz1989topological)

## Index {#dm_index}

Measure id: `dm_index`. Original family: Paths and distances.

**Definition.** Sum of the distances over unordered pairs (ordered pairs in a directed network); infinite unless connected.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `gutman_index; hyper_wiener_index; schultz_index; wiener_index` |  |
| [BCT (Octave)](../../tools/bct.html) | ≠ checked, differs by convention |  |  |
| [bctpy](../../tools/bctpy.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dm_global_efficiency` | NetworkX | any | no-value-on-some-inputs | (no value) directed | direction | abs 1e-12, rel 1e-12 | `nx.global_efficiency(G)` | NetworkX's global\_efficiency is not implemented for directed graphs. |
| `dm_global_efficiency` | BCT (Octave) | any | differs |  | defaults | abs 1e-12, rel 1e-12 | `Brain Connectivity Toolbox 2019-03-03 in Octave: efficiency_bin, on the binary adjacency matrix without loops or parallel edges` | The efficiency of a one-node network is 0/0: BCT returns NaN, the reference 0. |
| `dm_global_efficiency` | bctpy | any | no-value-on-some-inputs |  | defaults, normalization | abs 1e-12, rel 1e-12 | `bct.efficiency_bin(A binary, local = False)` | With one node efficiency\_bin() divides by n (n - 1) = 0 and returns NaN; the reference (like NetworkX) returns 0. |
| `dm_global_efficiency_weighted` | bctpy | any | agrees |  |  | abs 1e-12, rel 1e-12 | `bct.efficiency_wei(W summed, local = False)` |  |
| `dm_gutman` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `nx.gutman_index(G)` | NetworkX's schultz\_index, gutman\_index, and hyper\_wiener\_index are not implemented for multigraphs. |
| `dm_gutman_weighted` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `nx.gutman_index(G, weight = 'weight')` | NetworkX's schultz\_index, gutman\_index, and hyper\_wiener\_index are not implemented for multigraphs. |
| `dm_harmonic_diameter` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.harmonic_diameter(G)` |  |
| `dm_harmonic_diameter_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.harmonic_diameter(G, weight = 'weight')` |  |
| `dm_hyper_wiener` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `0.5 * nx.hyper_wiener_index(G)` | NetworkX's hyper\_wiener\_index is not implemented for multigraphs. |
| `dm_hyper_wiener_networkx` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `nx.hyper_wiener_index(G)` | NetworkX's schultz\_index, gutman\_index, and hyper\_wiener\_index are not implemented for multigraphs. |
| `dm_schultz` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `nx.schultz_index(G)` | NetworkX's schultz\_index, gutman\_index, and hyper\_wiener\_index are not implemented for multigraphs. |
| `dm_schultz_weighted` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `nx.schultz_index(G, weight = 'weight')` | NetworkX's schultz\_index, gutman\_index, and hyper\_wiener\_index are not implemented for multigraphs. |
| `dm_wiener` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.wiener_index(G)` |  |
| `dm_wiener_strength` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.wiener_index(G, weight = 'length') with length = 1 / weight` |  |
| `dm_wiener_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.wiener_index(G, weight = 'weight')` |  |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F023](../../findings.html#f023) | NetworkX | defect | hyper\_wiener\_index is twice the published value |

**References:** [gutman1994selected](../../references.html#gutman1994selected), [hage1995eccentricity](../../references.html#hage1995eccentricity), [klein1995hyper](../../references.html#klein1995hyper), [koschutzki2005centrality](../../references.html#koschutzki2005centrality), [latora2001efficient](../../references.html#latora2001efficient), [marchiori2000harmony](../../references.html#marchiori2000harmony), [randic1993novel](../../references.html#randic1993novel), [schultz1989topological](../../references.html#schultz1989topological)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [rubinov2010complex](../../references.html#rubinov2010complex)
{% endraw %}
