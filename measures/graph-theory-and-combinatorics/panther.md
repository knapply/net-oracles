---
title: "Panther"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Panther {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Similarity and link prediction. Concept id: `panther`. 1 measure.

## Definition {#concept-definition}

The k nodes most similar to a source by Panther: how often random paths contain both (Zhang et al. 2015).

## References {#concept-references}

[hagberg2008exploring](../../references.html#hagberg2008exploring), [jeh2002simrank](../../references.html#jeh2002simrank), [zhang2015panther](../../references.html#zhang2015panther)

## Panther {#panther}

Measure id: `panther`. Original family: Graph theory and combinatorics.

**Definition.** The k nodes most similar to a source by Panther: how often random paths contain both (Zhang et al. 2015).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `panther_similarity; panther_vector_similarity` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `panther` | NetworkX | undirected | no-value-on-some-inputs |  |  | abs 0.015, rel 0 | `nx.panther_similarity(G, hub, k = (non-isolated nodes) - 1, eps = 0.01, seed = 1)` | as for the definition oracle |

**References:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [jeh2002simrank](../../references.html#jeh2002simrank), [zhang2015panther](../../references.html#zhang2015panther)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
