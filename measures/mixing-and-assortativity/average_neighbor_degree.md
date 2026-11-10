---
title: "Average neighbor degree and degree connectivity"
layout: default
parent: "Mixing and assortativity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Average neighbor degree and degree connectivity {#concept-top}

Family: [Mixing and assortativity](index.html). Subfamily: Assortativity. Concept id: `average_neighbor_degree`. 3 measures.

## Definition {#concept-definition}

Average neighbor degree and degree connectivity. Entries grouped here: Avg deg conn; Avg nbr deg; Knn.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Avg deg conn](#avg_deg_conn) | `avg_deg_conn` | 1 |
| [Avg nbr deg](#avg_nbr_deg) | `avg_nbr_deg` | 1 |
| [Knn](#cat_knn) | `cat_knn` | 2 |

## Avg deg conn {#avg_deg_conn}

Measure id: `avg_deg_conn`. Original family: Mixing and assortativity.

**Definition.** Avg deg conn.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges and normalization): On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity. [details](#why-avg_deg_conn-networkx) | `average_degree_connectivity` |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-avg_deg_conn-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (multi-edges and normalization) on inputs tagged multi\_edges. On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-09 (0 means exact equality). 17 comparisons differ and 112 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `avg_deg_conn` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_degree_connectivity(G)` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_deg_conn_in_in` | NetworkX | directed | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_degree_connectivity(G, source = 'in', target = 'in')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_deg_conn_out_out` | NetworkX | directed | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_degree_connectivity(G, source = 'out', target = 'out')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_deg_conn_subset` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_degree_connectivity(G, nodes = even nodes)` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_deg_conn_weighted` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_degree_connectivity(G, weight = 'weight')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Avg nbr deg {#avg_nbr_deg}

Measure id: `avg_nbr_deg`. Original family: Mixing and assortativity.

**Definition.** Avg nbr deg.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges and normalization): On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity. [details](#why-avg_nbr_deg-networkx) | `average_neighbor_degree` |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-avg_nbr_deg-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (multi-edges and normalization) on inputs tagged multi\_edges. On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-09 (0 means exact equality). 20 comparisons differ and 124 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `avg_nbr_deg` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G)` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_nbr_deg_in_in` | NetworkX | directed | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G, source = 'in', target = 'in')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_nbr_deg_out_in` | NetworkX | directed | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G, source = 'out', target = 'in')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_nbr_deg_subset` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G, nodes = even nodes)` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_nbr_deg_total` | NetworkX | directed | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G, source = 'in+out', target = 'in+out')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |
| `avg_nbr_deg_weighted` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.average_neighbor_degree(G, weight = 'weight')` | On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Knn {#cat_knn}

Measure id: `cat_knn`. Original family: Descriptive statistics.

**Definition.** Knn.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_knn-igraph) | `knn` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_knn-pyigraph) | `knn` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_knn-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: knn.
- <a id="why-cat_knn-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: knn.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
