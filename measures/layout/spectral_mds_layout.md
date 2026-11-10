---
title: "Spectral and MDS layouts"
layout: default
parent: "Layout"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Spectral and MDS layouts {#concept-top}

Family: [Layout](index.html). Subfamily: Layout algorithms. Concept id: `spectral_mds_layout`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(D^{(2)}\)</td><td>matrix of squared graph distances \(d_{ij}^2\)</td></tr><tr><td>\(J\)</td><td>centering matrix \(I-\tfrac1n\mathbf 1\mathbf 1^{\top}\)</td></tr><tr><td>\(B\)</td><td>double-centered matrix</td></tr><tr><td>\(\lambda_k,v_k\)</td><td>the largest eigenvalues of \(B\) and their unit eigenvectors</td></tr></tbody></table></div>

## Definition {#concept-definition}

Spectral and MDS layouts. Entries grouped here: Layout spectral; Multidimensional scaling layout.

*Definition partly written:* Classical multidimensional scaling is written (Torgerson 1952). The Laplacian-eigenvector (spectral) layout is named by the sources and its formula is not given here, so it has no variant entry.

<div class="formula-block"><p class="formula-name"><strong>Classical scaling (Torgerson 1952)</strong> <span class="applies">applies to: any, connected</span></p><div class="formula">\[B=-\tfrac12\,J\,D^{(2)}J,\qquad x_i=\bigl(\sqrt{\lambda_1}\,v_1(i),\ \sqrt{\lambda_2}\,v_2(i)\bigr)\]</div><p class="formula-where">Coordinates are the leading eigenvector components of the double-centered squared distances, scaled by the square roots of the eigenvalues. Defined for connected graphs; negative or missing eigenvalues are dropped.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#layout_mds">Multidimensional scaling layout</a></td><td><code>layout_mds</code></td><td>2</td><td>Classical scaling of the graph distance matrix into two dimensions, as above.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/igraph.html">igraph (R)</a></th><th><a href="../../tools/pyigraph.html">igraph (Python)</a></th><th><a href="../../tools/graphlayouts.html">graphlayouts</a></th></tr></thead><tbody><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Not defined: \(d_{ij}=\infty\) for pairs in different components.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details></div>

## Layout spectral {#cat_layout_spectral}

Measure id: `cat_layout_spectral`. Original family: Layout.

**Definition.** Layout spectral.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphlayouts.html">graphlayouts</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: graphlayouts is documented-only in this survey; listed in its documentation. <a href="#why-cat_layout_spectral-graphlayouts">details</a></td><td><code>layout_spectral</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_layout_spectral-graphlayouts"></a>**[graphlayouts](../../tools/graphlayouts.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. graphlayouts (1.2.5) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of graphlayouts 1.2.5: help topics.

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Multidimensional scaling layout {#layout_mds}

Measure id: `layout_mds`. Original family: Layout.

**Definition.** Multidimensional scaling layout.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-layout_mds-igraph">details</a></td><td><code>layout_with_mds</code></td><td>API listing</td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-layout_mds-pyigraph">details</a></td><td><code>layout_mds</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-layout_mds-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: layout\_with\_mds.
- <a id="why-layout_mds-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: layout\_mds.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
