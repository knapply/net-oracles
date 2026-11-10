---
title: Home
layout: default
nav_order: 1
permalink: /
---

{% raw %}

<section class="hero" aria-labelledby="hero-title"><canvas id="hero-graph" class="hero-graph" aria-hidden="true"></canvas><div class="hero-body"><h1 id="hero-title">net-oracles</h1><p class="hero-lead">Which network-analysis tool implements which measure, and where their answers differ.</p><ul class="hero-counts"><li><b>47</b>tools</li><li><b>1635</b>measures</li><li><b>702</b>concepts</li><li><b>90</b>findings</li><li><b>1228</b>benchmark rows</li></ul></div></section>

A neutral, citable survey of network-analysis software: which tool implements which measure, how their conventions differ, which bugs and disagreements were found, and how the tools were benchmarked. Every claim carries a citation key; every table on these pages is generated from the machine-readable files in [`data/`](https://github.com/knapply/net-oracles/tree/main/data).

**47 tools** (34 run and compared), **1635 measures** grouped into 702 concepts in 21 families, **2524 tool-by-measure entries** (671 checked by running the tool), **90 findings** about other tools' behaviour, and 1228 benchmark rows.

## Where to go

<nav class="cards" aria-label="Sections"><a class="card" href="measures/"><strong>Families</strong><span>21 families, 702 concepts and 1635 measures.</span></a><a class="card" href="tools/"><strong>Tools</strong><span>47 tools, 34 run and compared.</span></a><a class="card" href="matrix.html"><strong>Capability matrix</strong><span>Measure by tool, with the state of each entry.</span></a><a class="card" href="findings.html"><strong>Findings</strong><span>90 bugs, disagreements and limitations.</span></a><a class="card" href="benchmarks.html"><strong>Benchmarks</strong><span>Method and 1228 timing rows.</span></a><a class="card" href="references.html"><strong>References</strong><span>Every cited package and paper.</span></a><a class="card" href="data.html"><strong>Data and schemas</strong><span>File formats, joins and the state vocabulary.</span></a><a class="card" href="llms.txt"><strong>llms.txt</strong><span>Every data file, its schema and how the files join, as plain text.</span></a></nav>

## How entries are labelled

Each tool-by-measure entry has one state:

| State | Meaning |
|---|---|
| `checked-agrees` | <span class="st st-g st-ok" role="img" aria-label="checked, agrees" title="checked, agrees">✓</span> checked, agrees |
| `checked-convention` | <span class="st st-g st-conv" role="img" aria-label="checked, differs by convention" title="checked, differs by convention">≠</span> checked, differs by convention |
| `checked-defect` | <span class="st st-g st-defect" role="img" aria-label="checked, defect" title="checked, defect">✗</span> checked, defect |
| `checked-no-value` | <span class="st st-g st-nov" role="img" aria-label="checked, no value on some inputs" title="checked, no value on some inputs">∅</span> checked, no value on some inputs |
| `reported-in-docs` | <span class="st st-g st-docs" role="img" aria-label="reported in docs" title="reported in docs">·</span> reported in docs |

The definitions are in `data/schema/capabilities.schema.json`. A tool marked *documented-only* was never run: its entries come from its documentation and are always `reported-in-docs`.

A *reference value* in these pages means the value of the published definition, evaluated independently (brute force on small graphs, in exact arithmetic where the quantity allows), and confirmed against other tools before a difference is attributed to a convention.
{% endraw %}
