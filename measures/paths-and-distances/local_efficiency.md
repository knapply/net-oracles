---
title: "Local efficiency"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Local efficiency {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Efficiency and reachability. Concept id: `local_efficiency`. 1 measure.

## Definition {#concept-definition}

Mean over the nodes of the global efficiency of the subgraph induced by each node's neighbors.

## References {#concept-references}

[gutman1994selected](../../references.html#gutman1994selected), [hage1995eccentricity](../../references.html#hage1995eccentricity), [klein1995hyper](../../references.html#klein1995hyper), [koschutzki2005centrality](../../references.html#koschutzki2005centrality), [latora2001efficient](../../references.html#latora2001efficient), [marchiori2000harmony](../../references.html#marchiori2000harmony), [randic1993novel](../../references.html#randic1993novel), [schultz1989topological](../../references.html#schultz1989topological)

## Local efficiency {#dm_local_efficiency}

Measure id: `dm_local_efficiency`. Original family: Paths and distances.

**Definition.** Mean over the nodes of the global efficiency of the subgraph induced by each node's neighbors.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, multi-edges, self-loops and ties): A bct call takes a binary adjacency matrix, which cannot carry loops or parallel edges: the driver keeps one arc per ordered pair and drops loops,... [details](#why-dm_local_efficiency-bct) |  |  |
| [bctpy](../../tools/bctpy.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (self-loops): This variant follows NetworkX in counting a self-loop as making a node its own neighbour. [details](#why-dm_local_efficiency-bctpy) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-dm_local_efficiency-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> BCT (Octave) 2019-03-03 was run and its value differs from the reference value by convention (direction, multi-edges, self-loops and ties) on the fixtures multi\_loops\_und. A bct call takes a binary adjacency matrix, which cannot carry loops or parallel edges: the driver keeps one arc per ordered pair and drops loops, while the reference counts every edge. Relation to the reference value: Loops, parallel edges: a binary adjacency matrix carries neither; degrees, coreness, local efficiency differ on the two multigraph fixtures. Mapping: the reference value computed with the tool's convention (a binary matrix has no diagonal) agrees with the tool within abs 1e-12, rel 1e-12 on all 1 comparison where the difference occurs. Tolerance before mapping: abs 1e-12, rel 1e-12 (0 means exact equality). 1 comparisons differ and 18 agree.
- <a id="why-dm_local_efficiency-bctpy"></a>**[bctpy](../../tools/bctpy.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> bctpy 0.6.1 was run and its value differs from the reference value by convention (self-loops) on inputs tagged loops. This variant follows NetworkX in counting a self-loop as making a node its own neighbour; BCT's matrix has no diagonal. Relation to the reference value: Loops, parallel edges: a binary adjacency matrix carries neither; degrees, coreness, local efficiency differ on the two multigraph fixtures. Mapping: the reference value computed with the tool's convention (a binary matrix has no diagonal) agrees with the tool within abs 1e-12, rel 1e-12 on all 1 comparison where the difference occurs. Tolerance before mapping: abs 1e-12, rel 1e-12 (0 means exact equality). 1 comparisons differ and 37 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dm_local_efficiency` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.local_efficiency(G)` |  |
| `dm_local_efficiency` | BCT (Octave) | undirected | differs |  | direction, multi\_edges, self\_loops, ties | abs 1e-12, rel 1e-12 | `Brain Connectivity Toolbox 2019-03-03 in Octave: mean(efficiency_bin(A, 1)), on the binary adjacency matrix without loops or parallel edges` | A bct call takes a binary adjacency matrix, which cannot carry loops or parallel edges: the driver keeps one arc per ordered pair and drops loops, while the reference counts every edge. |
| `dm_local_efficiency` | bctpy | undirected | differs | loops | self\_loops | abs 1e-12, rel 1e-12 | `bct.efficiency_bin(A binary, local = True)` | This variant follows NetworkX in counting a self-loop as making a node its own neighbour; BCT's matrix has no diagonal. |
| `dm_local_efficiency_definition` | bctpy | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `bct.efficiency_bin(A binary, local = True)` |  |

**References:** [gutman1994selected](../../references.html#gutman1994selected), [hage1995eccentricity](../../references.html#hage1995eccentricity), [klein1995hyper](../../references.html#klein1995hyper), [koschutzki2005centrality](../../references.html#koschutzki2005centrality), [latora2001efficient](../../references.html#latora2001efficient), [marchiori2000harmony](../../references.html#marchiori2000harmony), [randic1993novel](../../references.html#randic1993novel), [schultz1989topological](../../references.html#schultz1989topological)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [rubinov2010complex](../../references.html#rubinov2010complex)
{% endraw %}
