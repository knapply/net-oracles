---
title: "Bonacich power centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Bonacich power centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Spectral and walk-based. Concept id: `bonacich_power`. 1 measure.

## Definition {#concept-definition}

Bonacich power centrality of every node for a given attenuation exponent.

## References {#concept-references}

[bonacich1987power](../../references.html#bonacich1987power), [bonacich2001eigenvector](../../references.html#bonacich2001eigenvector), [brin1998anatomy](../../references.html#brin1998anatomy), [collatz1942einschliessungssatz](../../references.html#collatz1942einschliessungssatz), [katz1953new](../../references.html#katz1953new), [kleinberg1999authoritative](../../references.html#kleinberg1999authoritative), [langville2004deeper](../../references.html#langville2004deeper)

## Bonacich {#bonacich}

Measure id: `bonacich`. Original family: Centrality.

**Definition.** Bonacich power centrality of every node for a given attenuation exponent.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | ✓ checked, agrees | `bonpow; power_centrality` |  |
| [sna](../../tools/sna.html) | ✓ checked, agrees | `bonpow` |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `Bonacich power / beta centrality; betacent; bonamat` | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `bonacich` | igraph (R) | any | no-value-on-some-inputs |  | normalization, ties | abs 1e-10, rel 1e-09 | `igraph::power_centrality(g, exponent = beta)` | Without ties A 1 = 0 and the scaling constant is 0 / 0. |
| `bonacich_negative` | igraph (R) | any | no-value-on-some-inputs |  | normalization, ties | abs 1e-10, rel 1e-09 | `igraph::power_centrality(g, exponent = beta)` | Without ties A 1 = 0 and the scaling constant is 0 / 0. |
| `bonacich_rescale` | igraph (R) | any | no-value-on-some-inputs |  | ties | abs 1e-10, rel 1e-09 | `igraph::power_centrality(g, exponent = beta, rescale = TRUE)` | Without ties the scores sum to 0. |
| `bonacich_sna` | sna | any | no-value-on-some-inputs |  | defaults, normalization, ties | abs 1e-12, rel 5e-12 | `sna::bonpow(m, gmode, exponent = 1)` | 1 is an eigenvalue of A, so I - A is singular and the scores are undefined; without ties the scaling constant is 0 / 0. |
| `bonacich_unit` | igraph (R) | any | no-value-on-some-inputs |  | defaults, normalization, ties | abs 1e-14, rel 2e-12 | `igraph::power_centrality(g, exponent = 1)` | 1 is an eigenvalue of A, so I - A is singular and the scores are undefined; without ties the scaling constant is 0 / 0. |

**References:** [bonacich1987power](../../references.html#bonacich1987power), [bonacich2001eigenvector](../../references.html#bonacich2001eigenvector), [brin1998anatomy](../../references.html#brin1998anatomy), [collatz1942einschliessungssatz](../../references.html#collatz1942einschliessungssatz), [katz1953new](../../references.html#katz1953new), [kleinberg1999authoritative](../../references.html#kleinberg1999authoritative), [langville2004deeper](../../references.html#langville2004deeper)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
