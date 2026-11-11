#!/usr/bin/env python3
"""NetworkX (https://networkx.org), pure Python, one thread."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# An adapter named like its tool (networkx.py) must not shadow the tool itself.
sys.path[:] = [p for p in sys.path if os.path.abspath(p or ".") != HERE]
sys.path.insert(0, os.path.join(HERE, ".."))
from common import main  # noqa: E402
from nxbase import NetworkXBase  # noqa: E402


class Networkx(NetworkXBase):
    tool = "networkx"
    backend = None


if __name__ == "__main__":
    main(Networkx)
