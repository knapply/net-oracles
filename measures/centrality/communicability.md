---
title: "Communicability"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Communicability {#concept-top}

Family: [Centrality](index.html). Subfamily: Spectral and walk-based. Concept id: `communicability`. 1 measure.

## Definition {#concept-definition}

Communicability of every pair of nodes: the matrix exponential of the adjacency matrix, per component (Estrada and Hatano 2008).

## References {#concept-references}

[estrada2008communicability](../../references.html#estrada2008communicability), [estrada2009communicability](../../references.html#estrada2009communicability)

## Communicability {#cx_communicability}

Measure id: `cx_communicability`. Original family: Centrality.

**Definition.** Communicability of every pair of nodes: the matrix exponential of the adjacency matrix, per component (Estrada and Hatano 2008).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `communicability; communicability_exp; subgraph_centrality; subgraph_centrality_exp` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cx_communicability-igraph) | `subgraph_centrality` | API listing |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cx_communicability-bct) | `subgraph_centrality` | API listing |
| [netrankr](../../tools/netrankr.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, multi-edges and self-loops): netrankr reads the simple graph (parallel edges collapsed, loops dropped). [details](#why-cx_communicability-netrankr) | `indirect_relations` |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cx_communicability-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: subgraph\_centrality.
- <a id="why-cx_communicability-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: subgraph\_centrality.
- <a id="why-cx_communicability-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> netrankr 2.0.0 was run and its value differs from the reference value by convention (defaults, multi-edges and self-loops) on inputs tagged loops and multi\_edges. netrankr reads the simple graph (parallel edges collapsed, loops dropped); the reference value's adjacency matrix counts them. Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 1e-10, rel 1e-09 on all 1 comparison where the difference occurs. Tolerance before mapping: abs 1e-10, rel 1e-09 (0 means exact equality). 1 comparisons differ and 17 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_communicability` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-10, rel 1e-09 | `nx.communicability(G)` | NetworkX's communicability is not implemented for multigraphs. |
| `cx_communicability` | netrankr | undirected | differs | loops, multi\_edges | defaults, multi\_edges, self\_loops | abs 1e-10, rel 1e-09 | `indirect_relations(g, 'walks', FUN = walks_exp)` | netrankr reads the simple graph (parallel edges collapsed, loops dropped); the reference value's adjacency matrix counts them. netrankr has no value for a single node. |

**References:** [estrada2008communicability](../../references.html#estrada2008communicability), [estrada2009communicability](../../references.html#estrada2009communicability)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [rubinov2010complex](../../references.html#rubinov2010complex), [schoch2018centrality](../../references.html#schoch2018centrality)
{% endraw %}
