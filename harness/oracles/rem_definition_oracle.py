# oracle-entries: definition
"""Golden values for relational event models, computed directly from the
definitions.

Every fixture is read as the event stream of derived/rem.py. At
every event the oracle rebuilds the whole history from scratch: the count
matrix x (x_ij = weighted number of past events i -> j, with the window or
the decay weight w exp(-(t - t_e) ln 2 / T) ln 2 / T of Brandes, Lerner,
and Snijders 2009), the event counts, and the last event times, using only
events strictly before the event's time. Every statistic is then evaluated
for all ordered pairs at once with dense array formulas, e.g. transitive
closure sum_h min(x_sh, x_hr) as the minimum over an n x n x n array; the
engine instead updates its counters incrementally as each event arrives.

The fit maximizes the Cox partial likelihood of the ordinal model (Butts
2008) by Newton's method with step halving on the dense design (events x
dyads x statistics), with the information matrix inverted by numpy. When
the iteration does not converge in 200 steps or a coefficient passes 1e4
(the estimate does not exist: the likelihood is monotone, and the
iterates keep growing), every value is written as -999, as the engine
runner does.

    python3 oracles/rem_definition_oracle.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)
from derived.rem import event_stream  # noqa: E402

ORACLE = "definition"
UNDEFINED = -999.0


def history(ev, t, spec):
    """Count matrix, event-count matrix, and last-time matrix at time t."""
    s, r, times, w, kind = ev
    n = spec["_n"]
    x = np.zeros((n, n))
    cnt = np.zeros((n, n))
    last = np.full((n, n), -np.inf)
    memory = spec.get("memory", "full")
    param = float(spec.get("param", 0))
    etype = spec.get("event_type")
    for i, j, te, we, ke in zip(s, r, times, w, kind):
        if te >= t:
            break
        if etype is not None and ke != etype:
            continue
        last[i, j] = te
        weight = we if spec.get("weighted") else 1.0
        if memory == "window":
            if te < t - param:
                continue
        elif memory == "decay":
            lam = math.log(2) / param
            weight *= math.exp(-(t - te) * lam) * lam
        x[i, j] += weight
        cnt[i, j] += 1
    return x, cnt, last


def closure(a, b, triad, ca, cb):
    """sum_h f(a[s, h], b[h, r]) for every (s, r)."""
    if triad == "min":
        return np.minimum(a[:, :, None], b[None, :, :]).sum(axis=1)
    if triad == "product":
        return a @ b
    return (ca > 0).astype(float) @ (cb > 0).astype(float)


def recency(last, t):
    return np.where(np.isfinite(last), 1.0 / (1.0 + t - np.where(np.isfinite(last), last, 0)),
                    0.0)


def statistic(name, x, cnt, last, t, triad):
    """n x n matrix of statistic `name` for every dyad (s, r)."""
    n = x.shape[0]
    ones = np.ones(n)
    out_x, in_x = x.sum(axis=1), x.sum(axis=0)
    if name == "inertia":
        return x.copy()
    if name == "reciprocity":
        return x.T.copy()
    if name == "sender_out":
        return np.outer(out_x, ones)
    if name == "sender_in":
        return np.outer(in_x, ones)
    if name == "receiver_out":
        return np.outer(ones, out_x)
    if name == "receiver_in":
        return np.outer(ones, in_x)
    if name == "transitive":
        return closure(x, x, triad, cnt, cnt)
    if name == "cyclic":
        return closure(x, x, triad, cnt, cnt).T
    if name == "shared_out":
        return closure(x, x.T, triad, cnt, cnt.T)
    if name == "shared_in":
        return closure(x.T, x, triad, cnt.T, cnt)
    rec = recency(last, t)
    last_out, last_in = last.max(axis=1), last.max(axis=0)
    if name == "recency_dyad":
        return rec
    if name == "recency_reciprocal":
        return rec.T.copy()
    if name == "recency_sender_out":
        return np.outer(recency(last_out, t), ones)
    if name == "recency_sender_in":
        return np.outer(recency(last_in, t), ones)
    if name == "recency_receiver_out":
        return np.outer(ones, recency(last_out, t))
    if name == "recency_receiver_in":
        return np.outer(ones, recency(last_in, t))
    raise ValueError(f"unknown statistic {name!r}")


def design(fx, spec, stats):
    """Per event: (observed dyad index, events x dyads x p design)."""
    ev = event_stream(fx, ties=spec.get("ties", False))
    spec = dict(spec, _n=fx.n)
    n = fx.n
    off = ~np.eye(n, dtype=bool)
    obs, rows = [], []
    triad = spec.get("triad", "min")
    for k, t in enumerate(ev[2]):
        x, cnt, last = history(ev, t, spec)
        mats = [statistic(name, x, cnt, last, t, triad) for name in stats]
        idx = np.zeros((n, n), dtype=int)
        idx[off] = np.arange(n * (n - 1))
        obs.append(idx[ev[0][k], ev[1][k]])
        rows.append(np.stack([m[off] for m in mats], axis=1))
    return obs, rows


def newton(obs, rows, p):
    beta = np.zeros(p)

    def evaluate(b):
        ll, g, h = 0.0, np.zeros(p), np.zeros((p, p))
        for o, X in zip(obs, rows):
            eta = X @ b
            top = eta.max()
            w = np.exp(eta - top)
            z = w.sum()
            mean = (w[:, None] * X).sum(axis=0) / z
            ll += eta[o] - top - math.log(z)
            g += X[o] - mean
            d = X - mean
            h += (w[:, None] * d).T @ d / z
        return ll, g, h

    ll, g, h = evaluate(beta)
    for _ in range(200):
        try:
            step = np.linalg.solve(h, g)
        except np.linalg.LinAlgError:
            return None
        t = 1.0
        while True:
            nb = beta + t * step
            nll, ng, nh = evaluate(nb)
            if nll >= ll - 1e-12 * (1 + abs(ll)) or t < 1e-12:
                break
            t /= 2
        beta, ll, g, h = nb, nll, ng, nh
        if np.abs(beta).max() > 1e4:
            return None
        if np.abs(t * step).max() < 1e-11 * (1 + np.abs(beta).max()):
            se = np.sqrt(np.diag(np.linalg.inv(h)))
            return list(beta) + list(se)
    return None


def compute(fx, spec):
    if spec["fn"] == "rem_statistic":
        obs, rows = design(fx, spec, [spec["stat"]])
        return [(X[o, 0], X[:, 0].sum(), (X[:, 0] ** 2).sum()) for o, X in zip(obs, rows)]
    stats = spec["stats"]
    obs, rows = design(fx, spec, stats)
    res = newton(obs, rows, len(stats)) if obs else None
    return res if res is not None else [UNDEFINED] * (2 * len(stats))


def main() -> None:
    spec = load_area("rem")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (rem): wrote {count} golden files")


if __name__ == "__main__":
    main()
