---
title: "Global and local efficiency"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Global and local efficiency {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Efficiency and reachability. Concept id: `global_efficiency`. 2 measures.

## Definition {#concept-definition}

Global and local efficiency. Entries grouped here: Global and local efficiency; Swan efficiency.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Global and local efficiency](#efficiency_global) | `efficiency_global` | 4 |
| [Swan efficiency](#cat_efficiency_swan) | `cat_efficiency_swan` | 1 |

## Global and local efficiency {#efficiency_global}

Measure id: `efficiency_global`. Original family: Paths and distances.

**Definition.** Global and local efficiency.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `efficiency; global_efficiency; local_efficiency` | API listing |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `average_local_efficiency; global_efficiency; local_efficiency` | API listing |
| [sna](../../tools/sna.html) | · reported in docs | `efficiency` | API listing |
| [BCT (Octave)](../../tools/bct.html) | · reported in docs | `efficiency_bin; efficiency_wei` | API listing |

**Tools cited:** [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [rubinov2010complex](../../references.html#rubinov2010complex)

## Swan efficiency {#cat_efficiency_swan}

Measure id: `cat_efficiency_swan`. Original family: Descriptive statistics.

**Definition.** Swan efficiency.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [netrankr](../../tools/netrankr.html) | · reported in docs | `swan_efficiency` | API listing |

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)
{% endraw %}
