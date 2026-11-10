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

<nav class="cards" aria-label="Sections"><a class="card" href="measures/"><strong>Families</strong><span>21 families, 702 concepts and 1635 measures.</span></a><a class="card" href="tools/"><strong>Tools</strong><span>47 tools, 34 run and compared.</span></a><a class="card" href="matrix.html"><strong>Capability matrix</strong><span>Measure by tool, with the state of each entry and the reason for it.</span></a><a class="card" href="method.html"><strong>How entries are labelled</strong><span>What was compared, how, on which inputs, and what each state means.</span></a><a class="card" href="findings.html"><strong>Findings</strong><span>90 bugs, disagreements and limitations.</span></a><a class="card" href="benchmarks.html"><strong>Benchmarks</strong><span>Method and 1228 timing rows.</span></a><a class="card" href="references.html"><strong>References</strong><span>Every cited package and paper.</span></a><a class="card" href="data.html"><strong>Data and schemas</strong><span>File formats, joins and the state vocabulary.</span></a><a class="card" href="llms.txt"><strong>llms.txt</strong><span>Every data file, its schema and how the files join, as plain text.</span></a></nav>

## How entries are labelled

Each tool-by-measure entry has one state. Every state other than `checked-agrees` carries a reason, shown wherever the entry is shown. The full definitions, the comparison rules and the fixture list are on [How entries are labelled](method.html).

<div class="table-wrapper"><table><thead><tr><th>State</th><th>Meaning</th></tr></thead><tbody><tr><td><a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> <code>checked-agrees</code></td><td>The tool was run and its value equals the reference value of the published definition, within the stated tolerance, on every fixture the tool accepts. No convention is mapped.</td></tr><tr><td><a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> <code>checked-convention</code></td><td>The tool was run and on some fixtures its value differs from the reference value because it follows a different, documented convention. The entry states the convention, what each side does, the relation between the two values and the tolerances.</td></tr><tr><td><a class="st st-t st-defect" href="method.html#state-checked-defect"><span class="g" aria-hidden="true">✗</span>checked, defect</a> <code>checked-defect</code></td><td>The tool was run and on some inputs its value is wrong under the published definition. The entry states what is wrong, on which inputs, observed against expected, the tool version and the finding.</td></tr><tr><td><a class="st st-t st-nov" href="method.html#state-checked-no-value"><span class="g" aria-hidden="true">∅</span>checked, no value on some inputs</a> <code>checked-no-value</code></td><td>The tool was run but gave no value on the compared inputs, so no comparison could be made. The entry states on which inputs and why.</td></tr><tr><td><a class="st st-t st-docs" href="method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> <code>reported-in-docs</code></td><td>The tool lists the capability in its documentation or public API, but it was not run for this measure. The entry states why and the documentation source.</td></tr></tbody></table></div>

A tool marked *documented-only* was never run: its entries come from its documentation and are always `reported-in-docs`. A *reference value* is the value of the published definition, evaluated independently of every tool compared (see [How entries are labelled](method.html#reference-value)).
{% endraw %}
