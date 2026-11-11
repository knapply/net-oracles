# oracle-entries: definition
"""Golden values for the latent space model of Hoff, Raftery, and Handcock
(2002), computed directly from the definition.

Every fixture is read as its simple graph (loops dropped, repeated edges
once, weights ignored) with the positions of derived/models.py.
The oracle forms the dense matrices of distances D_ij = |z_i - z_j| and
eta = alpha - D and evaluates

  l = sum over pairs of y_ij eta_ij - ln(1 + exp(eta_ij))

over i < j (undirected) or all i != j (directed), d l / d alpha = sum
(y_ij - p_ij), and d l / d z_i = -sum_j w_ij (z_i - z_j) / D_ij with w_ij =
y_ij - p_ij (+ y_ji - p_ji when directed), by numpy array operations. The
move-delta variants evaluate l before and after moving node 0 from
scratch and subtract, and recompute the gradient after the move; the
engine updates them in O(n d) from the pairs of node 0 only.

    python3 oracles/latent_definition_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)
from derived.models import move_to, positions  # noqa: E402

ORACLE = "definition"


def evaluate(fx, z, alpha):
    n = fx.n
    Y = np.zeros((n, n))
    for s, t in zip(fx.src, fx.tgt):
        if s != t:
            Y[s, t] = 1
            if not fx.directed:
                Y[t, s] = 1
    diff = z[:, None, :] - z[None, :, :]
    D = np.sqrt((diff ** 2).sum(axis=2))
    eta = alpha - D
    P = 1 / (1 + np.exp(-eta))
    L = Y * eta - np.logaddexp(0, eta)
    off = ~np.eye(n, dtype=bool)
    mask = off if fx.directed else np.triu(off)
    ll = L[mask].sum()
    R = (Y - P) * off
    ga = R[mask].sum()
    W = R + R.T if fx.directed else R
    with np.errstate(divide="ignore", invalid="ignore"):
        K = np.where(D > 0, W / D, 0.0)
    grad = -(K[:, :, None] * diff).sum(axis=1)
    return ll, ga, grad


def compute(fx, spec):
    n, dim, alpha = fx.n, spec.get("dim", 2), float(spec["alpha"])
    z = np.array(positions(n, dim), dtype=float).reshape(n, dim)
    ll, ga, grad = evaluate(fx, z, alpha)
    if spec["fn"] == "latent_loglik":
        return [ll, ga] + list(grad.reshape(-1))
    z2 = z.copy()
    z2[0] = move_to(dim)
    ll2, _, grad2 = evaluate(fx, z2, alpha)
    return [ll2 - ll] + list(grad2.reshape(-1))


def main() -> None:
    spec = load_area("latent_space")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (latent space): wrote {count} golden files")


if __name__ == "__main__":
    main()
