---
title: "manynet"
layout: default
parent: Tools
---

{% raw %}

# manynet

<div class="table-wrapper"><table><thead><tr><th>Field</th><th>Value</th></tr></thead><tbody><tr><td>Identifier</td><td><code>manynet</code></td></tr><tr><td>Language</td><td>R</td></tr><tr><td>Version tested</td><td>2.4.0</td></tr><tr><td>License</td><td>MIT</td></tr><tr><td>Homepage</td><td><https://cran.r-project.org/package=manynet></td></tr><tr><td>Role</td><td>checked</td></tr><tr><td>Citation</td><td><a href="../references.html#tool_manynet">tool_manynet</a></td></tr></tbody></table></div>

## How it was run

Called from R on igraph objects.

## Coverage

<div class="table-wrapper"><table><thead><tr><th>State</th><th>Measures</th></tr></thead><tbody><tr><td><a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td>1</td></tr><tr><td><a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>2</td></tr></tbody></table></div>

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

<div class="table-wrapper"><table><thead><tr><th>Family</th><th>Subfamily</th><th>Concept</th><th>Measure (variant)</th><th>State</th><th>API names</th><th>Why, if not agrees</th></tr></thead><tbody><tr><td>Roles and positions</td><td>Structural holes and brokerage</td><td><a href="../measures/roles-and-positions/burt_constraint.html">Burt constraint</a></td><td><a href="../measures/roles-and-positions/burt_constraint.html#constraint">Constraint</a></td><td><a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td></tr><tr><td>Roles and positions</td><td>Structural holes and brokerage</td><td><a href="../measures/roles-and-positions/burt_efficiency.html">Burt efficiency</a></td><td><a href="../measures/roles-and-positions/burt_efficiency.html#efficiency">Efficiency</a></td><td><a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td></td><td>Differs by convention (defaults, direction, multi-edges, normalization, self-loops and ties): manynet (netrics) returns a different value from the reference on directed networks, on multigraphs with loops, and on the two-node network (about... <em>(reason incomplete)</em> <a href="../measures/roles-and-positions/burt_efficiency.html#why-efficiency-manynet">details</a></td></tr><tr><td>Roles and positions</td><td>Structural holes and brokerage</td><td><a href="../measures/roles-and-positions/effective_size.html">Effective size</a></td><td><a href="../measures/roles-and-positions/effective_size.html#effective_size">Effective size</a></td><td><a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td></td><td>Differs by convention (defaults, direction, multi-edges, normalization, self-loops and ties): manynet (netrics) returns a different value from the reference on directed networks, on multigraphs with loops, and on the two-node network (about... <em>(reason incomplete)</em> <a href="../measures/roles-and-positions/effective_size.html#why-effective_size-manynet">details</a></td></tr></tbody></table></div>

## Findings

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../findings.html#f082">F082</a></td><td>defect</td><td>Effective size and efficiency differ on directed networks and multigraphs with loops</td></tr><tr><td><a href="../findings.html#f083">F083</a></td><td>defect</td><td>hierarchy differs from the definition on all 25 fixtures</td></tr></tbody></table></div>
{% endraw %}
