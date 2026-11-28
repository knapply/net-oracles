"""Shared driver of the io_formats oracle scripts (manifest/io_formats.yaml):
every entry runs on the fixture `pair` only, since the cases are file texts and
do not use the fixture graph."""

from __future__ import annotations

import signal
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)


TIME_LIMIT = 600


def _alarm(signum, frame):
    raise TimeoutError(f"the oracle ran over its hard limit of {TIME_LIMIT} seconds")


def run(oracle: str, compute, version: str) -> None:
    """Writes the golden file of every entry that has an `oracle` block.
    `compute(engine)` returns the values of the entry whose `engine` block is
    given (None to skip an entry). The script has a hard time limit of
    TIME_LIMIT seconds (signal.alarm)."""
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, _alarm)
        signal.alarm(TIME_LIMIT)
    spec = load_area("io_formats")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if oracle not in v["oracles"] or not applies(v, fx):
                continue
            if "only_on" in v["oracles"][oracle] and name not in v["oracles"][oracle]["only_on"]:
                continue
            values = compute(v["params"])
            if values is not None:
                write_values(oracle, name, variant, values)
                count += 1
    write_version(oracle, version)
    print(f"{oracle} (io_formats): wrote {count} golden files")
