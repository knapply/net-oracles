---
title: "cdlib"
layout: default
parent: Tools
---

{% raw %}

# cdlib

<div class="table-wrapper"><table><thead><tr><th>Field</th><th>Value</th></tr></thead><tbody><tr><td>Identifier</td><td><code>cdlib</code></td></tr><tr><td>Language</td><td>Python</td></tr><tr><td>Version tested</td><td>0.4.1</td></tr><tr><td>License</td><td>BSD-2-Clause</td></tr><tr><td>Homepage</td><td><https://cdlib.readthedocs.io></td></tr><tr><td>Role</td><td>checked</td></tr><tr><td>Citation</td><td><a href="../references.html#tool_cdlib">tool_cdlib</a></td></tr></tbody></table></div>

## How it was run

Imported in CPython; evaluation functions called on communities.

## Coverage

<div class="table-wrapper"><table><thead><tr><th>State</th><th>Measures</th></tr></thead><tbody><tr><td><a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>2</td></tr></tbody></table></div>

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

<div class="table-wrapper"><table><thead><tr><th>Family</th><th>Subfamily</th><th>Concept</th><th>Measure (variant)</th><th>State</th><th>API names</th><th>Why, if not agrees</th></tr></thead><tbody><tr><td>Communities</td><td>Partition and cover quality</td><td><a href="../measures/communities/modularity.html">Modularity</a></td><td><a href="../measures/communities/modularity.html#modularity">Modularity</a></td><td><a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td></td><td>Differs by convention (direction, multi-edges and self-loops): cdlib's newman_girvan_modularity counts the parallel edges inside a community once while the edge total and the degrees count every copy (a triangle... <a href="../measures/communities/modularity.html#why-modularity-cdlib">details</a></td></tr><tr><td>Communities</td><td>Partition comparison and operations</td><td><a href="../measures/communities/compare_partitions.html">Compare partitions</a></td><td><a href="../measures/communities/compare_partitions.html#compare_partitions">Compare partitions</a></td><td><a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td></td><td>Differs by convention (defaults): For partitions of one element cdlib (through scikit-learn) returns 1.0. <a href="../measures/communities/compare_partitions.html#why-compare_partitions-cdlib">details</a></td></tr></tbody></table></div>

## Findings

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../findings.html#f037">F037</a></td><td>convention</td><td>Adjusted Rand index is 1 on degenerate partitions</td></tr></tbody></table></div>
{% endraw %}
