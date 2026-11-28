#!/usr/bin/env bash
# Downloads the pinned JGraphT jars (core and io, with the ANTLR runtime the io
# module needs) from Maven Central into $1 (default $ORACLE_ENV/jars) and prints
# the classpath.
set -euo pipefail
D="${1:-${ORACLE_ENV:-$HOME/.cache/oracle-env}/jars}"; mkdir -p "$D"
M=https://repo1.maven.org/maven2
for j in org/jgrapht/jgrapht-core/1.5.2/jgrapht-core-1.5.2 org/jgrapht/jgrapht-io/1.5.2/jgrapht-io-1.5.2 \
         org/jheaps/jheaps/0.14/jheaps-0.14 org/apfloat/apfloat/1.10.1/apfloat-1.10.1 \
         org/antlr/antlr4-runtime/4.12.0/antlr4-runtime-4.12.0; do
  f="$D/$(basename $j).jar"
  for try in 1 2 3 4; do
    [ -s "$f" ] && break
    curl -fsSL --max-time 120 "$M/$j.jar" -o "$f" || sleep 5
  done
  [ -s "$f" ]
done
echo "$D/jgrapht-core-1.5.2.jar:$D/jgrapht-io-1.5.2.jar:$D/jheaps-0.14.jar:$D/apfloat-1.10.1.jar:$D/antlr4-runtime-4.12.0.jar"
