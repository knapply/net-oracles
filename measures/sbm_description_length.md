---
title: "Sbm description length"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Sbm description length

Family: Statistical fitting. Identifier: `sbm_description_length`.

## Definition

Sbm description length.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [graph-tool](../tools/graphtool.html) | ✓ checked, agrees | `BlockState` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `sbm_dl_b1` | graph-tool | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 |  | The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node). |
| `sbm_dl_b2` | graph-tool | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 |  | The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node). |
| `sbm_dl_b3` | graph-tool | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 |  | The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node). |
| `sbm_dl_b5` | graph-tool | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 |  | The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node). |
| `sbm_dl_dc_b1` | graph-tool | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 |  | The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node). |
| `sbm_dl_dc_b2` | graph-tool | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 |  | The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node). |
| `sbm_dl_dc_b3` | graph-tool | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 |  | The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node). |
| `sbm_dl_dc_b5` | graph-tool | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 |  | The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node). |

Tools cited: [peixoto2014graphtool](../references.html#peixoto2014graphtool)
{% endraw %}
