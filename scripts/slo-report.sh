#!/usr/bin/env bash
# Current value of AVL-category-list (SRS §9.5): good probes / all probes over the last
# 28 days, from the scheduled runs of .github/workflows/slo-probe.yml. Manual runs are
# left out, so a probe pointed at another URL to show it can fail never counts.
# Needs the GitHub CLI, signed in. Usage: scripts/slo-report.sh
set -euo pipefail

gh run list --repo gkuchar/cosc-40943-team-11-market-match --workflow slo-probe.yml \
  --event schedule --limit 10000 --json conclusion,createdAt |
  jq -r '
    (now - 28*24*3600) as $since
    | map(select((.createdAt | fromdateiso8601) >= $since and (.conclusion == "success" or .conclusion == "failure")))
    | (map(select(.conclusion == "success")) | length) as $good
    | length as $all
    | if $all == 0 then "No completed scheduled probes in the last 28 days."
      else
        "Probes in the last 28 days: \($all) (first \(map(.createdAt) | min), last \(map(.createdAt) | max))\n"
        + "Good: \($good)  Bad: \($all - $good)\n"
        + "SLI: \(($good / $all * 10000 | round) / 100)% against a 99% target\n"
        + "Error budget used: \($all - $good) of 80 bad probes (1% of the 8,064 probes in a full 28-day window)"
      end'
