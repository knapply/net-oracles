---
title: "Reciprocity"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Reciprocity {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Reciprocity, dyad and triad census. Concept id: `reciprocity`. 2 measures.

## Definition {#concept-definition}

Reciprocity. Entries grouped here: Reciprocity; Node reciprocity.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Reciprocity](#reciprocity) | `reciprocity` | 8 |
| [Node reciprocity](#nxo_node_reciprocity) | `nxo_node_reciprocity` | 3 |

## Reciprocity {#reciprocity}

Measure id: `reciprocity`. Original family: Descriptive statistics.

**Definition.** Reciprocity.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `overall_reciprocity; reciprocity` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `reciprocity` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `reciprocity` |  |
| [sna](../../tools/sna.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction and ties): On a two-node network with one arc the two ordered pairs give the perfectly anticorrelated values (1, 0) and (0, 1), so the correlation is -1, as... [details](#why-reciprocity-sna) | `grecip; mutuality` |  |
| [ergm (statnet)](../../tools/ergm.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `mutual` |  |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-reciprocity-graphtool) | `edge_reciprocity` | API listing |
| [GraphBLAS algorithms](../../tools/graphblas.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-reciprocity-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-reciprocity-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> sna 2.8 was run and its value differs from the reference value by convention (defaults, direction and ties) on inputs tagged edge\_case. On a two-node network with one arc the two ordered pairs give the perfectly anticorrelated values (1, 0) and (0, 1), so the correlation is -1, as the definition oracle confirms; sna reports 0. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). No value (reciprocity) on the fixtures empty: The ratio is 0 / 0 without arcs; not compared. No value (reciprocity\_ratio) on the fixtures empty: The ratio is 0 / 0 without arcs; not compared. 1 comparisons differ and 55 agree. Finding F044 (convention): Reciprocity correlation is 0 on a single arc. Findings: [F044](../../findings.html#f044).
- <a id="why-reciprocity-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: edge\_reciprocity.
- <a id="why-reciprocity-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `reciprocity` | NetworkX | directed | no-value-on-some-inputs |  |  | abs 0, rel 1e-14 | `nx.overall_reciprocity(DiGraph without self-loops)` | NetworkX raises for a graph without edges, where the ratio is 0 / 0. |
| `reciprocity` | igraph (R) | directed | no-value-on-some-inputs |  | direction | abs 0, rel 1e-14 | `igraph::reciprocity(igraph::simplify(g), mode = 'default')` | The ratio is 0 / 0 without arcs; not compared. |
| `reciprocity` | igraph (Python) | directed | no-value-on-some-inputs |  | direction | abs 0, rel 1e-14 | `python-igraph: [simple.reciprocity(mode="default")] if simple.ecount() else None` | The ratio is 0 / 0 without arcs; not compared. |
| `reciprocity` | sna | directed | no-value-on-some-inputs |  | direction | abs 0, rel 1e-14 | `sna::grecip(m with its diagonal set to 0, measure = 'edgewise')` | The ratio is 0 / 0 without arcs; not compared. |
| `reciprocity` | ergm (statnet) | directed | no-value-on-some-inputs |  | ties | abs 0, rel 1e-14 | `2 * summary(nw ~ mutual) / summary(nw ~ edges)` | A network without ties has no reciprocity. |
| `reciprocity` | GraphBLAS algorithms | directed | no-value-on-some-inputs |  | defaults | abs 0, rel 1e-14 | `nx.overall_reciprocity(DiGraph without loops, backend = 'graphblas')` | As in NetworkX, overall\_reciprocity raises 'Not defined for empty graphs'. |
| `reciprocity_correlation` | sna | directed | differs | edge\_case | defaults, direction, ties | abs 1e-14, rel 1e-12 | `sna::grecip(m with its diagonal set to 0, measure = 'correlation')` | On a two-node network with one arc the two ordered pairs give the perfectly anticorrelated values (1, 0) and (0, 1), so the correlation is -1, as the definition oracle confirms; sna reports 0. Every tie between distinct nodes is absent (or present), so the correlation is 0 / 0. This reference reports NaN; sna defines it as 1. Not compared. |
| `reciprocity_dyadic` | sna | directed | agrees |  |  | abs 0, rel 1e-14 | `sna::grecip(m with its diagonal set to 0, measure = 'dyadic')` |  |
| `reciprocity_ratio` | igraph (R) | directed | no-value-on-some-inputs |  | direction | abs 0, rel 1e-14 | `igraph::reciprocity(igraph::simplify(g), mode = 'ratio')` | The ratio is 0 / 0 without arcs; not compared. |
| `reciprocity_ratio` | igraph (Python) | directed | no-value-on-some-inputs |  | direction | abs 0, rel 1e-14 | `python-igraph: [simple.reciprocity(mode="ratio")] if simple.ecount() else None` | The ratio is 0 / 0 without arcs; not compared. |
| `reciprocity_ratio` | sna | directed | no-value-on-some-inputs |  | direction | abs 0, rel 1e-14 | `sna::grecip(m with its diagonal set to 0, measure = 'dyadic.nonnull')` | The ratio is 0 / 0 without arcs; not compared. |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F044](../../findings.html#f044) | sna | convention | Reciprocity correlation is 0 on a single arc |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [davis2019algorithm](../../references.html#davis2019algorithm), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hunter2008ergm](../../references.html#hunter2008ergm), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)

## Node reciprocity {#nxo_node_reciprocity}

Measure id: `nxo_node_reciprocity`. Original family: Descriptive statistics.

**Definition.** Node reciprocity.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [GraphBLAS algorithms](../../tools/graphblas.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-nxo_node_reciprocity-ucinet) | `Reciprocity (arc vs dyad question has its own FAQ), normalized reciprocity (6.834); indrecip` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-nxo_node_reciprocity-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxo_node_reciprocity` | NetworkX | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.reciprocity(nx.DiGraph(G), nodes = every node)` |  |
| `nxo_node_reciprocity` | GraphBLAS algorithms | directed | differs | multi\_edges | direction, multi\_edges, weights | abs 1e-14, rel 1e-12 | `nx.reciprocity(DiGraph, nodes, backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [davis2019algorithm](../../references.html#davis2019algorithm), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
