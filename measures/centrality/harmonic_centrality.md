---
title: "Harmonic centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Harmonic centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Distance-based. Concept id: `harmonic_centrality`. 1 measure.

## Definition {#concept-definition}

Harmonic centrality of every node: the sum of 1/d over the other nodes (0 for an unreachable one).

## References {#concept-references}

[boldi2014axioms](../../references.html#boldi2014axioms), [freeman1978centrality](../../references.html#freeman1978centrality), [marchiori2000harmony](../../references.html#marchiori2000harmony), [rochat2009closeness](../../references.html#rochat2009closeness), [sabidussi1966centrality](../../references.html#sabidussi1966centrality), [staudt2016networkit](../../references.html#staudt2016networkit), [then2014more](../../references.html#then2014more), [wasserman1994social](../../references.html#wasserman1994social)

## Harmonic {#harmonic}

Measure id: `harmonic`. Original family: Centrality.

**Definition.** Harmonic centrality of every node: the sum of 1/d over the other nodes (0 for an unreachable one).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `harmonic_centrality` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `harmonic_centrality` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `harmonic_centrality` |  |
| [sna](../../tools/sna.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults and normalization): For a single node sna divides 0 by n - 1 = 0 and reports NaN. [details](#why-harmonic-sna) |  |  |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `HarmonicCloseness; TopHarmonicCloseness` |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `HarmonicCentrality` |  |
| [Gephi toolkit](../../tools/gephi.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (normalization): Gephi divides the sum of 1/d by the number of nodes the node reaches (0 if none), the reference by n - 1 (the standard normalization). [details](#why-harmonic-gephi) |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-harmonic-ucinet) | `fcent` | published documentation |
| [netrankr](../../tools/netrankr.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [centiserve](../../tools/centiserve.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-harmonic-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> sna 2.8 was run and its value differs from the reference value by convention (defaults and normalization) on inputs tagged edge\_case. For a single node sna divides 0 by n - 1 = 0 and reports NaN; igraph and this reference report 0, since there are no other nodes. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 1 comparisons differ and 35 agree.
- <a id="why-harmonic-gephi"></a>**[Gephi toolkit](../../tools/gephi.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Gephi toolkit 0.11.3 was run and its value differs from the reference value by convention (normalization) on the fixtures gnp\_dir\_sparse, gnp\_und\_sparse, multi\_loops\_dir, multi\_loops\_und, two\_triangles\_isolate. Gephi divides the sum of 1/d by the number of nodes the node reaches (0 if none), the reference by n - 1 (the standard normalization); the two agree when every node reaches every other. Checked to 1e-15 on the five fixtures. setNormalized does not change it. Relation to the reference value: Normalization: sum(1/d) / (nodes reached), the reference divides by n - 1; equal when every node reaches all. Mapping: the reference value computed with the tool's convention (the sum of 1/d divided by the number of nodes reached, 0 if none, not by n - 1) agrees with the tool within abs 1e-14, rel 1e-12 on all 5 comparisons where the difference occurs. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 5 comparisons differ and 23 agree.
- <a id="why-harmonic-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `harmonic` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.harmonic_centrality(G.reverse())` |  |
| `harmonic` | igraph (R) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::harmonic_centrality(g, mode = 'out', weights = NA, normalized = FALSE)` |  |
| `harmonic` | igraph (Python) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `python-igraph: g.harmonic_centrality(mode="out", weights=None, normalized=False)` |  |
| `harmonic` | NetworKit | any | no-value-on-some-inputs |  |  | abs 1e-14, rel 1e-12 | `nk.centrality.HarmonicCloseness(G, normalized = False)` |  |
| `harmonic` | JGraphT | any | agrees |  |  | abs 1e-14, rel 1e-12 | `JGraphT 1.5.2: new HarmonicCentrality<>(g, false, false) on a pseudograph` |  |
| `harmonic` | netrankr | any | no-value-on-some-inputs | (no value) directed | defaults, direction, weights | abs 1e-14, rel 1e-12 | `aggregate_positions(indirect_relations(g, 'dist_sp', FUN = dist_inv), 'sum')` | netrankr reads the network as undirected, unweighted and simple (the oracle writes nothing for a directed fixture) and has no value for a single node. |
| `harmonic` | centiserve | any | no-value-on-some-inputs |  |  | abs 1e-14, rel 1e-12 | `centiserve::closeness.latora(g, mode = 'out', normalized = FALSE)` | centiserve rejects a graph of one node. |
| `harmonic_all_undirected` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.harmonic_centrality(G)` |  |
| `harmonic_in` | NetworkX | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.harmonic_centrality(G)` |  |
| `harmonic_in` | igraph (R) | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::harmonic_centrality(g, mode = 'in', weights = NA)` |  |
| `harmonic_in` | igraph (Python) | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `python-igraph: g.harmonic_centrality(mode="in", weights=None, normalized=False)` |  |
| `harmonic_in` | NetworKit | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `nk.centrality.HarmonicCloseness(reversed G, normalized = False)` |  |
| `harmonic_in` | JGraphT | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `JGraphT 1.5.2: new HarmonicCentrality<>(g, true, false) on a pseudograph` |  |
| `harmonic_in` | centiserve | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `centiserve::closeness.latora(g, mode = 'in', normalized = FALSE)` |  |
| `harmonic_normalized` | igraph (R) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::harmonic_centrality(g, mode = 'out', weights = NA, normalized = TRUE)` |  |
| `harmonic_normalized` | igraph (Python) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `python-igraph: g.harmonic_centrality(mode="out", weights=None, normalized=True)` |  |
| `harmonic_normalized` | sna | any | differs | edge\_case | defaults, normalization | abs 1e-14, rel 1e-12 | `sna::closeness(m, gmode, cmode = 'suminvdir' \| 'suminvundir')` | For a single node sna divides 0 by n - 1 = 0 and reports NaN; igraph and this reference report 0, since there are no other nodes. |
| `harmonic_normalized` | NetworKit | any | no-value-on-some-inputs |  |  | abs 1e-14, rel 1e-12 | `nk.centrality.HarmonicCloseness(G, normalized = True)` |  |
| `harmonic_normalized` | Gephi toolkit | any | differs |  | normalization | abs 1e-14, rel 1e-12 | `Gephi toolkit 0.11.3: GraphDistance, node column 'harmonicclosnesscentrality' (identical with setNormalized(true) or (false))` | Gephi divides the sum of 1/d by the number of nodes the node reaches (0 if none), the reference by n - 1 (the standard normalization); the two agree when every node reaches every other. Checked to 1e-15 on the five fixtures. setNormalized does not change it. |
| `harmonic_weighted` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.harmonic_centrality(G.reverse(), distance = 'weight')` |  |
| `harmonic_weighted` | igraph (R) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::harmonic_centrality(g, mode = 'out', weights = E(g)$weight)` |  |
| `harmonic_weighted` | igraph (Python) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `python-igraph: g.harmonic_centrality(mode="out", weights=w, normalized=False)` |  |
| `harmonic_weighted` | NetworKit | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nk.centrality.HarmonicCloseness(G_weighted, normalized = False)` |  |
| `harmonic_weighted` | centiserve | any | agrees |  |  | abs 1e-14, rel 1e-12 | `centiserve::closeness.latora(g, mode = 'out', weights = E(g)$weight, normalized = FALSE)` |  |
| `harmonic_weighted_strength` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.harmonic_centrality(G.reverse(), distance = 'weight') with weight set to 1 / w` |  |

**References:** [boldi2014axioms](../../references.html#boldi2014axioms), [freeman1978centrality](../../references.html#freeman1978centrality), [marchiori2000harmony](../../references.html#marchiori2000harmony), [rochat2009closeness](../../references.html#rochat2009closeness), [sabidussi1966centrality](../../references.html#sabidussi1966centrality), [staudt2016networkit](../../references.html#staudt2016networkit), [then2014more](../../references.html#then2014more), [wasserman1994social](../../references.html#wasserman1994social)

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [jalili2015centiserver](../../references.html#jalili2015centiserver), [michail2020jgrapht](../../references.html#michail2020jgrapht), [schoch2018centrality](../../references.html#schoch2018centrality), [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
