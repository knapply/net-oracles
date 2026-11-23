"""The map equation (Rosvall and Bergstrom 2008, `rosvall2008maps`) of a
partition: two-level description length in bits, with teleportation `tau`
for directed graphs. Shared by communities_definition_oracle.py and
infomap_oracle.py, so the Infomap oracle needs no other definition script.
"""

from __future__ import annotations

import math

import numpy as np


def plogp(x):
    return x * math.log2(x) if x > 0 else 0.0


def map_equation(fx, membership, weighted, tau=0.15):
    n = fx.n
    w = [fx.weights[i] if weighted else 1.0 for i in range(len(fx.src))]
    if not fx.directed:
        s = [0.0] * n
        exit_w = {}
        total = 0.0
        for (a, b), x in zip(zip(fx.src, fx.tgt), w):
            s[a] += x
            s[b] += x
            total += 2 * x
            if membership[a] != membership[b]:
                exit_w[membership[a]] = exit_w.get(membership[a], 0.0) + x
                exit_w[membership[b]] = exit_w.get(membership[b], 0.0) + x
        if total == 0:
            return None
        p = [x / total for x in s]
        q = {c: exit_w.get(c, 0.0) / total for c in set(membership)}
    else:
        out_w = [0.0] * n
        for (a, _), x in zip(zip(fx.src, fx.tgt), w):
            out_w[a] += x
        # Transition matrix T[a][b] (rows sum to 1) and stationary p = p T.
        t = np.zeros((n, n))
        for (a, b), x in zip(zip(fx.src, fx.tgt), w):
            if out_w[a] > 0:
                t[a, b] += (1 - tau) * x / out_w[a]
        for a in range(n):
            ta = tau if out_w[a] > 0 else 1.0
            t[a, :] += ta / n
        m = t.T - np.eye(n)
        m[-1, :] = 1.0
        rhs = np.zeros(n)
        rhs[-1] = 1.0
        p = list(np.linalg.solve(m, rhs))
        size = {}
        for v in range(n):
            size[membership[v]] = size.get(membership[v], 0) + 1
        q = {c: 0.0 for c in size}
        leave = [dict() for _ in range(n)]
        for (a, b), x in zip(zip(fx.src, fx.tgt), w):
            if membership[a] != membership[b]:
                leave[a][membership[b]] = leave[a].get(membership[b], 0.0) + x
        for a in range(n):
            c = membership[a]
            ta = tau if out_w[a] > 0 else 1.0
            outside = sum(leave[a].values())
            link = (1 - ta) * outside / out_w[a] if out_w[a] > 0 else 0.0
            q[c] += p[a] * (ta * (1 - size[c] / n) + link)
    flow = {}
    for v in range(n):
        flow[membership[v]] = flow.get(membership[v], 0.0) + p[v]
    qt = sum(q.values())
    return (plogp(qt) - 2 * sum(plogp(x) for x in q.values()) - sum(plogp(x) for x in p)
            + sum(plogp(q[c] + flow[c]) for c in q))
