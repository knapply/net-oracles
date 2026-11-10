---
title: "Current-flow betweenness"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Current-flow betweenness {#concept-top}

Family: [Centrality](index.html). Subfamily: Betweenness, load and flow. Concept id: `current_flow_betweenness`. 3 measures.

## Definition {#concept-definition}

Current-flow betweenness approximated from sampled pairs of nodes (random pairs or given ones).

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Current flow approx](#cx_current_flow_approx) | `cx_current_flow_approx` | 1 |
| [Current flow subset](#cx_current_flow_subset) | `cx_current_flow_subset` | 1 |
| [Cx current flow](#cx_current_flow) | `cx_current_flow` | 2 |

## References {#concept-references}

[brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

## Current flow approx {#cx_current_flow_approx}

Measure id: `cx_current_flow_approx`. Original family: Centrality.

**Definition.** Current-flow betweenness approximated from sampled pairs of nodes (random pairs or given ones).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `approximate_current_flow_betweenness_centrality` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_cfb_approx` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 1e-14, rel 1e-12 | `nx.approximate_current_flow_betweenness_centrality(G, epsilon = 0.5, seed = 1), the runner passing the same pairs` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |

**References:** [brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Current flow subset {#cx_current_flow_subset}

Measure id: `cx_current_flow_subset`. Original family: Centrality.

**Definition.** Current-flow betweenness of every node and edge for flow between given source and target nodes.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `current_flow_betweenness_centrality_subset; edge_current_flow_betweenness_centrality_subset` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_cfb_subset_nx` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 1e-14, rel 1e-12 | `nx.current_flow_betweenness_centrality_subset(G, even, thirds)` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |
| `cx_ecfb_subset_nx` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 1e-14, rel 1e-12 | `nx.edge_current_flow_betweenness_centrality_subset(G, even, thirds)` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |

**References:** [brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Cx current flow {#cx_current_flow}

Measure id: `cx_current_flow`. Original family: Centrality.

**Definition.** Current-flow (random-walk) betweenness of every node and edge, from the grounded inverse of the Laplacian.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `current_flow_betweenness_centrality; edge_current_flow_betweenness_centrality` |  |
| [netrankr](../../tools/netrankr.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_cfb` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 1e-14, rel 1e-12 | `nx.current_flow_betweenness_centrality(G)` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |
| `cx_cfb_raw` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 1e-11, rel 1e-12 | `nx.current_flow_betweenness_centrality(G, normalized = False)` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |
| `cx_cfb_raw` | netrankr | undirected | no-value-on-some-inputs | (no value) directed, (no value) disconnected | defaults, direction, weights | abs 1e-11, rel 1e-12 | `aggregate_positions(indirect_relations(g, 'depend_curflow'), 'sum')` | netrankr reads the network as undirected, unweighted and simple and has no value for a single node; its resistance distance (type = "dist\_resist", "depend\_curflow") is defined only for connected graphs and raises an error otherwise. |
| `cx_cfb_weighted` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 5e-14, rel 1e-12 | `nx.current_flow_betweenness_centrality(G, weight = 'weight')` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |
| `cx_ecfb` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 1e-14, rel 1e-12 | `nx.edge_current_flow_betweenness_centrality(G)` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |
| `cx_ecfb_raw` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 1e-14, rel 1e-12 | `nx.edge_current_flow_betweenness_centrality(G, normalized = False)` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |

**References:** [brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [schoch2018centrality](../../references.html#schoch2018centrality)
{% endraw %}
