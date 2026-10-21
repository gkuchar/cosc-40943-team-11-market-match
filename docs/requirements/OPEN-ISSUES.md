# Open Issues

**Project:** _[Your project name]_
**Team:** _[Team NN]_

---

_**What this file is.** Every question about the project that you cannot answer yet, in one place, with the name of the person who can answer it. It is the shortest document in `docs/requirements/` and the one your client meetings run on._

_**Why it exists.** A draft specification with confident guesses in the gaps is more dangerous than one with holes in it, because nobody can tell the guesses from the facts. Writing "we do not know" is not an admission of failure in week 3, it is the correct state. What fails is knowing and not writing it down._

_**Where entries come from.** Three places, and all three are routine:_

- _Drafting a section of [vision-and-scope.md](vision-and-scope.md) and hitting something the client brief does not say._
- _Your agent's list. When you ask it to draft a section, ask it to list every question it could not answer from the material you gave it. Its list is longer than yours and it is not embarrassed to ask obvious things._
- _The meeting itself. Your client says something that contradicts your notes, or answers a question with "I would have to check"._

_**How they leave.** Answered in a client meeting, in Slack, or by reading a document. Record the answer and the date, mark it resolved, and put the substance where it belongs (an objective, a term in the [glossary](project-glossary.md), a business rule). This file is a queue, not a home: an answer that stays here has not been filed._

_**Identifiers here are numbers**, `OI-1` upward, and that is deliberate. Numbers are fine for a list that only ever grows at the bottom and gets cited lightly. The slug convention in [vision-and-scope.md](vision-and-scope.md) exists for identifiers that get **reordered** or **cited often**, which is not this list._

## Before a client meeting

_[Sort the open list by what it costs you to stay wrong, not by what is easy to ask. You will get through fewer questions than you plan to. Take the ones where a wrong guess sends the whole team down the wrong path for a month, and leave the ones you can settle by reading a document or trying the client's current tool yourself.]_

_[Send the shortlist to your client the day before. A client who has seen the questions arrives with answers instead of promises.]_

## Open

| ID | Question | Why it matters | Who can answer | Raised |
|---|---|---|---|---|
| OI-1 | Which use cases belong in the MVP, and in what priority order? | Every use case is marked High (provisional). Blocks vision and scope section 4.3 (MVP Scope) and sprint planning. | Client | 2026-09-14 |
| OI-3 | What format and case sensitivity does a Market Code have? | Blocks code validation in `UC-MKT-enter-market`. | Client; the generator is also readable in the client's repository | 2026-09-14 |
| OI-4 | Which Consumers may enter which Markets (access conditions)? | Blocks the access check in `UC-MKT-enter-market`; a wrong guess leaks one Organization's Market to another. | Client | 2026-09-14 |
| OI-5 | In what order are a Market's products shown to a Consumer? | Affects `UC-MKT-enter-market` and `UC-FDBK-rate-product`, and can bias which products get swiped. | Client | 2026-09-14 |
| OI-6 | Which additional-information formats can the back of a Card hold? | Blocks what `UC-PROD-view-product-details` must display. | Client | 2026-09-14 |
| OI-8 | What happens if activity capture fails while a Consumer views product details? | Decides whether a lost data point blocks the Consumer in `UC-PROD-view-product-details`. | Team, confirmed with the client | 2026-09-14 |
| OI-9 | Does Reach count every time a Card is shown, or once per Consumer per Card? | Sets the denominator of Reach and Approval Percentage in `UC-FDBK-rate-product`. | Client | 2026-09-14 |
| OI-10 | Are lottery entries (`BR-earn-entry`, `BR-entry-expiration`) in this release's scope? | Decides whether `UC-FDBK-rate-product` must count swipes toward entries. | Client | 2026-09-14 |
| OI-11 | What gesture thresholds turn a drag into a left or right swipe? | Blocks extension 2b of `UC-FDBK-rate-product`. | Team, confirmed with the client | 2026-09-14 |
| OI-12 | What retention policy applies to Demographic answers stored with each swipe? | Privacy exposure of `UC-FDBK-rate-product`; the business rules note that no demographic policy has been sourced. | Client | 2026-09-14 |
| OI-13 | Is flip rate the share of Card impressions that were flipped, or the share of swipes whose Card was flipped? | Sets the flip rate formula fed by `UC-FDBK-flip-card`. | Client | 2026-10-13 |
| OI-14 | Should the existing cumulative front and back time on a Card be kept, now that dwell time ends at the first Flip? | Decides whether `UC-FDBK-flip-card` keeps or drops the client's existing `front_dwell_ms` and `back_dwell_ms`. | Client | 2026-10-13 |
| OI-15 | Does moving through the photo carousel count as a Click, or only tapping to enlarge a photo? | Defines what `UC-FDBK-open-card-media` counts. | Client | 2026-10-13 |
| OI-16 | Should reports count every Click, or one Click per Consumer per photo or video? | Sets the Clicks figure a Brand sees from `UC-FDBK-open-card-media`. | Client | 2026-10-13 |
| OI-17 | Should per-media display time (`media_views`) be kept now that the client wants Clicks? | Decides whether `UC-FDBK-open-card-media` replaces or adds to existing capture. | Client | 2026-10-13 |
| OI-18 | Does Completion Time include time away from a Market the Consumer stopped and later resumed, or only active time? | Sets the Completion Time formula in `UC-FDBK-complete-market`; timestamps are stored either way. | Client | 2026-10-13 |
| OI-19 | Does the Engagement Funnel clock start at Market Code entry or when the first Card is viewed? | The client described it both ways; sets the start of Completion Time in `UC-FDBK-complete-market`. | Client | 2026-10-13 |
| OI-20 | If a Consumer chooses more Categories after completing the ones they chose, how does that affect completion? | Blocks extension 8a of `UC-FDBK-complete-market`. | Client | 2026-10-13 |
| OI-21 | Should Vendors see the full Engagement Funnel, or only Completion Time? | Sets Vendor access to data from `UC-FDBK-complete-market`. | Client | 2026-10-13 |
| OI-22 | Is the Engagement Funnel reported for Brand Markets only, or for Standard Markets too? | Sets the scope of `UC-FDBK-complete-market` reporting. | Client | 2026-10-13 |
| OI-23 | Which product fields are required when a product is created? | Blocks validation in `UC-BRND-create-product`. | Client | 2026-09-14 |
| OI-24 | What name length, image format, and media size limits apply to a product? | Blocks validation in `UC-BRND-create-product`. | Client | 2026-09-14 |
| OI-27 | In what time window do the 10,000 Consumers of the QR Code growth scenario arrive (all within minutes, or across an event), and how long does the event last? | Sets the load target for `SCA-qr-event-burst` and its load test. | Client | 2026-10-16 |
| OI-28 | Is there a response-time target for showing the next Card after a swipe, or for loading a dashboard? | `PER-not-yet-specified`; without a number no performance requirement can be tested. | Client | 2026-10-16 |
| OI-29 | Is there an availability target, for example during a live event? | `AVL-not-yet-specified`; decides whether event-time outages need a design response. | Client | 2026-10-16 |
| OI-30 | Must the consumer views meet an accessibility standard such as WCAG 2.1 AA, and on which devices and browsers? | `USE-not-yet-specified`; affects every user-facing view. | Client | 2026-10-16 |

## Resolved

| ID | Question | Answer | Answered by | Date | Filed in |
|---|---|---|---|---|---|
| OI-2 | Does a Market mean a target group, a collection of products, or both? | A Market is the collection of Cards, grouped into Categories, that Consumers swipe through. The target group is a separate concept, the Demographic. | Demetrie King, second client meeting | 2026-09-23 | [Market](project-glossary.md#market), [Demographic](project-glossary.md#demographic) (glossary v0.3) |
| OI-7 | Which viewing events and timing boundaries are measured when a Consumer views product details? | The timings measured on a Card are dwell time (from the Card appearing to the first Flip, zero if never flipped) and decision time (from the Card appearing to the swipe). Capture is specified in `UC-FDBK-flip-card` and `UC-FDBK-rate-product`. | Demetrie King, third client meeting | 2026-10-13 | [Average Dwell Time](project-glossary.md#average-dwell-time), [Average Decision Time](project-glossary.md#average-decision-time), [Flip](project-glossary.md#flip) (glossary v0.4) |
| OI-25 | Who may create products for a Brand? | The Admin creates Inventory items today. A Brand may also submit items, but every Brand-created item, and every update to one, needs the Admin's Approval before it goes live. | Demetrie King, second client meeting | 2026-09-23 | [Admin](project-glossary.md#admin), [Approval](project-glossary.md#approval), [Inventory](project-glossary.md#inventory) (glossary v0.3) |
| OI-26 | How does a created product join a Market and become visible to Consumers? | An Inventory item, once approved, is attached to a Category. The Admin assembles a Market by selecting its Categories, assigns it to an Organization, and launches it, and only then can Consumers reach it. | Demetrie King, second client meeting | 2026-09-23 | [Inventory](project-glossary.md#inventory), [Category](project-glossary.md#category), [Approval](project-glossary.md#approval), [Launch](project-glossary.md#launch) (glossary v0.3) |
