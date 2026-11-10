---
title: "Triad census"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Triad census {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Reciprocity, dyad and triad census. Concept id: `triad_census`. 2 measures.

## Definition {#concept-definition}

The 16 triad counts in MAN order (Holland and Leinhardt), one value per triad type.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Triad census](#triad_census) | `triad_census` | 7 |
| [Triads](#st_triads) | `st_triads` | 1 |

## References {#concept-references}

[batagelj2001subquadratic](../../references.html#batagelj2001subquadratic), [holland1976local](../../references.html#holland1976local)

## Triad census {#triad_census}

Measure id: `triad_census`. Original family: Descriptive statistics.

**Definition.** The 16 triad counts in MAN order (Holland and Leinhardt), one value per triad type.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `triadic_census` |  |
| [igraph (R)](../../tools/igraph.html) | ∅ checked, no value on some inputs | `triad_census` |  |
| [igraph (Python)](../../tools/pyigraph.html) | ≠ checked, differs by convention | `triad_census` |  |
| [sna](../../tools/sna.html) | ≠ checked, differs by convention | `triad.census; triad.classify` |  |
| [ergm (statnet)](../../tools/ergm.html) | ✓ checked, agrees | `triadcensus` |  |
| [RSiena](../../tools/rsiena.html) | · reported in docs | `TriadCensus` | API listing |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `Triad census, dyad census, hierarchy; nodetriadcensus` | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `triad_census` | NetworkX | any | differs | undirected, (no value) undirected | direction | abs 0, rel 0 | `nx.triadic_census(DiGraph(G))` | NetworkX defines the triad census only for directed graphs. NetworkX's triadic\_census accepts only directed graphs. |
| `triad_census` | igraph (R) | any | differs | multi\_edges | multi\_edges, ties | abs 0, rel 0 | `igraph::triad_census(g)` | igraph's triad census does not support multigraphs: parallel edges change its counts. This reference, sna, and the definition oracle classify each dyad as tied or not, so parallel edges count once. |
| `triad_census` | igraph (Python) | any | differs | multi\_edges | multi\_edges, ties | abs 0, rel 0 | `python-igraph: list(g.triad_census()),` | igraph's triad census does not support multigraphs: parallel edges change its counts. This reference, sna, and the definition oracle classify each dyad as tied or not, so parallel edges count once. |
| `triad_census` | sna | any | differs | edge\_case, undirected, (no value) undirected | defaults, direction | abs 0, rel 0 | `sna::triad.census(m, mode = 'digraph')` | sna returns NaN for networks with fewer than three nodes, which have no triads; this reference returns zero counts. |
| `triad_census` | ergm (statnet) | any | no-value-on-some-inputs |  | direction | abs 0, rel 0 | `summary(nw ~ triadcensus(0:15))` | The census is computed for directed networks with at least three nodes only. |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F039](../../findings.html#f039) | igraph (R) | defect | Triad census on multigraphs differs from the definition |

**References:** [batagelj2001subquadratic](../../references.html#batagelj2001subquadratic), [holland1976local](../../references.html#holland1976local)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hunter2008ergm](../../references.html#hunter2008ergm), [ripley2026manual](../../references.html#ripley2026manual)

## Triads {#st_triads}

Measure id: `st_triads`. Original family: Graph theory and combinatorics.

**Definition.** Triads.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_triads` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.triadic_census(G), (G, even nodes), (G, [0]) on the MultiDiGraph` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
