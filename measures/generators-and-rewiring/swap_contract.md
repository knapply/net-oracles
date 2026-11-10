---
title: "Edge swap and contract"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Edge swap and contract {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Rewiring and randomization. Concept id: `swap_contract`. 1 measure.

## Definition {#concept-definition}

Connectivity-preserving double edge swaps of a connected undirected network, as the rewired edge list and the number of swaps kept.

## References {#concept-references}

[colizza2006detecting](../../references.html#colizza2006detecting), [erdos2010simple](../../references.html#erdos2010simple), [hagberg2008exploring](../../references.html#hagberg2008exploring), [humphries2008network](../../references.html#humphries2008network), [maslov2002specificity](../../references.html#maslov2002specificity), [sporns2004small](../../references.html#sporns2004small), [telesford2011ubiquity](../../references.html#telesford2011ubiquity), [zhou2004rich](../../references.html#zhou2004rich)

## Swap contract {#swap_contract}

Measure id: `swap_contract`. Original family: Generators and rewiring.

**Definition.** Connectivity-preserving double edge swaps of a connected undirected network, as the rewired edge list and the number of swaps kept.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `connected_double_edge_swap; directed_edge_swap; double_edge_swap` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `rewire` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `rewire` | API listing |
| [sna](../../tools/sna.html) | · reported in docs | `rewire.ud` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `random_rewire` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `Curveball; CurveballGlobalTradeGenerator; CurveballUniformTradeGenerator; DegreePreservingShuffle; EdgeSwitching; EdgeSwitchingInPlace; EdgeSwitchingMarkovChainGenerator; GlobalCurveball` | API listing |
| [BCT (Octave)](../../tools/bct.html) | · reported in docs | `null_model_dir_sign; null_model_und_sign; randmio_dir; randmio_dir_connected; randmio_dir_signed; randmio_und; randmio_und_connected; randmio_und_signed; randomize_graph_partial_und; randomizer_bin_und` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `reference_lattice` | NetworkX | undirected | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nx.lattice_reference(G, niter = 2, seed = 7), contract checked on its result` | every draw on a star is rejected and NetworkX redraws forever; the reference stops each round after 100 (m + 1) rejected draws |
| `reference_random` | NetworkX | undirected | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nx.random_reference(G, niter = 2, seed = 7), contract checked on its result` | every draw on a star is rejected and NetworkX redraws forever; the reference stops each round after 100 (m + 1) rejected draws |
| `swap_connected` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.connected_double_edge_swap(G, nswap = 20, seed = 7), contract checked on its result` |  |
| `swap_directed` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.directed_edge_swap(G, nswap = 5, max_tries = 500, seed = 7), contract checked on its result` |  |
| `swap_double` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.double_edge_swap(G, nswap = 10, max_tries = 1000, seed = 7), contract checked on its result` |  |

**References:** [colizza2006detecting](../../references.html#colizza2006detecting), [erdos2010simple](../../references.html#erdos2010simple), [hagberg2008exploring](../../references.html#hagberg2008exploring), [humphries2008network](../../references.html#humphries2008network), [maslov2002specificity](../../references.html#maslov2002specificity), [sporns2004small](../../references.html#sporns2004small), [telesford2011ubiquity](../../references.html#telesford2011ubiquity), [zhou2004rich](../../references.html#zhou2004rich)

**Tools cited:** [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [rubinov2010complex](../../references.html#rubinov2010complex), [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
