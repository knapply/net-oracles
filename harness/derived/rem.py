"""Relational event streams for the relational event model validation.

Every fixture of validation/fixtures/ becomes a stream of directed events
that follows deterministically from its edge list, so that the engine
runner (validation/bindings/rem.py), the definition oracle, and the R
oracle (validation/oracles/r_rem.R, which repeats these rules) see the
same events:

- self-loops are dropped (an actor does not interact with itself);
- edge e (0-based, in file order) occurs c_e = 1 + (7 e + 3) mod 3 times;
- occurrence j of edge e runs from its first to its second endpoint,
  except when (5 e + 3 j) mod 4 = 3, when it runs the other way (so that
  repeated and reciprocated events occur in every fixture);
- occurrences are ordered by the key ((131 e + 71 j + 17) * 2654435761)
  mod 2^32, ties by (e, j), and the k-th event (0-based) happens at time
  k + 1, or at floor(k / 2) + 1 with ``ties`` (pairs of simultaneous
  events);
- its weight is the edge weight (1 for unweighted fixtures) and its type
  is (e + j) mod 2.
"""

from __future__ import annotations


def event_stream(fx, ties: bool = False):
    """(sender, receiver, time, weight, type) lists of a fixture's events,
    in time order."""
    occ = []
    for e, (u, v) in enumerate(zip(fx.src, fx.tgt)):
        if u == v:
            continue
        for j in range(1 + (7 * e + 3) % 3):
            key = ((131 * e + 71 * j + 17) * 2654435761) % 2**32
            s, r = (v, u) if (5 * e + 3 * j) % 4 == 3 else (u, v)
            w = fx.weights[e] if fx.weights is not None else 1.0
            occ.append((key, e, j, s, r, w))
    occ.sort()
    sender = [o[3] for o in occ]
    receiver = [o[4] for o in occ]
    time = [float(k // 2 + 1 if ties else k + 1) for k in range(len(occ))]
    weight = [float(o[5]) for o in occ]
    kind = [(o[1] + o[2]) % 2 for o in occ]
    return sender, receiver, time, weight, kind
