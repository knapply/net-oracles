"""Deterministic inputs for the NetworkX-order routines of
validation/manifest.d/nx_shims.yaml.

The engine runners (validation/bindings/nx_shims.py) and both oracles
(nx_shims_definition_oracle.py, nx_shims_networkx_oracle.py) derive their
inputs from a fixture with these rules, so all three see the same graphs:

- adjacency order is NetworkX's for a graph built by adding nodes 0..n - 1
  and then the fixture's edges in file order (`rows`);
- the tree of a fixture is the breadth-first tree from node 0 over the
  undirected reading in that order, its nodes renumbered by discovery
  (`bfs_tree`); the nodes of other components are left out;
- the simple digraph of a fixture has its distinct non-loop arcs sorted by
  (source, target), each with the largest weight among its parallel arcs
  (`simple_arcs`), which is the order NetworkX lists the edges of a DiGraph
  whose edges are added in that order;
- the Eulerian multigraph doubles every edge (undirected) or adds the
  reverse of every arc (directed), so every degree is even (balanced);
- the node sequences tested for simple paths and the Pruefer sequence are
  fixed formulas of n (`path_sequences`, `prufer_sequence`).
"""

from __future__ import annotations

from collections import deque
from types import SimpleNamespace


def make(n, src, tgt, directed, weights=None, name="derived"):
    return SimpleNamespace(n=n, src=list(src), tgt=list(tgt), directed=directed,
                           weights=list(weights) if weights is not None else None,
                           weighted=weights is not None, tags=[], name=name)


def rows(fx, direction=1):
    """Neighbour lists in NetworkX's order (direction 1: successors or
    neighbours; 2: predecessors)."""
    out = [dict() for _ in range(fx.n)]
    for a, b in zip(fx.src, fx.tgt):
        if fx.directed:
            if direction == 1:
                out[a].setdefault(b, None)
            else:
                out[b].setdefault(a, None)
        else:
            out[a].setdefault(b, None)
            out[b].setdefault(a, None)
    return [list(r) for r in out]


def bfs_tree(fx):
    """(k, edges): the breadth-first tree of the component of node 0 over the
    undirected reading, as (parent, child) pairs in discovery order with
    nodes renumbered 0..k-1 by discovery."""
    und = make(fx.n, fx.src, fx.tgt, False)
    adj = rows(und)
    label = {0: 0}
    edges = []
    queue = deque([0])
    while queue:
        v = queue.popleft()
        for w in adj[v]:
            if w not in label:
                label[w] = len(label)
                edges.append((label[v], label[w]))
                queue.append(w)
    return len(label), edges


def tree_fixture(fx, directed=False):
    k, edges = bfs_tree(fx)
    return make(k, [a for a, _ in edges], [b for _, b in edges], directed,
                name=fx.name + "_tree")


def simple_arcs(fx):
    """Distinct non-loop arcs (source, target, weight) sorted by (source, target);
    undirected edges become one arc per direction."""
    best = {}
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        if a == b:
            continue
        w = fx.weights[i] if fx.weighted else 1.0
        for key in ([(a, b)] if fx.directed else [(a, b), (b, a)]):
            best[key] = max(best.get(key, w), w)
    return [(a, b, best[(a, b)]) for a, b in sorted(best)]


def simple_digraph(fx):
    arcs = simple_arcs(fx)
    return make(fx.n, [a for a, _, _ in arcs], [b for _, b, _ in arcs], True,
                [w for _, _, w in arcs], name=fx.name + "_simple")


def eulerian(fx):
    """Every edge twice (undirected) or with its reverse (directed)."""
    src, tgt = [], []
    for a, b in zip(fx.src, fx.tgt):
        if fx.directed:
            src += [a, b]
            tgt += [b, a]
        else:
            src += [a, a]
            tgt += [b, b]
    return make(fx.n, src, tgt, fx.directed, name=fx.name + "_euler")


def prufer_sequence(k):
    return [(7 * i + 3) % k for i in range(max(k - 2, 0))]


def bfs_path(fx):
    """A shortest path (in NetworkX's search order) from node 0 to the
    farthest node reached, over out-neighbours."""
    adj = rows(fx)
    parent = {0: None}
    order = [0]
    queue = deque([0])
    while queue:
        v = queue.popleft()
        for w in adj[v]:
            if w not in parent:
                parent[w] = v
                order.append(w)
                queue.append(w)
    path = []
    v = order[-1]
    while v is not None:
        path.append(v)
        v = parent[v]
    return path[::-1]


def path_sequences(fx):
    """Node sequences whose simple-path status is tested, in a fixed order."""
    p = bfs_path(fx)
    n = fx.n
    return [p, p[::-1], p + [p[0]], [0, n - 1], [0], [], [0, 0], p[:1] + p[2:],
            [n - 1], p[:2], list(range(min(n, 3)))]


def simple_graph(fx, loops=False):
    """The distinct edges (or arcs) of a fixture in file order, as NetworkX's
    Graph or DiGraph keeps them; self-loops only with `loops`."""
    seen = set()
    src, tgt = [], []
    for a, b in zip(fx.src, fx.tgt):
        if a == b and not loops:
            continue
        key = (a, b) if fx.directed else (min(a, b), max(a, b))
        if key in seen:
            continue
        seen.add(key)
        src.append(a)
        tgt.append(b)
    return make(fx.n, src, tgt, fx.directed, name=fx.name + "_simple")


def dag(fx):
    """The arcs a -> b with a < b of the fixture, distinct, in file order."""
    seen = set()
    src, tgt = [], []
    for a, b in zip(fx.src, fx.tgt):
        lo, hi = min(a, b), max(a, b)
        if lo == hi or (lo, hi) in seen:
            continue
        seen.add((lo, hi))
        src.append(lo)
        tgt.append(hi)
    return make(fx.n, src, tgt, True, name=fx.name + "_dag")


def dag_lengths(d):
    """Arc lengths of a derived DAG with some negative values (a DAG has no
    negative cycle): 1.5 - ((a + 2 b) mod 4)."""
    return [1.5 - ((a + 2 * b) % 4) for a, b in zip(d.src, d.tgt)]


def node_times(n):
    """Publication times of the nodes of a citation network."""
    return [float((7 * v) % 11) for v in range(n)]


def node_weights(n):
    return [float(1 + (3 * v) % 5) for v in range(n)]


def degree_sequences(fx):
    """(sequence name, undirected degree list) pairs and directed (in, out)
    pairs derived from the fixture's simple graph."""
    s = simple_graph(fx)
    deg = [0] * fx.n
    indeg, outdeg = [0] * fx.n, [0] * fx.n
    for a, b in zip(s.src, s.tgt):
        outdeg[a] += 1
        indeg[b] += 1
        deg[a] += 1
        deg[b] += 1
    return deg, indeg, outdeg


def small(fx, limit=12):
    """Cycle and path enumerations run on fixtures of at most `limit` nodes:
    larger ones have too many (exponentially many in dense networks)."""
    return fx.n <= limit


def weighted_dag(fx):
    """The derived DAG with the negative arc lengths of `dag_lengths`."""
    d = dag(fx)
    d.weights = dag_lengths(d)
    d.weighted = True
    return d


def fw_graph(fx, negative):
    """The digraph of Floyd-Warshall tests: the simple digraph with the
    fixture's weights (every distinct arc), or the DAG with negative lengths."""
    return weighted_dag(fx) if negative else simple_digraph(fx)


def sort_graph(fx, limit=12):
    """The DAG whose topological orders are enumerated (at most `limit`
    nodes; None otherwise)."""
    return dag(fx) if fx.n <= limit else None


def sequence_cases(fx):
    """Undirected degree sequences tested for being graphical (the first is
    the degree sequence of the simple graph, so graphical) and (in, out)
    pairs for being digraphical (the first from the simple digraph)."""
    deg, _, _ = degree_sequences(fx)
    n = fx.n
    und = [deg,
           [deg[0] + 1] + deg[1:] if n else [],
           [n] + deg[1:] if n else [],
           sorted(deg),
           [0] * n,
           [n - 1] * n,
           [n + 2, 2] + [0] * max(n - 2, 0) if n >= 2 else [3]]
    sd = simple_graph(make(fx.n, fx.src, fx.tgt, True))
    indeg, outdeg = [0] * n, [0] * n
    for a, b in zip(sd.src, sd.tgt):
        outdeg[a] += 1
        indeg[b] += 1
    dirs = [(indeg, outdeg),
            (outdeg, indeg),
            ([indeg[0] + 1] + indeg[1:], outdeg) if n else ([], []),
            ([n] + indeg[1:], [n] + outdeg[1:]) if n else ([], []),
            ([0] * n, [0] * n),
            ([1] * n, [1] * n),
            ([n - 1] * n, [n - 1] * n)]
    return und, dirs
