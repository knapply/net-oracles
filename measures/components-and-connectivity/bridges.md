---
title: "Bridges"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Bridges {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Articulation points, bridges and biconnected components. Concept id: `bridges`. 1 measure.

## Definition {#concept-definition}

Bridges. Entries grouped here: Bridges.

*Definition not yet written.*

## Bridges {#bridges}

Measure id: `bridges`. Original family: Components and connectivity.

**Definition.** Bridges.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>bridges; has_bridges; local_bridges</code></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>bridges</code></td><td></td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-bridges-pyigraph">details</a></td><td><code>bridges</code></td><td>API listing</td></tr><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>bridges</code></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-bridges-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: bridges.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>bridges</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.bridges(nx.MultiGraph of the network)</code></td><td></td></tr><tr><td><code>bridges</code></td><td>igraph (R)</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td>direction, multi_edges</td><td>abs 0, rel 0</td><td><code>igraph::ends(u, igraph::bridges(u)) with u = as_undirected(g, mode = 'each')</code></td><td>The undirected reading of these networks has parallel edges (or arcs in both directions), and igraph's documentation does not say how bridges() treats them, so it is compared only where there are none.</td></tr><tr><td><code>bridges</code></td><td>rustworkx</td><td>any</td><td>differs</td><td>multi_edges, (no value) directed</td><td>direction, multi_edges</td><td>abs 0, rel 0</td><td><code>rx.bridges(G)</code></td><td>Two parallel edges between the same nodes are never a bridge for the reference (removing one leaves the other); rx.bridges() reads the multigraph as a simple graph and reports the pair as a bridge. rx.bridges() accepts only an undirected PyGraph.</td></tr></tbody></table></div>

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
