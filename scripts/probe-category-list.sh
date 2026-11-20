#!/usr/bin/env bash
# One probe for AVL-category-list (SRS §9.5). Exits 0 for a good event, 1 for a bad one.
# Good means: HTTP 200, a JSON content type, and a body that is a JSON array, within 10 seconds.
# A status check alone would pass on the app's web page, which answers 200 text/html for
# unknown paths such as /api/health, so this also checks the content type and the body.
# Usage: scripts/probe-category-list.sh [url]
set -uo pipefail

url="${1:-https://login.marketmatch.app/api/categories}"
body="$(mktemp)"
trap 'rm -f "$body"' EXIT

if ! meta="$(curl -sS --max-time 10 -o "$body" -w '%{http_code} %{content_type} %{time_total}' "$url")"; then
  echo "BAD $url: no answer within 10 s"
  exit 1
fi
read -r code ctype seconds <<<"$meta"

if [[ "$code" != "200" ]]; then
  echo "BAD $url: HTTP $code ($ctype, ${seconds}s)"
  exit 1
fi
if [[ "$ctype" != application/json* ]]; then
  echo "BAD $url: HTTP 200 but $ctype, not JSON (${seconds}s)"
  exit 1
fi
if ! jq -e 'type == "array"' "$body" >/dev/null 2>&1; then
  echo "BAD $url: HTTP 200 JSON, but the body is not a list (${seconds}s)"
  exit 1
fi
echo "GOOD $url: HTTP 200 $ctype, $(jq length "$body") Categories (${seconds}s)"
