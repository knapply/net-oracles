---
title: "Triad enumeration"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Triad enumeration {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Triads, motifs and local structure. Concept id: `triad_enumeration`. 2 measures.

## Definition {#concept-definition}

Triad enumeration. Entries grouped here: All triads; Liststriads.

*Definition not yet written.* Documented only (NetworkX all\_triads and UCINET Liststriads), never run; the sources give the name and the tool's function, not a formula, and no verified bibliography entry for the original definition is available.

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_all_triads">All triads</a></td><td><code>cat_all_triads</code></td><td>1</td></tr><tr><td><a href="#cat_liststriads">Liststriads</a></td><td><code>cat_liststriads</code></td><td>1</td></tr></tbody></table></div>

## All triads {#cat_all_triads}

Measure id: `cat_all_triads`. Original family: Cohesion and subgroups.

**Definition.** All triads.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_all_triads-networkx">details</a></td><td><code>all_triads</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_all_triads-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: all\_triads.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Liststriads {#cat_liststriads}

Measure id: `cat_liststriads`. Original family: Cohesion and subgroups.

**Definition.** Liststriads.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-cat_liststriads-ucinet">details</a></td><td><code>liststriads</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_liststriads-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
