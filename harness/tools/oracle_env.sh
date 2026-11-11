#!/usr/bin/env bash
# Bootstraps the system-tool oracles (JVM, Boost, LEMON, nauty, Octave) in a
# private conda-forge prefix under $ORACLE_ENV (default ~/.cache/oracle-env)
# using micromamba. Nothing is installed system-wide and no root is needed,
# so it works inside the locked-down runner containers. Usage:
#
#     source tools/oracle_env.sh [pkg ...]     # puts the prefix on PATH
#
# Default packages: openjdk, libboost-devel, nauty, octave, cmake, make, gxx.
set -euo pipefail
ORACLE_ENV="${ORACLE_ENV:-$HOME/.cache/oracle-env}"
MM="${MM:-$HOME/.cache/micromamba}"
PKGS=("$@")
[ ${#PKGS[@]} -gt 0 ] || PKGS=(openjdk libboost-devel nauty octave cmake make gxx_linux-64)
mkdir -p "$HOME/.cache"
# One bootstrap at a time: oracle scripts run in parallel.
(
  flock 9
  if [ ! -x "$MM" ]; then
    mkdir -p "$(dirname "$MM")"
    curl -fsSL https://github.com/mamba-org/micromamba-releases/releases/latest/download/micromamba-linux-64 -o "$MM"
    chmod +x "$MM"
  fi
  if [ ! -d "$ORACLE_ENV/conda-meta" ]; then
    MAMBA_ROOT_PREFIX="$HOME/.cache/mamba-root" "$MM" create -y -q -p "$ORACLE_ENV" -c conda-forge "${PKGS[@]}"
  fi
) 9>"$HOME/.cache/oracle-env.lock"
export PATH="$ORACLE_ENV/bin:$PATH"
export ORACLE_ENV
