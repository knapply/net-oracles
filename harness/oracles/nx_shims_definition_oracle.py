# oracle-entries: definition
"""Golden values for the routines of manifest/nx_shims.yaml from their
definitions (encodings in bindings/nx_shims.py, derived inputs in
derived/nx_shims.py): union-find and brute force on the derived graphs,
sharing no code with the engine.

    python3 oracles/nx_shims_definition_oracle.py
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)
from derived import nx_shims as D  # noqa: E402

ORACLE = "definition"


class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        self.p[a] = b
        return True


def components(fx):
    uf = UnionFind(fx.n)
    acyclic = True
    for a, b in zip(fx.src, fx.tgt):
        if not uf.union(a, b):
            acyclic = False  # a loop or a second path joins the pair
    return len({uf.find(v) for v in range(fx.n)}), acyclic


def max_in_degree(fx):
    if not fx.directed:
        return 0
    indeg = [0] * fx.n
    for b in fx.tgt:
        indeg[b] += 1
    return max(indeg, default=0)


def forest_counts(fx):
    comps, _ = components(fx)
    return [fx.n, len(fx.src), comps, max_in_degree(fx)]


def forest_flags(fx):
    comps, acyclic = components(fx)
    tree = acyclic and comps == 1
    if not fx.directed:
        return [int(tree), int(acyclic), -1, -1]
    one_parent = max_in_degree(fx) <= 1
    return [int(tree), int(acyclic), int(tree and one_parent), int(acyclic and one_parent)]


def adjacency(t):
    adj = [set() for _ in range(t.n)]
    for a, b in zip(t.src, t.tgt):
        adj[a].add(b)
        adj[b].add(a)
    return adj


def tree_centroid(fx):
    t = D.tree_fixture(fx)
    adj = adjacency(t)
    best, nodes = None, []
    for v in range(t.n):
        seen, worst = {v}, 0
        for w in adj[v]:
            if w in seen:
                continue
            size, stack = 0, [w]
            seen.add(w)
            while stack:
                x = stack.pop()
                size += 1
                for y in adj[x]:
                    if y not in seen:
                        seen.add(y)
                        stack.append(y)
            worst = max(worst, size)
        if best is None or worst < best:
            best, nodes = worst, [v]
        elif worst == best:
            nodes.append(v)
    return sorted(nodes)


def prufer(fx):
    t = D.tree_fixture(fx)
    if t.n < 3:
        return []
    adj = adjacency(t)
    seq = []
    for _ in range(t.n - 2):
        leaf = min(v for v in range(t.n) if len(adj[v]) == 1)
        (parent,) = adj[leaf]
        seq.append(parent)
        adj[parent].discard(leaf)
        adj[leaf].clear()
    return seq


def from_prufer(fx):
    k, _ = D.bfs_tree(fx)
    if k < 3:
        return []
    seq = D.prufer_sequence(k)
    degree = [1] * k
    for v in seq:
        degree[v] += 1
    edges = []
    for v in seq:
        leaf = min(u for u in range(k) if degree[u] == 1)
        edges.append((min(leaf, v), max(leaf, v)))
        degree[leaf] -= 1
        degree[v] -= 1
    last = [u for u in range(k) if degree[u] == 1]
    edges.append((last[0], last[1]))
    return sorted(edges)


def tree_lca(fx):
    t = D.tree_fixture(fx, directed=True)
    parent = {b: a for a, b in zip(t.src, t.tgt)}

    def ancestors(v):
        out = [v]
        while out[-1] in parent:
            out.append(parent[out[-1]])
        return out
    out = []
    for u, v in itertools.combinations_with_replacement(range(t.n), 2):
        au = ancestors(u)
        av = set(ancestors(v))
        out.append((u, v, next(x for x in au if x in av)))
    return sorted(out)


def greedy_branching(fx, kind):
    """A branching is a forest of directed trees: every node has at most one
    in-arc and the underlying undirected graph has no cycle. The greedy rule
    takes the arcs by weight, then source, then target, keeping each arc that
    keeps both conditions."""
    s = D.simple_digraph(fx)
    order = sorted(zip(s.src, s.tgt, s.weights), key=lambda e: (e[2], e[0], e[1]),
                   reverse=(kind == "max"))
    uf = UnionFind(s.n)
    has_parent = set()
    kept = []
    for a, b, _ in order:
        if b in has_parent or uf.find(a) == uf.find(b):
            continue
        uf.union(a, b)
        has_parent.add(b)
        kept.append((a, b))
    return sorted(kept)


def is_simple_path(fx):
    arcs = set()
    for a, b in zip(fx.src, fx.tgt):
        arcs.add((a, b))
        if not fx.directed:
            arcs.add((b, a))
    out = []
    for seq in D.path_sequences(fx):
        ok = (len(seq) > 0 and len(set(seq)) == len(seq)
              and all(0 <= v < fx.n for v in seq)
              and all((a, b) in arcs for a, b in zip(seq, seq[1:])))
        out.append(int(ok))
    return out


def cd_index(fx, delta, weighted):
    """Funk and Owen-Smith's consolidation-destabilization index of every
    node of the simple digraph (an arc j -> i is a citation of i by j):
    the mean over the papers j published after the focal paper and at most
    `delta` after it (citations in years T + 1 to T + t) that cite it or one
    of its references of -1 (j cites the focal paper and a reference), +1
    (j cites the focal paper only) or 0 (a reference only), each divided by
    the paper's weight; n counts those papers. -999 where n = 0."""
    s = D.simple_graph(fx)
    times, wts = D.node_times(s.n), D.node_weights(s.n)
    refs = [set() for _ in range(s.n)]
    cites = [set() for _ in range(s.n)]
    for a, b in zip(s.src, s.tgt):
        refs[a].add(b)
        cites[b].add(a)
    out = []
    for i in range(s.n):
        within = lambda j: times[i] < times[j] <= times[i] + delta  # noqa: E731
        citers = {j for j in cites[i] if within(j)}
        pool = set(citers)
        for r in refs[i]:
            pool |= {j for j in cites[r] if within(j)}
        if not pool:
            out.append(-999.0)
            continue
        total = 0.0
        for j in citers:
            f = -1.0 if refs[j] & refs[i] else 1.0
            total += f / (wts[j] if weighted else 1.0)
        out.append(total / len(pool))
    return out


class Undefined(Exception):
    """The definition gives no golden value for this fixture."""


def recursive_cycles(fx, ordered):
    """Every simple directed cycle (a self-loop is a cycle of one node) of
    the derived digraph, each rotated to start at its smallest node: a
    search from each start over larger nodes only. Fixtures above twelve
    nodes are left out (dense ones have exponentially many cycles)."""
    if not D.small(fx):
        return []
    s = D.simple_graph(fx, loops=True)
    adj = D.rows(s)
    found = []

    def extend(start, path, on_path):
        for w in adj[path[-1]]:
            if w == start:
                found.append(tuple(path))
            elif w > start and w not in on_path:
                on_path.add(w)
                path.append(w)
                extend(start, path, on_path)
                path.pop()
                on_path.discard(w)

    for start in range(s.n):
        extend(start, [start], {start})
    return sorted(found)


def cycle_basis_check(fx):
    """[cyclomatic number m - n + c, 1, same]: the number of cycles of a
    basis, whether each is a simple cycle of the graph (checked by the
    runner), and the GF(2) rank of the cycles' edge vectors, which must
    equal the cyclomatic number."""
    s = D.simple_graph(fx)
    comps, _ = components(s)
    cyc = len(s.src) - s.n + comps
    return [cyc, 1, cyc]


def has_cycle_in(nodes, arcs, directed):
    """Whether the edges (arcs) among `nodes` contain a cycle: directed, by
    repeatedly removing nodes without in-arcs; undirected, by union-find
    (a loop or a repeated pair is a cycle)."""
    arcs = [(a, b) for a, b in arcs if a in nodes and b in nodes]
    if not directed:
        uf = UnionFind(max(nodes, default=-1) + 1)
        return any(not uf.union(a, b) for a, b in arcs)
    indeg = {v: 0 for v in nodes}
    for _, b in arcs:
        indeg[b] += 1
    live = set(nodes)
    queue = [v for v in nodes if indeg[v] == 0]
    while queue:
        v = queue.pop()
        live.discard(v)
        for a, b in arcs:
            if a == v:
                indeg[b] -= 1
                if indeg[b] == 0:
                    queue.append(b)
    return bool(live)


def reachable(start, arcs, mode):
    seen, stack = {start}, [start]
    while stack:
        v = stack.pop()
        for a, b in arcs:
            nxt = []
            if mode in ("forward", "both") and a == v:
                nxt.append(b)
            if mode in ("backward", "both") and b == v:
                nxt.append(a)
            for w in nxt:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
    return seen


def find_cycle_check(fx, orientation, source):
    """[a cycle exists in the part of the graph the search covers, 1, 1, 1]
    (the runner checks that the cycle returned is closed, has distinct
    edges and follows the orientation): from `source` (node n // 2) the part
    reached by following arcs (forward for none and original, backward for
    reverse, either way for ignore and for an undirected graph), otherwise
    the whole graph."""
    s = D.simple_graph(fx, loops=True)
    arcs = list(zip(s.src, s.tgt))
    nodes = set(range(s.n))
    directed = s.directed and orientation in ("none", "original", "reverse")
    if source >= 0:
        mode = ({"none": "forward", "original": "forward", "reverse": "backward"}.get(
            orientation, "both") if s.directed else "both")
        nodes = reachable(s.n // 2, arcs, mode)
    return [int(has_cycle_in(nodes, arcs, directed)), 1, 1, 1]


def contracted(fx, self_loops, ordered=True):
    """Edges of the simple graph with node n - 1 merged into node 0: every
    edge is rewritten with the merged node's name, the edges between the two
    nodes vanish (or become a loop at 0 with `self_loops`), and repeated
    pairs keep one edge. Sorted (an undirected pair is (smaller, larger));
    with `ordered`, in the documented input order instead: the edges not
    touching n - 1 in file order, then its edges (in-edges before out-edges
    when directed) in file order, renamed, each pair once, as written."""
    s = D.simple_graph(fx, loops=True)
    if s.n < 2:
        return []
    u, v = 0, s.n - 1
    edges = list(zip(s.src, s.tgt))
    if ordered:
        if s.directed:
            touching = [e for e in edges if e[1] == v] + [e for e in edges if e[0] == v]
        else:
            touching = [e for e in edges if v in e]
        sequence = [e for e in edges if v not in e] + touching
    else:
        sequence = edges
    seen, out = set(), []
    for a, b in sequence:
        if {a, b} == {u, v} and not self_loops:
            continue
        a, b = (u if a == v else a), (u if b == v else b)
        key = (a, b) if s.directed else (min(a, b), max(a, b))
        if key not in seen:
            seen.add(key)
            out.append((a, b))
    if ordered:
        return out
    return sorted({(a, b) if s.directed else (min(a, b), max(a, b)) for a, b in out})


def triangle_list(fx):
    s = D.simple_graph(fx)
    adj = [set() for _ in range(s.n)]
    for a, b in zip(s.src, s.tgt):
        adj[a].add(b)
        adj[b].add(a)
    return sorted((a, b, c) for a in range(s.n) for b in adj[a] if b > a
                  for c in adj[a] & adj[b] if c > b)


def erdos_gallai(seq):
    """Erdos and Gallai: an even sum and, sorted non-increasingly, for every
    k: the k largest sum to at most k (k - 1) + the sum over the rest of
    min(d, k)."""
    d = sorted(seq, reverse=True)
    if any(x < 0 for x in d) or sum(d) % 2:
        return False
    return all(sum(d[:k]) <= k * (k - 1) + sum(min(x, k) for x in d[k:])
               for k in range(1, len(d) + 1))


def havel_hakimi(seq):
    """Repeatedly join the largest degree to the next largest ones."""
    d = sorted(seq, reverse=True)
    if any(x < 0 for x in d) or sum(d) % 2:
        return False
    while d:
        top = d.pop(0)
        if top > len(d):
            return False
        for i in range(top):
            d[i] -= 1
            if d[i] < 0:
                return False
        d.sort(reverse=True)
    return True


def multigraphical(seq):
    """Hakimi: an even sum and the largest degree at most the sum of the rest."""
    return (all(x >= 0 for x in seq) and sum(seq) % 2 == 0
            and (not seq or max(seq) <= sum(seq) - max(seq)))


def pseudographical(seq):
    return all(x >= 0 for x in seq) and sum(seq) % 2 == 0


def digraphical(ins, outs):
    """Fulkerson, Chen and Anstee: equal sums, and with the pairs sorted
    non-increasingly by (out, in), for every k the first k outs sum to at
    most the sum over the first k of min(in, k - 1) plus over the rest of
    min(in, k)."""
    if len(ins) != len(outs) or sum(ins) != sum(outs) or min(ins + outs, default=0) < 0:
        return False
    pairs = sorted(zip(outs, ins), reverse=True)
    return all(sum(a for a, _ in pairs[:k])
               <= sum(min(b, k - 1) for _, b in pairs[:k]) + sum(min(b, k) for _, b in pairs[k:])
               for k in range(1, len(pairs) + 1))


def graphical(fx, test):
    und, dirs = D.sequence_cases(fx)
    if test == 4:
        return [int(digraphical(i, o)) for i, o in dirs]
    check = {0: erdos_gallai, 1: havel_hakimi, 2: multigraphical, 3: pseudographical}[test]
    return [int(check(q)) for q in und]


def floyd_warshall(s):
    n = s.n
    inf = float("inf")
    dist = [[inf] * n for _ in range(n)]
    for a, b, w in zip(s.src, s.tgt, s.weights):
        dist[a][b] = min(dist[a][b], w)
    for v in range(n):
        dist[v][v] = min(dist[v][v], 0.0)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def fw_tree(fx, negative, part):
    s = D.fw_graph(fx, negative)
    dist = floyd_warshall(s)
    inf = float("inf")
    if part == "dist":
        return sorted((u, v, dist[u][v]) for u in range(s.n) for v in range(s.n)
                      if dist[u][v] != inf)
    return [1] * sum(1 for u in range(s.n) for v in range(s.n)
                     if u != v and dist[u][v] != inf)


def johnson_lengths(fx):
    """Reweighted lengths l(u, v) + h(u) - h(v) in the order of the rows,
    h(v) the shortest distance to v from any node (0 from v itself)."""
    s = D.weighted_dag(fx)
    dist = floyd_warshall(s)
    pot = [min(dist[u][v] for u in range(s.n)) for v in range(s.n)]
    adj = [dict() for _ in range(s.n)]
    for a, b, w in zip(s.src, s.tgt, s.weights):
        adj[a][b] = w
    return [w + pot[u] - pot[v] for u in range(s.n) for v, w in adj[u].items()]


def dag_reachability(fx):
    s = D.dag(fx)
    reach = [set() for _ in range(s.n)]
    for v in reversed(range(s.n)):  # arcs go from smaller to larger nodes
        for a, b in zip(s.src, s.tgt):
            if a == v:
                reach[v].add(b)
                reach[v] |= reach[b]
    return sorted((u, v) for u in range(s.n) for v in reach[u])


TOPO_LIMIT = 5000


def topological_sorts(fx):
    """Every topological order of the derived DAG (up to twelve nodes), by
    taking any node whose predecessors are all placed at each step; Undefined
    when there are more than TOPO_LIMIT orders."""
    s = D.sort_graph(fx)
    if s is None:
        return []
    pred = [set() for _ in range(s.n)]
    for a, b in zip(s.src, s.tgt):
        pred[b].add(a)
    out = []

    def extend(order, placed):
        if len(out) > TOPO_LIMIT:
            return
        if len(order) == s.n:
            out.append(tuple(order))
            return
        for v in range(s.n):
            if v not in placed and pred[v] <= placed:
                extend(order + [v], placed | {v})

    extend([], frozenset())
    if len(out) > TOPO_LIMIT:
        raise Undefined
    return sorted(out)


def colliders(fx, v_structures):
    s = D.simple_graph(fx)
    pred = [set() for _ in range(s.n)]
    arcs = set(zip(s.src, s.tgt))
    for a, b in arcs:
        pred[b].add(a)
    out = []
    for c in range(s.n):
        for a, b in itertools.combinations(sorted(pred[c]), 2):
            if v_structures and ((a, b) in arcs or (b, a) in arcs):
                continue
            out.append((a, c, b))
    return sorted(out)


def compute(spec, fx):
    fn = spec["fn"]
    if fn == "nxs_forest_counts":
        return forest_counts(fx)
    if fn == "nxs_forest_flags":
        return forest_flags(fx)
    if fn == "nxs_tree_centroid":
        return tree_centroid(fx)
    if fn == "nxs_prufer":
        return prufer(fx)
    if fn == "nxs_from_prufer":
        return from_prufer(fx)
    if fn == "nxs_tree_lca":
        return tree_lca(fx)
    if fn == "nxs_greedy_branching":
        return greedy_branching(fx, spec["kind"])
    if fn == "nxs_is_simple_path":
        return is_simple_path(fx)
    if fn == "nxs_cd_index":
        return cd_index(fx, spec["delta"], spec.get("weighted", False))
    if fn == "nxs_recursive_cycles":
        return recursive_cycles(fx, spec.get("ordered", True))
    if fn == "nxs_cycle_basis_check":
        return cycle_basis_check(fx)
    if fn == "nxs_find_cycle_check":
        return find_cycle_check(fx, spec.get("orientation_name", "none"), spec.get("source", -1))
    if fn == "nxs_contracted_nodes":
        return contracted(fx, spec["self_loops"], spec.get("ordered", True))
    if fn == "nxs_cd_index":
        return cd_index(fx, spec["delta"], spec.get("weighted", False))
    if fn == "nxs_triangle_list":
        return triangle_list(fx)
    if fn == "nxs_degree_sequence_test":
        return graphical(fx, spec["test"])
    if fn == "nxs_fw_tree":
        return fw_tree(fx, spec.get("negative", False), spec["part"])
    if fn == "nxs_fw_tree_valid":
        return fw_tree(fx, spec.get("negative", False), "valid")
    if fn == "nxs_johnson_lengths":
        return johnson_lengths(fx)
    if fn == "nxs_dag_reachability":
        return dag_reachability(fx)
    if fn == "nxs_topological_sorts":
        return topological_sorts(fx)
    if fn == "nxs_colliders":
        return colliders(fx, spec.get("v_structures", False))
    if fn == "nxs_euler_valid":
        e = D.eulerian(fx)
        uf = UnionFind(e.n)
        for a, b in zip(e.src, e.tgt):
            uf.union(a, b)
        if any(uf.find(a) != uf.find(0) for a in e.src):
            raise Undefined  # edges outside the component of node 0 are never reached
        return [1, 1, 1]
    raise ValueError(fn)


def main() -> None:
    spec = load_area("nx_shims")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            try:
                values = compute(v["params"], fx)
            except Undefined:
                continue
            write_values(ORACLE, name, variant, values)
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (nx shims): wrote {count} golden files")


if __name__ == "__main__":
    main()
