"""NetworkX measure calls, shared by the NetworkX adapters (plain and backends)."""
import os

from common import Adapter, sig, vec


class NetworkXBase(Adapter):
    package = ""  # distribution name of the backend
    backend = None  # nx backend name, or None for the pure Python implementation

    def __init__(self):
        os.environ.pop("NETWORKX_AUTOMATIC_BACKENDS", None)
        import networkx as nx
        self.nx = nx
        kw = {"backend": self.backend} if self.backend else {}
        self.calls = {
            "bfs": lambda G, c: {"reached": len(nx.single_source_shortest_path_length(G, c.sources[0]))},
            "components": lambda G, c: {"components": (nx.number_weakly_connected_components(G, **kw) if c.directed
                                                      else nx.number_connected_components(G, **kw))},
            "pagerank": lambda G, c: vec(nx.pagerank(G, alpha=0.85, tol=1e-6, max_iter=100, **kw).values()),
            "triangles": lambda G, c: {"triangles": sum(nx.triangles(G.to_undirected(as_view=True) if c.directed else G, **kw).values()) // 3},
            "betweenness": lambda G, c: ({"sum": sig(sum(nx.betweenness_centrality_subset(G, c.sources, list(G)).values()))}
                                         if not self.backend else
                                         {"sum_sampled": sig(sum(nx.betweenness_centrality(G, k=len(c.sources), seed=1, **kw).values()))}),
            "closeness": lambda G, c: vec(nx.closeness_centrality(G, **kw).values()),
        }

    def version(self):
        if not self.backend:
            return self.nx.__version__
        from importlib.metadata import version
        return version(self.package)  # the backend package; NetworkX itself is in the digest-free note

    def load(self, ctx):
        G = self.nx.DiGraph() if ctx.directed else self.nx.Graph()
        G.add_nodes_from(range(ctx.n))
        G.add_edges_from(map(tuple, ctx.edges.tolist()))
        return G
