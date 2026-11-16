#!/usr/bin/env python3
"""Definition oracle for the ERGM and SAOM kernels. Shares no code with the
engine:

- statistics by direct counting over node pairs and triples;
- change statistics as g(x with the tie) - g(x without it), each side
  counted from scratch (small fixtures);
- MPLE and dyad-independent MLE by logistic regression (Newton's method
  on the dense design of every dyad);
- simulated means as exact expectations: closed form per dyad for
  dyad-independent models, else a sum over every graph on the fixture's
  nodes (at most 20 dyads, vectorized over all 2^D graphs);
- `ergm_fit`: MPLE as above; maximum likelihood exactly on subgraphs of
  six or seven undirected nodes (2^15, 2^21 graphs) or five directed ones
  (2^20), every graph enumerated once and tabulated by its sufficient
  statistics, then Newton's method on
  l(theta) = log sum_{x agreeing with the data} exp(theta . g(x))
           - log sum_x exp(theta . g(x)),
  where "agreeing" is every observed dyad (one graph when nothing is
  missing; the missing dyads are summed out otherwise, Handcock and Gile
  2010); and the exact log-likelihood of dyad-independent models
  (independent unordered pairs, a four-outcome logit each, for directed
  models with mutual);
- SAOM with the outdegree effect only: each actor's ties form a Markov
  chain on (initial ties kept, new ties added), whose distribution at the
  end of the period is exp(Q) applied to the start (scipy expm).

The counting code works on Python integers (one graph) and on numpy
arrays (one entry per enumerated graph) alike.

    python3 oracles/ergm_definition_oracle.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import expm

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
MAX_ENUM_DYADS = 20


def rule(name, n):
    if name == "mod3":
        return [v % 3 for v in range(n)]
    if name == "num7":
        return [(7 * v) % 11 for v in range(n)]
    raise ValueError(name)


def simple_pairs(fx):
    out = set()
    for a, b in zip(fx.src, fx.tgt):
        if a != b:
            out.add((a, b) if fx.directed else (min(a, b), max(a, b)))
    return out


def adjacency_of(n, directed, pairs):
    a = [[0] * n for _ in range(n)]
    for i, j in pairs:
        a[i][j] = 1
        if not directed:
            a[j][i] = 1
    return a


def dyads(n, directed):
    return [(i, j) for i in range(n) for j in range(n) if i != j and (directed or i < j)]


def statistics(terms, n, directed, a):
    """g(x) for adjacency `a` (a[i][j] is 0/1 or an array of 0/1)."""
    zero = a[0][0] * 0 if n else 0
    dy = dyads(n, directed)
    outdeg = [sum((a[i][j] for j in range(n) if j != i), zero) for i in range(n)]
    indeg = [sum((a[j][i] for j in range(n) if j != i), zero) for i in range(n)]
    sp_cache = {}

    def sp(i, j):
        if (i, j) not in sp_cache:
            sp_cache[(i, j)] = sum((a[i][k] * a[k][j] for k in range(n) if k != i and k != j),
                                   zero)
        return sp_cache[(i, j)]

    def triples(kind):
        s = zero
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if len({i, j, k}) < 3:
                        continue
                    if kind == "t":
                        s = s + a[i][j] * a[j][k] * a[i][k]
                    else:
                        s = s + a[i][j] * a[j][k] * a[k][i]
        return s

    def gw(decay, s):
        r = 1.0 - math.exp(-decay)
        return math.exp(decay) * (1.0 - r ** s)

    def choose(d, k):
        # C(d, k) for integer arrays: product form.
        c = 1.0
        for t in range(k):
            c = c * (d - t) / (t + 1)
        return c * (d >= k)

    out = []
    for t in terms:
        p = t.split(":")
        name = p[0]
        if name == "edges":
            v = sum((a[i][j] for i, j in dy), zero)
        elif name == "mutual":
            v = sum((a[i][j] * a[j][i] for i, j in dy if i < j), zero)
        elif name == "isolates":
            v = sum(((outdeg[i] + (indeg[i] if directed else 0)) == 0 for i in range(n)), zero)
        elif name in ("kstar", "ostar"):
            v = sum((choose(outdeg[i], int(p[1])) for i in range(n)), zero)
        elif name == "istar":
            v = sum((choose(indeg[i], int(p[1])) for i in range(n)), zero)
        elif name == "ttriple":
            v = triples("t")
        elif name == "ctriple":
            v = triples("c") / 3
        elif name == "triangle":
            v = triples("t") + triples("c") / 3 if directed else triples("c") / 6
        elif name in ("gwdegree", "gwodegree"):
            v = sum((gw(float(p[1]), outdeg[i]) for i in range(n)), zero)
        elif name == "gwidegree":
            v = sum((gw(float(p[1]), indeg[i]) for i in range(n)), zero)
        elif name == "gwesp":
            v = sum((a[i][j] * gw(float(p[1]), sp(i, j)) for i, j in dy), zero)
        elif name == "gwdsp":
            v = sum((gw(float(p[1]), sp(i, j)) for i, j in dy), zero)
        elif name == "nodematch":
            x = rule(p[1], n)
            v = sum((a[i][j] for i, j in dy if x[i] == x[j]), zero)
        elif name == "nodefactor":
            x, lev = rule(p[1], n), int(float(p[2]))
            v = sum((a[i][j] * ((x[i] == lev) + (x[j] == lev)) for i, j in dy), zero)
        elif name == "nodecov":
            x = rule(p[1], n)
            v = sum((a[i][j] * (x[i] + x[j]) for i, j in dy), zero)
        else:
            raise ValueError(t)
        out.append(v)
    return out


def change_rows(terms, n, directed, pairs):
    """(change statistics, tie indicator) of every dyad, by toggling."""
    rows = []
    for i, j in dyads(n, directed):
        with_e = adjacency_of(n, directed, pairs | {(i, j)})
        without = adjacency_of(n, directed, pairs - {(i, j)})
        plus = statistics(terms, n, directed, with_e)
        minus = statistics(terms, n, directed, without)
        rows.append(([float(x - y) for x, y in zip(plus, minus)], float((i, j) in pairs)))
    return rows


DYAD_INDEPENDENT = {"edges", "nodematch", "nodefactor", "nodecov"}


def dyad_independent_rows(terms, n, directed, pairs):
    """Change statistics of dyad-independent terms depend on the dyad only."""
    s0 = statistics(terms, n, directed, adjacency_of(n, directed, set()))
    rows = []
    for i, j in dyads(n, directed):
        s1 = statistics(terms, n, directed, adjacency_of(n, directed, {(i, j)}))
        rows.append(([float(x - y) for x, y in zip(s1, s0)], float((i, j) in pairs)))
    return rows


def logistic_mle(rows, iters=200):
    x = np.array([r for r, _ in rows], dtype=float)
    y = np.array([t for _, t in rows], dtype=float)
    b = np.zeros(x.shape[1])
    for _ in range(iters):
        p = 1.0 / (1.0 + np.exp(-(x @ b)))
        grad = x.T @ (y - p)
        hess = (x * (p * (1 - p))[:, None]).T @ x
        step = np.linalg.solve(hess, grad)
        b = b + step
        if np.max(np.abs(step)) < 1e-13 * (1 + np.max(np.abs(b))):
            break
    return [float(v) for v in b]


def exact_means_enumerated(terms, coef, n, directed):
    dy = dyads(n, directed)
    masks = np.arange(1 << len(dy), dtype=np.int64)
    bit = {d: ((masks >> k) & 1).astype(np.int64) for k, d in enumerate(dy)}
    zero = np.zeros(len(masks), dtype=np.int64)
    a = [[zero] * n for _ in range(n)]
    for (i, j), v in bit.items():
        a[i][j] = v
        if not directed:
            a[j][i] = v
    s = [np.asarray(v, dtype=float) + np.zeros(len(masks)) for v in
         statistics(terms, n, directed, a)]
    eta = sum(c * v for c, v in zip(coef, s))
    w = np.exp(eta - eta.max())
    return [float((w * v).sum() / w.sum()) for v in s]


def exact_means_dyad_independent(terms, coef, n, directed):
    """Dyads are independent; with `mutual` the unit is the unordered pair."""
    means = [0.0] * len(terms)
    empty = statistics(terms, n, directed, adjacency_of(n, directed, set()))
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for i, j in pairs:
        states = [set(), {(i, j)}, {(j, i)}, {(i, j), (j, i)}] if directed else [set(), {(i, j)}]
        stats = [[float(x - y) for x, y in
                  zip(statistics(terms, n, directed, adjacency_of(n, directed, st)), empty)]
                 for st in states]
        w = [math.exp(sum(c * v for c, v in zip(coef, s))) for s in stats]
        z = sum(w)
        for k in range(len(terms)):
            means[k] += sum(wi * s[k] for wi, s in zip(w, stats)) / z
    return [m + e for m, e in zip(means, empty)]


ENUM_CHUNK = 1 << 16
_TALLIES = {}


def chunk_statistics(terms, n, directed, dy, masks):
    """The statistics of the graphs with the given bit masks (bit k = dyad
    k), one row per graph."""
    zero = np.zeros(len(masks), dtype=np.int64)
    a = [[zero] * n for _ in range(n)]
    for k, (i, j) in enumerate(dy):
        v = ((masks >> k) & 1).astype(np.int64)
        a[i][j] = v
        if not directed:
            a[j][i] = v
    return np.array([np.asarray(v, dtype=float) + np.zeros(len(masks))
                     for v in statistics(terms, n, directed, a)]).T


def tally(terms, n, directed):
    """Every graph on n nodes enumerated once (in chunks of 2^16), tabulated
    as the distinct sufficient-statistic vectors and how many graphs have
    each: the partition function of any coefficients is a sum over the
    tally. Cached per (terms, n, directed)."""
    key = (tuple(terms), n, directed)
    if key not in _TALLIES:
        dy = dyads(n, directed)
        counts = {}
        total = 1 << len(dy)
        for lo in range(0, total, ENUM_CHUNK):
            masks = np.arange(lo, min(total, lo + ENUM_CHUNK), dtype=np.int64)
            values, hits = np.unique(chunk_statistics(terms, n, directed, dy, masks),
                                     axis=0, return_counts=True)
            for row, hit in zip(map(tuple, values), hits):
                counts[row] = counts.get(row, 0) + int(hit)
        rows = sorted(counts)
        _TALLIES[key] = (np.array(rows, dtype=float),
                         np.array([counts[r] for r in rows], dtype=float))
    return _TALLIES[key]


def consistent_tally(terms, n, directed, pairs, missing):
    """The tally of the graphs that agree with the data on every observed
    dyad (the 2^M completions of the missing dyads)."""
    dy = dyads(n, directed)
    gone = [k for k, d in enumerate(dy) if d in set(missing)]
    base = sum(1 << k for k, d in enumerate(dy) if d in pairs and d not in set(missing))
    masks = np.array([base | sum(1 << gone[b] for b in range(len(gone)) if (c >> b) & 1)
                      for c in range(1 << len(gone))], dtype=np.int64)
    values, hits = np.unique(chunk_statistics(terms, n, directed, dy, masks), axis=0,
                             return_counts=True)
    return values.astype(float), hits.astype(float)


def log_partition(values, counts, b):
    """log sum_c N_c exp(c . b) over a tally, and the normalized weights."""
    e = values @ b + np.log(counts)
    top = e.max()
    w = np.exp(e - top)
    return top + math.log(w.sum()), w / w.sum()


def exact_mle_enumerated(terms, n, directed, pairs, missing=()):
    """The maximum likelihood estimate from the tallies, the missing dyads
    summed out (Newton's method with step halving):
    l(b) = log Z_consistent(b) - log Z(b)."""
    s, ns = tally(terms, n, directed)
    sc, nc = consistent_tally(terms, n, directed, pairs, missing)
    # With missing dyads, start at the complete-data estimate; where the
    # Newton direction does not ascend (the observed-data information is
    # not positive definite there), step along the gradient.
    b = np.array(exact_mle_enumerated(terms, n, directed, pairs)) if missing else \
        np.zeros(s.shape[1])

    def loglik(b):
        return log_partition(sc, nc, b)[0] - log_partition(s, ns, b)[0]
    for _ in range(500):
        _, w = log_partition(s, ns, b)
        _, wc = log_partition(sc, nc, b)
        m, mc = w @ s, wc @ sc
        cov = (s - m).T @ ((s - m) * w[:, None])
        covc = (sc - mc).T @ ((sc - mc) * wc[:, None])
        grad = mc - m
        try:
            step = np.linalg.solve(cov - covc, grad)
        except np.linalg.LinAlgError:
            step = grad
        if step @ grad <= 0:
            step = grad
        f0, scale = loglik(b), 1.0
        while True:
            nb = b + scale * step
            if loglik(nb) >= f0 - 1e-14 or scale < 1e-8:
                break
            scale /= 2
        b = nb
        if np.max(np.abs(grad)) < 1e-11 or (
                scale == 1.0 and np.max(np.abs(step)) < 1e-13 * (1 + np.max(np.abs(b)))):
            break
    return [float(v) for v in b]


def pair_states(terms, n, directed, pairs, i, j):
    """Statistics of the four states of the pair (i, j) relative to the
    empty pair, the rest of the graph empty (pair-independent terms)."""
    empty = statistics(terms, n, directed, adjacency_of(n, directed, set()))
    states = [set(), {(i, j)}, {(j, i)}, {(i, j), (j, i)}]
    return [[float(x - y) for x, y in
             zip(statistics(terms, n, directed, adjacency_of(n, directed, st)), empty)]
            for st in states], states


def exact_mle_pairs(terms, n, directed, pairs):
    """Maximum likelihood when unordered pairs are independent (directed
    models of edges, mutual and node covariates): a four-outcome
    multinomial logit per pair; returns the estimate and the exact
    log-likelihood."""
    units = []
    for i in range(n):
        for j in range(i + 1, n):
            stats, states = pair_states(terms, n, directed, pairs, i, j)
            seen = {(a, b) for a, b in ((i, j), (j, i)) if (a, b) in pairs}
            units.append((np.array(stats), states.index(seen)))
    b = np.zeros(len(terms))

    def loglik(b):
        return sum(float(x[k] @ b) - float(np.logaddexp.reduce(x @ b)) for x, k in units)
    for _ in range(500):
        grad = np.zeros(len(terms))
        hess = np.zeros((len(terms), len(terms)))
        for x, k in units:
            e = x @ b
            w = np.exp(e - e.max())
            w /= w.sum()
            m = w @ x
            grad += x[k] - m
            hess += (x - m).T @ ((x - m) * w[:, None])
        # Stop on the score itself (the step-size rule stopped short when the
        # log-likelihood, about -700 on the larger fixtures, could not
        # register the last improvements).
        if np.max(np.abs(grad)) < 1e-11:
            break
        step = np.linalg.solve(hess, grad)
        f0, scale = loglik(b), 1.0
        while True:
            nb = b + scale * step
            if loglik(nb) >= f0 - 1e-12 * abs(f0) or scale < 1e-8:
                break
            scale /= 2
        b = nb
    return [float(v) for v in b], loglik(b), len(units)


def logistic_loglik(rows, b):
    """sum over dyads of y eta - log(1 + e^eta)."""
    x = np.array([r for r, _ in rows], dtype=float)
    y = np.array([t for _, t in rows], dtype=float)
    eta = x @ np.array(b)
    return float((y * eta - np.logaddexp(0.0, eta)).sum())


def subgraph_nodes(spec, fixture):
    """The nodes of an `ergm_fit` subgraph, in order: the first `spec`
    nodes, or the fixture's list when `spec` maps fixtures to node lists."""
    if isinstance(spec, dict):
        return list(spec[fixture])
    return list(range(spec))


def fit_value(e, n, directed, pairs, fixture):
    """`ergm_fit`: the coefficients (then, with `loglik`, the exact
    log-likelihood and that of the null model)."""
    terms = e["terms"]
    names = {t.split(":")[0] for t in terms}
    if "nodes" in e:
        # The induced subgraph, every graph on its nodes enumerated (six or
        # seven undirected nodes, five directed).
        keep = subgraph_nodes(e["nodes"], fixture)
        index = {v: i for i, v in enumerate(keep)}
        sub = {(index[i], index[j]) for i, j in pairs if i in index and j in index}
        missing = [tuple(d) for d in e.get("missing", [])]
        return exact_mle_enumerated(terms, len(keep), directed, sub, missing)
    if directed and "mutual" in names and names <= DYAD_INDEPENDENT | {"mutual"} \
            and e["method"] != "mple":
        b, ll, units = exact_mle_pairs(terms, n, directed, pairs)
        if not e.get("loglik"):
            return b
        return b + [ll, -2 * units * math.log(2.0)]
    if names <= DYAD_INDEPENDENT:
        rows = dyad_independent_rows(terms, n, directed, pairs)
    elif e["method"] == "mple" and n <= 20:
        rows = change_rows(terms, n, directed, pairs)
    else:
        return None
    b = logistic_mle(rows)
    if not e.get("loglik"):
        return b
    nobs = len(rows)
    return b + [logistic_loglik(rows, b), -nobs * math.log(2.0)]


def saom_density(fx, beta, rate):
    """Expected ties and changed ties at time 1 (outdegree effect only)."""
    n = fx.n
    out = {v: set() for v in range(n)}
    for i, j in simple_pairs(fx):
        out[i].add(j)
    ties = dist = 0.0
    for i in range(n):
        d0 = len(out[i])
        free = n - 1 - d0
        states = [(a, b) for a in range(d0 + 1) for b in range(free + 1)]
        index = {s: k for k, s in enumerate(states)}
        q = np.zeros((len(states), len(states)))
        for (a, b), k in index.items():
            present, absent = a + b, n - 1 - a - b
            z = 1.0 + present * math.exp(-beta) + absent * math.exp(beta)
            moves = {(a - 1, b): a * math.exp(-beta), (a, b - 1): b * math.exp(-beta),
                     (a + 1, b): (d0 - a) * math.exp(beta),
                     (a, b + 1): (free - b) * math.exp(beta)}
            for s, r in moves.items():
                if r > 0:
                    q[k, index[s]] += rate * r / z
                    q[k, k] -= rate * r / z
        p = expm(q)[index[(d0, 0)]]
        ties += sum(p[k] * (a + b) for (a, b), k in index.items())
        dist += sum(p[k] * (d0 - a + b) for (a, b), k in index.items())
    return [ties, dist]


def compute(spec, ospec, fx):
    e = spec["params"]
    fn = e["fn"]
    n, directed = fx.n, fx.directed
    pairs = simple_pairs(fx)
    if fn == "ergm_statistics":
        return statistics(e["terms"], n, directed, adjacency_of(n, directed, pairs))
    if fn == "ergm_change_sums":
        rows = change_rows(e["terms"], n, directed, pairs)
        return [sum(r[k] for r, _ in rows) for k in range(len(e["terms"]))]
    if fn in ("ergm_mple", "ergm_mcmle"):
        names = {t.split(":")[0] for t in e["terms"]}
        if names <= DYAD_INDEPENDENT:
            rows = dyad_independent_rows(e["terms"], n, directed, pairs)
        else:
            rows = change_rows(e["terms"], n, directed, pairs)
        return logistic_mle(rows)
    if fn == "ergm_fit":
        return fit_value(e, n, directed, pairs, fx.name)
    if fn == "ergm_sim_mean":
        names = {t.split(":")[0] for t in e["terms"]}
        if names <= DYAD_INDEPENDENT | {"mutual"}:
            return exact_means_dyad_independent(e["terms"], e["coef"], n, directed)
        if len(dyads(n, directed)) <= MAX_ENUM_DYADS:
            return exact_means_enumerated(e["terms"], e["coef"], n, directed)
        return None
    if fn == "saom_sim_mean":
        if e["effects"] != ["outdegree"]:
            return None
        return saom_density(fx, e["beta"][0], e["rate"])
    return None


def main() -> None:
    spec = load_area("ergm")
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            ospec = v["oracles"].get(ORACLE)
            if ospec is None or not applies(v, fx):
                continue
            if "only_on" in ospec and name not in ospec["only_on"]:
                continue
            if name in ospec.get("undefined_on", []):
                continue
            values = compute(v, ospec, fx)
            if values is not None:
                write_values(ORACLE, name, variant, values)
    write_version(ORACLE, DEFINITION_VERSION)


if __name__ == "__main__":
    main()
