"""Checkers for planar embeddings, Kuratowski certificates and straight-line
drawings, shared by the planarity bindings and oracles (areas `planarity`).
Pure Python, exact integer arithmetic, no engine and no tool code.

An embedding is a rotation system: for every node the cyclic list of its
neighbours (simple form) or of its darts (dart form: dart 2e is the source
end of input edge e, 2e + 1 its target end). A face is traced by the rule
"after arriving over a dart, leave by the successor of its reverse dart in
the rotation at the node reached".

    check_simple_embedding(n, edges, rings)   structure and Euler's formula
    check_dart_embedding(n, src, tgt, rows)   [structure, Euler, loops]
    certificate_kind(edges)                   5, 33 (K5, K3,3), or 0
    outer_certificate_kind(edges)             4, 23 (K4, K2,3), or 0
    check_drawing(n, pts, edges, rings)       [bounds, distinct, crossings, angles]
"""

from __future__ import annotations

from functools import cmp_to_key


def simple_pairs(src, tgt):
    """Distinct unordered pairs (u < v) of the edges, loops dropped."""
    return sorted({(min(a, b), max(a, b)) for a, b in zip(src, tgt) if a != b})


def components(n, pairs):
    """Component label of each node (smallest node id in it)."""
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in pairs:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[max(ra, rb)] = min(ra, rb)
    return [find(v) for v in range(n)]


def count_faces(n, rows, src, tgt):
    """(faces, lengths) of the dart rotation system `rows` (one list of
    darts per node) of the multigraph with edges (src[e], tgt[e]);
    None if a dart is missing, repeated or at the wrong node."""
    m = len(src)
    where = {}
    for v, row in enumerate(rows):
        for pos, d in enumerate(row):
            if d in where or not 0 <= d < 2 * m:
                return None
            if (src[d // 2] if d % 2 == 0 else tgt[d // 2]) != v:
                return None
            where[d] = (v, pos)
    if len(where) != 2 * m:
        return None
    seen, lengths = set(), []
    for start in range(2 * m):
        if start in seen:
            continue
        d, length = start, 0
        while d not in seen:
            seen.add(d)
            length += 1
            v, pos = where[d ^ 1]
            row = rows[v]
            d = row[(pos + 1) % len(row)]
        lengths.append(length)
    return len(lengths), lengths


def euler_ok(n, src, tgt, faces):
    """V - E + F == C + C' for E edges with loops and parallels counted,
    C components and C' components with an edge (each of those has two
    sides, an isolated node counts one)."""
    label = components(n, [(a, b) for a, b in zip(src, tgt)])
    comps = len(set(label))
    nontrivial = len({label[v] for v in set(src) | set(tgt)})
    return n - len(src) + faces == comps + nontrivial


def check_dart_embedding(n, src, tgt, rows):
    """[structure, Euler, loop faces]: every dart once at its own node; faces
    satisfy Euler's formula for the multigraph; the faces of length one are
    exactly the loops' (one per loop; two for a node whose only edge is one loop)."""
    if len(rows) != n:
        return [0, 0, 0]
    traced = count_faces(n, rows, src, tgt)
    if traced is None:
        return [0, 0, 0]
    faces, lengths = traced
    loops = sum(1 for a, b in zip(src, tgt) if a == b)
    # both sides of a node whose only edge is one loop are faces of length one
    touching = [0] * n
    for a, b in zip(src, tgt):
        touching[a] += 1
        if b != a:
            touching[b] += 1
    lone = sum(1 for v in range(n) if touching[v] == 1 and (v, v) in set(zip(src, tgt)))
    return [1, int(euler_ok(n, src, tgt, faces)), int(lengths.count(1) == loops + lone)]


def check_simple_embedding(n, pairs, rings):
    """1 if `rings` (neighbours per node) list every neighbour of each node
    once, symmetrically, and the rotation system satisfies Euler's formula."""
    if len(rings) != n:
        return 0
    want = [set() for _ in range(n)]
    for a, b in pairs:
        want[a].add(b)
        want[b].add(a)
    for v in range(n):
        if len(rings[v]) != len(set(rings[v])) or set(rings[v]) != want[v]:
            return 0
    index = {p: i for i, p in enumerate(pairs)}
    rows = [[2 * index[(min(v, w), max(v, w))] + (0 if v < w else 1) for w in ring]
            for v, ring in enumerate(rings)]
    src, tgt = [p[0] for p in pairs], [p[1] for p in pairs]
    return check_dart_embedding(n, src, tgt, rows)[1]


def _chains(edges):
    """The branch nodes (degree 3 or more) and the paths between them, or
    None if the edge set is not a subdivision of a graph on them (a node of
    degree 1, a cycle without a branch node, a path ending in itself)."""
    adj = {}
    for a, b in edges:
        if a == b:
            return None
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    if len({frozenset(e) for e in edges}) != len(edges):
        return None
    if any(len(x) < 2 for x in adj.values()):
        return None
    branch = sorted(v for v, x in adj.items() if len(x) >= 3)
    paths, covered = [], 0
    for b in branch:
        for first in adj[b]:
            prev, cur, length = b, first, 1
            while cur not in branch:
                nxt = [w for w in adj[cur] if w != prev]
                if len(nxt) != 1:
                    return None
                prev, cur = cur, nxt[0]
                length += 1
            if cur == b:
                return None
            if b < cur or (b == cur):
                paths.append((b, cur))
            covered += length
    # every edge lies on exactly two traced walks (one from each end)
    if covered != 2 * len(edges):
        return None
    return branch, paths, adj


def certificate_kind(edges):
    """5 if `edges` form a subdivision of K5, 33 if of K3,3, else 0. The
    edge set must be exactly the subdivision (a minimal non-planar graph)."""
    got = _chains(edges)
    if got is None:
        return 0
    branch, paths, adj = got
    if len(set(paths)) != len(paths):
        return 0
    if len(branch) == 5 and len(paths) == 10 and all(len(adj[b]) == 4 for b in branch):
        return 5
    if len(branch) == 6 and len(paths) == 9 and all(len(adj[b]) == 3 for b in branch):
        near = {b: {y for x, y in paths if x == b} | {x for x, y in paths if y == b}
                for b in branch}
        side = {branch[0]}
        for w in near[branch[0]]:
            side |= near[w]
        other = set(branch) - side
        if (len(side) == 3 and len(other) == 3 and not side & near[branch[0]]
                and all(near[v] == other for v in side)):
            return 33
    return 0


def outer_certificate_kind(edges):
    """4 if `edges` form a subdivision of K4, 23 if of K2,3, else 0."""
    got = _chains(edges)
    if got is None:
        return 0
    branch, paths, adj = got
    if len(branch) == 4 and len(paths) == 6 and len(set(paths)) == 6 \
            and all(len(adj[b]) == 3 for b in branch):
        return 4
    if len(branch) == 2 and len(paths) == 3 and len(set(paths)) == 1 \
            and all(len(adj[b]) == 3 for b in branch):
        return 23
    return 0


def _orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def _on_segment(p, a, b):
    return (_orient(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0])
            and min(a[1], b[1]) <= p[1] <= max(a[1], b[1]))


def segments_conflict(p1, p2, q1, q2, shared):
    """True if the closed segments p1p2 and q1q2 meet anywhere other than
    at their one shared endpoint (`shared` is that endpoint or None)."""
    if shared is not None:
        a = p2 if p1 == shared else p1
        b = q2 if q1 == shared else q1
        # overlap along one ray from the shared endpoint
        return _orient(shared, a, b) == 0 and \
            (a[0] - shared[0]) * (b[0] - shared[0]) + (a[1] - shared[1]) * (b[1] - shared[1]) > 0
    o1, o2 = _orient(p1, p2, q1), _orient(p1, p2, q2)
    o3, o4 = _orient(q1, q2, p1), _orient(q1, q2, p2)
    if ((o1 > 0 > o2) or (o1 < 0 < o2)) and ((o3 > 0 > o4) or (o3 < 0 < o4)):
        return True
    return (_on_segment(q1, p1, p2) or _on_segment(q2, p1, p2)
            or _on_segment(p1, q1, q2) or _on_segment(p2, q1, q2))


def drawing_crossings(pts, edges):
    """True if two edges of the straight-line drawing cross or overlap, or
    a node lies on an edge it does not end. Segments are bucketed in a grid
    so that large drawings are tested in near-linear time."""
    if not edges:
        return False
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    span = max(max(xs) - min(xs), max(ys) - min(ys), 1)
    cell = max(span // max(int(len(edges) ** 0.5), 1), 1)
    buckets = {}
    for i, (a, b) in enumerate(edges):
        (x1, y1), (x2, y2) = pts[a], pts[b]
        for cx in range(min(x1, x2) // cell, max(x1, x2) // cell + 1):
            for cy in range(min(y1, y2) // cell, max(y1, y2) // cell + 1):
                buckets.setdefault((cx, cy), []).append(i)
    for v, (x, y) in enumerate(pts):
        for i in buckets.get((x // cell, y // cell), []):
            a, b = edges[i]
            if v not in (a, b) and _on_segment((x, y), pts[a], pts[b]):
                return True
    tested = set()
    for ids in buckets.values():
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                key = (ids[i], ids[j])
                if key in tested:
                    continue
                tested.add(key)
                a, b = edges[ids[i]]
                c, d = edges[ids[j]]
                common = {a, b} & {c, d}
                if len(common) == 2:
                    return True
                shared = pts[next(iter(common))] if common else None
                if segments_conflict(pts[a], pts[b], pts[c], pts[d], shared):
                    return True
    return False


def _angle_cmp():
    def half(v):
        return 0 if (v[1] > 0 or (v[1] == 0 and v[0] > 0)) else 1

    def cmp(a, b):
        if half(a[1]) != half(b[1]):
            return half(a[1]) - half(b[1])
        c = a[1][0] * b[1][1] - a[1][1] * b[1][0]
        return -1 if c > 0 else (1 if c < 0 else 0)
    return cmp_to_key(cmp)


def _cyclic_equal(a, b):
    if len(a) != len(b):
        return False
    if not a:
        return True
    if a[0] not in b:
        return False
    k = b.index(a[0])
    return all(a[i] == b[(k + i) % len(b)] for i in range(len(a)))


def angles_match(pts, rings, label):
    """True if, in every component, the counter-clockwise order of each
    node's neighbours in the drawing equals the rotation `rings` or its
    reverse for all nodes of the component together (a mirror image)."""
    forward, backward = {}, {}
    for v, ring in enumerate(rings):
        if len(ring) < 3:
            continue
        d = [(w, (pts[w][0] - pts[v][0], pts[w][1] - pts[v][1])) for w in ring]
        order = [w for w, _ in sorted(d, key=_angle_cmp())]
        c = label[v]
        forward[c] = forward.get(c, True) and _cyclic_equal(ring, order)
        backward[c] = backward.get(c, True) and _cyclic_equal(ring, order[::-1])
    return all(forward[c] or backward[c] for c in forward)


def grid_bounds(n):
    """Largest x and y of the (2n - 4) by (n - 2) grid (n >= 3); a path of
    one or two nodes lies on a row."""
    return (max(2 * n - 4, n - 1, 0), max(n - 2, 0))


def check_drawing(n, pts, pairs, rings):
    """[within the grid, distinct points, no crossing or overlap, angular
    order of every node's neighbours equals the rotation up to a mirror],
    each 1 or 0; `pts` are integer (x, y), `pairs` the simple edges."""
    wx, wy = grid_bounds(n)
    bounds = int(all(isinstance(x, int) and isinstance(y, int) and 0 <= x <= wx and 0 <= y <= wy
                     for x, y in pts))
    distinct = int(len(set(pts)) == n)
    if not distinct:
        return [bounds, 0, 0, 0]
    crossing = int(not drawing_crossings(pts, pairs))
    label = components(n, pairs)
    return [bounds, distinct, crossing, int(angles_match(pts, rings, label))]
