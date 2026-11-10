---
title: "R-MAT"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# R-MAT {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Growth and attachment models. Concept id: `rmat`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(a,b,c,d\)</td><td>quadrant probabilities with \(a+b+c+d=1\)</td></tr><tr><td>\(n\)</td><td>a power of 2: nodes \(2^{s}\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

R-MAT. Entries grouped here: R-MAT generator.

*Definition partly written:* The recursive quadrant rule is written; the tool options (noise, edge factor) are named only.

<div class="formula-block"><p class="formula-name"><strong>R-MAT (Chakrabarti, Zhan and Faloutsos 2004)</strong> <span class="applies">applies to: directed, multigraph</span></p><div class="formula">\[\Pr\bigl(\text{edge in quadrant }q\bigr)=a,b,c,d\ \text{ for top-left, top-right, bottom-left, bottom-right; recurse }s\text{ times}\]</div><p class="formula-where">Each edge is placed by choosing a quadrant of the adjacency matrix with these probabilities and recursing into it until a single cell remains; repeated cells give parallel edges. A generator returns a random sample, so a result is reproducible only for a fixed seed and random generator; tools use different generators.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#gen_rmat">R-MAT generator</a></td><td><code>gen_rmat</code></td><td>2</td><td>Recursive quadrant model above.</td></tr></tbody></table></div>

## R-MAT generator {#gen_rmat}

Measure id: `gen_rmat`. Original family: Generators and rewiring.

**Definition.** R-MAT generator.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gen_rmat-networkit">details</a></td><td><code>RmatGenerator</code></td><td>API listing</td></tr><tr><td><a href="../../tools/boost.html">Boost Graph Library</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gen_rmat-boost">details</a></td><td><code>rmat_graph_generator</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_rmat-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: RmatGenerator.
- <a id="why-gen_rmat-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: rmat\_graph\_generator.

**Tools cited:** [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
