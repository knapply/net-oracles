#!/usr/bin/env bash
# Downloads the pinned gephi-toolkit jar (all dependencies bundled) from Maven
# Central into $1 (default $ORACLE_ENV/jars), checks its SHA-256 against the
# digest published next to it, and prints the jar path. Only the binary jar is
# fetched; the source archive is never downloaded.
set -euo pipefail
V=0.11.3
D="${1:-${ORACLE_ENV:-$HOME/.cache/oracle-env}/jars}"; mkdir -p "$D"
U=https://repo1.maven.org/maven2/org/gephi/gephi-toolkit/$V/gephi-toolkit-$V-all.jar
f="$D/gephi-toolkit-$V-all.jar"
if [ ! -s "$f" ]; then
  curl -fsSL "$U" -o "$f.part"
  want=$(curl -fsSL "$U.sha256" | cut -d' ' -f1)
  have=$(sha256sum "$f.part" | cut -d' ' -f1)
  [ "$want" = "$have" ] || { echo "gephi-toolkit checksum mismatch" >&2; rm -f "$f.part"; exit 1; }
  mv "$f.part" "$f"
fi
echo "$f"
