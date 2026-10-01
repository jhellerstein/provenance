#!/usr/bin/env bash
# Build a determination-provenance paper variant with the bundled tectonic.
#
# Usage:
#   ./build.sh [main.tex]        # defaults to main.tex
#
# The repository ships a tectonic binary and font/package cache under
# ../complexity/.infinity/tex. In sandboxed/offline environments the cache
# directory may be read-only; this script therefore redirects the tectonic
# cache, XDG cache, and HOME to writable scratch locations and builds in a
# scratch copy, then copies the resulting PDF back next to the source.
set -euo pipefail

SRC="${1:-main.tex}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEC="$HERE/../complexity/.infinity/tex/tectonic"

if [[ ! -x "$TEC" ]]; then
  echo "tectonic not found at $TEC" >&2
  exit 1
fi

# Persist the download caches across runs; use a unique build dir per run so
# concurrent builds never clobber one another.
SCRATCH="${DET_SCRATCH:-${TMPDIR:-/tmp}/det-tex-scratch}"
export TECTONIC_CACHE_DIR="$SCRATCH/teccache"
export XDG_CACHE_HOME="$SCRATCH/xdg"
export HOME="$SCRATCH/home"
mkdir -p "$TECTONIC_CACHE_DIR" "$XDG_CACHE_HOME/fontconfig" "$HOME"

BUILD="$(mktemp -d "$SCRATCH/build.XXXXXX")"
trap 'rm -rf "$BUILD"' EXIT
# Copy all .tex, .sty, and the bib so modular \input / \usepackage resolve.
cp "$HERE"/*.tex "$BUILD"/ 2>/dev/null || true
cp "$HERE"/*.sty "$BUILD"/ 2>/dev/null || true
cp "$HERE"/*.bib "$BUILD"/ 2>/dev/null || true

( cd "$BUILD" && "$TEC" -X compile --keep-logs --keep-intermediates --outfmt pdf "$SRC" )

PDF="${SRC%.tex}.pdf"
LOG="${SRC%.tex}.log"
# Copy the PDF next to the source when that directory is writable; otherwise
# leave it in the scratch build dir and report its location.
if cp "$BUILD/$PDF" "$HERE/$PDF" 2>/dev/null; then
  echo "Wrote $HERE/$PDF"
else
  echo "Working dir read-only; PDF left at $BUILD/$PDF"
fi
# Report page count and any undefined references (never fail on no match).
( grep -aoE '\([0-9]+ pages?' "$BUILD/$LOG" | tail -1 ) || true
( grep -aiE 'undefined|multiply defined' "$BUILD/$LOG" | head -5 ) || true
