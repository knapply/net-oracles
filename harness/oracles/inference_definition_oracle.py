#!/usr/bin/env python3
"""Golden values for the inference area computed directly from the
definitions (manifest/inference.yaml has the inputs and
conventions).

- LR-QAP: logistic regression of the 0/1 dyads on an intercept and two
  dyadic covariates by Newton's method on the log-likelihood (dense solves);
  exact permutation p-values by enumerating every one of the n! relabelings
  (Y-permutation, Krackhardt 1988; double semi-partialling, Dekker,
  Krackhardt and Snijders 2007, with the residuals of each column on the
  others from ordinary least squares).
- Network autocorrelation: covariance, correlation, Moran's I and Geary's C
  at lags 0 to 3 in exact rational arithmetic, from breadth-first geodesic
  distances; exact p-values over all n! relabelings of y.

This oracle shares no code or algorithmic idea with the engine: it is
deliberately slow and simple. Each fit has a hard time limit of 300 seconds
(signal.alarm) and Newton's method at most 100 iterations.

    python3 oracles/inference_definition_oracle.py
"""

from __future__ import annotations

import itertools
import signal
import sys
from collections import deque
from fractions import Fraction
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)

ORACLE = "definition"
MAX_NODES = 80
MAX_EXACT = 8
TIME_LIMIT = 300
TIE_EPS = 1e-10
NAN = float("nan")


class TimeLimit(Exception):
    pass


def _alarm(signum, frame):
    raise TimeLimit()


# ---- inputs ---------------------------------------------------------------

def num7(n):
    return [(7 * v) % 11 for v in range(n)]


def simple_adjacency(fx):
    n = fx.n
    a = [[0] * n for _ in range(n)]
    for u, v in zip(fx.src, fx.tgt):
        if u == v:
            continue
        a[u][v] = 1
        if not fx.directed:
            a[v][u] = 1
    return a


def dyad_rule(rule, n):
    y = num7(n)
    m = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if rule == "dmat":
                m[i][j] = (i + 2 * j) % 5
            elif rule == "smat":
                m[i][j] = (i + j) % 4
            else:
                m[i][j] = abs(y[i] - y[j])
    return m


# ---- LR-QAP ---------------------------------------------------------------

def cells(n, directed):
    """Dyads column by column: every ordered pair off the diagonal, or the
    lower triangle (row > column)."""
    return [(r, c) for c in range(n) for r in range(n) if (r != c if directed else r > c)]


def read(m, r, c, directed):
    if not directed and r < c:
        return m[c][r]
    return m[r][c]


def logistic_fit(x, y):
    """(coefficients, standard errors, log-likelihood) or None when Newton's
    method does not converge in 100 iterations (no finite estimate)."""
    beta = np.zeros(x.shape[1])
    for _ in range(100):
        eta = x @ beta
        p = 1.0 / (1.0 + np.exp(-eta))
        w = p * (1.0 - p)
        info = x.T @ (x * w[:, None])
        grad = x.T @ (y - p)
        try:
            step = np.linalg.solve(info, grad)
        except np.linalg.LinAlgError:
            return None
        beta = beta + step
        if np.max(np.abs(beta)) > 50:
            return None
        if np.all(np.abs(step) <= 1e-12 * (1.0 + np.abs(beta))):
            eta = x @ beta
            p = 1.0 / (1.0 + np.exp(-eta))
            info = x.T @ (x * (p * (1.0 - p))[:, None])
            try:
                cov = np.linalg.inv(info)
            except np.linalg.LinAlgError:
                return None
            ll = float(np.sum(y * eta - np.logaddexp(0.0, eta)))
            return beta, np.sqrt(np.diag(cov)), ll
    return None


def ols_residuals(x, y):
    coef, *_ = np.linalg.lstsq(x, y, rcond=None)
    return y - x @ coef


def lrqap_design(fx):
    n = fx.n
    a = simple_adjacency(fx)
    cs = cells(n, fx.directed)
    x1 = dyad_rule("dmat" if fx.directed else "smat", n)
    x2 = dyad_rule("adiff", n)
    y = np.array([read(a, r, c, fx.directed) for r, c in cs], dtype=float)
    x = np.column_stack([np.ones(len(cs)),
                         [read(x1, r, c, fx.directed) for r, c in cs],
                         [read(x2, r, c, fx.directed) for r, c in cs]])
    return a, cs, x, y


def lr_qap_fit(fx):
    a, cs, x, y = lrqap_design(fx)
    fit = logistic_fit(x, y)
    if fit is None:
        return None
    beta, se, ll = fit
    z = beta / se
    p = x.shape[1]
    dev = -2.0 * ll
    ybar = y.mean()
    null_dev = -2.0 * float(np.sum(y * np.log(ybar) + (1 - y) * np.log(1 - ybar)))
    return [tuple(beta), tuple(se), tuple(z),
            (dev, dev + 2 * p, dev + p * np.log(len(y))), (null_dev,)]


def tail_counts(stats, observed):
    le = ge = ab = valid = 0
    tol = TIE_EPS * max(1.0, abs(observed))
    for s in stats:
        if s != s:
            continue
        valid += 1
        le += s <= observed + tol
        ge += s >= observed - tol
        ab += abs(s) >= abs(observed) - tol
    return le, ge, ab, valid


def lr_qap_exact(fx, method):
    a, cs, x, y = lrqap_design(fx)
    n = fx.n
    fit = logistic_fit(x, y)
    if fit is None:
        return None
    observed = fit[0] / fit[1]
    k = x.shape[1]
    draws = [[] for _ in range(k)]
    if method == "y":
        for perm in itertools.permutations(range(n)):
            yp = np.array([read(a, perm[r], perm[c], fx.directed) for r, c in cs], dtype=float)
            f = logistic_fit(x, yp)
            for col in range(k):
                draws[col].append(NAN if f is None else f[0][col] / f[1][col])
    else:
        for col in range(k):
            others = np.delete(x, col, axis=1)
            res = ols_residuals(others, x[:, col])
            rm = [[NAN] * n for _ in range(n)]
            for (r, c), v in zip(cs, res):
                rm[r][c] = v
            for perm in itertools.permutations(range(n)):
                xp = np.array([read(rm, perm[r], perm[c], fx.directed) for r, c in cs])
                f = logistic_fit(np.column_stack([others, xp]), y)
                draws[col].append(NAN if f is None else f[0][-1] / f[1][-1])
    out = []
    counts = [tail_counts(draws[col], observed[col]) for col in range(k)]
    for idx in range(3):
        out.append(tuple(c[idx] / c[3] if c[3] else NAN for c in counts))
    return out


# ---- network autocorrelation ----------------------------------------------

def distances(fx, neighborhood):
    """dist[i][j]: geodesic distance from i to j along the ties the
    neighbourhood type reads (None when unreachable)."""
    n = fx.n
    a = simple_adjacency(fx)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if neighborhood == "out":
                t = a[i][j]
            elif neighborhood == "in":
                t = a[j][i]
            else:
                t = a[i][j] or a[j][i]
            if t:
                adj[i].append(j)
    dist = []
    for s in range(n):
        d = [None] * n
        d[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] is None:
                    d[v] = d[u] + 1
                    q.append(v)
        dist.append(d)
    return dist


def autocorrelation(dist, y, kind, lag):
    n = len(y)
    mean = Fraction(sum(y), n)
    z = [Fraction(v) - mean for v in y]
    zz = sum(v * v for v in z)
    pairs = [(i, j) for i in range(n) for j in range(n) if dist[i][j] == lag]
    s0 = len(pairs)
    if s0 == 0:
        return None
    if kind == "geary":
        if zz == 0:
            return None
        num = sum((Fraction(y[i]) - y[j]) ** 2 for i, j in pairs)
        return Fraction(n - 1, 2 * s0) * num / zz
    cross = sum(z[i] * z[j] for i, j in pairs)
    if kind == "covariance":
        return cross / s0
    if zz == 0:
        return None
    if kind == "correlation":
        return Fraction(1) if lag == 0 else (cross / s0) / (zz / (n - 1))
    return Fraction(n, s0) * cross / zz


def nacf(fx, e):
    if fx.n == 0:
        return None
    dist = distances(fx, e.get("neighborhood", "out"))
    y = num7(fx.n)
    out = []
    for lag in range(e.get("lag_max", 3) + 1):
        v = autocorrelation(dist, y, e["kind"], lag)
        out.append(NAN if v is None else float(v))
    return out


def nacf_exact(fx, e):
    dist = distances(fx, e.get("neighborhood", "out"))
    y = num7(fx.n)
    out = []
    for lag in range(e.get("lag_max", 3) + 1):
        observed = autocorrelation(dist, y, e["kind"], lag)
        le = ge = valid = 0
        for perm in itertools.permutations(range(fx.n)):
            v = autocorrelation(dist, [y[p] for p in perm], e["kind"], lag)
            if v is None or observed is None:
                continue
            valid += 1
            le += v <= observed
            ge += v >= observed
        out.append((le / valid, ge / valid) if valid else (NAN, NAN))
    return out


# ---- network autocorrelation models ---------------------------------------

def weight_matrix(fx, weighted):
    n = fx.n
    w = np.zeros((n, n))
    weights = fx.weights or [1.0] * len(fx.src)
    for u, v, x in zip(fx.src, fx.tgt, weights):
        if u == v:
            continue
        if weighted:
            w[u, v] += x
            if not fx.directed:
                w[v, u] += x
        else:
            w[u, v] = 1.0
            if not fx.directed:
                w[v, u] = 1.0
    sums = w.sum(axis=1)
    nz = sums != 0
    w[nz] = w[nz] / sums[nz, None]
    return w


def lnam_profile(w, y, x, model, rho):
    """(log-likelihood, beta, sigma) maximized over beta and sigma at rho."""
    n = len(y)
    a = np.eye(n) - rho * w
    sign, logdet = np.linalg.slogdet(a)
    if sign <= 0:
        return -np.inf, None, None
    ty = a @ y
    tx = x if model == "lag" else a @ x
    beta, *_ = np.linalg.lstsq(tx, ty, rcond=None)
    r = ty - tx @ beta
    var = float(r @ r) / n
    if var <= 0:
        return -np.inf, None, None
    return -0.5 * n * (np.log(2 * np.pi * var) + 1) + logdet, beta, np.sqrt(var)


def lnam(fx, e):
    from scipy.optimize import minimize_scalar
    n = fx.n
    w = weight_matrix(fx, bool(e.get("weighted", False)))
    y = np.array(num7(n), dtype=float)
    x = np.column_stack([np.ones(n), [(3 * v) % 5 for v in range(n)]])
    model = e.get("model", "lag")
    # rho in (-1 / r, 1 / r), r the largest absolute row sum of W (it bounds
    # the spectral radius, so I - rho W is non-singular there).
    r = float(np.abs(w).sum(axis=1).max()) if n else 0.0
    hi = 1.0 / r if r > 0 else 1.0
    lo = -hi
    grid = np.linspace(lo, hi, 2001)[1:-1]
    vals = [lnam_profile(w, y, x, model, r)[0] for r in grid]
    k = int(np.argmax(vals))
    a = grid[k - 1] if k > 0 else lo
    b = grid[k + 1] if k + 1 < len(grid) else hi
    res = minimize_scalar(lambda r: -lnam_profile(w, y, x, model, r)[0], bounds=(a, b),
                          method="bounded", options={"xatol": 1e-12, "maxiter": 500})
    rho = float(res.x)
    ll, beta, sigma = lnam_profile(w, y, x, model, rho)
    return [tuple(float(b) for b in beta), (rho, sigma, ll)]


def compute(fx, e: dict):
    fn = e["fn"]
    if fn == "lr_qap":
        if fx.n < 2:
            return None
        if e.get("exhaustive"):
            if fx.n > MAX_EXACT:
                return None
            return lr_qap_exact(fx, e.get("method", "dsp"))
        fit = lr_qap_fit(fx)
        if fit is None:
            return None
        return fit[4:] if e.get("part") == "null_deviance" else fit[:4]
    if fn == "network_autocorrelation_model":
        return lnam(fx, e)
    if fn == "network_autocorrelation":
        if e.get("exhaustive"):
            return nacf_exact(fx, e) if fx.n <= MAX_EXACT else None
        return nacf(fx, e)
    return None


def main() -> None:
    spec = load_area("inference")
    signal.signal(signal.SIGALRM, _alarm)
    count = 0
    for fixture in fixture_names():
        fx = load_fixture(fixture)
        if fx.n > MAX_NODES:
            continue
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            o = v["oracles"][ORACLE]
            if fixture in o.get("undefined_on", []) or ("only_on" in o and fixture not in o["only_on"]):
                continue
            signal.alarm(TIME_LIMIT)
            try:
                with np.errstate(all="ignore"):
                    values = compute(fx, v["params"])
            except TimeLimit:
                print(f"  {variant} on {fixture}: over {TIME_LIMIT} s, skipped")
                values = None
            finally:
                signal.alarm(0)
            if values is None:
                continue
            write_values(ORACLE, fixture, variant, values)
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (inference): wrote {count} golden files")


if __name__ == "__main__":
    main()
