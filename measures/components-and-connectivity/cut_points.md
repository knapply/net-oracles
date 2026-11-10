---
title: "Cut points (articulation points)"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Cut points (articulation points) {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Articulation points, bridges and biconnected components. Concept id: `cut_points`. 1 measure.

## Definition {#concept-definition}

Cut points (articulation points). Entries grouped here: Cut points.

*Definition not yet written.*

## Cut points {#cut_points}

Measure id: `cut_points`. Original family: Components and connectivity.

**Definition.** Cut points.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>articulation_points</code></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>articulation_points</code></td><td></td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>articulation_points</code></td><td></td></tr><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>cutpoints</code></td><td></td></tr><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>articulation_points</code></td><td></td></tr><tr><td><a href="../../tools/boost.html">Boost Graph Library</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>articulation_points</code></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-cut_points-ucinet">details</a></td><td><code>cutpoints</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cut_points-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>cut_points</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.articulation_points(nx.MultiGraph of the network)</code></td><td></td></tr><tr><td><code>cut_points</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>igraph::articulation_points(simplify(as_undirected(g))), which does not depend on parallel edges</code></td><td></td></tr><tr><td><code>cut_points</code></td><td>igraph (Python)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>python-igraph: sorted(float(v) for v in su.articulation_points()),</code></td><td></td></tr><tr><td><code>cut_points</code></td><td>sna</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>sna::cutpoints(symmetrized m without its diagonal, mode = 'graph')</code></td><td></td></tr><tr><td><code>cut_points</code></td><td>rustworkx</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) directed</td><td>direction</td><td>abs 0, rel 0</td><td><code>rx.articulation_points(G)</code></td><td>rx.articulation_points() accepts only an undirected PyGraph.</td></tr><tr><td><code>cut_points</code></td><td>Boost Graph Library</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) directed</td><td>direction</td><td>abs 0, rel 0</td><td><code>Boost Graph Library articulation_points</code></td><td>BGL's articulation_points is defined for undirected graphs only; the driver does not call it on directed input.</td></tr></tbody></table></div>

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
