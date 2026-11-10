---
title: "Spectral gap"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Spectral gap {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Spectra. Concept id: `spectral_gap`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(\lambda_1\ge\lambda_2\ge\cdots\)</td><td>eigenvalues of the adjacency matrix</td></tr><tr><td>\(\mu_2\)</td><td>second-smallest Laplacian eigenvalue</td></tr></tbody></table></div>

## Definition {#concept-definition}

Spectral gap. Entries grouped here: Spectral gap.

*Definition partly written:* The tool function is known by name only; which matrix it uses is not recorded, so both published forms are given.

<div class="formula-block"><p class="formula-name"><strong>Spectral gap of a regular graph (Hoory, Linial and Wigderson 2006)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\mathrm{gap}(G)=d-\lambda_2\]</div><p class="formula-where">For a \(d\)-regular graph the difference between the largest adjacency eigenvalue \(\lambda_1=d\) and the second; equal to \(\mu_2\) of the Laplacian \(dI-A\), so it coincides with the algebraic connectivity.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Laplacian gap</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\mathrm{gap}_L(G)=\mu_2\]</div><p class="formula-where">For non-regular graphs the gap is usually taken as the algebraic connectivity \(\mu_2\) of the Laplacian; the adjacency form \(\lambda_1-\lambda_2\) is a different number.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_gap_spectral">Spectral gap</a></td><td><code>cat_gap_spectral</code></td><td>1</td><td>The gap between the first two eigenvalues; whether the tool uses the adjacency, Laplacian or normalized Laplacian is not recorded.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/netrankr.html">netrankr</a></th></tr></thead><tbody><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">\(\mu_2=0\): the Laplacian gap is 0; the adjacency gap \(\lambda_1-\lambda_2\) is 0 when two components share the largest eigenvalue.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">\(n&lt;2\): there is no second eigenvalue; not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Too few nodes for the formula</summary><ul><li>No tool entries.</li></ul></details></div>

## Spectral gap {#cat_gap_spectral}

Measure id: `cat_gap_spectral`. Original family: Matrices and spectra.

**Definition.** Spectral gap.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_gap_spectral-netrankr">details</a></td><td><code>spectral_gap</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_gap_spectral-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: spectral\_gap.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)
{% endraw %}
