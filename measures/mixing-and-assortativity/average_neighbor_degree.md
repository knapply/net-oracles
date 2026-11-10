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

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#avg_deg_conn">Avg deg conn</a></td><td><code>avg_deg_conn</code></td><td>1</td></tr><tr><td><a href="#avg_nbr_deg">Avg nbr deg</a></td><td><code>avg_nbr_deg</code></td><td>1</td></tr><tr><td><a href="#cat_knn">Knn</a></td><td><code>cat_knn</code></td><td>2</td></tr></tbody></table></div>

## Avg deg conn {#avg_deg_conn}

Measure id: `avg_deg_conn`. Original family: Mixing and assortativity.

**Definition.** Avg deg conn.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (multi-edges and normalization): On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity. <a href="#why-avg_deg_conn-networkx">details</a></td><td><code>average_degree_connectivity</code></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-avg_deg_conn-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (multi-edges and normalization) on inputs tagged multi\_edges. On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-09 (0 means exact equality). 17 comparisons differ and 112 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>avg_deg_conn</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>multi_edges</td><td>multi_edges, normalization</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.average_degree_connectivity(G)</code></td><td>On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both.</td></tr><tr><td><code>avg_deg_conn_in_in</code></td><td>NetworkX</td><td>directed</td><td>differs</td><td>multi_edges</td><td>multi_edges, normalization</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.average_degree_connectivity(G, source = 'in', target = 'in')</code></td><td>On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both.</td></tr><tr><td><code>avg_deg_conn_out_out</code></td><td>NetworkX</td><td>directed</td><td>differs</td><td>multi_edges</td><td>multi_edges, normalization</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.average_degree_connectivity(G, source = 'out', target = 'out')</code></td><td>On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both.</td></tr><tr><td><code>avg_deg_conn_subset</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>multi_edges</td><td>multi_edges, normalization</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.average_degree_connectivity(G, nodes = even nodes)</code></td><td>On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both.</td></tr><tr><td><code>avg_deg_conn_weighted</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>multi_edges</td><td>multi_edges, normalization</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.average_degree_connectivity(G, weight = 'weight')</code></td><td>On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both.</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Avg nbr deg {#avg_nbr_deg}

Measure id: `avg_nbr_deg`. Original family: Mixing and assortativity.

**Definition.** Avg nbr deg.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (multi-edges and normalization): On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity. <a href="#why-avg_nbr_deg-networkx">details</a></td><td><code>average_neighbor_degree</code></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-avg_nbr_deg-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (multi-edges and normalization) on inputs tagged multi\_edges. On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-09 (0 means exact equality). 20 comparisons differ and 124 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>avg_nbr_deg</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>multi_edges</td><td>multi_edges, normalization</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.average_neighbor_degree(G)</code></td><td>On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both.</td></tr><tr><td><code>avg_nbr_deg_in_in</code></td><td>NetworkX</td><td>directed</td><td>differs</td><td>multi_edges</td><td>multi_edges, normalization</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.average_neighbor_degree(G, source = 'in', target = 'in')</code></td><td>On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both.</td></tr><tr><td><code>avg_nbr_deg_out_in</code></td><td>NetworkX</td><td>directed</td><td>differs</td><td>multi_edges</td><td>multi_edges, normalization</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.average_neighbor_degree(G, source = 'out', target = 'in')</code></td><td>On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both.</td></tr><tr><td><code>avg_nbr_deg_subset</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>multi_edges</td><td>multi_edges, normalization</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.average_neighbor_degree(G, nodes = even nodes)</code></td><td>On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both.</td></tr><tr><td><code>avg_nbr_deg_total</code></td><td>NetworkX</td><td>directed</td><td>differs</td><td>multi_edges</td><td>multi_edges, normalization</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.average_neighbor_degree(G, source = 'in+out', target = 'in+out')</code></td><td>On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both.</td></tr><tr><td><code>avg_nbr_deg_weighted</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>multi_edges</td><td>multi_edges, normalization</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.average_neighbor_degree(G, weight = 'weight')</code></td><td>On a multigraph NetworkX sums over distinct neighbours while dividing by the degree with multiplicity; the reference counts every parallel edge in both.</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Knn {#cat_knn}

Measure id: `cat_knn`. Original family: Descriptive statistics.

**Definition.** Knn.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_knn-igraph">details</a></td><td><code>knn</code></td><td>API listing</td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_knn-pyigraph">details</a></td><td><code>knn</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_knn-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: knn.
- <a id="why-cat_knn-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: knn.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
