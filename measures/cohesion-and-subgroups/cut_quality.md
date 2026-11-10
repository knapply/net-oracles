---
title: "Cut quality (conductance, expansion, boundary)"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Cut quality (conductance, expansion, boundary) {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Relaxed cliques and subgroups. Concept id: `cut_quality`. 1 measure.

## Definition {#concept-definition}

Cut quality (conductance, expansion, boundary). Entries grouped here: Cut quality (conductance, expansion, boundary).

*Definition not yet written.* Documented only (NetworKit and NetworkX conductance, expansion and boundary), never run; the sources give the name and the tool's function, not a formula, and no verified bibliography entry for the original definition is available.

## Cut quality (conductance, expansion, boundary) {#cut_quality}

Measure id: `cut_quality`. Original family: Cohesion and subgroups.

**Definition.** Cut quality (conductance, expansion, boundary).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cut_quality-networkx">details</a></td><td><code>boundary_expansion; conductance; cut_size; edge_boundary; edge_expansion; mixing_expansion; node_boundary; node_expansion; normalized_cut_size; volume</code></td><td>API listing</td></tr><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cut_quality-networkit">details</a></td><td><code>Volume</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cut_quality-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: boundary\_expansion; conductance; cut\_size; edge\_boundary; edge\_expansion; mixing\_expansion; node\_boundary; node\_expansion; normalized\_cut\_size; volume.
- <a id="why-cut_quality-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: Volume.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
