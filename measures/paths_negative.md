---
title: "Paths negative"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Paths negative

Family: Paths and distances. Identifier: `paths_negative`.

## Definition

Paths negative.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `goldberg_radzik` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_bellman_ford_potential` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.single_source_bellman_ford_path_length(G, 0, weight = 'len')` |  |
| `paths_bellman_ford_shift` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.single_source_bellman_ford_path_length(G, 0, weight = 'len'); NetworkXUnbounded is a negative cycle` |  |
| `paths_goldberg_radzik_potential` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.goldberg_radzik(G, 0, weight = 'len')[1]` |  |
| `paths_goldberg_radzik_shift` | NetworkX | any | differs | loops | defaults, self\_loops | abs 1e-12, rel 1e-12 | `nx.goldberg_radzik(G, 0, weight = 'len')[1]; NetworkXUnbounded is a negative cycle` | NetworkX raises NetworkXUnbounded for any negative self-loop, reachable from the source or not (checked with nx.goldberg\_radzik and bellman\_ford\_predecessor\_and\_distance); the reference and the definition oracle report the unreachable node and no negative cycle. |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
