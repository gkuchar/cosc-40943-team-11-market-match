# Business Rules

**Project:** Market Match
**Team:** 11
**Client:** Demetrie King
**Version:** 0.5

---

_**How to use this template.** Instructions appear in italic square brackets. Fill in underneath them and leave them in place until the document is stable._

_**What a business rule is.** A corporate policy, a government regulation, a law, an industry standard, or a computational formula. Business rules are a rich source of requirements, because they dictate properties your system must have in order to conform to them._

_**What a business rule is not: a software requirement.** This is the distinction students get wrong, so read it twice. A rule is a property of the **business**. It exists whether or not your software does, it was true before you arrived, and it will still be true if the project is cancelled. "A student may only submit a peer evaluation during an active week" is a rule the course had before anyone wrote code._

_What belongs to your software is the **enforcement** of that rule, and that is a functional requirement, written in the specification and cited back here. Keeping the two apart is what lets you answer the question that comes up every semester: "who decided this, and can we change it?" If it is a rule, the client's organization decides and you comply. If it is a requirement, your team decides and you can negotiate._

## How to hear one in a meeting

_[Rules almost never arrive announced. They surface in the middle of a story about something else, usually in one of these shapes:]_

- _"Must comply with..."_
- _"Only `<someone>` may `<do something>`"_
- _"If `<condition>`, then `<something happens>`"_
- _"Must be calculated according to..."_
- _"...unless it has been more than a year."_

_Examples of a client stating a rule without knowing it: "A new client must pay 30 percent of the estimated consulting fee and travel expenses in advance." "Time-off approvals must comply with the company's vacation policy."_

_When you hear one, write it down in the meeting. You will not reconstruct it afterward, and the exact wording matters because the rule is someone else's sentence, not yours._

## The five shapes a rule takes

_[Useful for recognizing rules, not for organizing this document. Sections below are grouped by topic, not by these categories.]_

| Shape | What it does | Example |
|---|---|---|
| **Fact** | States something always true about the business | Every senior design team belongs to exactly one course section. |
| **Constraint** | Restricts what may be done, or by whom | Only a course admin may create a course section. |
| **Action enabler** | Triggers an action when a condition holds | If a student has not completed safety training in 12 months, the request is refused. |
| **Inference** | Derives a new fact from known facts | A team with no submissions for two consecutive weeks is at risk. |
| **Computation** | Defines how a value is calculated | The peer evaluation score is the mean of all scores received that week. |

_Computations are the ones teams forget are rules. A formula the client uses today is a rule you must reproduce exactly, not a design decision you get to make. Ask for the spreadsheet._

## What a rule turns into

_[One rule usually propagates into several requirements of different kinds. This is why the document exists as its own artifact rather than being scattered through the specification.]_

| Requirement type | How the rule shows up | Example |
|---|---|---|
| Business requirement | A regulation drives a business objective | The system must enable compliance with all federal and state chemical reporting regulations within five months. |
| User requirement | A privacy policy dictates who may do what | Only laboratory managers may generate chemical exposure reports for anyone other than themselves. |
| Functional requirement | A company policy becomes system behavior | If an invoice is received from an unregistered vendor, the system shall email the vendor the supplier intake form and the W-9. |
| Quality attribute | A safety regulation becomes a checked property | The system must maintain safety training records and check them before a user can request a hazardous chemical. |

## Identifiers and traceability

_Each rule carries a stable `BR-<slug>` identifier, a name-based slug coined from the rule's gist: `BR-active-weeks`, `BR-section-admin-only`, `BR-artifact-key-unique`. Never renumber, rename, or repoint one. The thematic grouping into sections below is organizational only and does not affect a rule's identity, so moving a rule between sections is free and renaming it is not._

_**Cite rules, do not copy them.** When a use case is governed by a rule, its Business Rules field carries the identifier only, never the rule's text. One rule, one home. A rule copied into three use cases will be updated in one of them._

_A rule may cite another rule by identifier where one depends on another._

## Every rule needs a source

_[The column teams leave blank, and the one that matters most. For each rule, record where it comes from: a named policy document, a regulation, a page of the client's handbook, or the person who told you and the date.]_

_A rule you cannot attribute is usually not a rule. It is your team's design decision wearing a rule's clothes, and it belongs in the specification where it can be argued with. The test: if you asked your client to change it tomorrow, who would have to approve? If the answer is "you", it was never a rule._

_Where a rule is expected to change, say so and say when. Rules change on the business's schedule, not on yours._

## Where your AI teammate helps, and where it is dangerous

_[Delegate: turning your meeting notes into candidate rules, spotting sentences in a transcript that have the shape of a rule, and finding use cases in your specification that a given rule ought to govern but does not cite.]_

_**Do not let it invent rules.** This section is the single most dangerous place in your requirements for fabricated content, because an invented rule reads exactly like a real one. "Passwords must be at least 8 characters." "Records must be retained for 7 years." Both are plausible, both are common, and neither is your client's policy unless your client said so. A fabricated rule then propagates into functional requirements, tests that pass, and code that enforces something nobody asked for._

_The Source column is the defense. Every rule traces to a document or a person, or it does not go in the file. When your agent proposes a rule, the only question is: who told us this?_

## Revision History

| Date | Version | Description | Author |
|---|---|---|---|
| 2026-09-11 | 0.1 | Initial rules from the client brief and first client meeting | Griffin Kuchar |
| 2026-10-12 | 0.2 | Added rules from the 09-07, 09-21, and 09-30 client meetings (organizations and roles, market setup, product approval, pricing, data collection, analytics definitions) | Griffin Kuchar |
| 2026-10-14 | 0.3 | Addressed review: added `BR-dashboard-access`, folded decision and dwell time into `BR-capture-feedback` by glossary reference, flagged the demographic data gap | Griffin Kuchar |
| 2026-10-25 | 0.4 | Product import rules from the 10-21-2026 client meeting and the client's 10-23-2026 text: widened `BR-approve-product` to every way a brand submits products; added `BR-products-brand-only`, `BR-connect-product-system`, `BR-multiple-categories`, and `BR-photo-size` | Matthew Stafford |
| 2026-10-28 | 0.5 | Product import answers from the 10-26-2026 client meeting: video links beyond YouTube and video files in `BR-product-media-limit`; JPEG and PNG in `BR-photo-size`; Brands create their own Categories, so `BR-create-market-admin-only` no longer covers Categories; added `BR-brand-categories`, `BR-admin-issues-api-key`, `BR-results-restart-on-change`, `BR-remove-product`, and `BR-keep-removed-product-data` | Matthew Stafford |

---

## 1. Introduction

### 1.1 Purpose

This document collects the policies, regulations, standards, and formulas that govern the Market Match business that our app operates in, so the specification can cite them rather than restate them.

### 1.2 Scope

These rules cover the participation and data policies of the Market Match business as
described in the client brief, the client meetings through 10-26-2026, and the client's
10-23-2026 text message.

In scope:

- **Consumer participation:** how consumers sign in, rate and inspect products, select
  markets, and accrue and forfeit lottery entries (2.1).
- **Brand participation:** how brands create, import, change, and remove products and
  their categories, how those products are approved, join markets, and receive feedback (2.2).
- **Market lifecycle:** how markets are created and how they receive feedback (2.3).
- **White-label operation:** how partner organizations brand their own instance, keep
  their data isolated, and connect via API (2.4).
- **Behavioral data capture:** what interaction data the platform records beyond explicit
  ratings, how its measures are defined, and who may see them (2.5).
- **Organizations and roles:** who creates organizations, which roles users hold, and
  which markets an organization's users can see (2.6).
- **Pricing:** what determines the price of a survey (2.7).
- **Data collection and privacy:** what personal information is collected and how it must
  be protected (2.8).

Out of scope for this document:

- **Prize disbursement.** These rules record how lottery entries are earned and expire,
  but the drawing, winner selection, and payout of cash prizes (including any sweepstakes
  or gambling regulations governing them) are business processes our system does not touch
  as currently defined.
- **API engineering constraints.** Authentication schemes, authorization, rate limiting,
  versioning, and documentation for `BR-connect-api` and `BR-connect-product-system` are our team's design decisions and
  belong in the specification, not here, since the client did not dictate them as policy.
- **Demographic data handling.** The client noted demographic collection "where
  appropriate," but the consent and legal-appropriateness policy governing it has not yet
  been sourced, so no rule captures it. The sources also conflict: on 09-21 the client said
  only an email is collected (`BR-collect-email-only`), yet the first client meeting lists
  "who the demographic is" as a tracked data point and the brand dashboard reports gender,
  age, and ethnicity. Whether demographics are collected at sign-in, and where they are
  stored, is flagged for the next client meeting. To be revisited once the client confirms.

---

## 2. Rules

### 2.1 Consumers

- **`BR-sign-in`:** A consumer can sign into the app via email + one-time code sent to email.
  **Source:**  Product demo by Demetrie King (meeting and date not recorded).
- **`BR-rate-product`:** A consumer can swipe right on a product to signal interest or swipe left on a product to signal disinterest.
  **Source:**  Product demo by Demetrie King (meeting and date not recorded).
- **`BR-tap-product`:** A consumer can tap on a product to reveal more information about a product.
  **Source:**  Market Match website.
- **`BR-select-market`:** A consumer can select a category of products (a market) from a catalog to begin rating products from by entering a market's ID code.
  **Source:**  Market Match website.
- **`BR-earn-entry`:** A consumer will earn one entry per 50 products rated into a lottery to potentially win cash prizes paid out Cash App or Venmo.
  **Source:**  Market Match website.
- **`BR-entry-expiration`:** A consumer's entry will expire after 30 days if unused.
  **Source:**  Market Match website.

### 2.2 Brands/Products

- **`BR-submit-product`:** A brand can create their product with a name, picture, and additional information.
  **Source:**  Market Match website.
- **`BR-join-market`:** A brand can join a market to have their product rated by consumers who select that market.
  **Source:**  Market Match website.
- **`BR-get-product-feedback`:** A brand can receive feedback on their product based on the ratings submitted by consumers.
  **Source:**  Market Match website.
- **`BR-product-media-limit`:** A product can have up to three pictures and one video. The video is a link to YouTube, Vimeo, or another video site, or a video file the brand sends; which other sites, and how large a file, are still open (`OI-49`).
  **Source:**  09-21-2026 Client Meeting; 10-26-2026 Client Meeting (links beyond YouTube, and video files).
- **`BR-text-card`:** An item that needs no picture can be created as a text-only card.
  **Source:**  09-21-2026 Client Meeting.
- **`BR-approve-product`:** Every product a brand submits (`BR-submit-product`), whether one at a time, by spreadsheet, or straight from its own system (`BR-connect-product-system`), and any later update the brand makes to its images or details, must be approved by the Market Match admin before it is published.
  **Source:**  09-21-2026 Client Meeting; 10-21-2026 Client Meeting (approval extends to imported products).
- **`BR-products-brand-only`:** Only brands upload products to Market Match. Vendors do not upload products; they select categories.
  **Source:**  Demetrie King, text message, 10-23-2026; confirmed in the 10-26-2026 Client Meeting.
- **`BR-connect-product-system`:** A brand the client is working with can send its products to Market Match straight from the system where it already keeps them, instead of the client entering each product by hand. Only brands the client is working with can connect this way.
  **Source:**  10-21-2026 Client Meeting.
- **`BR-multiple-categories`:** A product can belong to more than one category, so the client does not have to rebuild it for each category it fits. Expected to apply later rather than now; today a product belongs to one category.
  **Source:**  10-21-2026 Client Meeting.
- **`BR-photo-size`:** Brands supply product photos as JPEG or PNG files under 3 MB each; WebP and other formats are not accepted.
  **Source:**  10-21-2026 Client Meeting (size); 10-26-2026 Client Meeting (formats).
- **`BR-brand-categories`:** A brand creates its own categories and says which category each of its products belongs in. A brand's categories hold only that brand's products, so when the admin builds a market for a brand, choosing one of its categories brings in every product in it.
  **Source:**  10-26-2026 Client Meeting.
- **`BR-admin-issues-api-key`:** The admin gives each brand the key its own system uses to send products, after he has signed the brand and created its organization; brands do not create their own keys. Expected to change later, when brands may set themselves up.
  **Source:**  10-26-2026 Client Meeting.
- **`BR-results-restart-on-change`:** When a brand changes a product's photos or details, the product's results start fresh from the change, and its results from before the change are kept so the brand can compare the two.
  **Source:**  10-26-2026 Client Meeting.
- **`BR-remove-product`:** A brand can remove its own products without the admin's approval, but only a limited number of times, so that brands do not add and remove products over and over and skew their results. The limit is still open (`OI-48`).
  **Source:**  10-26-2026 Client Meeting.
- **`BR-keep-removed-product-data`:** When a brand removes a product, Market Match keeps the product's results, because the brand may later ask for them, and the client may charge for providing them.
  **Source:**  10-26-2026 Client Meeting.

### 2.3 Markets

- **`BR-submit-market`:** An entity can create a market with a name.
  **Source:**  Market Match website.
- **`BR-get-market-feedback`:** A market can receive feedback on its products' ratings submitted by consumers.
  **Source:**  Market Match website.
- **`BR-market-code`:** Each market has an auto-generated code that is unique to that market.
  **Source:**  09-21-2026 Client Meeting.
- **`BR-market-type`:** A market is either a brand market or a standard market.
  **Source:**  09-21-2026 Client Meeting.
- **`BR-market-organization`:** Each market is assigned to an organization.
  **Source:**  09-21-2026 Client Meeting.
- **`BR-market-categories`:** A market is made up of one or more categories, each holding the items consumers swipe through. A category can be a product grouping or a survey question.
  **Source:**  09-21-2026 Client Meeting.
- **`BR-public-market`:** A market can be given public access, in which case a consumer can join it by QR code or link without signing in or giving an email. Its results are still reported to the organization it is assigned to.
  **Source:**  09-21-2026 Client Meeting.
- **`BR-code-requires-sign-in`:** A consumer must be signed in to join a market by entering its unique code.
  **Source:**  09-30-2026 Client Meeting.
- **`BR-select-category`:** A consumer who joins a market chooses which of that market's categories to swipe through.
  **Source:**  09-30-2026 Client Meeting.
- **`BR-create-market-admin-only`:** Only the Market Match admin can create markets; brands and vendors cannot create their own. Expected to change after the current phase, once pricing for self-serve markets is set. Categories for a brand's own products are the brand's to create (`BR-brand-categories`).
  **Source:**  09-21-2026 Client Meeting; 10-26-2026 Client Meeting (brands create their own categories).

### 2.4 White-Label-Architecture (Organizations)

- **`BR-configure-branding`:** An organization can customize its instance of Market Match (outside of the main Market Match app) with its own logo, colors, and branding so the experience appears as its own product.
**Source:**  Client brief.
- **`BR-access-own-data`:** An organization can only access its own users, survey configurations, and collected data, kept fully separate from every other organization on the shared infrastructure.
**Source:**  Client brief.
- **`BR-connect-api`:** An organization can connect its external systems to Market Match through an authenticated API to manage surveys, users, campaigns, and responses programmatically.
**Source:**  Client brief.

### 2.5 Feedback

- **`BR-capture-feedback`:** Market Match captures behavioral data from consumer interactions beyond the explicit ratings consumers submit. The data points recorded are:
  - **Swipe Left / Swipe Right** (swipe direction)
  - **Time-to-Swipe**, averaged across consumers as **Average Decision Time**
  - **Average Dwell Time**
  - **Flip** (reported as flip rate)
  - media clicks (`BR-media-clicks`)
  - session activity

  Terms in bold are as defined in the [project glossary](project-glossary.md).
  **Source:**  Client brief; 09-30-2026 Client Meeting.
- **`BR-media-clicks`:** Market Match counts the clicks each of a product's pictures and its video receives. Video engagement is measured by clicks only, not watch time.
  **Source:**  09-30-2026 Client Meeting.
- **`BR-engagement-funnel`:** For each market, Market Match tracks consumers through three stages: viewing the market (which begins when the code is entered), starting to swipe, and completing it.
  **Source:**  09-30-2026 Client Meeting.
- **`BR-market-completion-time`:** A market's completion time is the average time consumers take to go through every item in all of its categories. It is reported for the market as a whole, not per item.
  **Source:**  09-30-2026 Client Meeting.
- **`BR-vendor-feedback-scope`:** A vendor can see, for its markets, only each item's right swipes, left swipes, and reach (ranked from most right-swiped to least, narrowable by category and top N) and the market's completion time. A vendor cannot see swipe-behavior data such as dwell time.
  **Source:**  09-30-2026 Client Meeting.
- **`BR-brand-feedback-scope`:** A brand can see swipe-behavior data for each of its products (swipes, like rate, flip rate, dwell time, media clicks), totaled across every market the product has appeared in rather than per market.
  **Source:**  09-30-2026 Client Meeting.
- **`BR-admin-feedback-scope`:** The Market Match admin can see swipe counts and users, but not an organization's detailed data points.
  **Source:**  09-30-2026 Client Meeting.

### 2.6 Organizations and Roles

- **`BR-create-organization`:** Only the Market Match admin can create an organization and add users to it by email.
  **Source:**  09-21-2026 Client Meeting.
- **`BR-default-consumer-role`:** Every user holds the consumer role by default when they sign in.
  **Source:**  09-21-2026 Client Meeting.
- **`BR-admin-role`:** Only Market Match (Demetrie King) holds the admin role.
  **Source:**  09-21-2026 Client Meeting.
- **`BR-assign-role`:** Only the admin can assign a user the brand or vendor role. A user with assigned roles can switch between them; a user with none cannot see the dashboard.
  **Source:**  09-21-2026 Client Meeting.
- **`BR-dashboard-access`:** Brand and vendor users get dashboard access only through **WorkOS**. The admin creates the user by email, adds them to an **Organization**, and assigns their **Role** there (`BR-create-organization`, `BR-assign-role`). The user then signs in at login.marketmatch.app with a **One-Time Code** or a security key and sees only what their Organization and Role allow. Terms in bold are as defined in the [project glossary](project-glossary.md).
  **Source:**  09-21-2026 Client Meeting.
- **`BR-view-org-markets`:** Only users whose email is assigned to an organization can see the markets assigned to that organization and their results. Departments of one institution that must not see each other's results are set up as separate organizations.
  **Source:**  09-21-2026 Client Meeting.

### 2.7 Pricing

- **`BR-survey-pricing`:** The price of a survey depends on what must be built (the number of categories and line items), how long the survey runs, and how many people it goes to.
  **Source:**  09-21-2026 Client Meeting.

### 2.8 Data Collection and Privacy

- **`BR-collect-email-only`:** The only personal information Market Match collects from an organization's users is their email address.
  **Source:**  09-21-2026 Client Meeting.
- **`BR-protect-pii`:** Personal data must be encrypted at rest and in transit and never stored in plaintext.
  **Source:**  09-07-2026 Client Meeting.