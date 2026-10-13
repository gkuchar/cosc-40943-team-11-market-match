# Use Cases

**Project:** Market Match
**Team:** 11
**Client:** Demetrie King
**Version:** 0.2

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
| 2026-10-13 | 0.2 | Rewrote `UC-FDBK-rate-product` and added `UC-FDBK-flip-card`, `UC-FDBK-open-card-media`, and `UC-FDBK-complete-market` to capture the data points from the third client meeting, checked against the client's repository | Matthew Stafford |

---

## 1. Introduction

### 1.1 Purpose

_[One paragraph: this document specifies the goals users can accomplish with the system, in enough detail that a developer knows what to build and a tester knows what to check.]_

This document describes how Market Match consumers enter a market, inspect products, and submit preferences, and how brands create products for participation. Each draft includes the actor's goal, system responses, failure paths, and resulting state so we can review the behavior with the client and derive implementation tasks and tests. Unconfirmed details are identified as assumptions or open issues.

### 1.2 Scope

_[Which feature areas from the vision and scope are covered here. Name the `FEAT-*` entries. If a feature has no use cases yet, say so rather than leaving the reader to notice.]_

These use cases cover `FEAT-consumer-feedback`, `FEAT-product-information`, and the data capture half of `FEAT-feedback-insights`, and partially cover `FEAT-market-participation` through consumer market entry and `FEAT-brand-participation` through product creation.

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
| FDBK | Consumer feedback and data capture: `FEAT-consumer-feedback`, `FEAT-feedback-insights` | `UC-FDBK-rate-product`: Rate a product; `UC-FDBK-flip-card`: Flip a card; `UC-FDBK-open-card-media`: Open a card photo or video; `UC-FDBK-complete-market`: Complete a market |
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
| Market ID code | String | Required; must resolve to an accessible market; format and case sensitivity pending client confirmation | Supplied by the authenticated consumer; access conditions pending client confirmation | Market Code |

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

Keep the product identity visible with its details. Product data is read only in this use case. Viewing activity is captured under `FEAT-feedback-insights`; the Flip and its dwell time are specified in `UC-FDBK-flip-card`. A failed details load must not be represented as a successful view. The effect of activity-recording failures remains pending client confirmation.

**Related Use Cases:** `UC-MKT-enter-market`: Enter a market; `UC-FDBK-rate-product`: Rate a product.
**Assumptions:** Inspecting details is optional before rating, as described in vision and scope section 1.2.
**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).
- [OI-6](OPEN-ISSUES.md#open): Which additional-information formats can the back of a Card hold?
- [OI-7](OPEN-ISSUES.md#resolved) (resolved): Which viewing events and timing boundaries are measured? Dwell time (Card appears to first Flip) and decision time (Card appears to swipe), captured in `UC-FDBK-flip-card` and `UC-FDBK-rate-product`. See [Average Dwell Time](project-glossary.md#average-dwell-time), [Average Decision Time](project-glossary.md#average-decision-time), and [Flip](project-glossary.md#flip).
- [OI-8](OPEN-ISSUES.md#open): What happens if activity capture fails while a Consumer views product details?

---

## FDBK: Consumer Feedback and Data Capture

These four use cases cover capturing every data point the client named for a Market. They do not cover the dashboards that report the data points. Each use case's Associated Information says what the client's repository (`MM-Version`, branch `tcu-fall-2026-stage`) captures today and what is missing, so the work left is visible. The data points apply to signed-in Consumers and to Public Access Consumers alike. A Public Access Consumer is identified only by an anonymous Market session.

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

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| Market session reference | Identifier | Required; must be an active session for this Market | Derived by the server from the session, never accepted from another Consumer | Market |
| Line Item reference | Identifier | Required; must belong to the session's Market and a chosen Category | Validated by the server | Line Item; SKU |
| Category reference | Identifier | Required; the Category the Card was shown under | Validated by the server | Category |
| Shown at | Timestamp | Required; recorded when the Card is displayed | System-captured | Reach |
| Swipe direction | Enumeration | Required; `RIGHT` or `LEFT`; any other value is rejected, not coerced | Consumer-supplied through the swipe | Swipe Left / Swipe Right |
| Time-to-Swipe | Duration, milliseconds | Required; ≥ 0; shown-at to swipe, for gesture and button swipes alike | Brand sees averages for its own SKUs; Vendor and Admin do not see it | Time-to-Swipe; Average Decision Time |
| Dwell time | Duration, milliseconds | Required; ≥ 0; shown-at to first Flip, zero if never flipped | Brand sees averages for its own SKUs; Vendor and Admin do not see it | Average Dwell Time |
| Demographic snapshot | Gender, age range, ethnicity, location | Copied from the signed-in Consumer's profile; empty for Public Access | Brand sees aggregates only, never one Consumer's answers | Demographic |
| Submission key | Identifier | Required; unique per swipe attempt; used to detect retries | System-generated | (none) |

Who sees what, per the third client meeting: a Brand sees per-SKU measures for its own SKUs, totalled across all Markets. A Vendor sees Likes and Passes ranked per Line Item, but not dwell or decision time. The Admin sees swipe counts and users but not Brand or Vendor data points.

The swipe, its measures, and its Demographic snapshot save as one unit or not at all. A failed save leaves no partial swipe.

**Current state in the client's repository:**
- Swipes are stored in `user_responses` and copied with a Demographic snapshot into `brand_swipe_analytics` by `POST /api/responses` and `POST /api/public/responses` in `worker/src/index.ts`.
- The measured times come from `components/SwipeCard.tsx`:
  - `dwellTime` runs from the time the Card is shown to the end of the swipe, so it already matches Time-to-Swipe.
  - `reactionTime` runs from the time shown to the first touch.
  - `front_dwell_ms` and `back_dwell_ms` are cumulative time on each side, which is *not* the client's dwell time.

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

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| Flipped | Boolean | Required on every stored impression and swipe | System-captured; Brand sees flip rate for its own SKUs | Flip |
| Dwell time | Duration, milliseconds | Required; ≥ 0; zero when not flipped; never reset by later flips | Brand sees averages for its own SKUs; Vendor and Admin do not see it | Average Dwell Time |
| Front and back time | Durations, milliseconds | Optional; cumulative time on each side, as captured today | Brand only | Card |

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
**Business Rules:** `BR-capture-feedback`

**Associated Information:**

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| Line Item reference | Identifier | Required; must belong to the session's Market | Validated by the server | Line Item; SKU |
| Media slot | Enumeration | Required; `PHOTO_1`, `PHOTO_2`, `PHOTO_3`, or `VIDEO`; must exist on the Card | System-captured | Card; Clicks |
| Media item | Identifier | Required; identifies the specific photo or video link in the slot when clicked | System-captured | Clicks |
| Clicked at | Timestamp | Required | System-captured | Clicks |
| Market session reference | Identifier | Required | Derived by the server | Market |

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
2. The system validates the Market, starts a Market session, and records the *entered* stage with its time.
3. The system displays the Market's Categories.
4. The Consumer chooses one or more Categories.
5. The system stores the chosen Categories, displays the first Card, and records the *viewed* stage with its time.
6. The Consumer swipes the first Card (`UC-FDBK-rate-product`).
7. The system records the *started* stage with its time. The Consumer swipes the remaining Cards in the chosen Categories, each through `UC-FDBK-rate-product`.
8. After the last Card in the chosen Categories is swiped, the system records the *completed* stage, marks the Market session complete, and shows the Consumer that the Market is finished.

**Extensions:**

- **2a. The Market Code is blank, unknown, or the Market is not accessible:**
  - 2a1. Handled by `UC-MKT-enter-market` extension 4a. No Market session is started.
- **2b. The Market session cannot be stored:**
  - 2b1. The system reports that the Market could not be opened and does not show Cards. A swipe needs a stored session to belong to. The Consumer retries from step 1.
- **2c. The signed-in Consumer has an incomplete Market session for this Market:**
  - 2c1. The system resumes that session instead of starting a new one, records the resume time, and shows only Cards not yet swiped. Rejoins at step 5 if Categories were chosen, otherwise at step 3.
- **2d. The Market is the demo Market:**
  - 2d1. The system lets the Consumer go through it but records no funnel stages. The use case continues without capture.
- **4a. The Consumer leaves before choosing a Category:**
  - 4a1. The Market session stays stored, reached *entered* only. The use case ends.
- **5a. The chosen Categories contain no Cards:**
  - 5a1. The system shows that there is nothing to swipe. The session reached *entered* only. The use case ends.
- **7a. The Consumer stops partway and leaves:**
  - 7a1. The Market session stays incomplete with its stages so far and the time of its last swipe. It counts as *started* but not *completed* in the funnel. A signed-in Consumer can resume through extension 2c.
  - 7a2. A Public Access Consumer has no identity, so returning later starts a new Market session.
- **8a. The Consumer chooses more Categories after completing the chosen ones:**
  - 8a1. The system records the added Categories against the same Market session. How this affects completion is an open issue.

**Priority:** High (provisional). The client called the Engagement Funnel and Completion Time what he most wants to showcase for a Brand Market.
**Frequency of Use:** One Market session per Consumer per Market visit. A single QR Code event in the client's growth scenario starts up to 10,000 sessions in a short window.
**Business Rules:** `BR-select-market`, `BR-capture-feedback`

**Associated Information:**

| Property name | Data type | Validation rule | Security or access concerns | Glossary reference |
|---|---|---|---|---|
| Market session | Identifier | Required; system-generated at step 2 | Anonymous for Public Access; tied to the user when signed in | Market |
| Entry method | Enumeration | Required; `MARKET_CODE` or `PUBLIC_ACCESS` | System-captured | Market Code; Public Access |
| Entered at | Timestamp | Required | System-captured | Engagement Funnel |
| Chosen Categories | List of identifiers | Required once chosen; each must belong to the Market | System-captured | Category |
| Viewed at | Timestamp | Set at step 5 | System-captured | Engagement Funnel |
| Started at | Timestamp | Set at the first stored swipe | System-captured | Engagement Funnel |
| Completed at | Timestamp | Set when every Card in the chosen Categories is swiped; empty otherwise | System-captured | Completion Time |
| Last activity at | Timestamp | Updated on every stored swipe | System-captured | Completion Time |

**Who sees what:**
- Brand Market: the owning Brand sees the funnel counts and average Completion Time.
- Standard Market: the Vendor sees the average Completion Time and, possibly, the funnel.
- No dashboard shows a single Consumer's session.
- Completion Time is derived from the stored timestamps rather than stored itself. The resume-gap rule is still open, and timestamps allow either rule to be computed later.

**Current state in the client's repository:**
- A Market session (`completed_markets`) is created on the Consumer's *first swipe*, not when the code is entered. Entering a code and leaving records nothing, and the *entered* and *viewed* stages are not captured.
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
- Public Access Consumers are captured through an anonymous Market session, with *entered* recorded when the link is opened.

**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).
- [OI-18](OPEN-ISSUES.md#open): Does Completion Time include time away from a Market the Consumer stopped and resumed, or only active time?
- [OI-19](OPEN-ISSUES.md#open): Does the funnel clock start at code entry (the client's first description) or when the first Card is viewed (his later description)? Both timestamps are captured so either can be reported.
- [OI-20](OPEN-ISSUES.md#open): How do Categories chosen after completion affect completion?
- [OI-21](OPEN-ISSUES.md#open): Should Vendors see the full Engagement Funnel or only Completion Time?
- [OI-22](OPEN-ISSUES.md#open): Is the funnel shown per Brand Market only, or also per Standard Market?

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
**Open Issues:** Tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).
- [OI-23](OPEN-ISSUES.md#open): Which product fields are required?
- [OI-24](OPEN-ISSUES.md#open): What name length, image format, and media size limits apply?
- [OI-25](OPEN-ISSUES.md#resolved) (resolved): Who may create products for a brand? The Admin today; a Brand may submit items, each needing the Admin's Approval. See [Admin](project-glossary.md#admin), [Approval](project-glossary.md#approval), and [Inventory](project-glossary.md#inventory).
- [OI-26](OPEN-ISSUES.md#resolved) (resolved): How does a created product join a market? Once approved it is attached to a Category, the Admin assembles the Market from Categories and launches it. See [Inventory](project-glossary.md#inventory), [Category](project-glossary.md#category), [Approval](project-glossary.md#approval), and [Launch](project-glossary.md#launch).

---

## Working these with your agent

_[Delegate: drafting the main success scenario once you have the trigger and the goal; proposing extensions you have not thought of, which it is genuinely good at; turning a filled-in use case into a first set of test cases; checking that every `BR-*` you cite exists in [business-rules.md](business-rules.md).]_

_Keep human: whether this is one use case or three, what the priority is, and whether an extension the agent proposed is a real path in your client's business or a generic one it has seen elsewhere. "The system handles concurrent edits" is a real requirement for some projects and invented complexity for others, and only you have met the client._

_The verification that catches the most: read the main success scenario aloud to someone who has not read the document, and stop wherever they ask a question. Every question is a missing step or a missing extension._

_**Checklist for each use case:** Does the name start with a verb? Can the system test every precondition? Does every step alternate actor and system? Is there at least one extension per step that can fail? Does every business rule appear as an identifier only? Could a tester write test cases from this without asking you anything?_
