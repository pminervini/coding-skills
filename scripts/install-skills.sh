#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/skills"
TARGET_DIR="${1:-$HOME/.claude/skills}"

if [ ! -d "$SKILLS_DIR" ]; then
  echo "Error: skills directory not found at $SKILLS_DIR" >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"

count=0
for d in "$SKILLS_DIR"/*; do
  [ -d "$d" ] || continue
  name="$(basename "$d")"
  ln -sfn "$d" "$TARGET_DIR/$name"
  count=$((count + 1))
  echo "Linked: $TARGET_DIR/$name -> $d"
done

echo "Installed $count skill link(s) into $TARGET_DIR"
