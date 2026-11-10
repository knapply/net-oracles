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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults and direction): NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n... [details](#why-nxs_cd_index-networkx) | `cd_index` |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-nxs_cd_index-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (defaults and direction) on inputs tagged directed. NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n every citer of a reference whatever its time; Funk and Owen-Smith (and the reference value's default) count only the papers published after the focal paper and at most delta after it. Reproduced by the reference value computed with NetworkX's citation window, which matches NetworkX on every fixture. Publication times are a fixed function of the node id (derived/nx\_shims.py), so any arc can bring in a citer outside the window: declared for every directed network (a two-node network with the arc 0 -&gt; 1 already differs: NetworkX 1, reference undefined, since the only citer predates the focal paper). The tolerance is NetworkX's rounding of the index to two decimals. Mapping: the reference value computed with the tool's convention (citers up to the end of the window, earlier ones included; every citer of a reference in the pool) agrees with the tool within abs 0.0050001, rel 0 on all 24 comparisons where the difference occurs. Tolerance before mapping: abs 0.0050001, rel 0 (0 means exact equality). 24 comparisons differ and 3 agree. Finding F032 (convention): cd\_index pools every citer of the references, whatever its time. Findings: [F032](../../findings.html#f032).

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
