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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `triadic_census` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges and ties): igraph's triad census does not support multigraphs: parallel edges change its counts. [details](#why-triad_census-igraph) | `triad_census` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges and ties): igraph's triad census does not support multigraphs: parallel edges change its counts. [details](#why-triad_census-pyigraph) | `triad_census` |  |
| [sna](../../tools/sna.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults and direction): sna returns NaN for networks with fewer than three nodes, which have no triads. [details](#why-triad_census-sna) | `triad.census; triad.classify` |  |
| [ergm (statnet)](../../tools/ergm.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `triadcensus` |  |
| [RSiena](../../tools/rsiena.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-triad_census-rsiena) | `TriadCensus` | API listing |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-triad_census-ucinet) | `Triad census, dyad census, hierarchy; nodetriadcensus` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-triad_census-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (R) 2.3.4 was run and its value differs from the reference value by convention (multi-edges and ties) on inputs tagged multi\_edges. igraph's triad census does not support multigraphs: parallel edges change its counts. This reference, sna, and the definition oracle classify each dyad as tied or not, so parallel edges count once. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 5 comparisons differ and 39 agree. Finding F039 (defect): Triad census on multigraphs differs from the definition. Findings: [F039](../../findings.html#f039).
- <a id="why-triad_census-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (Python) 1.0.0 was run and its value differs from the reference value by convention (multi-edges and ties) on inputs tagged multi\_edges. igraph's triad census does not support multigraphs: parallel edges change its counts. This reference, sna, and the definition oracle classify each dyad as tied or not, so parallel edges count once. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 6 comparisons differ and 47 agree.
- <a id="why-triad_census-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> sna 2.8 was run and its value differs from the reference value by convention (defaults and direction) on inputs tagged edge\_case and undirected. sna returns NaN for networks with fewer than three nodes, which have no triads; this reference returns zero counts. For undirected graphs sna reports only the four undirected triad classes, while igraph and this reference report all 16 types with every edge treated as mutual. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 1 comparisons differ and 14 agree.
- <a id="why-triad_census-rsiena"></a>**[RSiena](../../tools/rsiena.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. RSiena 1.6.6 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (RSiena exported functions and help titles; effects from getEffects()); API names: TriadCensus.
- <a id="why-triad_census-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_triads` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.triadic_census(G), (G, even nodes), (G, [0]) on the MultiDiGraph` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
