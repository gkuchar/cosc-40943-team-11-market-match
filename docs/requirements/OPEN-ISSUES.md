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
| OI-29 | How long does it take you today to enter one Brand's products into Market Match by hand, and how many products was that? | Baseline for `SM-product-onboarding`. | Client | 2026-10-21 |
| OI-30 | How much lower would that time need to be, and by when, for you to call product onboarding a success? | Target and deadline for `BO-product-onboarding` and `SM-product-onboarding`. | Client | 2026-10-21 |
| OI-31 | When a Brand connects its own system to Market Match, who sets it up: the Brand's own developer or IT staff, or the Brand user through Market Match's screens? | Decides whether the Brand's technical staff are a stakeholder, and who the actor is in the use cases for connecting a system. | Client | 2026-10-21; team proposal added 2026-10-25: the Brand user generates its own API Key in Market Match and passes it to its developers (`UC-BRND-generate-api-key`) |
| OI-32 | How often does a Brand send you its products: once when it starts with Market Match, or again whenever its product line changes? | Decides whether connecting a Brand's system is a one-time load or an ongoing sync, and how much updating an existing product through an import matters (`AS-stable-product-id`). Split from `OI-27`, whose volume half was answered. | Client | 2026-10-23 |
| OI-35 | While a Brand's change to a published product waits for your Approval, should Consumers keep seeing the current version, or should the product be hidden until you approve the change? | Sets what Consumers see in `UC-BRND-update-product` and `UC-BRND-approve-product`, and whether a pending change can pull a product out of a running Market. | Client | 2026-10-25 |
| OI-36 | Which spreadsheet file types must a Brand's import accept: CSV, Excel, Google Sheets, or several? | Blocks extension 3a of `UC-BRND-import-products`; Brands send Google Docs and Drives today, and the client's app reads CSV only. | Client | 2026-10-25 |
| OI-37 | When a Brand imports 10 to 200 products, may you approve them all in one decision after looking through them, or do you want to decide each product? | Blocks extension 5d of `UC-BRND-approve-product`, and decides how much of your time the import actually saves (`SM-product-onboarding`). | Client | 2026-10-25 |
| OI-38 | Which video links can a Brand give for a product: YouTube only, or any video link (for example Vimeo or the Brand's own site)? | `BR-product-media-limit` and the glossary's Card say YouTube (second client meeting), and the team expects any link; blocks extension 4c of `UC-BRND-create-product` and the video checks of every BRND submit use case. | Client | 2026-10-25 |
| OI-39 | May a Brand choose the Category for its product, or propose a new Category, or do you always choose it when you approve the product? | The client raised Brands bringing their own Categories (fourth client meeting, lines 247–255); decides whether a Category field belongs in `UC-BRND-create-product` and the imports, and step 5 of `UC-BRND-approve-product`. | Client | 2026-10-25 |
| OI-40 | When a Brand submits a SKU it already has, by hand, by spreadsheet, or through the API, should Market Match change that product or refuse the submission? | Decides extension 4d of `UC-BRND-create-product`, 4d and 7a of `UC-BRND-import-products`, and 4a and 4b of `UC-BRND-send-products`. | Client | 2026-10-25 |
| OI-41 | When a Brand changes a product's photos or details, should its data points so far (swipes, Clicks, viewing times) carry over, or start fresh? | A new photo can change how Consumers react, so old and new results may not belong together; sets POST-4 of `UC-BRND-update-product` and what the Brand Dashboard reports. | Client | 2026-10-25 |
| OI-42 | Can a Brand remove its own products? Does a removal need your Approval, and can a Brand remove all of its products at any time? | No use case removes a product yet; extension 3b of `UC-BRND-update-product` depends on it, and removing a product in a running Market affects its results. | Client | 2026-10-25 |
| OI-43 | Do you want Brands to be able to import a spreadsheet of products, or only connect their own systems through the API? | The client called a spreadsheet template "a reasonable ask" but said big Brands "just have a connection put together" (fourth client meeting, lines 342–356); decides whether `UC-BRND-import-products` is built. To ask at the 2026-10-26 meeting. | Client | 2026-10-25 |
| OI-44 | When a Brand sends 200 products at once, by spreadsheet or through the API, how long is acceptable before Market Match shows the result for every product? | Sets `PER-import-results` in the SRS, and decides whether an import can finish while the Brand waits or has to run in the background. | Client | 2026-10-25 |
| OI-45 | `BR-collect-email-only` says the only personal information collected is an email address, but Consumers give gender, age range, ethnicity, and location, which the feedback use cases store with each swipe. Which is right? | Sets `SEC-pii-protection` and what `UC-FDBK-rate-product` may store; the business rules already flag the conflict (§1.2). | Client | 2026-10-25 |
| OI-46 | `BR-engagement-funnel` names three stages (viewing, starting to swipe, completing), but the glossary and `UC-FDBK-complete-market` record four (entering the code, viewing, starting, completing). Is entering the Market Code its own stage? | Sets what the Engagement Funnel reports and which rule or use case changes. | Client | 2026-10-25 |
| OI-47 | How long should Market Match keep an Anonymous Consumer before removing it? You suggested about 30 days "or whatever is the usual parameter". | Sets `BR-anonymous-consumer-expiry` and the expiry time in `UC-MKT-create-anonymous-consumer`; a Consumer who rescans after expiry counts again. | Client | 2026-10-26 |
| OI-48 | If someone takes a Public Access Market anonymously and later signs in, should their anonymous swipes be joined to their account? | Decides whether `UC-MKT-create-anonymous-consumer` must link an Anonymous Consumer to a signed-in Consumer, which would count one person twice if it does not. | Client | 2026-10-26 |
| OI-49 | You said a Market someone never finishes "would just be a zero". Should those count as zero in the average Completion Time, or be left out of it? | Counting them as zero pulls the average down; sets the Completion Time formula for `UC-FDBK-complete-market`. | Client | 2026-10-26 |
| OI-50 | When someone already signed in scans a Public Access QR Code, should they count as themselves (with their Demographics) or as an Anonymous Consumer? | Blocks extension 1b of `UC-MKT-create-anonymous-consumer`, and decides which Completion Time start applies. | Client | 2026-10-26 |
| OI-51 | Should an Anonymous Consumer expire a fixed time after its first scan, or a fixed time after its last swipe? | Counting from the first scan can split one person who returns near the deadline into two Consumers; sets the expiry time in `UC-MKT-create-anonymous-consumer` and extension 3b of `UC-MKT-expire-anonymous-consumer`. | Client | 2026-10-26 |

## Resolved

| ID | Question | Answer | Answered by | Date | Filed in |
|---|---|---|---|---|---|
| OI-2 | Does a Market mean a target group, a collection of products, or both? | A Market is the collection of Cards, grouped into Categories, that Consumers swipe through. The target group is a separate concept, the Demographic. | Demetrie King, second client meeting | 2026-09-23 | [Market](project-glossary.md#market), [Demographic](project-glossary.md#demographic) (glossary v0.3) |
| OI-7 | Which viewing events and timing boundaries are measured when a Consumer views product details? | The timings measured on a Card are dwell time (from the Card appearing to the first Flip, zero if never flipped) and decision time (from the Card appearing to the swipe). Capture is specified in `UC-FDBK-flip-card` and `UC-FDBK-rate-product`. | Demetrie King, third client meeting | 2026-10-13 | [Average Dwell Time](project-glossary.md#average-dwell-time), [Average Decision Time](project-glossary.md#average-decision-time), [Flip](project-glossary.md#flip) (glossary v0.4) |
| OI-25 | Who may create products for a Brand? | The Admin creates Inventory items today. A Brand may also submit items, but every Brand-created item, and every update to one, needs the Admin's Approval before it goes live. | Demetrie King, second client meeting | 2026-09-23 | [Admin](project-glossary.md#admin), [Approval](project-glossary.md#approval), [Inventory](project-glossary.md#inventory) (glossary v0.3) |
| OI-26 | How does a created product join a Market and become visible to Consumers? | An Inventory item, once approved, is attached to a Category. The Admin assembles a Market by selecting its Categories, assigns it to an Organization, and launches it, and only then can Consumers reach it. | Demetrie King, second client meeting | 2026-09-23 | [Inventory](project-glossary.md#inventory), [Category](project-glossary.md#category), [Approval](project-glossary.md#approval), [Launch](project-glossary.md#launch) (glossary v0.3) |
| OI-27 | How many products does one organization send in a single import, and how often: once when it joins, or again whenever its catalog changes? | Between 10 and 200 SKUs per company, across the companies the client works with today and the brands at a CPG event he attended. How often was not answered and continues as `OI-32`. | Demetrie King, text message | 2026-10-23 | [Vision and scope §4.2](vision-and-scope.md#42-major-features-and-scope) (`FEAT-bulk-product-import`, v0.3) |
| OI-28 | Who may import products: Brands only, or Brands and Vendors? | Brands only. Vendors do not upload products; they select Categories. | Demetrie King, text message | 2026-10-23 | [Vision and scope §4.2](vision-and-scope.md#42-major-features-and-scope) (`FEAT-bulk-product-import`, v0.3) |
