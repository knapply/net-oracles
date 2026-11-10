---
title: "VoteRank"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# VoteRank {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `voterank`. 1 measure.

## Definition {#concept-definition}

VoteRank: up to a given number of influential spreaders, chosen one at a time by voting, in the order chosen.

## References {#concept-references}

[qi2012laplacian](../../references.html#qi2012laplacian), [zhang2016identifying](../../references.html#zhang2016identifying)

## Voterank {#cx_voterank}

Measure id: `cx_voterank`. Original family: Centrality.

**Definition.** VoteRank: up to a given number of influential spreaders, chosen one at a time by voting, in the order chosen.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `voterank` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_voterank` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.voterank(G)` |  |

**References:** [qi2012laplacian](../../references.html#qi2012laplacian), [zhang2016identifying](../../references.html#zhang2016identifying)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
