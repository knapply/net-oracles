---
title: "remstats / remify"
layout: default
parent: Tools
---

{% raw %}

# remstats / remify

<div class="table-wrapper"><table><thead><tr><th>Field</th><th>Value</th></tr></thead><tbody><tr><td>Identifier</td><td><code>remstats</code></td></tr><tr><td>Language</td><td>R</td></tr><tr><td>Version tested</td><td>remstats 4.1.0, remstimate 3.1.0, remify 4.1.0</td></tr><tr><td>License</td><td>see package DESCRIPTION</td></tr><tr><td>Homepage</td><td><https://cran.r-project.org/package=remstats></td></tr><tr><td>Role</td><td>checked</td></tr><tr><td>Citation</td><td><a href="../references.html#arena2026remstats">arena2026remstats</a></td></tr></tbody></table></div>

## How it was run

Called from R on relational event sequences.

## Coverage

<div class="table-wrapper"><table><thead><tr><th>State</th><th>Measures</th></tr></thead><tbody><tr><td><a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td>1</td></tr><tr><td><a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>1</td></tr></tbody></table></div>

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

<div class="table-wrapper"><table><thead><tr><th>Family</th><th>Subfamily</th><th>Concept</th><th>Measure (variant)</th><th>State</th><th>API names</th><th>Why, if not agrees</th></tr></thead><tbody><tr><td>Temporal and events</td><td>Relational event models</td><td><a href="../measures/temporal-and-events/rem_fit.html">Relational event model fit</a></td><td><a href="../measures/temporal-and-events/rem_fit.html#rem_fit">Rem fit</a></td><td><a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td></td><td>Differs by convention (ties): remstimate's coefficients differ by up to a few percent on these fixtures, while the reference agrees with the definition oracle's Newton iteration... <a href="../measures/temporal-and-events/rem_fit.html#why-rem_fit-remstats">details</a></td></tr><tr><td>Temporal and events</td><td>Relational event models</td><td><a href="../measures/temporal-and-events/rem_statistic.html">Relational event statistics</a></td><td><a href="../measures/temporal-and-events/rem_statistic.html#rem_statistic">Rem statistic</a></td><td><a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td></tr></tbody></table></div>
{% endraw %}
