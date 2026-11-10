---
title: "Sparse-matrix orderings and bandwidth"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Sparse-matrix orderings and bandwidth {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Graph matrices. Concept id: `matrix_bandwidth`. 1 measure.

## Definition {#concept-definition}

Sparse-matrix orderings and bandwidth. Entries grouped here: Sparse-matrix orderings and bandwidth/wavefront.

## Sparse-matrix orderings and bandwidth/wavefront {#matrix_bandwidth}

Measure id: `matrix_bandwidth`. Original family: Matrices and spectra.

**Definition.** Sparse-matrix orderings and bandwidth/wavefront.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-matrix_bandwidth-boost) | `aver_wavefront; bandwidth; cuthill_mckee_ordering; ith_bandwidth; ith_wavefront; king_ordering; max_wavefront; minimum_degree_ordering; rms_wavefront; sloan_ordering` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-matrix_bandwidth-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: aver\_wavefront; bandwidth; cuthill\_mckee\_ordering; ith\_bandwidth; ith\_wavefront; king\_ordering; max\_wavefront; minimum\_degree\_ordering; rms\_wavefront; sloan\_ordering.

**Tools cited:** [siek2002boost](../../references.html#siek2002boost)
{% endraw %}
