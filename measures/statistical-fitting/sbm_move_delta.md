---
title: "SBM move delta"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# SBM move delta {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `sbm_move_delta`. 1 measure.

## Definition {#concept-definition}

SBM move delta. Entries grouped here: Sbm move delta.

## Sbm move delta {#sbm_move_delta}

Measure id: `sbm_move_delta`. Original family: Statistical fitting.

**Definition.** Sbm move delta.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `sbm_move_delta_b1` | graph-tool | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `graph-tool entropy of the partition after the move minus before` | The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node). |
| `sbm_move_delta_b3` | graph-tool | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `graph-tool entropy of the partition after the move minus before` | The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node). |
| `sbm_move_delta_dc_b1` | graph-tool | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `graph-tool entropy of the partition after the move minus before` | The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node). |
| `sbm_move_delta_dc_b3` | graph-tool | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `graph-tool entropy of the partition after the move minus before` | The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node). |

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
