---
title: "Incremental maintenance on a changing graph"
layout: default
parent: "Temporal and events"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Incremental maintenance on a changing graph {#concept-top}

Family: [Temporal and events](index.html). Subfamily: Temporal descriptives. Concept id: `dynamic_update`. 1 measure.

## Definition {#concept-definition}

Incremental maintenance on a changing graph. Entries grouped here: Incremental maintenance on a changing graph.

*Definition not yet written.* Documented by name only; the sources record the tool function and no definition, and no primary paper was checked.

## Incremental maintenance on a changing graph {#dynamic_update}

Measure id: `dynamic_update`. Original family: Temporal and events.

**Definition.** Incremental maintenance on a changing graph.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-dynamic_update-networkit">details</a></td><td><code>DynBFS; DynBetweenness; DynBetweennessOneNode; DynConnectedComponents; DynKatzCentrality; DynPrunedLandmarkLabeling; DynWeaklyConnectedComponents</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-dynamic_update-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: DynBFS; DynBetweenness; DynBetweennessOneNode; DynConnectedComponents; DynKatzCentrality; DynPrunedLandmarkLabeling; DynWeaklyConnectedComponents.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
