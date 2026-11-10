---
title: "Flow betweenness"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Flow betweenness {#concept-top}

Family: [Centrality](index.html). Subfamily: Betweenness, load and flow. Concept id: `flow_betweenness`. 1 measure.

## Definition {#concept-definition}

Flow betweenness of every node: the share of maximum flow between other pairs that cannot avoid it. The ucinet convention uses the normalized scale; UCINET's documentation does not define its normalization precisely, so the all\_pairs and max scales are offered as other readings.

## References {#concept-references}

[borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

## Flow betweenness {#flow_betweenness}

Measure id: `flow_betweenness`. Original family: Centrality.

**Definition.** Flow betweenness of every node: the share of maximum flow between other pairs that cannot avoid it. The ucinet convention uses the normalized scale; UCINET's documentation does not define its normalization precisely, so the all\_pairs and max scales are offered as other readings.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [sna](../../tools/sna.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, multi-edges, normalization and ties): sna reads an adjacency matrix, so parallel edges collapse into one tie of capacity 1. [details](#why-flow_betweenness-sna) | `flowbet` |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-flow_betweenness-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-flow_betweenness-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> sna 2.8 was run and its value differs from the reference value by convention (defaults, multi-edges, normalization and ties) on inputs tagged multi\_edges. flow\_betweenness: sna reads an adjacency matrix, so parallel edges collapse into one tie of capacity 1; the reference adds their capacities. flow\_betweenness\_capacity: sna keeps one value per pair of nodes. flow\_betweenness\_fractional and flow\_betweenness\_normalized: sna collapses parallel edges. Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 1e-12, rel 1e-12 on all 6 comparisons where the difference occurs. Tolerance before mapping: abs 1e-12, rel 1e-12; abs 1e-09, rel 1e-09 (0 means exact equality). 6 comparisons differ and 80 agree.
- <a id="why-flow_betweenness-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `flow_betweenness` | sna | any | differs | multi\_edges | multi\_edges, ties | abs 1e-12, rel 1e-12 | `sna::flowbet(m, gmode = 'digraph' \| 'graph', cmode = 'rawflow', ignore.eval = TRUE)` | sna reads an adjacency matrix, so parallel edges collapse into one tie of capacity 1; the reference adds their capacities. sna's flow routines need at least two nodes. |
| `flow_betweenness_capacity` | sna | any | differs | multi\_edges | multi\_edges | abs 1e-09, rel 1e-09 | `sna::flowbet(m, gmode, cmode = 'rawflow') with the weights in the matrix` | sna keeps one value per pair of nodes. |
| `flow_betweenness_fractional` | sna | any | differs | multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `sna::flowbet(m, gmode, cmode = 'fracflow', ignore.eval = TRUE)` | sna collapses parallel edges. sna's flow routines need at least two nodes. |
| `flow_betweenness_normalized` | sna | any | differs | multi\_edges | defaults, multi\_edges, normalization | abs 1e-12, rel 1e-12 | `sna::flowbet(m, gmode, cmode = 'normflow', ignore.eval = TRUE)` | sna collapses parallel edges. No flow passes between pairs of other nodes, so the normalized score is 0/0; the reference reports NaN. |

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
