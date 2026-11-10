---
title: "Label propagation"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Label propagation {#concept-top}

Family: [Communities](index.html). Subfamily: Other detection algorithms. Concept id: `label_propagation`. 3 measures.

## Definition {#concept-definition}

Label propagation communities: every node repeatedly takes the dominant label among the nodes it reads.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Label propagation](#label_propagation) | `label_propagation` | 7 |
| [Cnx label propagation](#cnx_label_propagation) | `cnx_label_propagation` | 1 |
| [Seeded labels](#cnx_seeded_labels) | `cnx_seeded_labels` | 1 |

## References {#concept-references}

[cordasco2010community](../../references.html#cordasco2010community), [raghavan2007near](../../references.html#raghavan2007near), [traag2023large](../../references.html#traag2023large)

## Label propagation {#label_propagation}

Measure id: `label_propagation`. Original family: Communities.

**Definition.** Label propagation communities: every node repeatedly takes the dominant label among the nodes it reads.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention | `asyn_lpa_communities; fast_label_propagation_communities; label_propagation_communities` |  |
| [igraph (R)](../../tools/igraph.html) | ∅ checked, no value on some inputs | `cluster_label_prop` |  |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `community_label_propagation` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `LPDegreeOrdered; PLP` | API listing |
| [scikit-network](../../tools/sknetwork.html) | · reported in docs | `PropagationClustering` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `LabelPropagationClustering` | API listing |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `labelprop` | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `label_prop_quality` | igraph (R) | undirected | differs | loops | multi\_edges, self\_loops | abs 0.05, rel 0 | `mean over set.seed(1..100) of modularity(g, cluster_label_prop(g, weights = NA))` | the reference ignores self-loops (a node never reads its own label); igraph documents no rule for loops, but its mean on multi\_loops\_und (0.258) is what a node that reads its own label once per loop gives (0.265 over 300 simulated runs, against 0.206 with loops ignored), as NetworkX does |
| `label_prop_quality_fast` | NetworkX | undirected | differs | edge\_case, loops, multi\_edges | defaults, multi\_edges, self\_loops | abs 0.05, rel 0 | `mean over seeds of modularity(G, fast_label_propagation_communities(simple graph, seed = s))` | NetworkX runs on the simple graph here, while the reference counts parallel edges with their multiplicity; without edges modularity is undefined (the reference reports -1, NetworkX 0) |
| `label_prop_quality_retention` | NetworkX | undirected | differs | edge\_case, loops, multi\_edges | defaults, multi\_edges, self\_loops | abs 0.05, rel 0 | `mean over seeds of modularity(G, asyn_lpa_communities(simple graph, seed = s))` | NetworkX runs on the simple graph here, while the reference counts parallel edges with their multiplicity; without edges modularity is undefined (the reference reports -1, NetworkX 0) |
| `label_prop_semisync` | NetworkX | undirected | differs | loops, multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.community.label_propagation_communities(simple graph)` | NetworkX runs on the simple graph here (parallel edges once, no loops); the reference counts parallel edges with their multiplicity |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F029](../../findings.html#f029) | NetworkX | convention | Ties are broken by Python set or insertion order |

**References:** [cordasco2010community](../../references.html#cordasco2010community), [raghavan2007near](../../references.html#raghavan2007near), [traag2023large](../../references.html#traag2023large)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_sknetwork](../../references.html#tool_sknetwork)

## Cnx label propagation {#cnx_label_propagation}

Measure id: `cnx_label_propagation`. Original family: Communities.

**Definition.** Cnx label propagation.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_label_propagation` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.community.label_propagation_communities(G) on the simple undirected graph` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Seeded labels {#cnx_seeded_labels}

Measure id: `cnx_seeded_labels`. Original family: Communities.

**Definition.** Seeded labels.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_seeded_labels` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `per node: community index under asyn_lpa_communities and fast_label_propagation_communities (simple graph), and asyn_fluidc(k = min(3, n)) on the simple undirected graph (-1 if not connected), each with seed=random.Random(7)` |  |
| `nx_seeded_labels_valid` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's communities` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
