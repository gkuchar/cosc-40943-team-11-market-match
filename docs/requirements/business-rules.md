# Business Rules

**Project:** Market Match
**Team:** 11
**Client:** Demetrie King
**Version:** 0.1

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

---

## 1. Introduction

### 1.1 Purpose

This document collects the policies, regulations, standards, and formulas that govern the Market Match business that our app operates in, so the specification can cite them rather than restate them.

### 1.2 Scope

These rules cover the participation and data policies of the Market Match business as
described in the client brief and first client meeting.

In scope:

- **Consumer participation:** how consumers sign in, rate and inspect products, select
  markets, and accrue and forfeit lottery entries (2.1).
- **Brand participation:** how brands create products, join markets, and receive feedback
  (2.2).
- **Market lifecycle:** how markets are created and how they receive feedback (2.3).
- **White-label operation:** how partner organizations brand their own instance, keep
  their data isolated, and connect via API (2.4).
- **Behavioral data capture:** what interaction data the platform records beyond explicit
  ratings (2.5).

Out of scope for this document:

- **Prize disbursement.** These rules record how lottery entries are earned and expire,
  but the drawing, winner selection, and payout of cash prizes (including any sweepstakes
  or gambling regulations governing them) are business processes our system does not touch
  as currently defined.
- **API engineering constraints.** Authentication schemes, authorization, rate limiting,
  versioning, and documentation for `BR-connect-api` are our team's design decisions and
  belong in the specification, not here, since the client did not dictate them as policy.
- **Demographic data handling.** The client noted demographic collection "where
  appropriate," but the consent and legal-appropriateness policy governing it has not yet
  been sourced, so no rule captures it. To be revisited once the client confirms the policy.

---

## 2. Rules

### 2.1 Consumers

- **`BR-sign-in`:** A consumer can ssign into the app via email + one-time code sent to email.
- **`BR-rate-product`:** A consumer can swipe right on a product to signal interest or swipe left on a product to signal disinterest.
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
- **`BR-get-product-feedback`:** A brand can receieve feedback on their product based on the ratings submitted by consumers.
  **Source:**  Market Match website.

### 2.3 Markets

- **`BR-submit-market`:** An entity can create a market with a name.
  **Source:**  Market Match website.
- **`BR-get-market-feedback`:** A market can receieve feedback on its products' ratings submitted by consumers.
  **Source:**  Market Match website.

### 2.4 White-Label-Architecture (Organizations)

- **`BR-configure-branding`:** An organization can customize its instance of Market Match (outside of the main Market Match app) with its own logo, colors, and branding so the experience appears as its own product.
**Source:**  Client brief.
- **`BR-access-own-data`:** An organization can only access its own users, survey configurations, and collected data, kept fully separate from every other organization on the shared infrastructure.
**Source:**  Client brief.
- **`BR-connect-api`:** An organization can connect its external systems to Market Match through an authenticated API to manage surveys, users, campaigns, and responses programmatically.
**Source:**  Client brief.

### 2.5 Feedback

- **`BR-capture-feedback`:** Market Match captures behavioral data from consumer interactions beyond the explicit ratings consumers submit. This includes but is not limited to swipe direction, swipe speed, time spent viewing an item, and session activity.
**Source:**  Client brief.