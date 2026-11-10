---
title: "Infomap"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Infomap {#concept-top}

Family: [Communities](index.html). Subfamily: Other detection algorithms. Concept id: `infomap`. 1 measure.

## Definition {#concept-definition}

Infomap. Entries grouped here: Infomap.

*Definition not yet written.*

## Infomap {#infomap}

Measure id: `infomap`. Original family: Communities.

**Definition.** Infomap.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>cluster_infomap</code></td><td></td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-infomap-pyigraph">details</a></td><td><code>community_infomap</code></td><td>API listing</td></tr><tr><td><a href="../../tools/infomap.html">Infomap</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-infomap-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_infomap.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>infomap_native</code></td><td>Infomap</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) loops</td><td>self_loops</td><td>abs 1e-09, rel 1e-09</td><td><code>Infomap(two_level = True, directed = False, num_trials = 10, seed = 1) on the links without loops; its codelength</code></td><td>Infomap leaves self-links out unless asked; the reference value's flow counts them</td></tr><tr><td><code>infomap_native_weighted</code></td><td>Infomap</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) loops</td><td>self_loops</td><td>abs 1e-09, rel 1e-09</td><td><code>as infomap_native with link weights</code></td><td>Infomap leaves self-links out unless asked; the reference value's flow counts them</td></tr><tr><td><code>infomap_partition</code></td><td>Infomap</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>map equation (definition oracle, tau = 0.15) of the partition Infomap(two_level = True, num_trials = 10, seed = 1) finds</code></td><td></td></tr><tr><td><code>infomap_partition_weighted</code></td><td>Infomap</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>as infomap_partition with link weights</code></td><td></td></tr><tr><td><code>infomap_quality</code></td><td>igraph (R)</td><td>undirected</td><td>differs</td><td>edge_case</td><td>defaults, ties</td><td>abs 0.02, rel 0</td><td><code>mean over set.seed(1..5) of cluster_infomap(g, nb.trials = 10)$codelength</code></td><td>a network without edges has no random walk; the reference reports -1 (undefined) where igraph may report a codelength of 0</td></tr></tbody></table></div>

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [rosvall2008maps](../../references.html#rosvall2008maps)
{% endraw %}
