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

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `harmonic_centrality` |  |
| [igraph (R)](../../tools/igraph.html) | ✓ checked, agrees | `harmonic_centrality` |  |
| [igraph (Python)](../../tools/pyigraph.html) | ✓ checked, agrees | `harmonic_centrality` |  |
| [sna](../../tools/sna.html) | ≠ checked, differs by convention |  |  |
| [NetworKit](../../tools/networkit.html) | ✓ checked, agrees | `HarmonicCloseness; TopHarmonicCloseness` |  |
| [JGraphT](../../tools/jgrapht.html) | ✓ checked, agrees | `HarmonicCentrality` |  |
| [Gephi toolkit](../../tools/gephi.html) | ≠ checked, differs by convention |  |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `fcent` | published documentation |
| [netrankr](../../tools/netrankr.html) | ✓ checked, agrees |  |  |
| [centiserve](../../tools/centiserve.html) | ✓ checked, agrees |  |  |

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
