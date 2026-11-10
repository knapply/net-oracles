---
title: "Louvain quality"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Louvain quality

Family: Communities. Identifier: `louvain_quality`.

## Definition

Louvain communities of an undirected network by greedy modularity moves and aggregation.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention |  |  |
| [igraph (R)](../tools/igraph.html) | ≠ checked, differs by convention |  |  |
| [Gephi toolkit](../tools/gephi.html) | ≠ checked, differs by convention |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `louvain_quality` | NetworkX | undirected | differs | edge\_case | defaults | abs 0.02, rel 0 | `mean over seeds 1..20 of modularity(G, louvain_communities(G, weight = None, seed = s))` | NetworkX returns 0 for a network without edges; this reference returns NaN. |
| `louvain_quality` | igraph (R) | undirected | differs | directed, undirected | direction, ties | abs 0.02, rel 0 | `mean over set.seed(1..20) of modularity(g, cluster_louvain(g, weights = NA))` | Two different randomized procedures: the mean modularity over 20 seeds agrees within the tolerance on the corpus, but on small graphs the spread between runs exceeds it (0.219 against 0.187 on 7 nodes); the comparison is statistical, not per run. |
| `louvain_quality` | Gephi toolkit | undirected | differs |  | multi\_edges, self\_loops | abs 0.02, rel 0 | `Gephi toolkit 0.11.3: mean over 20 runs, on the main thread of a fresh JVM, of Modularity (setRandom(false), setUseWeight(false), setResolution(1.0)).getModularity(); an unseeded draw, fixed by the run order (see louvain_quality_weighted)` | With self-loops Gephi's modularity changes (mean of 20 runs 0.249 with the loops, 0.321 with the loops removed and parallel edges kept); the reference and the definition oracle count a loop as degree 2, the standard modularity of a multigraph. |
| `louvain_quality_resolution` | NetworkX | undirected | differs | edge\_case | defaults | abs 0.01, rel 0 | `mean over seeds 1..20 of modularity(G, louvain_communities(G, weight = None, resolution = 0.5, seed = s), resolution = 0.5)` | NetworkX returns 0 for a network without edges; this reference returns NaN. |
| `louvain_quality_resolution` | igraph (R) | undirected | differs | directed, undirected | defaults, direction, ties | abs 0.01, rel 0 | `mean over set.seed(1..20) of modularity(g, cluster_louvain(g, weights = NA, resolution = 0.5), resolution = 0.5)` | Two different randomized procedures: the mean modularity over the seeds agrees within the tolerance on the corpus but not on every graph; the comparison is statistical, not per run (and without edges modularity is 0 / 0: the reference NaN, the tools 0). |
| `louvain_quality_weighted` | NetworkX | undirected | differs | directed, edgeless, undirected | defaults, direction, ties | abs 0.005, rel 0 | `mean over seeds 1..20 of modularity(G, louvain_communities(G, weight = 'weight', seed = s), weight = 'weight')` | Two different randomized procedures: the mean modularity over the seeds agrees within the tolerance on the corpus but not on every graph; the comparison is statistical, not per run (and without edges modularity is 0 / 0: the reference NaN, the tools 0). |
| `louvain_quality_weighted` | igraph (R) | undirected | differs | directed, undirected | defaults, direction, ties | abs 0.005, rel 0 | `mean over set.seed(1..20) of modularity(g, cluster_louvain(g, weights = E(g)$weight), weights = E(g)$weight)` | Two different randomized procedures: the mean modularity over the seeds agrees within the tolerance on the corpus but not on every graph; the comparison is statistical, not per run (and without edges modularity is 0 / 0: the reference NaN, the tools 0). |
| `louvain_quality_weighted` | Gephi toolkit | undirected | agrees |  |  | abs 0.005, rel 0 | `Gephi toolkit 0.11.3: mean over 20 runs, on the main thread of a fresh JVM, of Modularity (setRandom(false), setUseWeight(true), setResolution(1.0)).getModularity()` |  |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F015](../findings.html#f015) | Gephi toolkit | defect | Louvain with setRandom(false) is not reproducible |
| [F016](../findings.html#f016) | Gephi toolkit | defect | Louvain sometimes does not return |
| [F022](../findings.html#f022) | Gephi toolkit | convention | Louvain resolution acts as the reciprocal of gamma |

## References

[blondel2008fast](../references.html#blondel2008fast), [dugue2015directed](../references.html#dugue2015directed), [leicht2008community](../references.html#leicht2008community), [newman2004analysis](../references.html#newman2004analysis), [newman2004finding](../references.html#newman2004finding), [newman2006modularity](../references.html#newman2006modularity), [reichardt2006statistical](../references.html#reichardt2006statistical), [traag2019louvain](../references.html#traag2019louvain)

Tools cited: [bastian2009gephi](../references.html#bastian2009gephi), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
