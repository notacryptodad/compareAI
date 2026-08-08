#!/usr/bin/env bash
# Cloudflare Pages build command. Set in the Pages project as:
#   Build command:       ./build.sh
#   Build output dir:    dist
# CF's image has python3+pip; we install pyyaml, gate on validate, then assemble dist/.
set -euo pipefail

python3 -m pip install --quiet pyyaml

echo "== validate (deploy gate) =="
# Staleness must not fail the public build (data ages between edits); schema/bucket/
# stage-claim errors MUST. --expire-days huge disables the hard staleness abort here;
# GitHub Actions keeps the strict 180-day check as the PR gate.
python3 scripts/validate.py --expire-days 100000

echo "== build data + viewer =="
python3 scripts/build_data.py

echo "== dist ==" && ls -la dist/
