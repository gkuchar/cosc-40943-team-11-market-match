# Use Cases

**Project:** Market Match
**Team:** 11
**Client:** Demetrie King
**Version:** 0.7

---

_**How to use this template.** Instructions appear in italic square brackets. Fill in underneath them and leave them in place until the document is stable._

_**What a use case is.** One goal a user can accomplish with your system, written as the dialogue between the actor and the system, including what happens when it goes wrong. It is the unit of work in this course: one use case becomes one issue, one branch, one pull request, and one set of tests._

_**Why the use case and not the user story.** You will meet user stories in industry, and they are a good planning tool: "As a student, I want to submit my report so that I get credit." A story is deliberately under-specified, because it is a **placeholder for a conversation** that happens later, between people. That is exactly the wrong property when the thing building your code is an agent that will implement precisely what the specification says and never ask what you meant. Use stories to plan and prioritize. Build against use cases._

_The difference that matters is the parts a story does not have: preconditions, the step-by-step flow, and above all the **extensions**, which is where the failure paths live. Most defects your team ships this semester will be in a path nobody wrote down._

## Identifiers

_Use cases are identified as `UC-<AREA>-<slug>`, where the area code groups related functionality and the slug is coined from the goal: `UC-RUB-create-rubric`, `UC-WAR-manage-activities`, `UC-STU-invite-students`._

_Pick your own area codes from your project's feature areas, three or four letters each, and list them at the top of the Use Case List. Areas correspond to the `FEAT-*` entries in your [vision and scope](vision-and-scope.md), which is where use cases come from._

_**Never renumber, rename, or repoint an identifier.** Moving a use case between areas would change its identifier, so put it in the right area the first time, and if you get it wrong, leave it. An identifier is an address, not a description._

_Within one use case, `PRE-1`, `POST-1`, and the step numbers are local and may be renumbered freely, because nothing outside the use case cites them._

## Revision History

| Date       | Version | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Author           |
| ---------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| 2026-09-14 | 0.1     | Draft four use cases derived from the vision and scope feature list                                                                                                                                                                                                                                                                                                                                                                                         | Chris Ramirez    |
| 2026-10-13 | 0.2     | Rewrote `UC-FDBK-rate-product` and added `UC-FDBK-flip-card`, `UC-FDBK-open-card-media`, and `UC-FDBK-complete-market` to capture the data points from the third client meeting, checked against the client's repository                                                                                                                                                                                                                                    | Matthew Stafford |
| 2026-10-25 | 0.4     | Added the product import use cases to the BRND list (`UC-BRND-import-products`, `UC-BRND-send-products`, `UC-BRND-update-product`, `UC-BRND-approve-product`, `UC-BRND-generate-api-key`); pointed BRND at `FEAT-product-management` and `FEAT-bulk-product-import`, and MKT at `FEAT-market-management`, replacing feature IDs retired in vision and scope v0.2. Wrote all six in full, with `UC-BRND-create-product` revised to wait for Approval and made the proving slice. Listed three FDBK reporting use cases. Added the business rules the MKT, PROD, and FDBK use cases carry out but did not cite, and removed `BR-capture-feedback` from `UC-PROD-view-product-details`, which captures nothing | Matthew Stafford |
| 2026-10-26 | 0.5     | Added `UC-MKT-create-anonymous-consumer` from the fourth client meeting: each Public Access Consumer becomes their own Anonymous Consumer, reused on rescan and removed after a retention period. Added `UC-MKT-expire-anonymous-consumer`, which removes expired Anonymous Consumers without lowering any Market's Consumer count | Griffin Kuchar |
| 2026-10-28 | 0.6     | Added `UC-MKT-link-anonymous-consumer`: a device's anonymous activity joins the account signed in on it, matched by the device reference rather than IP address; the client confirmed linking (OI-48). Made an anonymous return resume its Market session in `UC-FDBK-complete-market` (2c, 7a1, 7a2) so the Consumer count holds, and defined that count as distinct session owners | Griffin Kuchar |
| 2026-10-28 | 0.7     | Filed the fifth client meeting's answers into the BRND use cases: the Admin, not the Brand, generates API Keys (`UC-BRND-generate-api-key`); Brands put each product in one of their own Categories, creating new ones as needed, so the Admin no longer chooses a Category at Approval; the Admin can approve a Brand's products all at once; an existing SKU changes that product; results restart after an approved change; JPEG or PNG photos; video limited to YouTube and Vimeo links until the client answers on other sites and video files (`OI-57`). Added `UC-BRND-remove-product` | Matthew Stafford |

---

## 1. Introduction

### 1.1 Purpose

_[One paragraph: this document specifies the goals users can accomplish with the system, in enough detail that a developer knows what to build and a tester knows what to check.]_

This document describes how Market Match consumers enter a market, inspect products, and submit preferences, and how brands create products for participation. Each draft includes the actor's goal, system responses, failure paths, and resulting state so we can review the behavior with the client and derive implementation tasks and tests. Unconfirmed details are identified as assumptions or open issues.

### 1.2 Scope

_[Which feature areas from the vision and scope are covered here. Name the `FEAT-*` entries. If a feature has no use cases yet, say so rather than leaving the reader to notice.]_

These use cases cover `FEAT-consumer-feedback`, `FEAT-product-information`, and the data capture half of `FEAT-feedback-insights`, partially cover `FEAT-market-management` through consumer market entry, and cover `FEAT-product-management` and `FEAT-bulk-product-import` through the BRND use cases.

---

## 2. Use Case Template

_[The field definitions. Every use case below uses exactly these fields, in this order.]_

**UC ID and Name.** _The identifier plus a concise name stating the value this use case provides to a user. Begin with an action verb, followed by an object: "Create a rubric", not "Rubric creation" and not "Rubric management", which is a feature, not a goal._

**Created By** and **Date Created.** _Who wrote it, and when._

**Primary and Secondary Actors.** _An actor is a person or other entity outside the system that interacts with it. The primary actor initiates this use case; secondary actors participate in completing it. Actors usually correspond to the user classes you identified in the vision and scope._

**Trigger.** _The business event, system event, or user action that starts the use case. The trigger tells the system to begin testing the preconditions._

**Description.** _A brief statement of the reason for and the outcome of this use case._

**Preconditions.** _What must already be true before this use case can start. **The system must be able to test each precondition**, which is what separates a precondition from a hope. Label them `PRE-1`, `PRE-2`. Example: PRE-1. The user's identity has been authenticated._

**Postconditions.** _The state of the system at successful conclusion. Label them `POST-1`, `POST-2`. Example: POST-1. The price of the item in the database has been updated with the new value._

**Main Success Scenario.** _The actor's actions and the system's responses under normal, expected conditions, as a numbered list that alternates between the two and ends by accomplishing the goal in the name. Write "The system validates..." not "The system will validate..."; use cases are written in the present tense._

**Extensions.** _Where the real work is. Two kinds, both numbered relative to the step they branch from:_

- _**Alternative flows**, other ways the use case can still succeed. Number them `4a`, `4b` for branches from step 4, with their own sub-steps `4a1`, `4a2`. Say where the flow branches off and, if it does, where it rejoins._
- _**Exceptions**, anticipated error conditions and how the system responds. Numbered the same way._

_**A use case with no extensions is not finished.** For every step, ask: what if the input is invalid, the thing is not found, the user cancels, the user is not allowed, or the external system is down? An agent building from a flow with no failure paths will invent the error handling, and you will not find out until a demo._

**Priority.** _Relative priority of implementing this. Use the same scheme across all your use cases._

**Frequency of Use.** _Roughly how often this is performed, per an appropriate unit of time. An early indicator of load, concurrency, and transaction volume, and it is the field that tells your architecture which use cases matter._

**Business Rules.** _The `BR-*` identifiers that govern this use case. **Identifiers only, never the rule's text**, so the rule has one home in [business-rules.md](business-rules.md) and cannot go stale here._

**Associated Information.** _Everything a developer needs that is not a step: the data fields and their validation rules, quality attributes that apply, display and sort strategies, and what happens if execution fails for a systemic reason such as a network timeout. If the use case makes a durable change, say whether a failure rolls it back, completes it, or leaves it partially done._

_Data fields are specified as a table:_

| Property name | Data type | Validation rule             | Security or access concerns | Glossary reference |
| ------------- | --------- | --------------------------- | --------------------------- | ------------------ |
| _[field]_     | _[type]_  | _[required, format, range]_ | _[who may see or set it]_   | _[term]_           |

**Related Use Cases.** _Other use cases this one invokes or is invoked by, by identifier and name._

**Assumptions.** _Anything assumed about this use case or how it executes._

**Open Issues.** _What you do not know yet. Mirror it into [OPEN-ISSUES.md](OPEN-ISSUES.md) so it is visible in one place._

---

## 3. Use Case List

_[Your area codes, then a table of every use case by area. Write this list first, before specifying any single use case in detail. It is the cheapest thing to review with your client, and finding out you missed a whole area costs minutes here rather than a week later.]_

| Area code | Feature area                                                                           | Use cases                                                                                                                                                                                                                                                                                                                                                       |
| --------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MKT       | Market participation: `FEAT-market-management`, `FEAT-consumer-feedback`                                         | `UC-MKT-enter-market`: Enter a market; `UC-MKT-create-anonymous-consumer`: Create an Anonymous Consumer; `UC-MKT-expire-anonymous-consumer`: Remove an expired Anonymous Consumer; `UC-MKT-link-anonymous-consumer`: Link anonymous activity to a signed-in Consumer |
| PROD      | Product information: `FEAT-product-information`                                        | `UC-PROD-view-product-details`: View product details                                                                                                                                                                                                                                                                                                            |
| FDBK      | Consumer feedback and data capture: `FEAT-consumer-feedback`, `FEAT-feedback-insights` | `UC-FDBK-rate-product`: Rate a product; `UC-FDBK-flip-card`: Flip a card; `UC-FDBK-open-card-media`: Open a card photo or video; `UC-FDBK-complete-market`: Complete a market; listed, not yet written: `UC-FDBK-view-brand-insights`: View a Brand's product insights; `UC-FDBK-view-vendor-results`: View a Vendor's market results; `UC-FDBK-view-platform-activity`: View platform activity                                                                                                                                                                                   |
| BRND      | Brand participation: `FEAT-product-management`, `FEAT-bulk-product-import`             | `UC-BRND-create-product`: Create a product; `UC-BRND-import-products`: Import products from a spreadsheet; `UC-BRND-send-products`: Send products from a connected system; `UC-BRND-update-product`: Update a product; `UC-BRND-remove-product`: Remove a product; `UC-BRND-approve-product`: Approve or return a submitted product; `UC-BRND-generate-api-key`: Generate an API key |

---

## 4. Use Cases

_[One `###` heading per use case, grouped under a `##` heading per area.]_

## MKT: Market Participation

### UC-MKT-enter-market: Enter a market

**UC ID and Name:** `UC-MKT-enter-market`: Enter a market
**Created By:** Chris Ramirez
**Date Created:** 2026-09-14
**Primary Actor:** Consumer
**Secondary Actors:** None
**Trigger:** The consumer chooses to enter a market.
**Description:** The consumer enters a market ID code to access participating products and begin providing feedback.

**Preconditions:**

- PRE-1. The consumer has an authenticated session.

**Postconditions:**

- POST-1. The market matching the accepted code is selected.
- POST-2. The system displays a participating product or states that no products are available.

**Main Success Scenario:**

1. The consumer chooses to enter a market.
2. The system requests a market ID code.
3. The consumer enters the code and submits it.
4. The system validates the code, selects the matching accessible market, and displays a participating product.

**Extensions:**

- **3a. The consumer cancels:**
  - 3a1. The system leaves the current market selection unchanged; the use case ends.
- **4a. The code is blank or does not identify an accessible market:**
  - 4a1. The system explains that the market cannot be entered and leaves the current selection unchanged. The consumer returns to step 3 to correct the code or cancels.
- **4b. The market contains no available products:**
  - 4b1. The system selects the market and displays an empty-state message; the use case succeeds without starting a rating.
- **4c. The market cannot be loaded:**
  - 4c1. The system reports the failure and retains the previous selection. The consumer retries from step 3 or ends the use case.

**Priority:** High (provisional)
**Frequency of Use:** Once per market entry or switch; daily volume is unconfirmed.
**Business Rules:** `BR-select-market`, `BR-code-requires-sign-in`

**Associated Information:**

| Property name  | Data type | Validation rule                                                                                         | Security or access concerns                                                           | Glossary reference |
| -------------- | --------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------ |
| Market ID code | String    | Required; must resolve to an accessible market; format and case sensitivity pending client confirmation | Supplied by the authenticated consumer; access conditions pending client confirmation | Market Code        |

Display the selected market name and its participating product cards. Product ordering is pending client confirmation. This use case creates no rating, product, or market. A failed lookup leaves the previous selection unchanged.

**Related Use Cases:** `UC-PROD-view-product-details`: View product details; `UC-FDBK-rate-product`: Rate a product.
**Assumptions:** Email and one-time-code sign-in occurs before market entry, following vision and scope section 1.2. A market ID code is distinct from a sign-in code.
**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).

- [OI-1](OPEN-ISSUES.md#open): Which use cases belong in the MVP, and in what priority order?
- [OI-2](OPEN-ISSUES.md#resolved) (resolved): Does a market mean a target group, a collection of products, or both? A Market is the collection of Cards; the target group is a Demographic. See [Market](project-glossary.md#market) and [Demographic](project-glossary.md#demographic).
- [OI-3](OPEN-ISSUES.md#open): What format and case sensitivity does a Market Code have?
- [OI-4](OPEN-ISSUES.md#open): Which Consumers may enter which Markets?
- [OI-5](OPEN-ISSUES.md#open): In what order are a Market's products shown?

---

### UC-MKT-create-anonymous-consumer: Create an Anonymous Consumer

**UC ID and Name:** `UC-MKT-create-anonymous-consumer`: Create an Anonymous Consumer
**Created By:** Griffin Kuchar
**Date Created:** 2026-10-26
**Primary Actor:** Consumer, not signed in
**Secondary Actors:** None
**Trigger:** The Consumer scans a Public Access Market's QR Code or opens its link.
**Description:** Reaching a Public Access Market by QR Code or link already works. This use case covers only who the Consumer is recorded as once there. Market Match gives each person their own Anonymous Consumer, so each person counts as one Consumer and their activity can be analyzed per person, instead of every scan landing on one shared user. The Anonymous Consumer is reused when the same device returns and expires after a retention period (`UC-MKT-expire-anonymous-consumer`).

**Preconditions:**

- PRE-1. The link identifies a launched Market.
- PRE-2. That Market is set to Public Access.

**Postconditions:**

- POST-1. The Consumer is represented by exactly one Anonymous Consumer for this Market on this device.
- POST-2. The Market's Consumer count includes that Anonymous Consumer once, however many times the QR Code is rescanned on the same device.
- POST-3. The Anonymous Consumer holds no email, no name, and no Demographic answers.
- POST-4. The Anonymous Consumer has an expiry time set from its creation.

**Main Success Scenario:**

1. The Consumer scans the QR Code or opens the link.
2. The system finds no valid Anonymous Consumer reference for this Market on the device.
3. The system creates an Anonymous Consumer for this Market, sets its expiry time, and keeps its reference on the device.
4. The system continues with `UC-FDBK-complete-market` step 2, which starts the Market session for this Anonymous Consumer. Every swipe, Flip, Click, and funnel stage after that is stored against it.

**Extensions:**

- **1a. The Market is the demo Market:**
  - 1a1. No Anonymous Consumer is created and nothing is counted, as in `UC-FDBK-complete-market` extension 2d.
- **1b. The Consumer is already signed in on this device:**
  - 1b1. The system uses the signed-in Consumer and creates no Anonymous Consumer. Whether this is right is open. Rejoins at step 4.
- **2a. The device holds an unexpired Anonymous Consumer reference for this Market (a rescan, a lost connection, a closed tab):**
  - 2a1. The system reuses that Anonymous Consumer and creates no new one, so the Consumer count does not grow. Rejoins at step 4.
- **2b. The device holds an Anonymous Consumer reference for this Market that has expired:**
  - 2b1. The system ignores it. Continues at step 3 as a new Anonymous Consumer.
- **2c. The device holds a reference the server did not issue, or one issued for another Market:**
  - 2c1. The system ignores it, so one device cannot act as another's Anonymous Consumer. Continues at step 3.
- **3a. The device cannot keep the reference (private browsing, or storage blocked or cleared):**
  - 3a1. The system still creates the Anonymous Consumer and continues. A later scan from the same person cannot be recognized and counts as a new Consumer; this is an accepted limit of not signing in. The same applies when the person scans again from a different device.
- **3b. Creating the Anonymous Consumer fails:**
  - 3b1. The system reports that the Market could not be opened and shows no Cards, because a swipe needs an owner to be counted against. Nothing partial is kept. The Consumer retries from step 1.

**Priority:** High (provisional). Most Consumers reach Markets this way today (TCU, UTD), and every Public Access figure that counts or averages per Consumer is wrong until this is built.
**Frequency of Use:** Once per person per Public Access Market, plus a reuse on each rescan. The client's growth scenario is 10,000 people scanning one QR Code at an event, so Anonymous Consumers are created in bursts.
**Business Rules:** `BR-public-market`, `BR-anonymous-consumer`, `BR-anonymous-consumer-expiry`

**Associated Information:**

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| Anonymous Consumer | Identifier | System-generated, unguessable; one per Market per device | Never shown on any dashboard; holds no personal information | Anonymous Consumer |
| Device reference | Opaque value | Issued by the server at step 3; kept on the device; checked by the server on every request | Must not be guessable or reusable across Markets (extension 2c) | Anonymous Consumer |
| Market reference | Identifier | Required; a launched Public Access Market | From the QR Code or link | Market; Public Access |
| Created at | Timestamp | Set at step 3 | System-captured | Anonymous Consumer |
| Expires at | Timestamp | Created at plus the retention period; the period is open, 30 days proposed | System-captured | Anonymous Consumer |

**Expiry is checked on every request.** The server compares Expires at whenever it accepts a device reference, not only at step 2. A request carrying an expired reference is refused, and the Consumer comes back through this use case at extension 2b. Removal by `UC-MKT-expire-anonymous-consumer` is cleanup, not what keeps an expired reference out.

**Who sees what.** The Organization the Market is assigned to sees Anonymous Consumers only as a count and in aggregates, never one by one (`BR-public-market`, `BR-view-org-markets`). The Admin sees the count. Averages per Consumer, such as average swipes, divide by the number of Anonymous Consumers.

**Inflated counts.** Repeated or scripted scans, or clearing storage between scans, mint new Anonymous Consumers and inflate the Consumer count that Organizations rely on. Rate limiting is decided in the design.

**Systemic failure.** A link that fails PRE-1 or PRE-2 creates nothing. Logs name the Anonymous Consumer and Market by ID only, never the device reference.

**Current state in the client's repository** (as recorded in `UC-FDBK-complete-market`; not re-read for this draft):

- Joining by QR Code or link works, but every Public Access session is stored under one shared user, `anonymous-public`, so the TCU Market showed one Consumer for every scan (fourth client meeting, lines 172–194).

**Related Use Cases:**

- `UC-FDBK-complete-market`: Complete a market (continues from step 4 and owns the Market session).
- `UC-MKT-expire-anonymous-consumer`: Remove an expired Anonymous Consumer.
- `UC-MKT-link-anonymous-consumer`: Link anonymous activity to a signed-in Consumer.
- `UC-MKT-enter-market`: Enter a market (the signed-in path, by Market Code).

**Assumptions:**

- An Anonymous Consumer belongs to one Market. The same device scanning a different Public Access Market gets a different Anonymous Consumer, so Markets are counted separately.
- Demographics are not asked of an Anonymous Consumer (fourth client meeting, line 126).

**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).

---

### UC-MKT-expire-anonymous-consumer: Remove an expired Anonymous Consumer

**UC ID and Name:** `UC-MKT-expire-anonymous-consumer`: Remove an expired Anonymous Consumer
**Created By:** Griffin Kuchar
**Date Created:** 2026-10-26
**Primary Actor:** Market Match, through a scheduled time event
**Secondary Actors:** None
**Trigger:** The scheduled removal check runs. Daily is proposed; how it is scheduled is decided in the design.
**Description:** Market Match removes every Anonymous Consumer whose expiry time has passed. The Market's Consumer count and the swipes, Flips, Clicks, and Engagement Funnel stages it recorded stay, so the Organization keeps its figures while no per-device identity is kept past the retention period. This carries out the client's "lock in the consumer count and then later on it can just drop off" (fourth client meeting, line 212).

**Preconditions:**

- PRE-1. A retention period is set for Anonymous Consumers.

**Postconditions:**

- POST-1. Every Anonymous Consumer whose expiry time has passed is removed, and its device reference is no longer accepted.
- POST-2. Its Market sessions and their data points stay and still count toward every Market figure.
- POST-3. Every Market's Consumer count is the same after the run as before it.
- POST-4. No Anonymous Consumer whose expiry time has not passed is changed.
- POST-5. The run's outcome is logged by count and by ID only.

**Main Success Scenario:**

1. The scheduled check runs.
2. The system finds the Anonymous Consumers whose expiry time has passed.
3. For each one, the system detaches it from its Market sessions, so they keep counting without pointing at an identity, and removes it. Both happen as one unit.
4. The system logs how many Anonymous Consumers it removed.

**Extensions:**

- **2a. No Anonymous Consumer has expired:**
  - 2a1. The system logs a run with nothing removed. The use case ends.
- **3a. The Anonymous Consumer's Market session is incomplete:**
  - 3a1. The session stays incomplete and counts as _started_ but not _completed_ (or _entered_ or _viewed_ only, if no Card was swiped). A later scan from that device is a new Anonymous Consumer, per `UC-MKT-create-anonymous-consumer` extension 2b.
- **3b. The Consumer is partway through the Market when the expiry time passes:**
  - 3b1. Removal goes ahead. The Consumer's next request is refused as expired and handled by `UC-MKT-create-anonymous-consumer` extension 2b, so the rest of their swipes land in a new Market session. Whether expiry should count from the last swipe instead is open.
- **3c. Removing one Anonymous Consumer fails:**
  - 3c1. That Anonymous Consumer is left as it was, the failure is logged with its ID, and the system continues with the rest. The next run retries it.
- **3d. The run stops partway:**
  - 3d1. Anonymous Consumers already removed stay removed. The next run finds the rest at step 2 and handles each once.
- **\*a. The check does not run on schedule:**
  - \*a1. Expired Anonymous Consumers are still refused, because `UC-MKT-create-anonymous-consumer` checks the expiry time on every request rather than relying on this removal. They are removed on the next run, late, and nothing is counted twice.

**Priority:** Medium (provisional). Counting is correct without it; it limits how long Market Match keeps an identity for people who never signed in.
**Frequency of Use:** Once per scheduled run. A run removes about as many Anonymous Consumers as were created one retention period earlier, so a 10,000-scan event in the client's growth scenario becomes a 10,000-removal run later.
**Business Rules:** `BR-anonymous-consumer-expiry`, `BR-anonymous-consumer`, `BR-public-market`, `BR-capture-feedback`

**Associated Information:**

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| Anonymous Consumer | Identifier | Selected when its Expires at is in the past | Removed; never shown on any dashboard before or after | Anonymous Consumer |
| Expires at | Timestamp | Set by `UC-MKT-create-anonymous-consumer`; compared to the time of the run | System-captured | Anonymous Consumer |
| Market session reference | Identifier | Kept; its link to the Anonymous Consumer is cleared | Still counted in aggregates | Market |
| Run outcome | Count and list of IDs | Removed count; IDs of any failures | Logged by ID only, never the device reference | (none) |

**How the Consumer count is computed.** A Market's Consumer count is the number of distinct owners of its Market sessions: a Consumer, an Anonymous Consumer, or, once detached by this use case, the session itself. An Anonymous Consumer has one Market session per Market, because a return resumes it (`UC-FDBK-complete-market` extension 2c), so detaching it leaves the count unchanged (POST-3). The FDBK reporting use cases must count the same way.

**Systemic failure.** For each Anonymous Consumer, detaching and removing are stored together or not at all, so no Market session is left pointing at a removed identity. Every failure is logged by ID; no `catch` is empty.

**Current state in the client's repository** (as recorded in `UC-FDBK-complete-market`; not re-read for this draft): Public Access activity sits under one shared `anonymous-public` user, and nothing expires.

**Related Use Cases:**

- `UC-MKT-create-anonymous-consumer`: Create an Anonymous Consumer (creates it and sets its expiry time).
- `UC-FDBK-complete-market`: Complete a market (the Market sessions that stay).
- `UC-FDBK-view-brand-insights`, `UC-FDBK-view-vendor-results`, `UC-FDBK-view-platform-activity` (listed, not yet written): their counts must not drop when Anonymous Consumers are removed.

**Assumptions:**

- Data points stay after removal; only the identity goes. Drawn from the client's "lock in the consumer count and then later on it can just drop off" (fourth client meeting, line 212); not yet confirmed.
- Expiry is counted from when the Anonymous Consumer was created (`UC-MKT-create-anonymous-consumer` POST-4).

**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).

- [OI-47](OPEN-ISSUES.md#open): How long is an Anonymous Consumer kept before it is removed?
- [OI-49](OPEN-ISSUES.md#open): Does a Market session that is never completed count as zero in average Completion Time, or is it left out?
- [OI-51](OPEN-ISSUES.md#open): Should an Anonymous Consumer expire a fixed time after its first scan, or after its last swipe?

---

### UC-MKT-link-anonymous-consumer: Link anonymous activity to a signed-in Consumer

**UC ID and Name:** `UC-MKT-link-anonymous-consumer`: Link anonymous activity to a signed-in Consumer
**Created By:** Griffin Kuchar
**Date Created:** 2026-10-28
**Primary Actor:** Consumer
**Secondary Actors:** None
**Trigger:** The Consumer completes sign-in. Sign-in creates the account on first login (`BR-default-consumer-role`); whether signing in to an existing account also links is open.
**Description:** A person who swiped anonymously and then signs up keeps that activity under their account, so they count as one Consumer rather than two. Matching uses only the server-issued device reference from `UC-MKT-create-anonymous-consumer`, never IP address: campus Wi-Fi and phone carriers put thousands of people behind one IP, so IP matching would attach strangers' swipes to a named account.

**Preconditions:**

- PRE-1. The Consumer is signed in.

**Postconditions:**

- POST-1. Each valid, unexpired Anonymous Consumer whose reference the device presented has its Market sessions moved to the Consumer and is then removed.
- POST-2. Each affected Market counts the person once.
- POST-3. The device no longer holds the linked references.
- POST-4. Nothing is linked from another device or by network address.

**Main Success Scenario:**

1. The Consumer completes sign-in.
2. The system reads the Anonymous Consumer references held on the device.
3. The system checks that each reference was issued by the server and that its Anonymous Consumer has not expired.
4. For each valid reference, the system moves the Anonymous Consumer's Market sessions, with their swipes, Flips, Clicks, and funnel stages, to the Consumer and removes the Anonymous Consumer. Both happen as one unit.
5. The system clears the linked references from the device. Sign-in continues as normal.

**Extensions:**

- **2a. The device holds no references (a different device, or storage was cleared):**
  - 2a1. Nothing is linked. The anonymous activity stays anonymous until it expires (`UC-MKT-expire-anonymous-consumer`). This is the accepted limit of matching by device.
- **3a. A reference's Anonymous Consumer has expired or was already removed:**
  - 3a1. The system skips it and clears it from the device. The other references continue.
- **3b. A reference was not issued by the server:**
  - 3b1. The system ignores it and clears it from the device. The other references continue.
- **3c. The device is shared, and holds references from more than one person:**
  - 3c1. Every valid reference on the device links to whoever signs in first. A device reference cannot tell people apart; see Assumptions.
- **4a. The Consumer already has their own Market session in the same Market:**
  - 4a1. Both sessions are kept under the Consumer. They have one owner, so the person counts once in that Market under the counting rule in `UC-MKT-expire-anonymous-consumer`. Whether reports should merge the two sessions' swipes is left to the FDBK reporting use cases.
- **4b. Linking fails:**
  - 4b1. Sign-in still succeeds. Nothing partial is moved, the references stay on the device, and the failure is logged by ID. Linking is tried again at the next sign-in on that device.
- **4c. A moved Market session is incomplete:**
  - 4c1. The Consumer can resume it as a signed-in Consumer, through `UC-FDBK-complete-market` extension 2c.

**Priority:** Low (provisional). Counting is correct for anonymous visitors without it; it only prevents one person counting twice after signing up.
**Frequency of Use:** At most once per sign-in, and only on a device that holds Anonymous Consumer references. Low while most Public Access visitors never sign in.
**Business Rules:** `BR-anonymous-consumer`, `BR-sign-in`, `BR-default-consumer-role`

**Associated Information:**

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| Device reference | Opaque value | Must have been issued by the server (`UC-MKT-create-anonymous-consumer`) | Never logged; cleared from the device once handled | Anonymous Consumer |
| Anonymous Consumer | Identifier | Must exist and not be expired | Removed once linked | Anonymous Consumer |
| Consumer reference | Identifier | Taken from the signed-in session, never from input | One Consumer cannot claim another's activity | Consumer |
| Moved Market sessions | List of identifiers | Every Market session of each valid Anonymous Consumer | Still seen only in aggregates by the Market's Organization | Market |

**No network address is used.** IP address and other network data are never used to match, and never stored or logged for this use case.

**Demographics are not backfilled.** Swipes moved from an Anonymous Consumer keep their empty Demographic snapshot, even after the Consumer enters Demographics at sign-up. Whether they should get them is open.

**Systemic failure.** For each Anonymous Consumer, moving its sessions and removing it are stored together or not at all, so no session is left without an owner and none is counted twice. Logs name the Consumer, Anonymous Consumer, and Market by ID only.

**Current state in the client's repository:** Nothing links anonymous activity to an account; Public Access activity sits under the shared `anonymous-public` user (as recorded in `UC-FDBK-complete-market`; not re-read for this draft).

**Related Use Cases:**

- `UC-MKT-create-anonymous-consumer`: Create an Anonymous Consumer (issues the device reference this matches on).
- `UC-MKT-expire-anonymous-consumer`: Remove an expired Anonymous Consumer (a linked Anonymous Consumer is already removed, so it never expires).
- `UC-FDBK-complete-market`: Complete a market (a moved incomplete session resumes through extension 2c).

**Assumptions:**

- A device holds one person's anonymous activity. On a shared device, everything links to whoever signs in first (extension 3c).
- The link is made at sign-in on the same device the person scanned on. There is no other way to claim anonymous activity.

**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).

- [OI-48](OPEN-ISSUES.md#resolved) (resolved): Should a Consumer's anonymous activity be joined to their account when they sign up? Yes, per the client (2026-10-26).
- [OI-52](OPEN-ISSUES.md#open): Should swipes made anonymously get the Demographics the Consumer enters at sign-up?
- [OI-53](OPEN-ISSUES.md#open): Should anonymous activity link only when someone creates an account, or also when an existing user signs in on that device?
- [OI-54](OPEN-ISSUES.md#open): Should a Consumer be told, or asked, before their earlier anonymous swipes are joined to their account?

---

## PROD: Product Information

### UC-PROD-view-product-details: View product details

**UC ID and Name:** `UC-PROD-view-product-details`: View product details
**Created By:** Chris Ramirez
**Date Created:** 2026-09-14
**Primary Actor:** Consumer
**Secondary Actors:** None
**Trigger:** The consumer taps a displayed product.
**Description:** The consumer inspects additional product information before deciding whether to express interest or disinterest.

**Preconditions:**

- PRE-1. The consumer has an authenticated session and a selected market.
- PRE-2. The system displays a product belonging to that market.

**Postconditions:**

- POST-1. The system displays the selected product's available additional information.
- POST-2. Viewing details alone creates no preference rating.

**Main Success Scenario:**

1. The consumer taps the displayed product.
2. The system retrieves and displays the product's additional information.

**Extensions:**

- **2a. No additional information is supplied:**
  - 2a1. The system indicates that no additional details are available and retains the product card; the use case ends.
- **2b. Product details cannot be loaded:**
  - 2b1. The system reports the failure and retains the product card. The consumer retries from step 1 or leaves the details view.
- **2c. The product is no longer available in the market:**
  - 2c1. The system reports its unavailability and refreshes the available products; the use case ends without recording a rating.

**Priority:** High (provisional)
**Frequency of Use:** As desired before rating a product; actual volume is unconfirmed.
**Business Rules:** `BR-tap-product`

**Associated Information:**

| Property name          | Data type  | Validation rule                                                                                  | Security or access concerns                  | Glossary reference |
| ---------------------- | ---------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------- | ------------------ |
| Product reference      | Identifier | Required; identifies the displayed product in the selected market                                | System checks product accessibility          | Card               |
| Additional information | Content    | Display supplied content; handle missing content explicitly; formats pending client confirmation | Consumer reads content supplied by the brand | Card               |

Keep the product identity visible with its details. Product data is read only in this use case. Viewing activity is captured under `FEAT-feedback-insights`; the Flip and its dwell time are specified in `UC-FDBK-flip-card`. A failed details load must not be represented as a successful view. The effect of activity-recording failures remains pending client confirmation.

**Related Use Cases:** `UC-MKT-enter-market`: Enter a market; `UC-FDBK-rate-product`: Rate a product.
**Assumptions:** Inspecting details is optional before rating, as described in vision and scope section 1.2.
**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).

- [OI-6](OPEN-ISSUES.md#open): Which additional-information formats can the back of a Card hold?
- [OI-7](OPEN-ISSUES.md#resolved) (resolved): Which viewing events and timing boundaries are measured? Dwell time (Card appears to first Flip) and decision time (Card appears to swipe), captured in `UC-FDBK-flip-card` and `UC-FDBK-rate-product`. See [Average Dwell Time](project-glossary.md#average-dwell-time), [Average Decision Time](project-glossary.md#average-decision-time), and [Flip](project-glossary.md#flip).
- [OI-8](OPEN-ISSUES.md#open): What happens if activity capture fails while a Consumer views product details?

---

## FDBK: Consumer Feedback and Data Capture

These four use cases cover capturing every data point the client named for a Market. They do not cover the dashboards that report the data points. Each use case's Associated Information says what the client's repository (`MM-Version`, branch `tcu-fall-2026-stage`) captures today and what is missing, so the work left is visible. The data points apply to signed-in Consumers and to Public Access Consumers alike. A Public Access Consumer is identified by an Anonymous Consumer (`UC-MKT-create-anonymous-consumer`).

### UC-FDBK-rate-product: Rate a product

**UC ID and Name:** `UC-FDBK-rate-product`: Rate a product
**Created By:** Chris Ramirez; revised by Matthew Stafford
**Date Created:** 2026-09-14; revised 2026-10-13
**Primary Actor:** Consumer
**Secondary Actors:** None
**Trigger:** The system displays a Card to a Consumer in a Market.
**Description:** The Consumer swipes a Card right to like it or left to pass. Market Match records that the Card was shown and records the swipe direction, Time-to-Swipe, and dwell time for that Card. These are the inputs to Reach, Likes, Passes, Like Rate, Approval Percentage, Average Decision Time, and Average Dwell Time.

**Preconditions:**

- PRE-1. The Consumer has an active Market session, either signed in through Join Market or anonymous through Public Access.
- PRE-2. The Card belongs to a Category the Consumer chose in that Market.
- PRE-3. The Consumer has not already swiped this Card in this Market session.

**Postconditions:**

- POST-1. A Card impression is stored for the Card, Market, and Market session, with the time the Card was shown.
- POST-2. The swipe is stored against the correct Line Item, Market, Category, and Market session, with its direction, Time-to-Swipe, and dwell time, exactly once.
- POST-3. For a signed-in Consumer, the Consumer's Demographic answers at the moment of the swipe are stored with it.
- POST-4. The system displays the next Card, or completes the Market when no Cards remain.

**Main Success Scenario:**

1. The system displays the Card and records a Card impression with the time it was shown.
2. The Consumer swipes the Card right to like it or left to pass.
3. The system computes Time-to-Swipe (from the time shown to the swipe) and dwell time (from the time shown to the first Flip, or zero if the Card was never flipped, per `UC-FDBK-flip-card`).
4. The system stores the swipe with its direction and both measures, and displays the next Card.

**Extensions:**

- **2a. The Consumer uses the like or pass button instead of a swipe gesture:**
  - 2a1. The system treats the button press as the swipe and measures Time-to-Swipe and dwell time exactly as in step 3. Rejoins at step 3.
- **2b. The gesture does not resolve to left or right:**
  - 2b1. The system returns the Card to center and records no swipe. The impression and timing clock are unchanged. Rejoins at step 2.
- **2c. The Consumer leaves the Market without swiping the Card:**
  - 2c1. The impression from step 1 stays stored and counts toward Reach. No swipe is stored, so the Card counts toward neither Likes nor Passes. The use case ends.
- **4a. The signed-in session has expired:**
  - 4a1. The system keeps the swipe on the device and asks the Consumer to sign in again. After sign-in it submits the kept swipe once and rejoins at step 4. If the Consumer does not sign in, the swipe is not stored and the use case ends.
- **4b. Saving fails or its outcome cannot be confirmed:**
  - 4b1. The system does not advance as if the save succeeded. It retries the same submission. The server recognizes a retry of an already stored swipe and does not store it twice.
- **4c. The Card was the last unswiped Card in the Consumer's chosen Categories:**
  - 4c1. After storing the swipe, the system continues with `UC-FDBK-complete-market` step 8.
- **4d. The Market is the demo Market:**
  - 4d1. The system lets the Consumer swipe but stores nothing that counts toward any Brand, Vendor, or Admin figure. Rejoins at step 4.

**Priority:** High (provisional)
**Frequency of Use:** Once per Card shown and once per swipe. The MVP recorded about 3,600 swipes at one I-Fest. The client's growth scenario is an event where 10,000 people scan one QR Code, so swipes arrive in bursts from many Consumers at once.
**Business Rules:** `BR-rate-product`, `BR-capture-feedback`

**Associated Information:**

| Property name            | Data type                              | Validation rule                                                       | Security or access concerns                                                  | Glossary reference                   |
| ------------------------ | -------------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------ |
| Market session reference | Identifier                             | Required; must be an active session for this Market                   | Derived by the server from the session, never accepted from another Consumer | Market                               |
| Line Item reference      | Identifier                             | Required; must belong to the session's Market and a chosen Category   | Validated by the server                                                      | Line Item; SKU                       |
| Category reference       | Identifier                             | Required; the Category the Card was shown under                       | Validated by the server                                                      | Category                             |
| Shown at                 | Timestamp                              | Required; recorded when the Card is displayed                         | System-captured                                                              | Reach                                |
| Swipe direction          | Enumeration                            | Required; `RIGHT` or `LEFT`; any other value is rejected, not coerced | Consumer-supplied through the swipe                                          | Swipe Left / Swipe Right             |
| Time-to-Swipe            | Duration, milliseconds                 | Required; ≥ 0; shown-at to swipe, for gesture and button swipes alike | Brand sees averages for its own SKUs; Vendor and Admin do not see it         | Time-to-Swipe; Average Decision Time |
| Dwell time               | Duration, milliseconds                 | Required; ≥ 0; shown-at to first Flip, zero if never flipped          | Brand sees averages for its own SKUs; Vendor and Admin do not see it         | Average Dwell Time                   |
| Demographic snapshot     | Gender, age range, ethnicity, location | Copied from the signed-in Consumer's profile; empty for Public Access | Brand sees aggregates only, never one Consumer's answers                     | Demographic                          |
| Submission key           | Identifier                             | Required; unique per swipe attempt; used to detect retries            | System-generated                                                             | (none)                               |

Who sees what, per the third client meeting: a Brand sees per-SKU measures for its own SKUs, totalled across all Markets. A Vendor sees Likes and Passes ranked per Line Item, but not dwell or decision time. The Admin sees swipe counts and users but not Brand or Vendor data points.

The swipe, its measures, and its Demographic snapshot save as one unit or not at all. A failed save leaves no partial swipe.

**Current state in the client's repository:**

- Swipes are stored in `user_responses` and copied with a Demographic snapshot into `brand_swipe_analytics` by `POST /api/responses` and `POST /api/public/responses` in `worker/src/index.ts`.
- The measured times come from `components/SwipeCard.tsx`:
  - `dwellTime` runs from the time the Card is shown to the end of the swipe, so it already matches Time-to-Swipe.
  - `reactionTime` runs from the time shown to the first touch.
  - `front_dwell_ms` and `back_dwell_ms` are cumulative time on each side, which is _not_ the client's dwell time.

Gaps this use case closes:

- No Card impression is recorded. Reach on every dashboard is total swipes, so a Card that was shown and never swiped is not counted.
- Button swipes are sent with zero timings (`App.tsx`).
- The public route coerces unknown directions to `LEFT`.
- There is no unique constraint and no retry detection, so a double submit stores two swipes.
- Average Decision Time is hardcoded to 0 on the Brand Dashboard (`avgSwipeTime`).
- Demo swipes are written to `user_responses` and can leak into Brand and Vendor totals.
- Analytics inserts swallow errors with an empty `catch`, so a failed write is silently lost.

**Related Use Cases:**

- `UC-MKT-enter-market`: Enter a market.
- `UC-PROD-view-product-details`: View product details (optional before rating).
- `UC-FDBK-flip-card`: Flip a card (supplies dwell time).
- `UC-FDBK-open-card-media`: Open a card photo or video.
- `UC-FDBK-complete-market`: Complete a market (invoked after the last Card).

**Assumptions:**

- One swipe per Card per Market session, as the client's app already hides swiped Cards on return.
- Markets the client deliberately loops are an exception left to the client's existing behavior.

**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).

- [OI-9](OPEN-ISSUES.md#open): Should Reach count every Card impression or one per Consumer per Card?
- [OI-10](OPEN-ISSUES.md#open): Are lottery entries (`BR-earn-entry`) in this release's scope?
- [OI-11](OPEN-ISSUES.md#open): What gesture thresholds apply?
- [OI-5](OPEN-ISSUES.md#open): What product ordering applies?
- [OI-12](OPEN-ISSUES.md#open): What retention policy applies to Demographic snapshots?

---

### UC-FDBK-flip-card: Flip a card

**UC ID and Name:** `UC-FDBK-flip-card`: Flip a card
**Created By:** Matthew Stafford
**Date Created:** 2026-10-13
**Primary Actor:** Consumer
**Secondary Actors:** None
**Trigger:** The Consumer taps a displayed Card to turn it over.
**Description:** The Consumer flips a Card to read its back. Market Match records that the Card was flipped and how long after the Card appeared the first Flip happened. That is the Consumer's dwell time for the Card, and the flip is the input to flip rate.

**Preconditions:**

- PRE-1. The Consumer has an active Market session.
- PRE-2. The system is displaying a Card that has a Card impression recorded and has not yet been swiped.

**Postconditions:**

- POST-1. The Card shows its back.
- POST-2. On the first Flip of this Card in this viewing, the Card is marked as flipped, and the time from shown-at to the Flip is held as its dwell time.
- POST-3. The flipped marker and dwell time are stored with the Card's swipe (`UC-FDBK-rate-product` step 4), or with its impression if the Consumer leaves without swiping.

**Main Success Scenario:**

1. The Consumer taps the Card.
2. The system turns the Card to its back.
3. The system records this as the Card's first Flip, holding the time from shown-at to the Flip as dwell time.

**Extensions:**

- **1a. The Consumer swipes without ever flipping:**
  - 1a1. The Card is stored as not flipped with a dwell time of zero, per the client's ruling in the third meeting. Handled in `UC-FDBK-rate-product` step 3.
- **3a. The Card has already been flipped in this viewing:**
  - 3a1. The system turns the Card over, front or back, and does not change the stored dwell time or count another Flip. Time on each side keeps accumulating.
- **3b. The Card's back has no additional information:**
  - 3b1. The Flip is still recorded, because the Consumer chose to flip. The empty-back display is handled in `UC-PROD-view-product-details` extension 2a.
- **3c. The Consumer leaves the Market after flipping but before swiping:**
  - 3c1. The flipped marker and dwell time are stored with the Card impression, so the Flip counts toward flip rate even though the Card has no swipe.

**Priority:** High (provisional)
**Frequency of Use:** At most one recorded first Flip per Card shown. Volume is unknown, because no flip count is stored today.
**Business Rules:** `BR-tap-product`, `BR-capture-feedback`

**Associated Information:**

| Property name       | Data type               | Validation rule                                                  | Security or access concerns                                          | Glossary reference |
| ------------------- | ----------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------- | ------------------ |
| Flipped             | Boolean                 | Required on every stored impression and swipe                    | System-captured; Brand sees flip rate for its own SKUs               | Flip               |
| Dwell time          | Duration, milliseconds  | Required; ≥ 0; zero when not flipped; never reset by later flips | Brand sees averages for its own SKUs; Vendor and Admin do not see it | Average Dwell Time |
| Front and back time | Durations, milliseconds | Optional; cumulative time on each side, as captured today        | Brand only                                                           | Card               |

**Current state in the client's repository:**

- `components/SwipeCard.tsx` toggles `isFlipped` on tap but never sends a Flip. Only cumulative `front_dwell_ms` and `back_dwell_ms` reach the server (`user_responses`, migration `0005`).
- Front time equals the client's dwell time only when the Consumer flips once and never flips back.
- Flip rate is hardcoded to 0 on the Brand and Vendor Dashboards.
- `buildAnalyticsFromApiData` in `components/BrandDashboard.tsx` stores Approval Percentage in a field named `flipRate`.
- Nothing is recorded for a Card the Consumer flips and then abandons.

**Related Use Cases:**

- `UC-PROD-view-product-details`: View product details. The same Consumer action; that use case covers what is shown, this one what is recorded.
- `UC-FDBK-rate-product`: Rate a product.

**Assumptions:**

- A Flip is a tap that turns the Card over, as it is in the client's app today.
- Opening a photo or video is a Click (`UC-FDBK-open-card-media`), not a Flip.

**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).

- [OI-13](OPEN-ISSUES.md#open): Is flip rate the share of Card impressions that were flipped, or the share of swipes whose Card was flipped?
- [OI-14](OPEN-ISSUES.md#open): Should the existing front and back time be kept now that dwell time is defined to the first Flip?

---

### UC-FDBK-open-card-media: Open a card photo or video

**UC ID and Name:** `UC-FDBK-open-card-media`: Open a card photo or video
**Created By:** Matthew Stafford
**Date Created:** 2026-10-13
**Primary Actor:** Consumer
**Secondary Actors:** YouTube, which hosts the video
**Trigger:** The Consumer taps one of a Card's photos or its video.
**Description:** The Consumer opens a photo or the video on a Card. Market Match records a Click against that specific piece of media, so a Brand can see which photos and video draw attention and swap out what does not.

**Preconditions:**

- PRE-1. The Consumer has an active Market session.
- PRE-2. The system is displaying a Card that has at least one photo or a video. A Text Card has neither.

**Postconditions:**

- POST-1. A Click is stored against the Line Item, the media's slot (photo 1, 2, 3, or video), the specific media item in that slot, the Market, and the Market session.
- POST-2. The system displays the opened photo or video.

**Main Success Scenario:**

1. The Consumer taps a photo or the video on the Card.
2. The system records a Click for that media item.
3. The system displays the photo or plays the video.

**Extensions:**

- **1a. The photo is the front photo shown automatically when the Card appears:**
  - 1a1. Its automatic display is not a Click. The Card impression covers it. A deliberate tap back to the front photo is a Click. Rejoins at step 2.
- **1b. The Consumer taps the same media again in the same viewing:**
  - 1b1. The system records another Click with its own time. Whether reports count every Click or one per Consumer is an open issue, and storing each Click supports either.
- **2a. Recording the Click fails:**
  - 2a1. The system still displays the media, because a lost Click must not block the Consumer. It retries the Click without duplicating it, and if it cannot, the failure is logged rather than silently dropped.
- **3a. The video cannot be loaded from YouTube:**
  - 3a1. The Click stays recorded, because the Consumer's tap is the data point. The system shows that the video is unavailable, and the Consumer returns to the Card.
- **3b. Opening the video takes the Consumer out of Market Match to YouTube:**
  - 3b1. The Click is recorded before the Consumer leaves. Watch time is not measured, because the client said the Brand reads that from YouTube.

**Priority:** Medium (provisional)
**Frequency of Use:** Zero or more per Card shown. Volume is unknown, because no Clicks are captured today.
**Business Rules:** `BR-capture-feedback`, `BR-media-clicks`

**Associated Information:**

| Property name            | Data type   | Validation rule                                                                | Security or access concerns | Glossary reference |
| ------------------------ | ----------- | ------------------------------------------------------------------------------ | --------------------------- | ------------------ |
| Line Item reference      | Identifier  | Required; must belong to the session's Market                                  | Validated by the server     | Line Item; SKU     |
| Media slot               | Enumeration | Required; `PHOTO_1`, `PHOTO_2`, `PHOTO_3`, or `VIDEO`; must exist on the Card  | System-captured             | Card; Clicks       |
| Media item               | Identifier  | Required; identifies the specific photo or video link in the slot when clicked | System-captured             | Clicks             |
| Clicked at               | Timestamp   | Required                                                                       | System-captured             | Clicks             |
| Market session reference | Identifier  | Required                                                                       | Derived by the server       | Market             |

Clicks are tied to the specific media item, not just its slot. The client's stated reason for Clicks is that a Brand swaps a photo when it gets little traction. Counting by slot alone would merge the old photo's Clicks with its replacement's.

Only the owning Brand sees Clicks, totalled per media item across all Markets.

**Current state in the client's repository:**

- No Clicks are captured.
- `SwipeAnalytics.mediaClicks` is declared in `types.ts` but never filled. The Brand Dashboard's media Clicks section renders an empty object.
- The video is an autoplaying muted iframe with `pointer-events-none` (`components/SwipeCard.tsx`), so it cannot be tapped today.
- What is captured is the time each carousel slot is displayed. `media_views` is keyed by slot labels such as `'Image 1 (Front)'` and `'Video'`, signed-in swipes only, and holds no media item identity.

**Related Use Cases:**

- `UC-FDBK-rate-product`: Rate a product.
- `UC-FDBK-flip-card`: Flip a card.
- `UC-BRND-create-product`: Create a product (supplies the media).

**Assumptions:**

- A Click is any deliberate tap that opens or navigates to a photo or the video, including carousel navigation.

**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).

- [OI-15](OPEN-ISSUES.md#open): Does navigating the photo carousel count as a Click, or only tapping to enlarge?
- [OI-16](OPEN-ISSUES.md#open): Should reports count every Click or one per Consumer per media item?
- [OI-17](OPEN-ISSUES.md#open): Should per-media display time (`media_views`) be kept now that the client wants Clicks?

---

### UC-FDBK-complete-market: Complete a market

**UC ID and Name:** `UC-FDBK-complete-market`: Complete a market
**Created By:** Matthew Stafford
**Date Created:** 2026-10-13
**Primary Actor:** Consumer
**Secondary Actors:** None
**Trigger:** The Consumer enters a Market Code in Join Market, or opens a Public Access link or QR Code.
**Description:** The Consumer goes through a Market from entry to the last Card of the Categories they chose. Market Match records each Engagement Funnel stage as the Consumer reaches it. Brands and Vendors can then see how many Consumers entered, viewed, started, and completed a Market, and the average Completion Time.

**Preconditions:**

- PRE-1. The Market has been launched.
- PRE-2. For a Market Code, the Consumer is signed in. For a Public Access link, the Market is set to Public Access.

**Postconditions:**

- POST-1. A Market session is stored with the time of each funnel stage the Consumer reached: entered, viewed, started, and completed.
- POST-2. The Categories the Consumer chose are stored with the Market session.
- POST-3. On completion, the Market session is marked complete with its completed-at time, from which Completion Time is derived.

**Main Success Scenario:**

1. The Consumer enters the Market Code in Join Market, or opens the Public Access link.
2. The system validates the Market, starts a Market session, and records the _entered_ stage with its time.
3. The system displays the Market's Categories.
4. The Consumer chooses one or more Categories.
5. The system stores the chosen Categories, displays the first Card, and records the _viewed_ stage with its time.
6. The Consumer swipes the first Card (`UC-FDBK-rate-product`).
7. The system records the _started_ stage with its time. The Consumer swipes the remaining Cards in the chosen Categories, each through `UC-FDBK-rate-product`.
8. After the last Card in the chosen Categories is swiped, the system records the _completed_ stage, marks the Market session complete, and shows the Consumer that the Market is finished.

**Extensions:**

- **2a. The Market Code is blank, unknown, or the Market is not accessible:**
  - 2a1. Handled by `UC-MKT-enter-market` extension 4a. No Market session is started.
- **2b. The Market session cannot be stored:**
  - 2b1. The system reports that the Market could not be opened and does not show Cards. A swipe needs a stored session to belong to. The Consumer retries from step 1.
- **2c. The Consumer has an incomplete Market session for this Market, either signed in or as the same Anonymous Consumer (`UC-MKT-create-anonymous-consumer` extension 2a):**
  - 2c1. The system resumes that session instead of starting a new one, records the resume time, and shows only Cards not yet swiped. Rejoins at step 5 if Categories were chosen, otherwise at step 3.
- **2d. The Market is the demo Market:**
  - 2d1. The system lets the Consumer go through it but records no funnel stages. The use case continues without capture.
- **4a. The Consumer leaves before choosing a Category:**
  - 4a1. The Market session stays stored, reached _entered_ only. The use case ends.
- **5a. The chosen Categories contain no Cards:**
  - 5a1. The system shows that there is nothing to swipe. The session reached _entered_ only. The use case ends.
- **7a. The Consumer stops partway and leaves:**
  - 7a1. The Market session stays incomplete with its stages so far and the time of its last swipe. It counts as _started_ but not _completed_ in the funnel. The Consumer can resume through extension 2c, signed in or as the same unexpired Anonymous Consumer.
  - 7a2. A Public Access Consumer who returns on the same device before their Anonymous Consumer expires resumes the same Market session (extension 2c), as the client described for a return at the 26th of 50 Cards (fourth client meeting, lines 146–148). One who returns from another device, or after expiry, starts a new Market session as a new Anonymous Consumer.
- **8a. The Consumer chooses more Categories after completing the chosen ones:**
  - 8a1. The system records the added Categories against the same Market session. How this affects completion is an open issue.

**Priority:** High (provisional). The client called the Engagement Funnel and Completion Time what he most wants to showcase for a Brand Market.
**Frequency of Use:** One Market session per Consumer per Market visit. A single QR Code event in the client's growth scenario starts up to 10,000 sessions in a short window.
**Business Rules:** `BR-select-market`, `BR-code-requires-sign-in`, `BR-public-market`, `BR-select-category`, `BR-capture-feedback`, `BR-engagement-funnel`, `BR-market-completion-time`

**Associated Information:**

| Property name     | Data type           | Validation rule                                                         | Security or access concerns                                  | Glossary reference         |
| ----------------- | ------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------ | -------------------------- |
| Market session    | Identifier          | Required; system-generated at step 2                                    | Anonymous for Public Access; tied to the user when signed in | Market                     |
| Entry method      | Enumeration         | Required; `MARKET_CODE` or `PUBLIC_ACCESS`                              | System-captured                                              | Market Code; Public Access |
| Entered at        | Timestamp           | Required                                                                | System-captured                                              | Engagement Funnel          |
| Chosen Categories | List of identifiers | Required once chosen; each must belong to the Market                    | System-captured                                              | Category                   |
| Viewed at         | Timestamp           | Set at step 5                                                           | System-captured                                              | Engagement Funnel          |
| Started at        | Timestamp           | Set at the first stored swipe                                           | System-captured                                              | Engagement Funnel          |
| Completed at      | Timestamp           | Set when every Card in the chosen Categories is swiped; empty otherwise | System-captured                                              | Completion Time            |
| Last activity at  | Timestamp           | Updated on every stored swipe                                           | System-captured                                              | Completion Time            |

**Who sees what:**

- Brand Market: the owning Brand sees the funnel counts and average Completion Time.
- Standard Market: the Vendor sees the average Completion Time and, possibly, the funnel.
- No dashboard shows a single Consumer's session.
- Completion Time is derived from the stored timestamps rather than stored itself. The resume-gap rule is still open, and timestamps allow either rule to be computed later.

**Current state in the client's repository:**

- A Market session (`completed_markets`) is created on the Consumer's _first swipe_, not when the code is entered. Entering a code and leaving records nothing, and the _entered_ and _viewed_ stages are not captured.
- Despite its name, a `completed_markets` row does not mean completion. No completed-at, completion flag, or chosen Categories reach the server.
- `completeSurvey` in `App.tsx` only updates browser storage.
- A signed-in Consumer gets a new session row on each visit. Resume works in the browser only.
- The Admin Dashboard's Engagement Funnel (`components/admin/UserAnalytics.tsx`) is hardcoded percentages.
- Public Access sessions all use the `anonymous-public` user, so they cannot be told apart beyond the session id.

**Related Use Cases:**

- `UC-MKT-enter-market`: Enter a market (step 1 for a Market Code).
- `UC-FDBK-rate-product`: Rate a product (steps 6–7).

**Assumptions:**

- A Market is complete when every Line Item in the Categories the Consumer chose has been swiped, not every Category in the Market. Decided by the team on 2026-10-13 from the client's five-choose-three example; not yet confirmed with the client.
- Public Access Consumers are captured through an Anonymous Consumer (`UC-MKT-create-anonymous-consumer`), with _entered_ recorded when the link is opened.

**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).

- [OI-18](OPEN-ISSUES.md#open): Does Completion Time include time away from a Market the Consumer stopped and resumed, or only active time?
- [OI-19](OPEN-ISSUES.md#open): Does the funnel clock start at code entry (the client's first description) or when the first Card is viewed (his later description)? Both timestamps are captured so either can be reported.
- [OI-20](OPEN-ISSUES.md#open): How do Categories chosen after completion affect completion?
- [OI-21](OPEN-ISSUES.md#open): Should Vendors see the full Engagement Funnel or only Completion Time?
- [OI-22](OPEN-ISSUES.md#open): Is the funnel shown per Brand Market only, or also per Standard Market?

---

## BRND: Brand Participation

These use cases cover how a Brand's products get into Market Match and reach Consumers: one at a time (`UC-BRND-create-product`), many at once by spreadsheet (`UC-BRND-import-products`) or straight from the Brand's own system through Market Match's API (`UC-BRND-send-products`), changed later (`UC-BRND-update-product`), removed (`UC-BRND-remove-product`), and reviewed by the Admin before any Consumer sees them (`UC-BRND-approve-product`). `UC-BRND-generate-api-key` is how the Admin gives a Brand the API Key its own system needs. Together they cover `FEAT-product-management` and `FEAT-bulk-product-import`.

Every way in ends in the same place: a submitted product, or a change to one, waits for the Admin's Approval and no Consumer sees it until he approves it. A Brand identifies each product by its own SKU, unique within that Brand (another Brand may use the same SKU), which is how Market Match recognizes a product it already has: submitting a SKU the Brand already has changes that product (`AS-stable-product-id` in [vision and scope](vision-and-scope.md)). Each product belongs to one of the Brand's own Categories, which the Brand creates (`BR-brand-categories`). A Brand sends 10 to 200 SKUs at a time today, and expects to send new batches as new designs come out, up to 500 SKUs before an event (fifth client meeting).

A Brand also sees, for every product it has submitted however it arrived, whether it is waiting, approved, or returned and why. That list is part of each use case's postconditions rather than a use case of its own.

---

### UC-BRND-create-product: Create a product

**UC ID and Name:** `UC-BRND-create-product`: Create a product
**Created By:** Chris Ramirez; revised by Matthew Stafford
**Date Created:** 2026-09-14; revised 2026-10-25 and 2026-10-28
**Primary Actor:** Brand
**Secondary Actors:** Admin, who reviews the product (`UC-BRND-approve-product`)
**Trigger:** The Brand chooses to add a product to its Inventory.
**Description:** The Brand supplies one product's content through Market Match and puts it in one of its Categories. Market Match stores it in the Brand's Inventory as waiting for Approval, so the Admin reviews it before any Consumer sees it.

**Preconditions:**

- PRE-1. The user is signed in with the Brand role and belongs to a Brand's Organization.

**Postconditions:**

- POST-1. The product is stored in the Brand's Inventory under the Brand's SKU and in the Category the Brand chose, waiting for Approval.
- POST-2. No Consumer can see the product.
- POST-3. The product is in the Admin's list of products waiting for Approval.
- POST-4. The product is in the Brand's list of submitted products, shown as waiting for Approval.

**Main Success Scenario:**

1. The Brand chooses to add a product.
2. The system asks for the product's SKU, whether it is a Card or a Text Card, its title, description, price, and Category, and, for a Card, its photos and video, and offers the Brand's existing Categories.
3. The Brand supplies the content, including at least one photo for a Card's front, chooses a Category, and submits it.
4. The system checks the content against the required fields and media limits, and checks that the SKU is not already one of the Brand's products.
5. The system stores the product in the Brand's Inventory as waiting for Approval and confirms it to the Brand.

**Extensions:**

- **3a. The Brand cancels before submitting:**
  - 3a1. No product is created. The use case ends.
- **3b. The product is a Text Card:**
  - 3b1. The Brand supplies the title and the text only. Photos and a video are not asked for. Rejoins at step 4.
- **3c. The product is a Card:**
  - 3c1. The Brand supplies one to three photos, the first being the Card's front, and may add one video link. Rejoins at step 4.
- **3d. The Category the product belongs in does not exist yet:**
  - 3d1. The Brand names a new Category. The system creates it for this Brand only and selects it. Rejoins at step 3.
- **4a. A required field is missing or a field is invalid:**
  - 4a1. The system names each failing field and stores nothing; the form keeps what the Brand typed. The Brand corrects it and returns to step 3, or cancels.
- **4b. A Card has no photo, more than three photos, or more than one video link, or a photo is not JPEG or PNG or is 3 MB or larger:**
  - 4b1. As 4a, naming the photo and the limit it breaks.
- **4c. The video link is not a YouTube or Vimeo link:**
  - 4c1. As 4a, naming the video link and the sites accepted.
- **4d. The SKU is already one of the Brand's products:**
  - 4d1. The system says the SKU is already one of the Brand's products, stores nothing, and offers to change that product instead (`UC-BRND-update-product`).
- **4e. The Brand's access was removed after the form was opened:**
  - 4e1. The system stores nothing and tells the user they no longer have access. The use case ends.
- **5a. Saving fails:**
  - 5a1. The system reports that the product was not saved. Nothing is stored, including a Category created in 3d; the form keeps what the Brand typed so it can submit again.

**Priority:** High (provisional). Built after `UC-BRND-generate-api-key`, the proving slice (`v0.1.0`), as the first slice through every product layer, from a signed-in Brand through the API to the database and media storage.
**Frequency of Use:** Once per new product. Most of a Brand's 10 to 200 SKUs are expected to arrive through `UC-BRND-import-products` or `UC-BRND-send-products`; this use case is for a product added by hand.
**Business Rules:** `BR-submit-product`, `BR-products-brand-only`, `BR-approve-product`, `BR-text-card`, `BR-product-media-limit`, `BR-photo-size`, `BR-brand-categories`

**Associated Information:**

These are the fields the client fills in today (fifth client meeting); a longer list of product details that varies by kind of product is to come from him (`OI-55`).

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| SKU | String | Required; unique within the Brand's Inventory; cannot be changed later | Supplied by the Brand; identifies the product on later imports | SKU |
| Card type | Enumeration | Required; `CARD` or `TEXT_CARD` | Supplied by the Brand | Card; Text Card |
| Title | String | Required; the client set no length limit, so the design sets one | Shown to Consumers once approved | Card |
| Description | String | Required | Shown to Consumers once approved | Card |
| Price | Decimal | Optional; ≥ 0 | Shown only where a Market shows prices | Line Item |
| Category | Identifier | Required; one of the Brand's own Categories, or a new one the Brand names (3d) | A Brand sees and uses only its own Categories | Category |
| Photos | One to three images | Cards only; the first is the front; each JPEG or PNG and under 3 MB | Shown to Consumers once approved | Card |
| Video link | URL | Cards only; optional; at most one; a YouTube or Vimeo link | Shown to Consumers once approved | Card |

The client also accepts other video sites and video files (fifth client meeting). This release takes YouTube and Vimeo links only (team decision, 2026-10-28): other sites wait for his list, and video files wait for his answer on their size and on storing them, which adds to his Cloudflare storage (`OI-57`). Adding either later is a new extension here, not a change to this flow.
| Brand reference | Identifier | Required; taken from the signed-in user's Organization, never from input | A Brand creates products only in its own Inventory | Brand |
| Approval status | Enumeration | Set by the system: `WAITING`, `APPROVED`, or `RETURNED` | Only the Admin changes it, in `UC-BRND-approve-product` | Approval |

**Current state in the client's repository:**
- A Brand's "Add Item" saves the product as `ACTIVE`, live at once, with no Approval (`components/BrandDashboard.tsx`; `POST /api/products` in `worker/src/index.ts`).
- When no SKU is given, the server makes one up (`SKU-<timestamp>`), and nothing keeps SKUs unique.
- The server allows any image type up to 5 MB and uploaded videos up to 25 MB, not the client's JPEG or PNG under 3 MB, and accepts YouTube and Vimeo links as well as uploaded video.
- Only the Admin can create Categories (`POST /api/categories`), and a Category belongs to an Organization (`categories.org_id` in `worker/src/schema.ts`).

**Related Use Cases:**
- `UC-BRND-import-products` and `UC-BRND-send-products`: many products at once.
- `UC-BRND-update-product`: change the product later.
- `UC-BRND-remove-product`: remove it.
- `UC-BRND-approve-product`: the Admin's review that follows.
- `UC-PROD-view-product-details`: what a Consumer sees once the product is approved and in a Market.

**Assumptions:**
- Brands send prices along with their products, as they do today (fourth client meeting). A price is optional because Text Cards and many surveys have none.

**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).
- [OI-57](OPEN-ISSUES.md#open): Which other video sites, and may Brands send video files, how large, and stored in Market Match? Not needed for this release, which takes YouTube and Vimeo links only.
- [OI-55](OPEN-ISSUES.md#open): Which further product details, by kind of product? Phase 1 uses the fields above.
- Resolved in the fifth client meeting: required fields for phase 1 ([OI-23](OPEN-ISSUES.md#resolved)), JPEG or PNG under 3 MB ([OI-24](OPEN-ISSUES.md#resolved)), video links ([OI-38](OPEN-ISSUES.md#resolved)), the Brand chooses the Category ([OI-39](OPEN-ISSUES.md#resolved)), and an existing SKU changes that product ([OI-40](OPEN-ISSUES.md#resolved)).
- [OI-25](OPEN-ISSUES.md#resolved) and [OI-26](OPEN-ISSUES.md#resolved) (resolved): who may create products, and how an approved product reaches a Market. See [Approval](project-glossary.md#approval), [Inventory](project-glossary.md#inventory), and [Category](project-glossary.md#category).

---

### UC-BRND-import-products: Import products from a spreadsheet

**UC ID and Name:** `UC-BRND-import-products`: Import products from a spreadsheet
**Created By:** Matthew Stafford
**Date Created:** 2026-10-25; revised 2026-10-28
**Primary Actor:** Brand
**Secondary Actors:** Admin, who reviews the imported products (`UC-BRND-approve-product`)
**Trigger:** The Brand chooses to import a spreadsheet of products.
**Description:** The Brand submits one spreadsheet listing many products, typically 10 to 200 SKUs. Market Match checks every row, stores each valid one waiting for Approval, and tells the Brand which rows failed and why. This replaces the Brand sending a Google Drive of photos and details that the client copies in by hand, at a minute to a minute and a half per product. Whether the client wants spreadsheet import at all, or only the API, is open; this use case stands until he answers.

**Preconditions:**

- PRE-1. The user is signed in with the Brand role and belongs to a Brand's Organization.

**Postconditions:**

- POST-1. Each valid row is stored in the Brand's Inventory, waiting for Approval: as a new product when its SKU is new to the Brand, or as a change to the existing product when it is not.
- POST-2. No failed row is stored.
- POST-3. No Consumer sees any imported product or change until the Admin approves it.
- POST-4. Every Category a valid row names that the Brand did not have exists, for this Brand only.
- POST-5. The Brand has a result for every row: received for Approval, or failed with its reasons. The received products are in the Brand's list of submitted products.

**Main Success Scenario:**

1. The Brand chooses to import products.
2. The system provides the spreadsheet layout it accepts, one row per product.
3. The Brand submits a filled-in spreadsheet.
4. The system checks every row against the required fields and media limits, and checks that no SKU appears on more than one row.
5. The system shows the Brand how many rows are new products, how many change existing products, which new Categories they create, and which rows fail and why.
6. The Brand confirms the import.
7. The system stores each valid row as waiting for Approval and reports the result for every row.

**Extensions:**

- **3a. The file is not a spreadsheet the system accepts, or it has no rows:**
  - 3a1. The system says so and stores nothing. Which file types are accepted is open. The Brand returns to step 3 or cancels.
- **3b. Required columns are missing or not recognized:**
  - 3b1. The system names the missing columns and stores nothing. The Brand corrects the spreadsheet and returns to step 3.
- **3c. The spreadsheet has more rows than one import accepts:**
  - 3c1. The system says so, giving the limit (`SCA-import-batch-limit`), and stores nothing. The Brand splits it and imports each part.
- **4a. A row is missing a required field or has an invalid one:**
  - 4a1. The system marks that row failed, naming its SKU and each reason. The other rows are unaffected.
- **4b. The same SKU appears on more than one row:**
  - 4b1. The system marks every one of those rows failed, naming the SKU, because it cannot tell which is meant. The other rows are unaffected.
- **4c. A row's photo cannot be retrieved from its link, is not JPEG or PNG, or is 3 MB or larger:**
  - 4c1. The system marks that row failed, naming the SKU and the photo.
- **4d. A row's SKU is already one of the Brand's products:**
  - 4d1. The row is shown as a change to that product.
- **4e. A row names a Category the Brand does not have:**
  - 4e1. The row is shown as creating that Category, so the Brand can catch a misspelled name before confirming.
- **5a. Every row fails:**
  - 5a1. There is nothing to import. The Brand corrects the spreadsheet and returns to step 3, or cancels.
- **6a. The Brand cancels instead of confirming:**
  - 6a1. Nothing is stored. The use case ends.
- **7a. A row's SKU matches a product or change still waiting for Approval:**
  - 7a1. The row replaces the waiting version, so the Admin reviews only the latest.
- **7b. A row's SKU matches a product the Brand removed:**
  - 7b1. The row is stored as a new product. The removed product and its results stay apart from it (`UC-BRND-remove-product`).
- **7c. Storing stops partway through:**
  - 7c1. The system reports which rows were stored. Importing the same spreadsheet again stores the rest without duplicating any row, because each row is matched by its SKU.
- **\*a. At any step, the Brand's access is removed:**
  - \*a1. The system stores nothing the Brand has not yet confirmed and tells the user they no longer have access.

**Priority:** High (provisional), pending the client's answer on whether he wants spreadsheet import.
**Frequency of Use:** Once when a Brand joins, then once per new batch of products, such as a clothing Brand's new designs. Each import carries 10 to 200 rows; a Brand with more sends several.
**Business Rules:** `BR-submit-product`, `BR-products-brand-only`, `BR-approve-product`, `BR-text-card`, `BR-product-media-limit`, `BR-photo-size`, `BR-brand-categories`

**Associated Information:**

One spreadsheet row carries the same product fields as `UC-BRND-create-product` (SKU, card type, title, description, price, Category by name, up to three photo links, a video link), with photos and video given as links rather than files. The import adds:

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| Row number | Integer | Set by the system | Shown only to the importing Brand | (none) |
| Row result | Enumeration | `NEW`, `CHANGE`, or `FAILED` with the SKU and reasons | Shown only to the importing Brand | Approval |
| Brand reference | Identifier | Taken from the signed-in user's Organization for every row, never from the spreadsheet | A spreadsheet cannot write into another Brand's Inventory or Categories | Brand |

Market Match downloads each linked photo when the row is checked and keeps its own copy, so the Card never depends on the Brand's website (`KD-photos-copied` in the [architecture](../design/architectural-design.md)). This is what the client does by hand today, storing every photo in Market Match from the Brand's Google Drive (fifth client meeting).

**Current state in the client's repository:**
- A four-step CSV wizard (`components/brand/csv/`) checks rows in the browser only. The client has not tried it (fourth client meeting).
- `POST /api/products/bulk` (`worker/src/index.ts`) checks nothing on the server, stores every row as `ACTIVE` with no Approval, and always creates new products: a repeated SKU becomes a duplicate, and a blank one is made up. It saves each photo link as given.
- The Admin's CSV upload (`components/admin/GlobalInventoryManager.tsx`) skips the row checks entirely.

**Related Use Cases:**
- `UC-BRND-create-product`: the same product, one at a time.
- `UC-BRND-send-products`: the same import, sent from the Brand's own system.
- `UC-BRND-approve-product`: the Admin's review that follows.

**Assumptions:**
- Brands fill in Market Match's spreadsheet layout rather than each sending its own. The client called that "a reasonable ask" for smaller Brands (fourth client meeting).
- `AS-stable-product-id`: a Brand keeps the same SKU for a product from one import to the next.

**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).
- [OI-43](OPEN-ISSUES.md#open): Does the client want spreadsheet import, or only the API?
- [OI-36](OPEN-ISSUES.md#open): Which spreadsheet file types must an import accept?
- [OI-57](OPEN-ISSUES.md#open): Which video sites besides YouTube and Vimeo?
- Resolved in the fifth client meeting: [OI-23](OPEN-ISSUES.md#resolved), [OI-24](OPEN-ISSUES.md#resolved), [OI-32](OPEN-ISSUES.md#resolved), [OI-39](OPEN-ISSUES.md#resolved), and [OI-40](OPEN-ISSUES.md#resolved).

---

### UC-BRND-send-products: Send products from a connected system

**UC ID and Name:** `UC-BRND-send-products`: Send products from a connected system
**Created By:** Matthew Stafford
**Date Created:** 2026-10-25; revised 2026-10-28
**Primary Actor:** The Brand's product system, wherever the Brand already keeps its products (one prospective partner uses a Shopify store)
**Secondary Actors:** Admin, who reviews the products (`UC-BRND-approve-product`)
**Trigger:** The Brand's product system sends a batch of products to Market Match's API.
**Description:** A Brand sends its products straight from the system where it keeps them, the way a seller connects to Shopify: Market Match publishes an API for products, and the Brand's system calls it with the API Key the Admin gave the Brand. No one types or uploads anything in Market Match. Market Match checks each product, stores each valid one waiting for Approval, and answers with a result for every product so the Brand's system knows what to fix. The API Key alone decides which Brand the products belong to.

**Preconditions:**

- PRE-1. The Brand has an active API Key (`UC-BRND-generate-api-key`).

**Postconditions:**

- POST-1. Each valid product is stored in the API Key's Brand's Inventory, waiting for Approval: as a new product when its SKU is new to the Brand, or as a change when it is not.
- POST-2. No failed product is stored.
- POST-3. No Consumer sees any product or change until the Admin approves it.
- POST-4. Every Category a valid product names that the Brand did not have exists, for this Brand only.
- POST-5. The Brand's system has a result for every product: received for Approval, or failed with its SKU and reasons. The received products are in the Brand's list of submitted products.

**Main Success Scenario:**

1. The Brand's system sends a batch of products with its API Key.
2. The system confirms that the API Key is active and finds the one Brand it belongs to.
3. The system checks every product against the required fields and media limits, and checks that no SKU appears twice in the batch.
4. The system stores each valid product in that Brand's Inventory as waiting for Approval, in the Category it names.
5. The system answers with the result for every product.

**Extensions:**

- **1a. The batch is not in the form Market Match's API accepts:**
  - 1a1. The system rejects the whole batch with the reason and stores nothing.
- **1b. The batch names a Brand other than the API Key's Brand, or a product belonging to another Brand:**
  - 1b1. The system rejects the whole batch, stores nothing, and records the attempt so the Admin can see it. A batch never needs to name a Brand, because the API Key decides it.
- **2a. The API Key is unknown, has been replaced by a newer one, or has been revoked, or the Brand's access has been removed:**
  - 2a1. The system rejects the batch, stores nothing, and records the attempt so the Admin can see it.
- **2b. The batch has more products than one sending accepts:**
  - 2b1. The system rejects the batch with the limit (`SCA-import-batch-limit`), and the Brand's system sends smaller batches; a Brand with 500 SKUs sends three.
- **3a. A product is missing a required field or has an invalid one, including a Card with no photo or too many, a photo that is not JPEG or PNG or is 3 MB or larger, or a video link Market Match does not accept:**
  - 3a1. The system marks that product failed, naming its SKU and each reason. The other products are unaffected.
- **3b. The same SKU appears more than once in the batch:**
  - 3b1. The system marks each of those products failed, naming the SKU. The other products are unaffected.
- **3c. A product's photo cannot be retrieved from its link:**
  - 3c1. The system marks that product failed, naming the SKU and the photo.
- **4a. A product's SKU is already one of the Brand's products:**
  - 4a1. It is stored as a change to that product.
- **4b. A product's SKU matches a product or change still waiting for Approval:**
  - 4b1. The new one replaces the waiting version, so the Admin reviews only the latest.
- **4c. A product names a Category the Brand does not have:**
  - 4c1. The system creates that Category for the Brand and says so in the product's result.
- **4d. A product's SKU matches a product the Brand removed:**
  - 4d1. It is stored as a new product. The removed product and its results stay apart from it.
- **4e. Storing stops partway through:**
  - 4e1. Products already stored stay stored. The Brand's system sends the same batch again, and the rest are stored without duplicates, because each product is matched by its SKU.

**Priority:** High (provisional). This is the capability prospective partners asked for, and whose absence stopped those conversations (fourth client meeting).
**Frequency of Use:** Once when a Brand connects, then once per new batch of products. 10 to 200 SKUs at a time today; up to 500 before an event, sent as several batches.
**Business Rules:** `BR-connect-product-system`, `BR-products-brand-only`, `BR-approve-product`, `BR-text-card`, `BR-product-media-limit`, `BR-photo-size`, `BR-brand-categories`

**Associated Information:**

Each product carries the same fields as `UC-BRND-create-product`, with the Category by name and photos and video given as links. Sending adds:

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| API Key | Secret | Required; must be active | Decides the only Brand the batch can write to; never echoed back in a result | API Key |
| Product result | Enumeration | `NEW`, `CHANGE`, or `FAILED` with the SKU and reasons, one per product | Returned only to the caller holding that API Key | Approval |

Market Match publishes the contract the Brand's system must follow: the fields, their format, the batch limit, and the results it returns. That contract is an external interface in the [software requirements specification](software-requirements-specification.md) (`FR-API-published-contract`), not part of this use case. As with a spreadsheet, Market Match downloads each linked photo and keeps its own copy (`KD-photos-copied`). How the API Key is checked and how a batch is delivered are decided in the architecture (`KD-api-key-storage`, `KD-import-in-request`).

**Current state in the client's repository:**
- No system can call Market Match without a signed-in user. Every protected route reads the `mm_session` cookie (`worker/src/middleware/auth.ts`), and there is no API Key of any kind.

**Related Use Cases:**
- `UC-BRND-generate-api-key`: how the Admin gives the Brand its API Key.
- `UC-BRND-import-products`: the same import, by spreadsheet.
- `UC-BRND-create-product`: one product at a time, by a person in Market Match, where this use case is many products at once from the Brand's own system with no person in Market Match.
- `UC-BRND-approve-product`: the Admin's review that follows.

**Assumptions:**
- The Brand's developers have Market Match's published product contract and build their system's side against it.
- `AS-stable-product-id`: the Brand's system keeps the same SKU for a product from one sending to the next.
- `AS-org-can-supply-products`: the Brand's system can send its products in the form Market Match accepts.

**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).
- [OI-55](OPEN-ISSUES.md#open): Which further product details, by kind of product? They widen the published contract.
- [OI-57](OPEN-ISSUES.md#open): Which video sites besides YouTube and Vimeo?
- Resolved in the fifth client meeting: [OI-23](OPEN-ISSUES.md#resolved), [OI-24](OPEN-ISSUES.md#resolved), [OI-31](OPEN-ISSUES.md#resolved), [OI-32](OPEN-ISSUES.md#resolved), [OI-39](OPEN-ISSUES.md#resolved), and [OI-40](OPEN-ISSUES.md#resolved).

---

### UC-BRND-update-product: Update a product

**UC ID and Name:** `UC-BRND-update-product`: Update a product
**Created By:** Matthew Stafford
**Date Created:** 2026-10-25; revised 2026-10-28
**Primary Actor:** Brand
**Secondary Actors:** Admin, who reviews the change (`UC-BRND-approve-product`)
**Trigger:** The Brand chooses to change one of its products.
**Description:** The Brand changes a product's photos, video, details, or Category through Market Match, including fixing a product the Admin returned. The change waits for the Admin's Approval before any Consumer sees it. Once approved, the product's results start fresh, and its earlier results are kept for comparison.

**Preconditions:**

- PRE-1. The user is signed in with the Brand role and belongs to a Brand's Organization.
- PRE-2. The Brand's Inventory has at least one product.

**Postconditions:**

- POST-1. The change is stored against the product, waiting for Approval.
- POST-2. No Consumer sees the change until the Admin approves it. What Consumers see of the product in the meantime is open.
- POST-3. The change is in the Admin's list of products waiting for Approval, marked as a change, and in the Brand's list of submitted products.
- POST-4. Once the Admin approves the change, the product's data points (swipes, Clicks, viewing times) start fresh from that moment, and those from before it are kept and reported to the Brand as the earlier period, dated by the change.

**Main Success Scenario:**

1. The Brand chooses one of its products.
2. The system shows the product's current content and its Approval status.
3. The Brand changes the content and submits it.
4. The system checks the content against the required fields and media limits.
5. The system stores the change as waiting for Approval and confirms it to the Brand.

**Extensions:**

- **1a. The product belongs to another Brand:**
  - 1a1. The system refuses and shows nothing of it. The use case ends.
- **3a. The Brand cancels:**
  - 3a1. Nothing changes. The use case ends.
- **3b. The Brand tries to change the SKU:**
  - 3b1. The system does not allow it, because the SKU is how later imports find this product. To use a different SKU, the Brand creates a new product (`UC-BRND-create-product`) and may remove the old one (`UC-BRND-remove-product`).
- **3c. The Brand moves the product to a Category it does not have yet:**
  - 3c1. As `UC-BRND-create-product` extension 3d.
- **4a. The content fails the checks:**
  - 4a1. As `UC-BRND-create-product` extensions 4a to 4c. Nothing is stored; the form keeps what the Brand typed. The Brand corrects it and returns to step 3.
- **5a. The product already has a change waiting for Approval:**
  - 5a1. The new change replaces the waiting one, so the Admin reviews only the latest.
- **5b. The product had been returned by the Admin:**
  - 5b1. The change puts it back in the Admin's list. This is how a Brand fixes a returned product. A product that was never approved has no results, so none restart.
- **5c. Saving fails:**
  - 5c1. The system reports that the change was not saved. Nothing is stored; the form keeps what the Brand typed.
- **\*a. At any step, the Brand's access is removed:**
  - \*a1. The system stores nothing and tells the user they no longer have access.

**Priority:** Medium (provisional)
**Frequency of Use:** Whenever a Brand changes a product or fixes a returned one, such as swapping the photos that draw fewer Clicks. Changes also arrive through `UC-BRND-import-products` and `UC-BRND-send-products` when a SKU already exists. Whether a limit on how often applies to changes as well as removals is open.
**Business Rules:** `BR-approve-product`, `BR-products-brand-only`, `BR-text-card`, `BR-product-media-limit`, `BR-photo-size`, `BR-brand-categories`, `BR-results-restart-on-change`

**Associated Information:**

The changeable fields are those of `UC-BRND-create-product` except the SKU and the Brand. The change adds:

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| Product reference | Identifier | Required; must be in the signed-in Brand's Inventory | A Brand changes only its own products | Inventory |
| Submitted at | Timestamp | Set by the system | Shown to the Brand and the Admin | Approval |
| Changed at | Timestamp | Set by the system when the Admin approves the change | Divides the product's results into before and after; shown to the Brand | Approval |

**Current state in the client's repository:**
- `PUT /api/products/:id` (`worker/src/index.ts`) lets a Brand change its own product, checked by `brand_id` or `org_id`, and the change is live at once, with no Approval. Results recorded before the change stay mixed with those after it.

**Related Use Cases:**
- `UC-BRND-approve-product`: the Admin's review of the change.
- `UC-BRND-create-product`: where the product began.
- `UC-BRND-remove-product`: taking the product out instead of changing it.

**Assumptions:**
- A change replaces the whole content the Brand submits, not a single field at a time.

**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).
- [OI-35](OPEN-ISSUES.md#open): While a change waits for Approval, do Consumers keep seeing the current version, or is the product hidden?
- [OI-56](OPEN-ISSUES.md#open): Does the limit on removals also count changes?
- Resolved in the fifth client meeting: results restart after a change ([OI-41](OPEN-ISSUES.md#resolved)), Brands may remove products ([OI-42](OPEN-ISSUES.md#resolved)), and how often Brands send products ([OI-32](OPEN-ISSUES.md#resolved)).

---

### UC-BRND-remove-product: Remove a product

**UC ID and Name:** `UC-BRND-remove-product`: Remove a product
**Created By:** Matthew Stafford
**Date Created:** 2026-10-28
**Primary Actor:** Brand
**Secondary Actors:** Admin, who keeps the removed product's results
**Trigger:** The Brand chooses to remove one of its products.
**Description:** The Brand takes a product it no longer wants out of Market Match, without waiting for the Admin's Approval. The product can no longer be put in a Market, but Market Match keeps its results, because the Brand may ask for them later. A Brand can remove products only a limited number of times, so it cannot add and remove products over and over and skew its results.

**Preconditions:**

- PRE-1. The user is signed in with the Brand role and belongs to a Brand's Organization.
- PRE-2. The Brand's Inventory has at least one product.

**Postconditions:**

- POST-1. The product is no longer in the Brand's Inventory, cannot be added to a Market, and is not in the Admin's list of products waiting for Approval.
- POST-2. The product's data points are kept, and the Admin can still retrieve them.
- POST-3. The removal is recorded with who made it and when, and counts toward the Brand's limit.

**Main Success Scenario:**

1. The Brand chooses one of its products to remove.
2. The system shows the product and how many removals the Brand has left.
3. The Brand confirms the removal.
4. The system removes the product from the Brand's Inventory, keeps its results, records the removal, and confirms it to the Brand.

**Extensions:**

- **1a. The product belongs to another Brand:**
  - 1a1. The system refuses and shows nothing of it. The use case ends.
- **2a. The Brand has used all of its removals:**
  - 2a1. The system says so and removes nothing. The use case ends. How many removals a Brand has, over what period, is open.
- **2b. The product is in a Market that is running:**
  - 2b1. Whether the Brand may remove it during the Market is open. Until answered, the system says it is in a running Market and removes nothing.
- **2c. The product, or a change to it, is waiting for Approval:**
  - 2c1. The system says the waiting submission will be withdrawn too. On confirmation it leaves the Admin's list. A product that was never approved has no results to keep. Rejoins at step 4.
- **3a. The Brand cancels:**
  - 3a1. Nothing changes. The use case ends.
- **4a. Saving fails:**
  - 4a1. The system reports that the product was not removed. Nothing changes, and no removal is counted.
- **\*a. At any step, the Brand's access is removed:**
  - \*a1. The system removes nothing and tells the user they no longer have access.

**Priority:** Medium (provisional)
**Frequency of Use:** Rare: limited by design to a few times per Brand. The limit is open.
**Business Rules:** `BR-remove-product`, `BR-keep-removed-product-data`, `BR-products-brand-only`

**Associated Information:**

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| Product reference | Identifier | Required; must be in the signed-in Brand's Inventory | A Brand removes only its own products | Inventory |
| Removed by, removed at | Identifier, timestamp | Set by the system | Recorded for every removal; shown to the Admin | Brand |
| Removals left | Integer | Set by the system from the Brand's limit | Shown to the Brand | (none) |

A removed product's SKU is free again: a later product with that SKU, by hand, spreadsheet, or API, is a new product, and the removed product's results stay with the removed product.

**Current state in the client's repository:**
- No Brand screen removes a product; the client removes products for Brands (fifth client meeting). But `DELETE /api/products/:id` (`worker/src/index.ts`) already lets a Brand delete its own product, and it erases the product row outright, with no limit and nothing kept.

**Related Use Cases:**
- `UC-BRND-update-product`: changing a product instead of removing it.
- `UC-BRND-create-product`: adding a product again under the same SKU.
- `UC-FDBK-view-brand-insights`: where a Brand would see a removed product's results, which the client may charge for.

**Assumptions:**
- Removing a product hides it rather than erasing it, so its results can still be reported.

**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).
- [OI-56](OPEN-ISSUES.md#open): How many removals, over what period, do changes count too, and may a Brand remove a product from a running Market? Blocks extensions 2a and 2b.

---

### UC-BRND-approve-product: Approve or return a submitted product

**UC ID and Name:** `UC-BRND-approve-product`: Approve or return a submitted product
**Created By:** Matthew Stafford
**Date Created:** 2026-10-25; revised 2026-10-28
**Primary Actor:** Admin
**Secondary Actors:** Brand, which sees the decision
**Trigger:** The Admin opens the products waiting for his Approval.
**Description:** The Admin reviews the products each Brand submitted, new or changed, whether added by hand, imported by spreadsheet, or sent through the API, and approves them, one at a time or all at once, or returns them to the Brand with a reason. An approved product sits in the Brand's Category, ready to be put in a Market. This replaces the client copying in and checking each product himself, at a minute to a minute and a half per product.

**Preconditions:**

- PRE-1. The user is signed in as the Admin.

**Postconditions:**

- POST-1. An approved new product is in its Brand's Category and can be included in a Market.
- POST-2. An approved change replaces what Consumers see of the product, and the product's results start fresh from that moment (`UC-BRND-update-product` POST-4).
- POST-3. A returned product stays out of Consumers' sight if it was new, or keeps its last approved version if it was a change, and the Brand sees why it was returned in its list of submitted products.
- POST-4. Every decision is recorded, one per product, with who made it and when.

**Main Success Scenario:**

1. The Admin opens the products waiting for Approval.
2. The system lists them Brand by Brand, showing for each product whether it is new or a change, its Category, and how it arrived.
3. The Admin chooses a product.
4. The system shows the product as Consumers would see it on its Card and, for a change, what changed.
5. The Admin approves the product.
6. The system records the approval and marks the product approved in the Brand's list of submitted products.
7. The Admin repeats from step 3 until done.

**Extensions:**

- **1a. Nothing is waiting:**
  - 1a1. The system says so. The use case ends.
- **3a. The Admin approves many of a Brand's products at once:**
  - 3a1. After looking through the Brand's list, the Admin selects all of its waiting products, or several, and approves them in one decision.
  - 3a2. The system records a separate approval for each selected product, as in step 6, and reports how many were approved. Rejoins at step 7.
- **5a. The Admin returns the product instead:**
  - 5a1. The Admin gives the reason. The system records the return, keeps the product out of Consumers' sight or keeps its last approved version, and shows the Brand the reason. The Brand fixes it through `UC-BRND-update-product`. Rejoins at step 7.
- **5b. The product belongs in more than one Category:**
  - 5b1. Today a product is in one Category, the one its Brand chose. The client expects to allow more than one later.
- **6a. The Brand sent a newer version, or removed the product, while the Admin was reviewing:**
  - 6a1. The system tells the Admin and records no decision for that product. For a newer version it rejoins at step 4; for a removed product at step 7.
- **6b. Recording the decision fails:**
  - 6b1. The system reports it and nothing changes. For many products at once (3a), it reports which were recorded. The Admin decides the rest again.

**Priority:** High (provisional). Nothing a Brand submits reaches a Consumer without it.
**Frequency of Use:** Once per submitted product or change; a Brand's batch brings 10 to 200 at once. The client's target is to approve a 100-product import in 10 to 15 minutes (`SM-product-onboarding`).
**Business Rules:** `BR-approve-product`, `BR-admin-role`, `BR-brand-categories`, `BR-multiple-categories`, `BR-results-restart-on-change`

**Associated Information:**

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| Product or change reference | Identifier | Required; one or more; each must be waiting for Approval | Admin only | Approval |
| Decision | Enumeration | Required; `APPROVED` or `RETURNED` | Admin only | Approval |
| Reason | String | Required when returned | Shown to the product's Brand only | Approval |
| Decided by | Identifier | Set by the system | Recorded for every decision | Admin |
| Decided at | Timestamp | Set by the system | Recorded for every decision | Approval |

The Brand sees each decision in its list of submitted products. Market Match sends no notice of its own: the client emails a Brand himself when its products are approved, and may automate that later (fifth client meeting).

**Current state in the client's repository:**
- There is no Approval anywhere. Product statuses are `ACTIVE`, `INACTIVE`, and `ARCHIVED` (`types.ts`), and every product is saved `ACTIVE`.
- A `BrandItem` type with `PENDING`, `APPROVED`, and `REJECTED` is declared in `types.ts` but never used.
- The closest thing is the Admin's status toggle, which hides `INACTIVE` products from Consumers.
- The Admin can already attach a product he creates to a Brand (fifth client meeting).

**Related Use Cases:**
- `UC-BRND-create-product`, `UC-BRND-import-products`, `UC-BRND-send-products`, `UC-BRND-update-product`: where the products under review come from.
- `UC-BRND-remove-product`: a Brand withdrawing a product while it waits.

**Assumptions:**
- The Admin gives a reason whenever he returns a product, so the Brand knows what to fix.

**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).
- [OI-35](OPEN-ISSUES.md#open): While a change waits for Approval, what do Consumers see?
- Resolved in the fifth client meeting: approving all at once ([OI-37](OPEN-ISSUES.md#resolved)) and the Brand choosing the Category ([OI-39](OPEN-ISSUES.md#resolved)).

---

### UC-BRND-generate-api-key: Generate an API key

**UC ID and Name:** `UC-BRND-generate-api-key`: Generate an API key
**Created By:** Matthew Stafford
**Date Created:** 2026-10-25; revised 2026-10-28
**Primary Actor:** Admin
**Secondary Actors:** Brand, which receives the API Key and gives it to whoever sets up its system; the Brand's product system, which uses it (`UC-BRND-send-products`)
**Trigger:** The Admin has signed a Brand and set up its Organization, and chooses to give the Brand an API Key.
**Description:** The Admin generates an API Key for one Brand so the Brand's own system can send products through Market Match's API, and hands it to the Brand himself. The key belongs to that Brand alone and reaches only its Inventory, it is shown once, and generating a new one ends the old one. Brands do not generate their own keys, so the Admin controls who can send products; the client expects Brands to set themselves up later (fifth client meeting).

**Preconditions:**

- PRE-1. The user is signed in as the Admin.
- PRE-2. The Brand's Organization exists (`BR-create-organization`).

**Postconditions:**

- POST-1. The Brand has exactly one active API Key, and it reaches only that Brand's Inventory.
- POST-2. Any API Key the Brand had before no longer works.
- POST-3. The key was shown once, when it was generated, and cannot be shown again.
- POST-4. The generation is recorded with who did it and when.

**Main Success Scenario:**

1. The Admin chooses a Brand and chooses to generate an API Key for it.
2. The system creates a new API Key for that Brand.
3. The system shows the key once, with a link to Market Match's published product contract.
4. The Admin confirms he has saved the key, to give to the Brand.
5. The system records the generation and no longer shows the key.

**Extensions:**

- **1a. The Brand already has an active API Key:**
  - 1a1. The system warns that the current key will stop working at once and the Brand's system must switch to the new one. The Admin confirms, and the old key ends at step 2, or cancels and nothing changes.
- **1b. The Admin revokes the Brand's API Key without generating a new one:**
  - 1b1. The system stops accepting the key at once and records the revocation. Products already received keep their Approval status. The use case ends.
- **2a. Creating the key fails:**
  - 2a1. The system reports it, and any existing key keeps working. The use case ends.
- **4a. The Admin leaves without saving the key:**
  - 4a1. The key cannot be shown again. The Admin generates a new one (1a), which ends this one.
- **5a. The Brand later reports the key lost or leaked:**
  - 5a1. The Admin generates a new one (1a), which ends the leaked key at once.
- **\*a. The Admin removes the Brand's access, by deleting the Brand's Organization:**
  - \*a1. The key stops working at once, and every later sending with it is refused (`UC-BRND-send-products` extension 2a). A Brand's access is removed when its Organization no longer exists; a single Brand user losing the Brand role does not end the key, because the key belongs to the Brand, not to a user.

**Priority:** High (provisional). The proving slice (`v0.1.0`, team decision 2026-10-28): it is settled, and it exercises `SEC-api-key-strength` and `SEC-api-key-ending`, ranked second in the architecture. `UC-BRND-send-products` cannot happen without it.
**Frequency of Use:** Once per Brand the client signs that connects its system, plus a new key whenever one is lost, leaked, or replaced. The client signs Brands one at a time, after a conversation with each.
**Business Rules:** `BR-admin-issues-api-key`, `BR-connect-product-system`, `BR-products-brand-only`, `BR-create-organization`, `BR-admin-role`

**Associated Information:**

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| Brand reference | Identifier | Required; chosen by the Admin; must be an existing Brand Organization | Only the Admin generates keys | Brand; Organization |
| API Key | Secret | Issued at step 2 | Shown only at step 3; never shown again; how it is stored is decided in the architecture | API Key |
| Status | Enumeration | `ACTIVE`, `REPLACED`, or `REVOKED` | Shown to the Admin only, never the key itself | API Key |
| Generated by, generated at | Identifier, timestamp | Set by the system | Recorded for every key | Admin |
| Ended by, ended at | Identifier, timestamp | Set by the system when the key is replaced or revoked | Recorded for every key that ends | API Key |

How the Admin hands the key to the Brand happens outside Market Match.

**Current state in the client's repository:**
- No API Key exists. The Admin creates Organizations in WorkOS, and every request to Market Match comes from a signed-in user.

**Related Use Cases:**
- `UC-BRND-send-products`: what the API Key is for.

**Assumptions:**
- The Brand passes the key only to whoever sets up its system, and tells the Admin if it is lost or leaked.

**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).
- Resolved in the fifth client meeting: the Admin, not the Brand, gives out API Keys ([OI-31](OPEN-ISSUES.md#resolved)).

---

## Working these with your agent

_[Delegate: drafting the main success scenario once you have the trigger and the goal; proposing extensions you have not thought of, which it is genuinely good at; turning a filled-in use case into a first set of test cases; checking that every `BR-*` you cite exists in [business-rules.md](business-rules.md).]_

_Keep human: whether this is one use case or three, what the priority is, and whether an extension the agent proposed is a real path in your client's business or a generic one it has seen elsewhere. "The system handles concurrent edits" is a real requirement for some projects and invented complexity for others, and only you have met the client._

_The verification that catches the most: read the main success scenario aloud to someone who has not read the document, and stop wherever they ask a question. Every question is a missing step or a missing extension._

_**Checklist for each use case:** Does the name start with a verb? Can the system test every precondition? Does every step alternate actor and system? Is there at least one extension per step that can fail? Does every business rule appear as an identifier only? Could a tester write test cases from this without asking you anything?_
