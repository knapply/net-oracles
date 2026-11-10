---
title: "graspologic"
layout: default
parent: Tools
---

{% raw %}

# graspologic

<div class="table-wrapper"><table><thead><tr><th>Field</th><th>Value</th></tr></thead><tbody><tr><td>Identifier</td><td><code>graspologic</code></td></tr><tr><td>Language</td><td>Python</td></tr><tr><td>Version tested</td><td>3.4.4</td></tr><tr><td>License</td><td>MIT</td></tr><tr><td>Homepage</td><td><https://graspologic-org.github.io/graspologic/></td></tr><tr><td>Role</td><td>checked</td></tr><tr><td>Citation</td><td><a href="../references.html#tool_graspologic">tool_graspologic</a></td></tr></tbody></table></div>

## How it was run

Imported in CPython; functions called on NumPy matrices.

## Coverage

<div class="table-wrapper"><table><thead><tr><th>State</th><th>Measures</th></tr></thead><tbody><tr><td><a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>2</td></tr></tbody></table></div>

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

<div class="table-wrapper"><table><thead><tr><th>Family</th><th>Subfamily</th><th>Concept</th><th>Measure (variant)</th><th>State</th><th>API names</th><th>Why, if not agrees</th></tr></thead><tbody><tr><td>Communities</td><td>Partition and cover quality</td><td><a href="../measures/communities/modularity.html">Modularity</a></td><td><a href="../measures/communities/modularity.html#modularity">Modularity</a></td><td><a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td></td><td>Differs by convention (direction, multi-edges, normalization, self-loops and weights): graspologic-native adds an undirected self-loop's weight once to the community's internal weight but twice to the node's degree (exact rational... <a href="../measures/communities/modularity.html#why-modularity-graspologic">details</a></td></tr><tr><td>Matrices and spectra</td><td>Graph matrices</td><td><a href="../measures/matrices-and-spectra/laplacian_matrix.html">Laplacian matrix</a></td><td><a href="../measures/matrices-and-spectra/laplacian_matrix.html#gm_laplacian">Gm laplacian</a></td><td><a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td></td><td>Differs by convention (direction): For a directed graph graspologic's 'I-DAD' form is D_in^-1/2 (D_in - A) D_in^-1/2 with in-degrees (graspologic/utils/utils.py, to_laplacian), and a... <a href="../measures/matrices-and-spectra/laplacian_matrix.html#why-gm_laplacian-graspologic">details</a></td></tr></tbody></table></div>

## Findings

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../findings.html#f072">F072</a></td><td>convention</td><td>The I-DAD normalized Laplacian normalizes by in-degrees on directed graphs</td></tr></tbody></table></div>
{% endraw %}
