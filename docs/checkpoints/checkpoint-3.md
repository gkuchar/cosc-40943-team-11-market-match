# Checkpoint 3 evidence

Evidence audit: 2026-11-16. Deadline: Thursday Nov 19, 11:59 PM; demo: Friday Nov 20. [Course checklist](https://washingtonwei.github.io/cosc-40943/project/#checkpoint-3-checklist).

Application changes: [draft MM-Version PR #47](https://github.com/Market-Match/MM-Version/pull/47), commit `120973d7dfdf425ca435a4184687b707325acf03` on `codex/checkpoint-3`. This PR is not merged, tagged, or deployed.

| Item | Evidence | Status / remaining work |
| --- | --- | --- |
| Release | [Draft notes and release procedure](release-v0.2.0.md) | No `v0.2.0` tag created or deployment performed in this work. Gate and review remain. |
| Fan-out / traceability | [Matrix](../traceability.md); run `python scripts/check-traceability.py` | All 25 defined UC/FRs have rows; 23 local matrix/checkpoint links resolve. One recorded built use case, not several. 24 release assignments need a team decision; the audit exits 1 until assigned. Deferred flows keep API Key generation Partial. |
| Pipeline | [Existing workflow](https://github.com/Market-Match/MM-Version/blob/e6b49ca/.github/workflows/pull-request.yml); [architecture §8.2.11](../design/architectural-design.md#8211-static-analysis) | Existing analyzer failures and unenforced required checks are `TD-analyzer-findings` and `TD-gate-scope` in architecture §11. A successful build does not pass the gate. |
| Observability | [`/api/health` proposal in PR #47](https://github.com/Market-Match/MM-Version/pull/47) | Local test checks D1 success → 200, failure → 503, and `Cache-Control: no-store`. Platform log-stream evidence, deployed health check, and operational metrics still needed. Dashboard analytics are not service-health metrics. |
| Calibration / forecast | [Calibration](calibration.md) | Needs real estimates, WAR actuals, contributor names, remaining capacity, and agreed release assignments. |
| Charter rule from review | [AGENTS.md](../../AGENTS.md); [source review comment](https://github.com/gkuchar/cosc-40943-team-11-market-match/pull/35#discussion_r4566516549) | Rule prepared: field requiredness needs specification evidence. A teammate must review and merge its PR; this agent must not merge PRs. |
| Measured SLO | [SRS §9.2](../requirements/software-requirements-specification.md#92-performance) `PER-import-results` | SLI/window/target/error budget defined from the existing requirement. Current measured value unavailable: required product import flow is not implemented/traced. |
| Degradation test | [Committed regression suite](https://github.com/Market-Match/MM-Version/blob/120973d7dfdf425ca435a4184687b707325acf03/worker/test/checkpoint-3.test.mjs); [BRND test list](../design/brnd.md#tests) PRE-2, WorkOS fails | Passed locally on Node 24.11.1: WorkOS membership request throws → 502, fixed error body, and no API Key storage access. Mutation bypassing the failure decision → test fails (500 instead of 502). No application failure hook added. |

## Local test evidence

`npm run test:worker`: 2 tests passed (WorkOS outage; D1 readiness). Uses Node's built-in runner and the already-installed TypeScript compiler; adds no package dependency. WorkOS and D1 are test doubles, so this is not deployed availability, a real D1 integration check, or a measurement of `PER-import-results`.

To reproduce red in PowerShell, set `$env:CHECKPOINT_MUTATION = 'workos-fail-open'`, run `node --test --test-name-pattern='WorkOS membership' worker/test/checkpoint-3.test.mjs`, then remove that environment variable. The loader changes the failure decision in memory only. The test fails; with the variable removed, `npm run test:worker` passes. The CLI exit code and failing assertion are the evidence, not the shell cleanup command's exit code.

## Analyzer gate results

Run against existing application branch `codex/checkpoint-3`, based on staging `e6b49ca`. No check, rule, or finding was suppressed. Logs were captured locally under the operating system's temporary directory, `market-match-checkpoint3-gate`.

| Check | Result |
| --- | --- |
| Build | Pass |
| Frontend TypeScript | Fail: 19 errors |
| Worker TypeScript | Fail: 17 errors after installing the existing locked Worker dependencies; initial attempt lacked Cloudflare types |
| Frontend ESLint | Fail: 650 errors, 6 warnings |
| Worker ESLint | Fail: 66 errors |
| Frontend Prettier | Fail: 60 files in this Windows checkout |
| Worker Prettier | Fail: 4 unchanged source files after formatting the touched route and test |
| SQLFluff | Not run successfully: `sqlfluff` is not installed locally |

These are blockers, not a baseline or permission to merge red. Existing architecture §11 records the type/lint debt; local formatting results are checkout-specific and do not replace CI evidence. The full application cleanup is not completed by adding two passing regression tests.

## Slack message draft — not sent

Checkpoint 3 evidence: [release](release-v0.2.0.md), [traceability](../traceability.md), [pipeline and debt](../design/architectural-design.md#8211-static-analysis), [observability and test results](#local-test-evidence), [calibration and forecast](calibration.md), [review-derived charter rule](../../AGENTS.md), [SLO](../requirements/software-requirements-specification.md#92-performance), [degradation test evidence](#local-test-evidence). Open blockers are listed above. Replace relative links with GitHub links at the reviewed commit before posting; include the application release and test PR links. A team member posts the single message by the deadline.
