# Traceability Matrix

**Project:** Market Match
**Team:** Team 11
**Version:** 0.1
**Last checked:** 2026-10-25, sections 1–3, by Matthew Stafford (agent-assisted)

---

_**How to use this template.** Instructions appear in italic square brackets. Fill in underneath them and leave them in place until the document is stable._

_**What this file is.** The map of your project, from the reason something exists to the thing that does it. Every other document owns its own contents; this one owns the **links between them**, so nobody has to restate anything to find out what connects to what._

_**Why it exists before any code does.** The question it answers in week 4 is "did we specify everything we promised, and nothing we did not?" The question it answers in week 12 is "this broke, what was it supposed to do, and who asked for it?" Those are the same question, and the file that answers the second one is the file you started in week 4. Starting it later means reconstructing links from memory, which is the same work done worse._

_**It grows.** Week 4 fills in the first two tables. Week 8 adds the third, which links each use case to its design, code, and tests and carries your release plan._

_**Run the checks by hand this week.** Each table below ends with two checks. They are cheap, and they fail loudly. Hand the whole file to your agent and ask it to run them, then verify what it tells you, because a check reported as passing by the thing that also wrote the table is not evidence._

---

## 1. Feature to use case area

_[Your vision and scope lists product **features** (`FEAT-<slug>`), each a capability a stakeholder can see. Your use case file groups behavior into **use case areas** (`UC-<AREA>-*`). This table connects them, and it is where **business objectives attach**: the objective hangs on the feature, and every use case underneath inherits it. That is why the objective is named here once, rather than repeated on forty use cases._

_Features and areas are deliberately many-to-many. A feature that lands on exactly one area is probably too narrow, and a feature that reads "create, edit, and delete X" is a list of use cases wearing a feature's clothes._

_A worked example from Project Pulse showed one feature reaching two areas, and an enabling feature marked as serving no objective directly.]_

_[An enabling feature that serves no measurable objective on its own says so. That is different from forgetting to fill the column in.]_

| Feature | Business objectives | Use case areas |
|---|---|---|
| `FEAT-consumer-feedback` | `BO-user-engagement` | `MKT`, `FDBK` |
| `FEAT-product-information` | `BO-user-engagement` | `PROD` |
| `FEAT-product-management` | `BO-product-onboarding` | `BRND` |
| `FEAT-bulk-product-import` | `BO-product-onboarding` | `BRND` |
| `FEAT-market-management` | `BO-user-engagement` | `MKT` |
| `FEAT-feedback-insights` | `BO-feedback-visibility`, `BO-user-engagement` | `FDBK` (capture only; the dashboards that report it have no use cases yet) |
| `FEAT-user-administration` | (enabling, serves no objective directly) | none (out of MVP scope, vision and scope §4.3) |
| `FEAT-api-integration` | `BO-enterprise-expansion` | none (out of MVP scope, vision and scope §4.3) |
| `FEAT-white-label` | `BO-enterprise-expansion` | none (out of MVP scope, vision and scope §4.3) |

`BO-platform-scalability` and `BO-data-privacy` are carried by no single feature. They apply across the whole platform, so they are to be met through the quality attributes in the [software requirements specification](requirements/software-requirements-specification.md) §9 (pending: §9 is not yet written) and measured by `SM-platform-stability` and `SM-data-protection`, not through a feature's use cases.

**Checks.**

1. **Every feature has at least one area.** A feature with none means your vision promises something nobody has specified.
2. **Every area is reached by a feature.** An area no feature points at means you have use cases no stakeholder asked for.

---

## 2. Business rule to what enforces it

_[A business rule is a property of your client's business, so it has no implementation of its own. What it has is a set of requirements that enforce it, and this table is how you find them. Rules are **cited, never restated**: the rule's text lives in `business-rules.md` and nowhere else, and this table holds only the identifier and the links._

_The **Source** column is duplicated here from `business-rules.md` on purpose, and it is the one exception in this file. It is the column reviewers and clients actually read, and a rule whose source is one click away is a rule nobody checks._

_A worked example from Project Pulse named each enforcing use case with the step and extension that carry the rule, and marked a rule with no recorded source as Not recorded.]_

| Business rule | Source | Enforced by |
|---|---|---|
| `BR-sign-in` | Product demo by Demetrie King (date not recorded) | Out of MVP scope (vision and scope §4.3) |
| `BR-rate-product` | Product demo by Demetrie King (date not recorded) | `UC-FDBK-rate-product` step 2 and extension 2a |
| `BR-tap-product` | Market Match website | `UC-PROD-view-product-details` steps 1–2; `UC-FDBK-flip-card` steps 1–3 |
| `BR-select-market` | Market Match website | `UC-MKT-enter-market` steps 2–4 and extension 4a; `UC-FDBK-complete-market` steps 1–2 |
| `BR-earn-entry` | Market Match website | Pending `OI-10` (lottery scope) |
| `BR-entry-expiration` | Market Match website | Pending `OI-10` (lottery scope) |
| `BR-submit-product` | Market Match website | `UC-BRND-create-product` steps 2–5; `UC-BRND-import-products` steps 3–7 |
| `BR-join-market` | Market Match website | Out of MVP scope (vision and scope §4.3) |
| `BR-get-product-feedback` | Market Match website | `UC-FDBK-view-brand-insights` (listed, not yet written) |
| `BR-product-media-limit` | 09-21-2026 client meeting | `UC-BRND-create-product` step 4 and extensions 4b, 4c; `UC-BRND-import-products` step 4; `UC-BRND-send-products` step 3 and extension 3a; `UC-BRND-update-product` step 4 and extension 4a |
| `BR-text-card` | 09-21-2026 client meeting | `UC-BRND-create-product` step 2 and extension 3b; cited by `UC-BRND-import-products`, `UC-BRND-send-products`, and `UC-BRND-update-product` through the same card type field, with no step of their own |
| `BR-approve-product` | 09-21-2026 and 10-21-2026 client meetings | `UC-BRND-create-product` step 5; `UC-BRND-import-products` step 7; `UC-BRND-send-products` step 4; `UC-BRND-update-product` step 5; `UC-BRND-approve-product` steps 5–6 and extension 5a; `FR-PROD-hidden-until-approved` |
| `BR-products-brand-only` | Demetrie King, text message, 10-23-2026 | `UC-BRND-create-product` PRE-1; `UC-BRND-import-products` PRE-1; `UC-BRND-update-product` PRE-1; `UC-BRND-send-products` PRE-1; `UC-BRND-generate-api-key` PRE-1; `FR-PROD-brand-scoped-storage`; `SEC-brand-isolation` |
| `BR-connect-product-system` | 10-21-2026 client meeting | `UC-BRND-generate-api-key` steps 1–5 and extensions 1a, 1b, and \*a; `UC-BRND-send-products` PRE-1, step 2, and extensions 1b and 2a; `FR-PROD-brand-scoped-storage`; `SEC-brand-isolation`; `SEC-api-key-strength`; `SEC-api-key-ending` |
| `BR-multiple-categories` | 10-21-2026 client meeting | `UC-BRND-approve-product` extension 5c |
| `BR-photo-size` | 10-21-2026 client meeting | `UC-BRND-create-product` extension 4b; `UC-BRND-import-products` extension 4c; `UC-BRND-send-products` extension 3a; `UC-BRND-update-product` extension 4a |
| `BR-submit-market` | Market Match website | Out of MVP scope (vision and scope §4.3) |
| `BR-get-market-feedback` | Market Match website | `UC-FDBK-view-vendor-results` (listed, not yet written) |
| `BR-market-code` | 09-21-2026 client meeting | Out of MVP scope (vision and scope §4.3) |
| `BR-market-type` | 09-21-2026 client meeting | Out of MVP scope (vision and scope §4.3) |
| `BR-market-organization` | 09-21-2026 client meeting | Out of MVP scope (vision and scope §4.3) |
| `BR-market-categories` | 09-21-2026 client meeting | Out of MVP scope (vision and scope §4.3) |
| `BR-public-market` | 09-21-2026 client meeting | Joining: `UC-FDBK-complete-market` PRE-2 and step 1. Reporting to the organization: `UC-FDBK-view-vendor-results` (listed, not yet written) |
| `BR-code-requires-sign-in` | 09-30-2026 client meeting | `UC-MKT-enter-market` PRE-1; `UC-FDBK-complete-market` PRE-2 |
| `BR-select-category` | 09-30-2026 client meeting | `UC-FDBK-complete-market` steps 3–5 |
| `BR-create-market-admin-only` | 09-21-2026 client meeting | Categories: `UC-BRND-approve-product` extension 5b. Markets: Out of MVP scope (vision and scope §4.3) |
| `BR-configure-branding` | Client brief | Out of MVP scope (vision and scope §4.3) |
| `BR-access-own-data` | Client brief | Out of MVP scope (vision and scope §4.3) |
| `BR-connect-api` | Client brief | Out of MVP scope (vision and scope §4.3) |
| `BR-capture-feedback` | Client brief; 09-30-2026 client meeting | `UC-FDBK-rate-product` steps 1–4; `UC-FDBK-flip-card` step 3 and extension 3c; `UC-FDBK-open-card-media` step 2; `UC-FDBK-complete-market` steps 2, 5, 7, and 8 |
| `BR-media-clicks` | 09-30-2026 client meeting | `UC-FDBK-open-card-media` step 2 and extension 3b |
| `BR-engagement-funnel` | 09-30-2026 client meeting | `UC-FDBK-complete-market` steps 2, 5, 7, and 8; stage count pending `OI-46` |
| `BR-market-completion-time` | 09-30-2026 client meeting | Capture: `UC-FDBK-complete-market` step 8. Report: `UC-FDBK-view-brand-insights` and `UC-FDBK-view-vendor-results` (listed, not yet written) |
| `BR-vendor-feedback-scope` | 09-30-2026 client meeting | `UC-FDBK-view-vendor-results` (listed, not yet written) |
| `BR-brand-feedback-scope` | 09-30-2026 client meeting | `UC-FDBK-view-brand-insights` (listed, not yet written) |
| `BR-admin-feedback-scope` | 09-30-2026 client meeting | `UC-FDBK-view-platform-activity` (listed, not yet written) |
| `BR-create-organization` | 09-21-2026 client meeting | Out of MVP scope (vision and scope §4.3); relied on by `UC-BRND-generate-api-key`, since only the Admin puts a Brand on Market Match |
| `BR-default-consumer-role` | 09-21-2026 client meeting | Out of MVP scope (vision and scope §4.3) |
| `BR-admin-role` | 09-21-2026 client meeting | `UC-BRND-approve-product` PRE-1 |
| `BR-assign-role` | 09-21-2026 client meeting | Out of MVP scope (vision and scope §4.3) |
| `BR-dashboard-access` | 09-21-2026 client meeting | Out of MVP scope (vision and scope §4.3) |
| `BR-view-org-markets` | 09-21-2026 client meeting | Out of MVP scope (vision and scope §4.3) |
| `BR-survey-pricing` | 09-21-2026 client meeting | Out of MVP scope (vision and scope §4.3) |
| `BR-collect-email-only` | 09-21-2026 client meeting | `SEC-pii-protection`, pending `OI-45` |
| `BR-protect-pii` | 09-07-2026 client meeting | `SEC-pii-protection` |

**Checks.**

1. **Every rule is enforced by something.** A rule with an empty third column is a policy your software ignores. That may be the right answer, and it is only the right answer if you decided it on purpose. Write the decision in `OPEN-ISSUES.md` rather than leaving the cell blank.
2. **Every requirement that cites a rule cites one that exists.** Search your use cases and specification for every `BR-` identifier and confirm each one is defined in `business-rules.md`. This is the check that catches a draft citing `BR-late-penalty` because a late penalty is the kind of thing a course usually has. A generated document cites plausible identifiers with complete confidence, and nothing else in your process will notice.

---

## 3. Use case to design, code, and test (week 8)

_[In week 8 the spine extends past the use case: **business objective → feature → use case area → use case → design → code → test.** This table has one row per use case, plus one row per non-use-case FR (`FR-<AREA>-<slug>`) that needs building. Add a row the day a use case is written, not the day it is built._

_**Build** and **Verify** are two separate states, so that a use case which is built but untested stays visibly unverified rather than being absorbed into a single "done":_

- _Build: `❌ Not started`, `📐 Designed` (its design pull request merged), `🟡 In progress`, `✅ Built`. It says nothing about tests._
- _Verify: `✅ Verified` (tests cover the main flow and every extension, and pass), `🟡 Partial` (the Tests cell names the gap), `🔎 None`, or left blank while there is nothing built to verify._

_**Release** is your **release plan**: the release the row's code ships in. It tracks the build only; a shipped row with missing tests keeps its Release, and the gap shows in Verify. Use `v0.1.0` (the proving slice, Checkpoint 2), `v0.2.0` (Checkpoint 3), `v1.0.0` (the December MVP), `Spring`, or `Out`. Every row has one by Checkpoint 2; an empty cell is work nobody planned. Place rows by risk first, then by what your client needs first, then by dependency, and change a Release cell only by pull request, saying why. Your client's agreement on scope by feature stays in vision and scope's MVP Scope section; this column carries it down to use cases. How to forecast from it: [Process and Planning](https://washingtonwei.github.io/cosc-40943/modules/process-and-planning/#46-from-estimates-to-a-release-plan)._

_A worked example from Project Pulse, which numbers its releases from its own tags, showed a built and verified row naming its code and tests, designed rows naming their design document, and a not-started row that already carried a Release.]_

| Use case or FR | Build | Verify | Release | Design | Code | Tests |
|---|---|---|---|---|---|---|
| `UC-MKT-enter-market` | ❌ Not started |  | After `v0.1.0`; pending `OI-1` |  |  |  |
| `UC-PROD-view-product-details` | ❌ Not started |  | After `v0.1.0`; pending `OI-1` |  |  |  |
| `UC-FDBK-rate-product` | ❌ Not started |  | After `v0.1.0`; pending `OI-1` |  |  |  |
| `UC-FDBK-flip-card` | ❌ Not started |  | After `v0.1.0`; pending `OI-1` |  |  |  |
| `UC-FDBK-open-card-media` | ❌ Not started |  | After `v0.1.0`; pending `OI-1` |  |  |  |
| `UC-FDBK-complete-market` | ❌ Not started |  | After `v0.1.0`; pending `OI-1` |  |  |  |
| `UC-BRND-create-product` | ❌ Not started |  | `v0.1.0` (proving slice) |  |  |  |
| `UC-BRND-import-products` | ❌ Not started |  | After `v0.1.0`; pending `OI-1` |  |  |  |
| `UC-BRND-send-products` | ❌ Not started |  | After `v0.1.0`; pending `OI-1` |  |  |  |
| `UC-BRND-update-product` | ❌ Not started |  | After `v0.1.0`; pending `OI-1` |  |  |  |
| `UC-BRND-approve-product` | ❌ Not started |  | After `v0.1.0`; pending `OI-1` |  |  |  |
| `UC-BRND-generate-api-key` | ❌ Not started |  | After `v0.1.0`; pending `OI-1` |  |  |  |
| `FR-PROD-brand-scoped-storage` | ❌ Not started |  | `v0.1.0` (with the proving slice) |  |  |  |
| `FR-PROD-hidden-until-approved` | ❌ Not started |  | `v0.1.0` (with the proving slice) |  |  |  |
| `FR-PROD-server-checks` | ❌ Not started |  | `v0.1.0` (with the proving slice) |  |  |  |
| `FR-API-published-contract` | ❌ Not started |  | After `v0.1.0`; pending `OI-1` |  |  |  |

**Checks.**

1. **Every use case and FR has a row, and every row has a Release.** A missing row is a requirement nothing tracks; an empty Release is work nobody planned.
2. **Nothing reads Verified without a test you can name.** Open the test cited in each `✅ Verified` row and confirm it exercises that use case, extensions included.

---

## Working this document with your agent

_[Delegate: running both checks and reporting what fails; finding every `BR-`, `FEAT-`, and `UC-` identifier cited anywhere in `docs/` and listing the ones with no definition; regenerating the second table from the Business Rules fields of your use cases after you have edited them._

_Keep human: whether an area with no feature is a missing feature or a use case that should not exist, and whether an unenforced rule is an oversight or a decision. Both are questions about your client's business, and the answer is not in your repository._

_**The specific failure to watch for:** an agent asked to "fill in the traceability matrix" produces a complete, well-formed table in which every cell is populated and some of the links are invented. A blank cell is information. A confidently wrong link is worse than no link, because it makes the check pass. Verify every row you did not write yourself by opening the document at the other end.]_
