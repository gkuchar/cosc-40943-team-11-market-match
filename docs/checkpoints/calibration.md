# Checkpoint 3 calibration

As of 2026-11-16. Only `UC-BRND-generate-api-key` has recorded implementation evidence in [traceability](../traceability.md). Other finished use cases must be added when their implementation evidence is identified.

| Use case | Person | Coarse estimate range (hours) | Refined estimate range (hours) | Actual WAR hours since each estimate | Actual / coarse midpoint | Actual / refined midpoint | Biggest miss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `UC-BRND-generate-api-key` | Contributor names not supplied; one row per contributor required | Not supplied | Not supplied | Not supplied | Unavailable | Unavailable | Needs contributor explanation from actual work |
| `UC-BRND-generate-api-key` | Team total | Not supplied | Not supplied | Not supplied | Unavailable | Unavailable | Cannot determine without estimates and WAR lines |

Do not replace missing hours with zero. Actual hours come from WAR lines tagged with the use case ID, logged since the relevant estimate. For each estimate, midpoint = (low + high) / 2; ratio = actual / midpoint. Compute the team ratio as summed actual hours / summed estimate midpoints for matching work, rather than averaging individual ratios. Preserve distinct start dates for coarse and refined estimates.

**Forecast:** unavailable. Required hours = sum of unfinished `v1.0.0` estimate midpoints × team calibration ratio; available hours = sum of members' realistically available hours before the agreed MVP demo. Neither the release assignments, estimates, actuals, demo date, nor remaining capacity is complete in the repository. A fit/no-fit claim would invent evidence. Record the numerical comparison here once supplied; if it does not fit, agree scope changes with the client and update Release cells through a PR.
