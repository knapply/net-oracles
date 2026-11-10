---
title: "GAP Benchmark Suite"
layout: default
parent: Tools
---

{% raw %}
# GAP Benchmark Suite

| Field | Value |
|---|---|
| Identifier | `gapbs` |
| Language | C++ |
| Version tested | 941462c7c42e |
| License | BSD-3-Clause |
| Homepage | <https://github.com/sbeamer/gapbs> |
| Role | benchmarked-only |
| Citation | [beamer2015gap](../references.html#beamer2015gap) |

## How it was run

Compiled reference kernels run with the thread counts listed in the benchmark data.

## Findings

| Id | Kind | Title |
|---|---|---|
| [F088](../findings.html#f088) | convention | Rank held by dangling vertices is not passed on |
| [F089](../findings.html#f089) | convention | The BC verifier uses a float-epsilon tolerance against its own float accumulation |
{% endraw %}
