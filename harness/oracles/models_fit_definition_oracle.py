# oracle-entries: definition
"""Golden values for fitting and sampling stochastic block models and latent
space models (manifest/models_fit.yaml), from the definitions.

Deterministic fits are checked against exhaustive search and the defining
formulas; samplers against the exact distribution they target, found by
enumeration or quadrature. Nothing here shares code with the engine.

Stochastic block models (Peixoto 2017), on fixtures of 2 to 8 nodes with
edges:
  sbm_fit_optimum     the least description length over every partition of
                      the nodes (restricted growth strings; the formulas of
                      sbm_definition_oracle.py)
  sbm_*posterior      the exact posterior P(b) proportional to
                      exp(-beta Sigma(b)) over those partitions: the
                      probability that nodes i and j share a block (i < j,
                      row-major), then the probability of b blocks, b = 1..n
  *_check             a vector of ones: the property checks run in the
                      binding (bindings/models_fit.py), which evaluates the
                      engine's output with this oracle's formulas

Latent space models (Hoff, Raftery and Handcock 2002): see the functions
below the block model part.

    python3 oracles/models_fit_definition_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)
import sbm_definition_oracle as sbm  # noqa: E402

ORACLE = "definition"
CHECK_LENGTHS = {"sbm_fit_check": 6, "sbm_sample_check": 3, "latent_fit_check": 6,
                 "latent_sample_check": 5}


def small(fx):
    """Fixtures the enumerations cover: 2 to 8 nodes and at least one edge."""
    return 2 <= fx.n <= 8 and len(fx.src) > 0


def partitions(n):
    """Every partition of 0..n-1 as a restricted growth string."""
    out = []

    def rec(cur, top):
        if len(cur) == n:
            out.append(tuple(cur))
            return
        for label in range(top + 2):
            cur.append(label)
            rec(cur, max(top, label))
            cur.pop()
    rec([0], 0)
    return out


_cache = {}


def lengths(fx, dc):
    key = (fx.name, dc)
    if key not in _cache:
        parts = partitions(fx.n)
        _cache[key] = (parts, np.array([sbm.description_length(fx, list(p), dc)[0]
                                        for p in parts]))
    return _cache[key]


def posterior(fx, dc, beta):
    parts, sigma = lengths(fx, dc)
    w = np.exp(-beta * (sigma - sigma.min()))
    w /= w.sum()
    n = fx.n
    co = np.zeros((n, n))
    blocks = np.zeros(n + 1)
    for p, wi in zip(parts, w):
        a = np.array(p)
        co += wi * (a[:, None] == a[None, :])
        blocks[a.max() + 1] += wi
    iu = np.triu_indices(n, 1)
    return [float(x) for x in co[iu]] + [float(x) for x in blocks[1:]]


def latent_posterior(fx, dim, sd):
    """The posterior of the two-node network under the sampler's priors
    (independent N(0, sd[2]^2) coordinates, N(0, sd[3]^2) intercept), by
    quadrature. Only the distance D of the nodes enters the likelihood, and
    under the prior the difference of the two positions is N(0, 2 sd[2]^2 I),
    so D has density proportional to D^(dim-1) exp(-D^2 / (4 sd[2]^2));
    the likelihood sums over the ordered pairs (directed) or the one pair.
    Returns the mean and standard deviation of alpha, then of the
    log-likelihood."""
    s, sa = sd[2], sd[3]
    ties = sum(1 for a, b in zip(fx.src, fx.tgt) if a != b)
    pairs = 2 if fx.directed else 1
    grid_d = np.linspace(0.0, 14.0 * s, 4001)
    grid_a = np.linspace(-8.0 * sa, 8.0 * sa, 4001)
    dm, am = np.meshgrid(grid_d, grid_a, indexing="ij")
    eta = am - dm
    ll = ties * eta - pairs * np.logaddexp(0.0, eta)
    prior_d = grid_d ** (dim - 1) * np.exp(-grid_d ** 2 / (4.0 * s * s))
    w = prior_d[:, None] * np.exp(-grid_a ** 2 / (2.0 * sa * sa))[None, :] * np.exp(ll)
    w /= w.sum()
    ea, el = (w * am).sum(), (w * ll).sum()
    return [float(ea), float(el), float(np.sqrt((w * am ** 2).sum() - ea ** 2)),
            float(np.sqrt((w * ll ** 2).sum() - el ** 2))]


def compute(fx, spec):
    fn = spec["fn"]
    dc = bool(spec.get("degree_corrected", False))
    if fn in CHECK_LENGTHS:
        return [1] * CHECK_LENGTHS[fn]
    if fn == "sbm_fit":
        return [float(lengths(fx, dc)[1].min())] if small(fx) else None
    if fn == "sbm_sample_posterior":
        return posterior(fx, dc, float(spec.get("beta", 1.0))) if small(fx) else None
    if fn == "latent_sample_posterior":
        return latent_posterior(fx, spec.get("dim", 1), spec["sd"]) if fx.n == 2 else None
    return None


def main() -> None:
    spec = load_area("models_fit")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            values = compute(fx, v["params"])
            if values is None:
                continue
            write_values(ORACLE, name, variant, values)
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (models fit): wrote {count} golden files")


if __name__ == "__main__":
    main()
