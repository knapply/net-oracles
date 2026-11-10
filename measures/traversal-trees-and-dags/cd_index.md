---
title: "CD index"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# CD index {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `cd_index`. 1 measure.

## Definition {#concept-definition}

CD index. Entries grouped here: CD index.

## CD index {#nxs_cd_index}

Measure id: `nxs_cd_index`. Original family: Graph theory and combinatorics.

**Definition.** CD index.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention | `cd_index` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_cd_index_delta0` | NetworkX | directed | differs | directed | defaults, direction | abs 0.0050001, rel 0 | `nx.cd_index(G, v, time_delta = 0, time = 'time')` | NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n every citer of a reference whatever its time; Funk and Owen-Smith (and the reference value's default) count only the papers published after the focal paper and at most delta after it. NetworkX 1, reference undefined, since the only citer predates the focal paper). The tolerance is NetworkX's rounding of the index to two decimals. |
| `nxs_cd_index_delta1` | NetworkX | directed | differs | directed | defaults, direction | abs 0.0050001, rel 0 | `nx.cd_index(G, v, time_delta = 1, time = 'time'), -999 if it raises` | NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n every citer of a reference whatever its time; Funk and Owen-Smith (and the reference value's default) count only the papers published after the focal paper and at most delta after it. NetworkX 1, reference undefined, since the only citer predates the focal paper). The tolerance is NetworkX's rounding of the index to two decimals. |
| `nxs_cd_index_delta3_weighted` | NetworkX | directed | differs | directed | defaults, direction | abs 0.0050001, rel 0 | `nx.cd_index(G, v, time_delta = 3, time = 'time', weight = 'w')` | NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n every citer of a reference whatever its time; Funk and Owen-Smith (and the reference value's default) count only the papers published after the focal paper and at most delta after it. NetworkX 1, reference undefined, since the only citer predates the focal paper). The tolerance is NetworkX's rounding of the index to two decimals. |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F032](../../findings.html#f032) | NetworkX | convention | cd\_index pools every citer of the references, whatever its time |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
