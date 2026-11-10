---
title: "E-I index"
layout: default
parent: "Mixing and assortativity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# E-I index {#concept-top}

Family: [Mixing and assortativity](index.html). Subfamily: Segregation and homophily indices. Concept id: `ei_index`. 1 measure.

## Definition {#concept-definition}

E-I index. Entries grouped here: Ei index.

## Ei index {#ei_index}

Measure id: `ei_index`. Original family: Mixing and assortativity.

**Definition.** Ei index.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-ei_index-ucinet) | `E-I index; EI` | published documentation |
| [egor](../../tools/egor.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction, multi-edges, self-loops and ties): egor's comp\_ei() counts alters, each neighbour once whatever the number or direction of the ties to it, and no self-loop. [details](#why-ei_index-egor) |  |  |
| [netseg](../../tools/netseg.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: netseg is documented-only in this survey; listed in its documentation. [details](#why-ei_index-netseg) | `ei` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-ei_index-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.
- <a id="why-ei_index-egor"></a>**[egor](../../tools/egor.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> egor 1.25.10 was run and its value differs from the reference value by convention (defaults, direction, multi-edges, self-loops and ties) on inputs tagged directed, isolates, loops and multi\_edges. egor's comp\_ei() counts alters, each neighbour once whatever the number or direction of the ties to it, and no self-loop; the reference value's node E-I index counts ties (each edge, in either direction, separately, a self-loop as an internal tie), and an ego without alters has no value in egor where the reference reports undefined (-1). Undirected fixtures without parallel edges or loops agree. Relation to the reference value: Tie vs alter counting: comp\_ei counts each neighbour once whatever the number or direction of ties; the reference counts ties. Mapping: the reference value computed with the binary undirected reading (as the adjacency-matrix reading, and a directed network symmetrized): each alter counted once whatever the number or direction of ties agrees with the tool within abs 1e-15, rel 1e-14 on all 6 comparisons where the difference occurs. Tolerance before mapping: abs 1e-15, rel 1e-14 (0 means exact equality). 6 comparisons differ and 22 agree. Finding F073 (convention): comp\_ei counts each neighbour once. Findings: [F073](../../findings.html#f073).
- <a id="why-ei_index-netseg"></a>**[netseg](../../tools/netseg.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. netseg (1.0-3) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of netseg 1.0-3: help topics.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ei_index_node` | egor | any | differs | directed, isolates, loops, multi\_edges | defaults, direction, multi\_edges, self\_loops, ties | abs 1e-15, rel 1e-14 | `egor::comp_ei(egor object, alt.attr = 'group', ego.attr = 'group')` | egor's comp\_ei() counts alters, each neighbour once whatever the number or direction of the ties to it, and no self-loop; the reference value's node E-I index counts ties (each edge, in either direction, separately, a self-loop as an internal tie), and an ego without alters has no value in egor where the reference reports undefined (-1). Undirected fixtures without parallel edges or loops agree. |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F073](../../findings.html#f073) | egor | convention | comp\_ei counts each neighbour once |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [tool_egor](../../references.html#tool_egor), [tool_netseg](../../references.html#tool_netseg)
{% endraw %}
