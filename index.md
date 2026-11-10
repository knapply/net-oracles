---
title: Home
layout: default
nav_order: 1
permalink: /
---

{% raw %}
# net-oracles

A neutral, citable survey of network-analysis software: which tool implements which measure, how their conventions differ, which bugs and disagreements were found, and how the tools were benchmarked. Every claim carries a citation key; every table on these pages is generated from the machine-readable files in [`data/`](https://github.com/knapply/net-oracles/tree/main/data).

**47 tools** (34 run and compared), **1635 measures** in 21 families, **2524 tool-by-measure entries** (671 checked by running the tool), **90 findings** about other tools' behaviour, and 1228 benchmark rows.

## Where to go

| Page | What it holds |
|---|---|
| [Capability matrix](matrix.html) | Measure by tool, one section per family, with the state of each entry. |
| [Measures](measures/) | One page per measure: who implements it, convention differences, tolerances, findings, citations. |
| [Tools](tools/) | One page per tool: version tested, license, how it was run, coverage, findings. |
| [Findings](findings.html) | Bugs, disagreements and limitations found in other tools, with reproductions where recorded. |
| [Benchmarks](benchmarks.html) | Method and timing summaries for the other tools; raw rows are in `data/benchmarks/`. |
| [References](references.html) | Every cited package and paper. |
| [Data and schemas](data.html) | File formats, joins and the state vocabulary. |

## How entries are labelled

Each tool-by-measure entry has one state:

| State | Meaning |
|---|---|
| `checked-agrees` | checked, agrees (✓) |
| `checked-convention` | checked, differs by convention (≠) |
| `checked-defect` | checked, defect (✗) |
| `checked-no-value` | checked, no value on some inputs (∅) |
| `reported-in-docs` | reported in docs (·) |

The definitions are in `data/schema/capabilities.schema.json`. A tool marked *documented-only* was never run: its entries come from its documentation and are always `reported-in-docs`.

A *reference value* in these pages means the value of the published definition, evaluated independently (brute force on small graphs, in exact arithmetic where the quantity allows), and confirmed against other tools before a difference is attributed to a convention.
{% endraw %}
