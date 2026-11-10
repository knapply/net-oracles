---
title: "Motif census"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Motif census {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Triads, motifs and local structure. Concept id: `motif_census`. 1 measure.

## Definition {#concept-definition}

Motif census. Entries grouped here: Motif census.

## Motif census {#motif_census}

Measure id: `motif_census`. Original family: Cohesion and subgroups.

**Definition.** Motif census.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's documentation; no comparison set up for this measure yet. [details](#why-motif_census-igraph) | `count_motifs; graphlets; motifs; sample_motifs` | documentation |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-motif_census-pyigraph) | `motifs_randesu; motifs_randesu_estimate; motifs_randesu_no` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's documentation; no comparison set up for this measure yet. [details](#why-motif_census-graphtool) | `motif_significance; motifs` | documentation |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-motif_census-bct) | `find_motif34; motif3funct_bin; motif3funct_wei; motif3struct_bin; motif3struct_wei; motif4funct_bin; motif4funct_wei; motif4struct_bin; motif4struct_wei` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-motif_census-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (R package igraph: exported functions and help titles); API names: count\_motifs; graphlets; motifs; sample\_motifs.
- <a id="why-motif_census-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: motifs\_randesu; motifs\_randesu\_estimate; motifs\_randesu\_no.
- <a id="why-motif_census-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (graph-tool public classes and functions); API names: motif\_significance; motifs.
- <a id="why-motif_census-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: find\_motif34; motif3funct\_bin; motif3funct\_wei; motif3struct\_bin; motif3struct\_wei; motif4funct\_bin; motif4funct\_wei; motif4struct\_bin; motif4struct\_wei.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [rubinov2010complex](../../references.html#rubinov2010complex)
{% endraw %}
