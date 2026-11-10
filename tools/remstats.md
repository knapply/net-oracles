---
title: "remstats / remify"
layout: default
parent: Tools
---

{% raw %}

# remstats / remify

| Field | Value |
|---|---|
| Identifier | `remstats` |
| Language | R |
| Version tested | remstats 4.1.0, remstimate 3.1.0, remify 4.1.0 |
| License | see package DESCRIPTION |
| Homepage | <https://cran.r-project.org/package=remstats> |
| Role | checked |
| Citation | [arena2026remstats](../references.html#arena2026remstats) |

## How it was run

Called from R on relational event sequences.

## Coverage

| State | Measures |
|---|---|
| <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | 1 |
| <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | 1 |

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names | Why, if not agrees |
|---|---|---|---|---|---|---|
| Temporal and events | Relational event models | [Relational event model fit](../measures/temporal-and-events/rem_fit.html) | [Rem fit](../measures/temporal-and-events/rem_fit.html#rem_fit) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (ties): remstimate's coefficients differ by up to a few percent on these fixtures, while the reference agrees with the definition oracle's Newton iteration... [details](../measures/temporal-and-events/rem_fit.html#why-rem_fit-remstats) |
| Temporal and events | Relational event models | [Relational event statistics](../measures/temporal-and-events/rem_statistic.html) | [Rem statistic](../measures/temporal-and-events/rem_statistic.html#rem_statistic) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
{% endraw %}
