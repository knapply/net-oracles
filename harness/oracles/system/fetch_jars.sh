#!/usr/bin/env bash
# Downloads the pinned JGraphT jars from Maven Central into $1 (default
# $ORACLE_ENV/jars) and prints the classpath.
set -euo pipefail
D="${1:-${ORACLE_ENV:-$HOME/.cache/oracle-env}/jars}"; mkdir -p "$D"
M=https://repo1.maven.org/maven2
for j in org/jgrapht/jgrapht-core/1.5.2/jgrapht-core-1.5.2 org/jheaps/jheaps/0.14/jheaps-0.14 org/apfloat/apfloat/1.10.1/apfloat-1.10.1; do
  f="$D/$(basename $j).jar"; [ -s "$f" ] || curl -fsSL "$M/$j.jar" -o "$f"
done
echo "$D/jgrapht-core-1.5.2.jar:$D/jheaps-0.14.jar:$D/apfloat-1.10.1.jar"
