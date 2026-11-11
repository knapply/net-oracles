"""Deterministic inputs for the block model and latent space validation.

The engine runners (validation/bindings/models.py) and the definition
oracles (validation/oracles/sbm_definition_oracle.py and
latent_definition_oracle.py) read every fixture with these rules, so both
evaluate the same partitions and positions:

- the partition into k blocks gives node i the label (7 i + 3) mod k;
- the move-delta variants move node 0 to label (b_0 + 1) mod k, or to the
  fresh label k when k = 1 (a new block);
- coordinate a of node i in d dimensions is
  1.5 sin(0.73 (d i + a)) + 0.2 ((d i + a) mod 3);
- the latent move-delta variants move node 0 to (0.3, -0.2, 0.1, ...)
  (the first d values of 0.3, -0.2, 0.1 repeated).
"""

from __future__ import annotations

import math


def blocks(n: int, k: int) -> list[int]:
    return [(7 * i + 3) % k for i in range(n)]


def move_target(labels: list[int], k: int) -> int:
    return k if k == 1 else (labels[0] + 1) % k


def positions(n: int, dim: int) -> list[list[float]]:
    return [[1.5 * math.sin(0.73 * (dim * i + a)) + 0.2 * ((dim * i + a) % 3)
             for a in range(dim)] for i in range(n)]


def move_to(dim: int) -> list[float]:
    base = [0.3, -0.2, 0.1]
    return [base[a % 3] for a in range(dim)]
