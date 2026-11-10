---
title: "Chordless cycles"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Chordless cycles

Family: Graph theory and combinatorics. Identifier: `chordless_cycles`.

## Definition

Every chordless (induced) cycle.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `chordless_cycles` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cyc_chordless` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.chordless_cycles(M)` |  |
| `cyc_chordless_bound5` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.chordless_cycles(M, length_bound = 5)` |  |

## References

[depina1995applications](../references.html#depina1995applications), [dias2013efficient](../references.html#dias2013efficient), [gupta2021finding](../references.html#gupta2021finding), [hagberg2008exploring](../references.html#hagberg2008exploring), [itai1978finding](../references.html#itai1978finding), [johnson1975finding](../references.html#johnson1975finding), [kavitha2009cycle](../references.html#kavitha2009cycle), [kirchhoff1847ueber](../references.html#kirchhoff1847ueber)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
