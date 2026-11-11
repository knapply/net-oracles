#!/usr/bin/env bash
# Builds one isolated Python environment per reference-tool oracle from
# oracles/envs/<name>.txt into $NETORACLES_ORACLE_ENVS/<name>
# (default ~/oracle-envs). An environment is rebuilt only when its
# requirements file changed. A first line "# python: 3.12" picks the
# interpreter (python3.12) when the tool needs a particular version.
#
#   bash tools/oracle_envs.sh              # every environment
#   bash tools/oracle_envs.sh networkit    # only these
#   bash tools/oracle_envs.sh --sync-runner   # copy the requirement files
#                                             # into tools/runner/oracle-envs
#   bash tools/oracle_envs.sh --check-runner  # fail if those copies drifted
set -u
cd "$(dirname "$0")/.."
ENVS=${NETORACLES_ORACLE_ENVS:-$HOME/oracle-envs}
mkdir -p "$ENVS"
names=("$@")
if [ ${#names[@]} -eq 0 ]; then
  for f in oracles/envs/*.txt; do names+=("$(basename "$f" .txt)"); done
fi
status=0
for name in "${names[@]}"; do
  req=oracles/envs/$name.txt
  dir=$ENVS/$name
  sum=$(sha256sum "$req" | cut -d' ' -f1)
  if [ -f "$dir/.requirements.sha256" ] && [ "$(cat "$dir/.requirements.sha256")" = "$sum" ]; then
    continue
  fi
  py=python3
  want=$(sed -n '1s/^# *python: *\([0-9.]*\).*/\1/p' "$req")
  [ -n "$want" ] && command -v "python$want" >/dev/null && py=python$want
  echo "== building $name with $($py --version)"
  rm -rf "$dir"
  if $py -m venv "$dir" && "$dir/bin/pip" install -q --no-cache-dir -r "$req"; then
    echo "$sum" > "$dir/.requirements.sha256"
  else
    echo "   $name: install failed"
    rm -rf "$dir"
    status=1
  fi
done
exit $status
