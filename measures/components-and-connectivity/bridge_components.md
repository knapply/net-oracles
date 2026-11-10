---
title: "Bridge components"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Bridge components {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Articulation points, bridges and biconnected components. Concept id: `bridge_components`. 1 measure.

## Definition {#concept-definition}

Bridge components. Entries grouped here: Bridge components (connectivity).

*Definition not yet written.* Documented only (NetworkX), never run; the sources give the function name. A bridge-connected component is a class of nodes joined after all bridges are removed, which coincides with the 2-edge-connected components of the k-edge-connected components entry (k = 2); the tool's own definition and ordering are not recorded.

## Bridge components (connectivity) {#cat_bridge_component-connectivity}

Measure id: `cat_bridge_component@connectivity`. Original family: Components and connectivity.

**Definition.** Bridge components (connectivity).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_bridge_component-connectivity-networkx">details</a></td><td><code>bridge_components</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_bridge_component-connectivity-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: bridge\_components.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
