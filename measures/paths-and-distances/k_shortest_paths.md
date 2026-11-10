---
title: "K shortest paths"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# K shortest paths {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Shortest paths. Concept id: `k_shortest_paths`. 1 measure.

## Definition {#concept-definition}

K shortest paths. Entries grouped here: Paths k shortest.

*Definition not yet written.*

## Paths k shortest {#paths_k_shortest}

Measure id: `paths_k_shortest`. Original family: Paths and distances.

**Definition.** Paths k shortest.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>shortest_simple_paths</code></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-paths_k_shortest-igraph">details</a></td><td><code>k_shortest_paths</code></td><td>API listing</td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-paths_k_shortest-pyigraph">details</a></td><td><code>get_k_shortest_paths</code></td><td>API listing</td></tr><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-paths_k_shortest-rustworkx">details</a></td><td><code>digraph_k_shortest_path_lengths; graph_k_shortest_path_lengths; k_shortest_path_lengths</code></td><td>API listing</td></tr><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-paths_k_shortest-jgrapht">details</a></td><td><code>EppsteinKShortestPath; EppsteinShortestPathIterator; YenKShortestPath; YenShortestPathIterator</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-paths_k_shortest-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: k\_shortest\_paths.
- <a id="why-paths_k_shortest-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: get\_k\_shortest\_paths.
- <a id="why-paths_k_shortest-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: digraph\_k\_shortest\_path\_lengths; graph\_k\_shortest\_path\_lengths; k\_shortest\_path\_lengths.
- <a id="why-paths_k_shortest-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: EppsteinKShortestPath; EppsteinShortestPathIterator; YenKShortestPath; YenShortestPathIterator.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>paths_k_shortest_unweighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>lengths of the first 10 paths of nx.shortest_simple_paths(H, 0, n - 1), H the simple graph</code></td><td></td></tr><tr><td><code>paths_k_shortest_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.path_weight of the first 10 paths of nx.shortest_simple_paths(H, 0, n - 1, weight = 'weight'), H the simple graph keeping the lightest parallel edge</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
