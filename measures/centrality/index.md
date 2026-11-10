---
title: "Centrality"
layout: default
parent: Measures
has_children: true
nav_order: 1
permalink: /measures/centrality/
---

{% raw %}
# Centrality

142 measures in 76 concepts and 11 subfamilies. Each concept page has a section per measure (variant); the anchor of a section is the measure id (characters other than letters, digits, underscore, dot and hyphen become hyphens).

## Betweenness, load and flow

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Betweenness](betweenness.html) | 5 | 17 | Shortest-path betweenness of every node (Brandes 2001). |
| [Communicability betweenness](communicability_betweenness.html) | 1 | 2 | Communicability betweenness of every node: the loss of communicability when the node's edges are removed (Estrada, Higham and Hatano 2009). |
| [Current-flow betweenness](current_flow_betweenness.html) | 3 | 2 | Current-flow betweenness approximated from sampled pairs of nodes (random pairs or given ones). |
| [Edge betweenness](edge_betweenness.html) | 1 | 8 | Shortest-path betweenness of every edge (Brandes 2001 accumulation, as used by Girvan and Newman). |
| [Edge load centrality](edge_load_centrality.html) | 1 | 1 | Load on every edge: NetworkX's edge load centrality, over ordered pairs of adjacent nodes. |
| [Flow betweenness](flow_betweenness.html) | 1 | 2 | Flow betweenness of every node: the share of maximum flow between other pairs that cannot avoid it. The ucinet convention uses the normalized scale;... |
| [Group betweenness centrality](group_betweenness.html) | 1 | 2 | Group degree, closeness or betweenness of a set of nodes (Everett and Borgatti). |
| [K-path centrality](k_path_centrality.html) | 2 | 2 | K-path centrality. Entries grouped here: Geokpath; KPath Centrality. |
| [Load centrality](load_centrality.html) | 2 | 3 | Load centrality of every node: flow split equally among predecessors (Goh, Kahng and Kim 2001). |
| [Percolation centrality](percolation_centrality.html) | 1 | 2 | Percolation centrality of every node for given percolation states (Piraveenan, Prokopenko and Hossain 2013). |
| [Stress centrality](stress_centrality.html) | 2 | 2 | Stress centrality. Entries grouped here: Stresscent; Subgraph centrality and stress centrality. |

## Centralization and tables

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Centrality table (raw and normalized)](centrality_table.html) | 1 | 1 | Centrality table (raw and normalized). Entries grouped here: Net\_centrality\_table() (raw and normalised columns). |
| [Centralization](centralization.html) | 6 | 3 | Freeman centralization of degree, betweenness, closeness or eigenvector centrality. |

## Degree and strength

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Alpha-tuned degree and closeness](weighted_degree_alpha.html) | 1 | 1 | Alpha-tuned degree and closeness. Entries grouped here: Opsahl alpha-tuned degree and closeness. |
| [Degree](degree.html) | 3 | 12 | Degree of every node: edge endpoints by direction, loops counted twice. |
| [Group degree centrality](group_degree.html) | 2 | 3 | Group degree, closeness or betweenness of a set of nodes (Everett and Borgatti). |
| [Strength (weighted degree)](strength.html) | 1 | 7 | Strength (weighted degree). Entries grouped here: Strength. |

## Distance-based

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Average distance centrality](average_distance_centrality.html) | 2 | 1 | Average distance centrality. Entries grouped here: Averagedis; Pairwisedis. |
| [Bottleneck centrality](bottleneck_centrality.html) | 1 | 1 | Bottleneck centrality. Entries grouped here: Bottleneck. |
| [Centroid centrality](centroid_centrality.html) | 1 | 1 | Centroid centrality. Entries grouped here: Centroid. |
| [Closeness](closeness.html) | 8 | 15 | Closeness of every node: the inverse of its mean distance to the nodes it reaches, with the unreachable-node rule of the chosen tool. |
| [Decay centrality](decay_centrality.html) | 1 | 1 | Decay centrality. Entries grouped here: Decay. |
| [Graph centrality (inverse eccentricity)](graph_centrality.html) | 1 | 1 | Graph centrality (inverse eccentricity). Entries grouped here: Graphcent. |
| [Group closeness centrality](group_closeness.html) | 1 | 3 | Group degree, closeness or betweenness of a set of nodes (Everett and Borgatti). |
| [Harmonic centrality](harmonic_centrality.html) | 1 | 10 | Harmonic centrality of every node: the sum of 1/d over the other nodes (0 for an unreachable one). |
| [Radiality and integration](radiality.html) | 2 | 2 | Radiality and integration. Entries grouped here: Radiality; Valente-Foreman integration and radiality. |
| [Reach and m-reach](reach_centrality.html) | 3 | 6 | Number (or share) of other nodes within distance k of every node. |

## Group centrality

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Prominent group](group_prominence.html) | 1 | 1 | Prominent group. Entries grouped here: Prominent group. |

## Key players

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Key player set (KPP)](key_player_set.html) | 5 | 2 | The set of k key players that best satisfies a key player criterion (Borgatti's greedy swap search or exact enumeration), with its score. |
| [Key player single-node scores (KPP)](key_player_single.html) | 4 | 2 | Key player criterion (fragmentation, distance-weighted fragmentation, m-reach or distance-weighted reach) of a given set of nodes. |

## Local and structural scores

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Alpha centrality](alpha_centrality.html) | 1 | 1 | Alpha centrality. Entries grouped here: Alpha. |
| [Bridging centrality](bridging_centrality.html) | 1 | 1 | Bridging centrality. Entries grouped here: Bridging centrality. |
| [Bridging coefficient](bridging_coefficient.html) | 1 | 1 | Bridging coefficient. Entries grouped here: Bridging coefficient. |
| [Community-based centrality](community_centrality.html) | 1 | 1 | Community-based centrality. Entries grouped here: Communitycent. |
| [Concentration](concentration.html) | 1 | 1 | Concentration. Entries grouped here: Concent. |
| [Cross-clique centrality](cross_clique_centrality.html) | 1 | 1 | Cross-clique centrality. Entries grouped here: Crossclique. |
| [Diffusion centrality and diffusion degree](diffusion_centrality.html) | 3 | 4 | Diffusion centrality and diffusion degree. Entries grouped here: Diffusion; Diffusion degree; Diffusion efficiency. |
| [Dispersion](dispersion.html) | 1 | 1 | Dispersion of the tie between each given pair of nodes (Backstrom and Kleinberg), one value per pair. |
| [Edge percolated component](epc.html) | 1 | 1 | Edge percolated component. Entries grouped here: Epc. |
| [Entropy centrality](entropy_centrality.html) | 1 | 1 | Entropy centrality. Entries grouped here: Entropy. |
| [Gil-Schmidt power index](gil_schmidt_power.html) | 1 | 1 | Gil-Schmidt power index. Entries grouped here: Gilschmidt. |
| [Induced centrality](induced_centrality.html) | 1 | 1 | Induced centrality. Entries grouped here: Induced centrality. |
| [Laplacian centrality](laplacian_centrality.html) | 1 | 2 | Laplacian centrality. Entries grouped here: Cx laplacian. |
| [Leverage centrality](leverage_centrality.html) | 1 | 1 | Leverage centrality. Entries grouped here: Leverage. |
| [Lin centrality](lin_centrality.html) | 1 | 1 | Lin centrality. Entries grouped here: Lincent. |
| [Lobby index](lobby_index.html) | 1 | 1 | Lobby index. Entries grouped here: Lobby. |
| [Local reaching centrality](local_reaching_centrality.html) | 1 | 1 | Global reaching centrality of a network (Mones et al.): the mean gap between the largest local reaching centrality and every node's, divided by n - 1. |
| [MNC and DMNC](mnc_dmnc.html) | 2 | 1 | MNC and DMNC. Entries grouped here: Dmnc; Mnc. |
| [Permanence](permanence.html) | 1 | 1 | Permanence. Entries grouped here: Permanence Centrality. |
| [Prestige](prestige.html) | 1 | 1 | Prestige. Entries grouped here: Prestige. |
| [Second-order centrality](second_order_centrality.html) | 1 | 1 | Second-order centrality of every node: the standard deviation of its return times in a random walk (Kermarrec et al. 2011). |
| [Semi-local centrality](semilocal_centrality.html) | 1 | 1 | Semi-local centrality. Entries grouped here: Semilocal. |
| [Topological coefficient](topological_coefficient.html) | 1 | 1 | Topological coefficient. Entries grouped here: Topocoefficient. |
| [Trophic levels and incoherence](trophic_levels.html) | 1 | 1 | Trophic incoherence parameter of a directed network: the standard deviation of the trophic differences (Johnson et al.). |
| [VoteRank](voterank.html) | 1 | 1 | VoteRank: up to a given number of influential spreaders, chosen one at a time by voting, in the order chosen. |

## Partial rankings (netrankr)

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Hyperbolic index](hyperbolic_index.html) | 1 | 1 | Hyperbolic index. Entries grouped here: Hyperbolic index. |
| [Neighborhood inclusion](neighborhood_inclusion.html) | 2 | 1 | Neighborhood inclusion. Entries grouped here: Neighborhood inclusion; Neighborhood inclusion, positional dominance, rank intervals. |
| [Positional dominance](positional_dominance.html) | 1 | 1 | Positional dominance. Entries grouped here: Positional dominance. |
| [Rank comparison and ordering](rank_comparison.html) | 7 | 1 | Rank comparison and ordering. Entries grouped here: Comparable pairs; Compare ranks; Get rankings; Incomparable pairs; Index builder; Is preserved; and 1 more. |
| [Rank intervals](rank_intervals.html) | 1 | 1 | Rank intervals. Entries grouped here: Rank intervals. |
| [Rank probabilities and expected ranks](rank_probabilities.html) | 4 | 1 | Rank probabilities and expected ranks. Entries grouped here: Approx rank expected; Approx rank relative; Exact rank prob; Mcmc rank prob. |

## Resistance and information

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Information centrality (current-flow closeness)](information_centrality.html) | 2 | 5 | Stephenson and Zelen's information centrality of every node. |

## Spectral and walk-based

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Bonacich power centrality](bonacich_power.html) | 1 | 3 | Bonacich power centrality of every node for a given attenuation exponent. |
| [ClusterRank](clusterrank.html) | 1 | 1 | ClusterRank. Entries grouped here: Clusterrank. |
| [Communicability](communicability.html) | 1 | 4 | Communicability of every pair of nodes: the matrix exponential of the adjacency matrix, per component (Estrada and Hatano 2008). |
| [EigenTrust](eigentrust.html) | 1 | 1 | EigenTrust. Entries grouped here: Eigentrust. |
| [Eigenvector centrality](eigenvector_centrality.html) | 3 | 12 | Eigenvector centrality of every node, with the principal eigenvalue and a connectedness flag. |
| [HITS hubs and authorities](hits.html) | 2 | 9 | Hub and authority scores of every node (Kleinberg 1999), with the leading singular value. |
| [Hubbell centrality](hubbell_centrality.html) | 1 | 1 | Hubbell centrality. Entries grouped here: Hubbell. |
| [Katz centrality](katz_centrality.html) | 2 | 10 | Katz centrality of every node by fixed-point iteration (Katz 1953). |
| [LeaderRank](leaderrank.html) | 1 | 1 | LeaderRank. Entries grouped here: Leaderrank. |
| [Markov centrality](markov_centrality.html) | 1 | 1 | Markov centrality. Entries grouped here: Markovcent. |
| [PageRank](pagerank.html) | 5 | 13 | PageRank of every node by power iteration (Brin and Page 1998), with a GAP-suite preset. |
| [SALSA](salsa.html) | 1 | 1 | SALSA. Entries grouped here: Salsa. |

## Walk-based and distance-based indices (netrankr)

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Distance transformations for indices](distance_transform_indices.html) | 5 | 1 | Distance transformations for indices. Entries grouped here: Dist 2pow; Dist dpow; Dist inv; Dist powd; Swan combinatory. |
| [Walk-based index components](walk_indices.html) | 6 | 1 | Walk-based index components. Entries grouped here: Walks attenuated; Walks exp; Walks exp even; Walks exp odd; Walks limit prop; Walks uptok. |
{% endraw %}
