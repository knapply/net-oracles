#!/usr/bin/env python3
# oracle-env: powerlaw
"""Golden values from the powerlaw package (Alstott, Bullmore, and Plenz
2014) for power-law fits of degree distributions: the exponent, the
Kolmogorov-Smirnov distance and the cut-off. Inputs and encodings:
../bindings/graph_theory.py. The package is run as a black box with the exact
discrete maximum likelihood (`estimate_discrete=False`), not its
closed-form approximation.

    ~/oracle-envs/powerlaw/bin/python oracles/graph_theory_powerlaw_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import numpy as np
    import powerlaw
except ImportError:  # the tool is not installed here
    print("powerlaw is not installed")
    sys.exit(3)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture, write_values,  # noqa: E402
                    write_version)

ORACLE = "powerlaw"
AREA = "graph_theory"


def degrees(fx):
    d = [0] * fx.n
    for a, b in zip(fx.src, fx.tgt):
        d[a] += 1
        d[b] += 1
    return d


def fit(fx, xmin, discrete):
    positive = [x for x in degrees(fx) if x >= 1]
    if len({x for x in positive if x >= max(xmin or 1, 1)}) < 2:
        return None
    kwargs = {"discrete": discrete, "verbose": False}
    if discrete:
        kwargs["estimate_discrete"] = False
    if xmin:
        kwargs["xmin"] = xmin
    return powerlaw.Fit(np.array(positive, dtype=float), **kwargs)


ATTRIBUTE = {"gt_plfit_alpha": "alpha", "gt_plfit_alpha_continuous": "alpha",
             "gt_plfit_distance": "D", "gt_plfit_xmin_bounded": "xmin"}


def main() -> None:
    spec = load_area(AREA)
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            e = v["params"]
            xmin = float(e["xmin"]) if e.get("xmin") else None
            result = fit(fx, xmin, e.get("discrete", True))
            if result is None:
                values = [-1]
            else:
                attribute = ATTRIBUTE[variant]
                try:
                    getattr(result.power_law, "alpha")
                except ValueError:
                    # The tool finds no data in the fitted range (its own
                    # xmin search leaves nothing above xmin): no value here.
                    continue
                # Fitted parameters live on the power_law distribution; xmin
                # (and, in older releases, alpha) on the fit itself.
                if attribute == "D" or hasattr(result.power_law, attribute):
                    value = getattr(result.power_law, attribute)
                else:
                    value = getattr(result, attribute)
                values = [float(value)]
            write_values(ORACLE, name, variant, values)
            count += 1
    print(f"powerlaw {powerlaw.__version__} ({AREA}): wrote {count} golden files")
    write_version(ORACLE, f"powerlaw {powerlaw.__version__}")


if __name__ == "__main__":
    main()
