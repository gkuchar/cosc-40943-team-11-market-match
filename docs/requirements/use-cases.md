# Use Cases

**Project:** Market Match
**Team:** 11
**Client:** Demetrie King
**Version:** 0.1

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

| Date | Version | Description | Author |
|---|---|---|---|
| 2026-09-14 | 0.1 | Draft four use cases derived from the vision and scope feature list | Chris Ramirez |

---

## 1. Introduction

### 1.1 Purpose

_[One paragraph: this document specifies the goals users can accomplish with the system, in enough detail that a developer knows what to build and a tester knows what to check.]_

This document describes how Market Match consumers enter a market, inspect products, and submit preferences, and how brands create products for participation. Each draft includes the actor's goal, system responses, failure paths, and resulting state so we can review the behavior with the client and derive implementation tasks and tests. Unconfirmed details are identified as assumptions or open issues.

### 1.2 Scope

_[Which feature areas from the vision and scope are covered here. Name the `FEAT-*` entries. If a feature has no use cases yet, say so rather than leaving the reader to notice.]_

These initial use cases cover `FEAT-consumer-feedback`, `FEAT-product-information`, and `FEAT-feedback-data`, and partially cover `FEAT-market-participation` through consumer market entry and `FEAT-brand-participation` through product creation.

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

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| _[field]_ | _[type]_ | _[required, format, range]_ | _[who may see or set it]_ | _[term]_ |

**Related Use Cases.** _Other use cases this one invokes or is invoked by, by identifier and name._

**Assumptions.** _Anything assumed about this use case or how it executes._

**Open Issues.** _What you do not know yet. Mirror it into [OPEN-ISSUES.md](OPEN-ISSUES.md) so it is visible in one place._

---

## 3. Use Case List

_[Your area codes, then a table of every use case by area. Write this list first, before specifying any single use case in detail. It is the cheapest thing to review with your client, and finding out you missed a whole area costs minutes here rather than a week later.]_

| Area code | Feature area | Use cases |
|---|---|---|
| MKT | Market participation: `FEAT-market-participation` | `UC-MKT-enter-market`: Enter a market |
| PROD | Product information: `FEAT-product-information` | `UC-PROD-view-product-details`: View product details |
| FDBK | Consumer feedback and data capture: `FEAT-consumer-feedback`, `FEAT-feedback-data` | `UC-FDBK-rate-product`: Rate a product |
| BRND | Brand participation: `FEAT-brand-participation` | `UC-BRND-create-product`: Create a product |

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
**Business Rules:** `BR-select-market`

**Associated Information:**

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| Market ID code | String | Required; must resolve to an accessible market; format and case sensitivity pending client confirmation | Supplied by the authenticated consumer; access conditions pending client confirmation | Market (meaning pending client confirmation) |

Display the selected market name and its participating product cards. Product ordering is pending client confirmation. This use case creates no rating, product, or market. A failed lookup leaves the previous selection unchanged.

**Related Use Cases:** `UC-PROD-view-product-details`: View product details; `UC-FDBK-rate-product`: Rate a product.
**Assumptions:** Email and one-time-code sign-in occurs before market entry, following vision and scope section 1.2. A market ID code is distinct from a sign-in code.
**Open Issues:** Which use cases belong in the MVP, and in what priority order? Does a market mean a target group, a collection of products, or both? What code format, case sensitivity, access conditions, and product ordering apply?

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
**Business Rules:** `BR-tap-product`, `BR-capture-feedback`

**Associated Information:**

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| Product reference | Identifier | Required; identifies the displayed product in the selected market | System checks product accessibility | Card |
| Additional information | Content | Display supplied content; handle missing content explicitly; formats pending client confirmation | Consumer reads content supplied by the brand | Card |

Keep the product identity visible with its details. Product data is read only in this use case. Viewing activity is captured under FEAT-feedback-data, with event and timing definitions pending client confirmation. A failed details load must not be represented as a successful view. The effect of activity-recording failures remains pending client confirmation.

**Related Use Cases:** `UC-MKT-enter-market`: Enter a market; `UC-FDBK-rate-product`: Rate a product.
**Assumptions:** Inspecting details is optional before rating, as described in vision and scope section 1.2.
**Open Issues:** Which additional-information formats are supported? Which viewing events and timing boundaries are measured, and what happens if activity capture fails?

---

## FDBK: Consumer Feedback and Data Capture

### UC-FDBK-rate-product: Rate a product

**UC ID and Name:** `UC-FDBK-rate-product`: Rate a product
**Created By:** Chris Ramirez
**Date Created:** 2026-09-14
**Primary Actor:** Consumer
**Secondary Actors:** None
**Trigger:** The consumer swipes a displayed product left or right.
**Description:** The consumer indicates interest or disinterest, and Market Match stores the preference and associated interaction data.

**Preconditions:**

- PRE-1. The consumer has an authenticated session and a selected market.
- PRE-2. The system displays a product currently available for rating in that market.

**Postconditions:**

- POST-1. The preference is stored against the correct product, market, and consumer interaction.
- POST-2. The accompanying captured interaction measurements are stored with the submission.
- POST-3. The system confirms the save and displays another product or states that no products remain.

**Main Success Scenario:**

1. The consumer swipes right to indicate interest or left to indicate disinterest.
2. The system validates the submission, stores the preference and accompanying interaction data, confirms the save, and displays the next available product.

**Extensions:**

- **2a. The gesture does not resolve to left or right:**
  - 2a1. The system retains the product and records no preference; the consumer may return to step 1.
- **2b. The product is unavailable or the session is no longer valid:**
  - 2b1. The system rejects the rating and asks the consumer to refresh the market or sign in again; the use case ends without a new rating.
- **2c. Saving fails or its outcome cannot be confirmed:**
  - 2c1. The system does not claim success and retains the submission for retry. When the consumer retries, the system checks whether that submission was already saved before resuming step 2, avoiding a duplicate rating from the retry.
- **2d. No products remain after a successful save:**
  - 2d1. The system confirms the saved rating and states that no products remain; the use case succeeds.

**Priority:** High (provisional)
**Frequency of Use:** Once per submitted swipe. Vision and scope reports approximately 3,600 swipes at the most recent I-Fest; peak rate and future load are unconfirmed.
**Business Rules:** `BR-rate-product`, `BR-capture-feedback`

**Associated Information:**

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| Product and market references | Identifiers | Required; product belongs to the selected market and is available | System validates the association | Card; Market |
| Swipe direction | Enumeration | Required; left or right | Consumer supplies through a swipe | Swipe Left / Swipe Right |
| Consumer/session reference | Identifier | Derived from the authenticated interaction; association policy pending client confirmation | Do not accept another consumer's identity from submitted input | Consumer |
| Swipe speed | Numeric measurement | Nonnegative when measurable; units and missing-value policy pending client confirmation | Captured by the system; access pending client confirmation | Swipe |
| Time spent viewing | Duration | Nonnegative when measurable; timing boundaries pending client confirmation | Captured by the system | Time-to-Swipe (relationship pending client confirmation) |
| Session activity | Event data | Events and required fields pending client confirmation | Capture, access, and retention pending client confirmation | Consumer |

Proposed failure behavior: the rating and its accompanying captured measurements save as one complete submission; a failed save leaves no partial submission. A timeout can have an unknown outcome, so retrying must reconcile an existing save rather than count it twice. This does not decide whether a consumer may intentionally rate the same product again. Gesture thresholds, measurement completeness, and ordering remain open. The historical swipe total does not establish a response-time target.

**Related Use Cases:** `UC-MKT-enter-market`: Enter a market; `UC-PROD-view-product-details`: View product details (optional before rating).
**Assumptions:** This draft covers preference submission. Any connection to lottery entries in business-rules.md needs a separate release-scope decision with the client.
**Open Issues:** Are lottery entries in the release scope? Can consumers intentionally rate a product more than once? What product ordering, gesture thresholds, measurement units, timing boundaries, and missing-data behavior apply? Confirm retry and all-or-nothing save behavior, data access and retention, and peak-load and response-time targets.

---

## BRND: Brand Participation

### UC-BRND-create-product: Create a product

**UC ID and Name:** `UC-BRND-create-product`: Create a product
**Created By:** Chris Ramirez
**Date Created:** 2026-09-14
**Primary Actor:** Brand
**Secondary Actors:** None
**Trigger:** The brand chooses to create a product.
**Description:** The brand supplies product content so the product can subsequently participate in a market and receive consumer feedback.

**Preconditions:**

- PRE-1. The brand has an authenticated session authorized to create products.

**Postconditions:**

- POST-1. A product containing the accepted content is stored and associated with the creating brand.
- POST-2. The brand receives confirmation identifying the created product.

**Main Success Scenario:**

1. The brand chooses to create a product.
2. The system requests the product name, picture, and additional information.
3. The brand supplies the content and submits it.
4. The system validates and stores the product under the brand, then displays confirmation with the saved content.

**Extensions:**

- **3a. The brand cancels before submitting:**
  - 3a1. The system ends the use case without creating a product.
- **4a. Content fails validation:**
  - 4a1. The system identifies affected fields, retains entered content where possible, and creates no product. The brand corrects the content and returns to step 3 or cancels.
- **4b. Authorization has expired or been removed:**
  - 4b1. The system rejects creation and asks the brand to restore authorized access; the use case ends without a new product.
- **4c. Content upload or saving fails:**
  - 4c1. The system reports that creation has not been confirmed and retains entered content where possible. If the brand retries the same submission, the system reconciles any completed save before resuming step 4 without creating a duplicate.

**Priority:** High (provisional)
**Frequency of Use:** Once per new product; number of products per brand and creation rate are unconfirmed.
**Business Rules:** `BR-submit-product`

**Associated Information:**

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| Product name | String | Proposed: required and nonblank; length and uniqueness pending client confirmation | Supplied by the authorized brand; displayed to participating consumers | Card |
| Picture | Image content | Requiredness, formats, and size limits pending client confirmation | Supplied by the authorized brand | Card |
| Additional information | Content | Requiredness and supported text/media formats pending client confirmation | Supplied by the authorized brand; displayed in product details | Card |
| Brand reference | Identifier | Required; derived from authorized session | Cannot be assigned to an unrelated brand through input | Brand |

Confirmation displays the saved product name, picture, and available additional information. Proposed failure behavior: creation saves the complete accepted product or leaves no usable partial product; incomplete uploads are not exposed as created products. An uncertain save is reconciled on retry. Creating a product does not enroll it in a market in this draft; joining and publication need confirmation with the client.

**Related Use Cases:** `UC-PROD-view-product-details`: View product details (after the product participates in a market).
**Assumptions:** Brands have authenticated product-creation access; exact roles are unconfirmed. Market joining is a separate goal, following vision and scope section 1.2.
**Open Issues:** Which product fields are required, and what name, format, and media limits apply? Who may create products for a brand? How does a created product join a market and become visible to consumers?

---

## Working these with your agent

_[Delegate: drafting the main success scenario once you have the trigger and the goal; proposing extensions you have not thought of, which it is genuinely good at; turning a filled-in use case into a first set of test cases; checking that every `BR-*` you cite exists in [business-rules.md](business-rules.md).]_

_Keep human: whether this is one use case or three, what the priority is, and whether an extension the agent proposed is a real path in your client's business or a generic one it has seen elsewhere. "The system handles concurrent edits" is a real requirement for some projects and invented complexity for others, and only you have met the client._

_The verification that catches the most: read the main success scenario aloud to someone who has not read the document, and stop wherever they ask a question. Every question is a missing step or a missing extension._

_**Checklist for each use case:** Does the name start with a verb? Can the system test every precondition? Does every step alternate actor and system? Is there at least one extension per step that can fail? Does every business rule appear as an identifier only? Could a tester write test cases from this without asking you anything?_
