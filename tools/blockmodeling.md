---
title: "blockmodeling"
layout: default
parent: Tools
---

{% raw %}

# blockmodeling

<div class="table-wrapper"><table><thead><tr><th>Field</th><th>Value</th></tr></thead><tbody><tr><td>Identifier</td><td><code>blockmodeling</code></td></tr><tr><td>Language</td><td>R</td></tr><tr><td>Version tested</td><td>1.1.8</td></tr><tr><td>License</td><td>see package DESCRIPTION</td></tr><tr><td>Homepage</td><td><https://cran.r-project.org/package=blockmodeling></td></tr><tr><td>Role</td><td>checked</td></tr><tr><td>Citation</td><td><a href="../references.html#ziberna2007generalized">ziberna2007generalized</a></td></tr></tbody></table></div>

## How it was run

Called from R on matrices.

Capabilities listed by introspection of R package blockmodeling: exported functions and help titles.

## Coverage

<div class="table-wrapper"><table><thead><tr><th>State</th><th>Measures</th></tr></thead><tbody><tr><td><a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td>1</td></tr><tr><td><a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>1</td></tr><tr><td><a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>3</td></tr></tbody></table></div>

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

<div class="table-wrapper"><table><thead><tr><th>Family</th><th>Subfamily</th><th>Concept</th><th>Measure (variant)</th><th>State</th><th>API names</th><th>Why, if not agrees</th></tr></thead><tbody><tr><td>Roles and positions</td><td>Blockmodels</td><td><a href="../measures/roles-and-positions/block_density.html">Block density</a></td><td><a href="../measures/roles-and-positions/block_density.html#block_density">Block density</a></td><td><a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td></tr><tr><td>Roles and positions</td><td>Blockmodels</td><td><a href="../measures/roles-and-positions/blockmodel_criterion.html">Blockmodel criterion function</a></td><td><a href="../measures/roles-and-positions/blockmodel_criterion.html#cat_c_crit_fun">Crit Fun C</a></td><td><a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td><code>critFunC</code></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="../measures/roles-and-positions/blockmodel_criterion.html#why-cat_c_crit_fun-blockmodeling">details</a></td></tr><tr><td>Roles and positions</td><td>Blockmodels</td><td><a href="../measures/roles-and-positions/blockmodel_search.html">Direct blockmodel search</a></td><td><a href="../measures/roles-and-positions/blockmodel_search.html#blockmodel_search">Direct blockmodel search (structural, regular, generalised block types)</a></td><td><a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td><code>optParC; optRandomParC</code></td><td>Not run: listed in the tool's documentation; no comparison set up for this measure yet. <a href="../measures/roles-and-positions/blockmodel_search.html#why-blockmodel_search-blockmodeling">details</a></td></tr><tr><td>Roles and positions</td><td>Equivalence and clustering</td><td><a href="../measures/roles-and-positions/regular_equivalence.html">Regular equivalence (REGE, CATREGE)</a></td><td><a href="../measures/roles-and-positions/regular_equivalence.html#regular_equivalence">Regular equivalence</a></td><td><a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td><code>REGD.for; REGD.ne.for; REGD.ow.for; REGE; REGE.FC; REGE.FC.ow; REGE.for; REGE.ne.for; REGE.nm.diag.for; REGE.nm.for; REGE.nm.ne.for; REGE.ow</code></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="../measures/roles-and-positions/regular_equivalence.html#why-regular_equivalence-blockmodeling">details</a></td></tr><tr><td>Roles and positions</td><td>Equivalence and clustering</td><td><a href="../measures/roles-and-positions/structural_equivalence.html">Structural equivalence</a></td><td><a href="../measures/roles-and-positions/structural_equivalence.html#structural_equivalence">Structural equivalence</a></td><td><a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td><code>sedist</code></td><td>Differs by convention (direction): On a symmetric matrix (every undirected fixture and complete5_dir) blockmodeling::sedist agrees with the reference. <a href="../measures/roles-and-positions/structural_equivalence.html#why-structural_equivalence-blockmodeling">details</a></td></tr></tbody></table></div>

## Findings

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../findings.html#f084">F084</a></td><td>convention</td><td>Profiles keep the entries for the two nodes themselves on asymmetric matrices</td></tr></tbody></table></div>
{% endraw %}
