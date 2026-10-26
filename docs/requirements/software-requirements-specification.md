# Software Requirements Specification

**Project:** Market Match
**Team:** 11
**Client:** Demetrie King
**Version:** 0.1

---

_**How to use this template.** Instructions appear in italic square brackets. Fill in underneath them and leave them in place until the document is stable._

_**What this document is, and what it is not.** The specification describes the external behavior of your system completely enough that a developer can build it and a tester can check it. What it is **not** is a container for everything you have written. Your glossary, vision and scope, use cases, and business rules are separate documents with their own identifiers, and this one **links to them rather than repeating them**._

_That makes the specification mostly a hub. Read that as a feature. One fact, one home: a business rule copied in here is a business rule that will disagree with `business-rules.md` by October, and nobody will notice which copy is right. The sections below that say "link to" are supposed to be short._

_What this document owns outright: the requirements that have no other home. Functional requirements that are not part of any use case, quality attributes, external interfaces, data requirements, operating environment, and constraints._

## Identifiers

_Every requirement in this document carries a name-based slug. Create only the spaces your project actually needs._

| Space | For | Example |
|---|---|---|
| `FR-<AREA>-<slug>` | Functional requirements outside any use case | `FR-SAVE-autosave-active` |
| `UI-<slug>` | User interface requirements | `UI-spa-views` |
| `SI-<slug>` | Software and system interfaces | `SI-llm-proxy-only` |
| `CI-<slug>` | Communications interfaces | `CI-email-notifications` |
| `DI-<slug>` | Data requirements | `DI-persist-graph` |
| `OE-<slug>` | Operating environment | `OE-supported-browsers` |
| `CO-<slug>` | Design and implementation constraints | `CO-single-application` |
| `AS-<slug>` / `DE-<slug>` | Assumptions and dependencies | `AS-supported-browser`, `DE-llm-service` |

_Quality attributes get one space per attribute, so the identifier says which kind of quality it is at the place it is cited: `USE-` usability, `PER-` performance, `SEC-` security, `SAF-` safety, `AVL-` availability, `ROB-` robustness, `SCA-` scalability, `INT-` interoperability, `MNT-` maintainability._

_Requirements cited from elsewhere keep their own identifiers: `UC-*` from [use-cases.md](use-cases.md), `BR-*` from [business-rules.md](business-rules.md), `BO-*`, `SM-*`, `FEAT-*` from [vision-and-scope.md](vision-and-scope.md)._

## Revision History

| Date       | Version | Description | Author      |
|------------|---|---|-------------|
| 09/14/2026 | 0.1 | Initial draft | Vinh Nguyen |
| 10/25/2026 | 0.2 | Product import requirements: §5.2 functional requirements for Brand-scoped storage, Approval, server-side checks, and the published product contract; §8.3 and §8.4 for Brands' own systems; §9.2, §9.3, §9.4, §9.6, and §9.7 attributes for import, API Keys, and privacy | Matthew Stafford |
| 10/26/2026 | 0.3 | Added FDBK functional requirements, updated the business domain model and data dictionary, documented feedback reports, and added data management considerations covering privacy, integrity, and retention. | Kritika Karanjit |

---

## 1. Introduction

### 1.1 The purpose of Market Match

Market Match is a swipe-based marketing and consumer feedback platform designed to make market research more interactive. The platform connects consumers, brands, and markets. Consumers can access a market and swipe through products to indicate interest or disinterest, while brands can use the resulting feedback to better understand consumer preferences.

An MVP of Market Match already exists and recorded approximately 3,600 swipes at the most recent I-Fest. Market Match is beginning to expand to additional colleges and is working with TCU to gather feedback about what students would like to see at events.

The client wants Market Match to grow beyond a traditional survey platform into a broader marketing platform where organizations can collect consumer feedback about products and ideas, including products that have not yet been released. The client also wants to expand toward enterprise organizations through white-label instances and API connections. As Market Match expands, the platform needs to remain stable while supporting increasing numbers of users and larger amounts of collected data.

### 1.2 The purpose of this document

This document specifies the functional and nonfunctional requirements for the Market Match release to be delivered by Team 11, with the release scope to be confirmed with the client and recorded in [vision-and-scope.md](vision-and-scope.md). It provides a shared reference for the client, developers, and testers to understand the expected system behavior, data requirements, external interfaces, quality attributes, operating environment, and implementation constraints. These requirements guide development and provide a basis for testing and evaluating whether the delivered software meets the agreed client needs.

The specification links to the project glossary, vision and scope, use cases, and business rules rather than duplicating their content. Requirements that are not defined in those documents are specified here, and unresolved questions are tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md).

### 1.3 Document conventions

_[Any typographical conventions, and the identifier formats above, so that someone adding a requirement later knows how to name it.]_

The following conventions apply throughout this specification:

- **Requirement wording:** "Shall" identifies a required system behavior or property. Functional requirements in section 5.2 use the EARS patterns provided there to state the relevant trigger or condition and the expected system response. Each requirement must be specific enough to verify through a test, inspection, or measurement.
- **Identifiers:** Requirements use the formats defined in [Identifiers](#identifiers). Prefixes and feature area codes are uppercase, and descriptive slugs use lowercase words separated by hyphens. Identifiers are unique within their namespace and remain stable when requirements are moved or revised. A retired identifier is marked withdrawn rather than reused for a different requirement.
- **Cross-references:** References to use cases, business rules, objectives, success metrics, and features retain the identifiers assigned in their source documents. Their definitions remain in those documents rather than being copied into this specification.
- **Terminology:** Project terms follow the definitions in the [project glossary](project-glossary.md). Acronyms are expanded on first use in the document's project-specific content.
- **Formatting:** Backticks distinguish identifiers, field names, and literal values. Markdown links point to supporting documents or sections. Italic template instructions and worked examples are drafting guidance, not approved Market Match requirements.
- **Unresolved decisions:** Unconfirmed requirements and values are explicitly marked as proposed or to be confirmed, with the corresponding question recorded in [OPEN-ISSUES.md](OPEN-ISSUES.md). Assumptions are identified separately from confirmed requirements.

### 1.4 References

_[Every document this specification refers to, with a link. At minimum, the four other documents in this folder. Include external standards you must conform to.]_

| Reference | Purpose |
|---|---|
| [Project glossary](project-glossary.md) | Defines the terms used consistently throughout the Market Match requirements. |
| [Vision and scope](vision-and-scope.md) | Records the business objectives, success metrics, stakeholders, features, and release boundaries. |
| [Use cases](use-cases.md) | Specifies user workflows, system responses, alternative flows, and exceptions. |
| [Business rules](business-rules.md) | Records the business policies and rules that the software must enforce, with their sources. |
| [Open issues](OPEN-ISSUES.md) | Tracks unanswered questions and unresolved requirements decisions. |
| [First client meeting notes](../client-meetings/client-meeting-1.md) | Provides initial client context, the existing consumer workflow, user types, and expansion goals. |
| [Napkin Round 0](../napkin-round-0.md) | Records the team's initial technical assessment, proposed direction, and project risks; proposals are not client-approved requirements. |
| [The Easy Approach to Requirements Syntax (EARS)](https://alistairmavin.com/ears/) | Provides the requirement-writing approach used for non-use-case functional requirements in section 5.2. |

Referenced project documents are working drafts. Template examples and unresolved proposals in those documents do not establish requirements for Market Match. Applicable external standards and their required versions will be added when confirmed with the client or through an explicit team decision.

---

## 2. Overall Description

### 2.1 Product perspective

_[How this system relates to other systems and to the user's environment. Self-contained, or one component of something larger? Link to the product perspective section of your vision and scope and to your architecture's context diagram rather than redrawing them.]_

### 2.2 User classes and characteristics

_[The kinds of user, and what distinguishes them: frequency of use, technical skill, privilege level, whether they are inside or outside the client's organization. Link to the stakeholder profiles in your vision and scope; what belongs here is what affects the software's behavior, especially permissions.]_

### 2.3 Operating environment

_[The environment the software runs in: hardware, operating systems and versions, browsers, where users and servers are located, and any other software it has to coexist with.]_

_Examples:_

- _`OE-supported-browsers`: The system shall operate correctly on the current and previous major versions of Chrome, Firefox, Safari, and Edge._
- _`OE-server-platform`: The system shall run on a server running the current corporate-approved version of Linux._
- _`OE-access-paths`: The system shall permit access from the corporate intranet, from a VPN connection, and from Android and iOS phones and tablets._

### 2.4 Design and implementation constraints

_[Anything that limits the developers' options: corporate or regulatory policy, hardware limits, required languages or databases, coding standards, interfaces to other applications.]_

_Examples:_

- _`CO-database-engine`: The system shall use the corporate standard database engine._
- _`CO-language-version`: The backend shall be written in Java 21._
- _`CO-coding-standard`: Design, code, and maintenance documentation shall conform to the client's development standard._

_The constraint students forget: **who maintains this after you graduate, and what do they already know how to run?** If the answer is one person who knows Python, a Spring Boot service is a constraint violation nobody wrote down._

### 2.5 Assumptions and dependencies

_[An assumption is a factor you believe true without proof, which would change these requirements if it turned out false. A dependency is something outside your control that the project relies on: an external API, a third-party library, a change someone else has to make.]_

_Examples:_

- _`AS-supported-browser`: Users access the system with a browser that supports the ECMAScript version the frontend targets._
- _`DE-payroll-integration`: Operation depends on changes being made in the Payroll System to accept payment requests for meals ordered through this system._

---

## 3. Project Glossary

_[Link only. The glossary is [project-glossary.md](project-glossary.md).]_

## 4. Vision and Scope

_[Link only. Business requirements, objectives, metrics, and scope live in [vision-and-scope.md](vision-and-scope.md).]_

---

## 5. Functional Requirements

### 5.1 Use cases

_[Link to [use-cases.md](use-cases.md). Most of your system's behavior is specified there, as use cases, and it does not get restated here.]_

### 5.2 Non-use-case functional requirements

_[Behavior that is real, testable, and belongs to no single use case: autosave, validation applied everywhere, notification, authorization, audit logging. If you find yourself writing the same step into six use cases, it belongs here instead._

_Group them under sub-headings by concern, and write each one using an [EARS](https://alistairmavin.com/ears/) shape so that it cannot be read two ways:_

- _**Ubiquitous:** The `<system>` shall `<response>`._
- _**Event driven:** When `<trigger>`, the `<system>` shall `<response>`._
- _**State driven:** While `<in a state>`, the `<system>` shall `<response>`._
- _**Optional:** Where `<feature is included>`, the `<system>` shall `<response>`._
- _**Unwanted behavior:** If `<precondition>`, then the `<system>` shall `<response>`._

_A worked example from Project Pulse paired an event-driven autosave requirement with its 30-second interval._

_**Every requirement here needs an oracle.** If you cannot say how a tester would tell whether it holds, it is not a requirement yet.]_

#### Products a Brand submits

These hold for every way a Brand's products come in: `UC-BRND-create-product`, `UC-BRND-import-products`, `UC-BRND-send-products`, and `UC-BRND-update-product`.

- **`FR-PROD-brand-scoped-storage`** (ubiquitous): The system shall store every product and every change a Brand submits in that Brand's Inventory only, taking the Brand from the signed-in user's Organization or from the API Key and never from the submitted content. *Oracle:* a submission that names another Brand, or another Brand's product, stores nothing in that Brand's Inventory. Carries out `BR-products-brand-only` and `BR-connect-product-system`.
- **`FR-PROD-hidden-until-approved`** (state driven): While a product or a change is waiting for Approval or has been returned, the system shall not show it to any Consumer. *Oracle:* no Market a Consumer can reach contains a waiting or returned product, or the content of a waiting change. Carries out `BR-approve-product`.
- **`FR-PROD-server-checks`** (ubiquitous): The system shall apply the same product checks on the server (required fields, media limits, and one SKU per Brand) to every product submission, whether made by hand, by spreadsheet, or through the API. *Oracle:* the same invalid product is refused, with the same reasons, by all three routes. Today the client's app checks spreadsheet rows only in the browser.

#### The product API

- **`FR-API-published-contract`** (ubiquitous): The system shall publish the product import contract (the fields, their formats, the 200-product batch limit, and the result returned for each product) where every Brand with an API Key can read it. *Oracle:* a batch built only from the published contract is accepted. Needed by `UC-BRND-send-products` and `UC-BRND-generate-api-key`.

#### Consumer feedback and insights

These requirements support `FEAT-consumer-feedback` and `FEAT-feedback-insights` across `UC-FDBK-rate-product`, `UC-FDBK-flip-card`, `UC-FDBK-open-card-media`, and `UC-FDBK-complete-market`.

- **`FR-FDBK-session-association`** (ubiquitous): The system shall associate captured consumer feedback and interaction records with the relevant Market session and applicable Product, Line Item, or media item. *Oracle:* A stored swipe, flip, or media interaction can be traced to its Market session and the item involved.

- **`FR-FDBK-public-identity`** (state driven): While a Public Access Consumer's temporary identity remains valid, the system shall associate that Consumer's return visits on the same device with the same identity. *Oracle:* A Public Access Consumer who leaves and returns before the identity expires is not counted as a new Consumer solely because of the return visit. The exact expiration period remains to be determined.

- **`FR-FDBK-feedback-insights`** (event driven): When an authorized Brand requests feedback insights for its products, the system shall calculate the applicable metrics using the feedback and interaction data captured for those products. *Oracle:* The reported metrics can be reconciled with the underlying feedback records, and data from unrelated Brands is excluded.

- **`FR-FDBK-market-funnel`** (ubiquitous): The system shall support Engagement Funnel reporting for both Brand Markets and Standard Markets using their recorded Market session stages. *Oracle:* Funnel counts can be derived from recorded session stages for either Market type. Vendor visibility remains unresolved under `OI-21`.

---

## 6. Business Rules

_[Link only, to [business-rules.md](business-rules.md). Business rules are a rich source of requirements because they dictate properties the system must have in order to conform to them, but the rules themselves are properties of the client's business, not of your software, and they have their own document.]_

---

## 7. Data Requirements

### 7.1 Business domain model

_[The entities in the problem domain and how they relate, as a mermaid class diagram. Model the **business**, not your database schema: this is what the client would recognize, before any decision about tables or persistence.]_

```mermaid
classDiagram
    class Consumer
    class Market
    class MarketSession
    class Category
    class Product
    class Card
    class Feedback
    class CardFlip
    class MediaItem
    class MediaInteraction

    Consumer "1" --> "0..*" MarketSession : participates in
    Market "1" --> "0..*" MarketSession : has
    Market "1" --> "0..*" Category : contains
    Category "1" --> "0..*" Card : contains
    Card "*" --> "1" Product : presents
    MarketSession "1" --> "0..*" Feedback : records
    MarketSession "1" --> "0..*" CardFlip : records
    MarketSession "1" --> "0..*" MediaInteraction : records
    Feedback "*" --> "1" Card : rates
    CardFlip "*" --> "1" Card : flips
    Card "1" --> "0..*" MediaItem : displays
    MediaInteraction "*" --> "1" MediaItem : opens
```

### 7.2 Data dictionary

_[Each entity's fields, with data type, allowed values, defaults, and validation rules. Where a use case already specifies a field's validation in its Associated Information, cite the use case instead of repeating it.]_

#### FDBK - Consumer Feedback and Data Capture

The following fields support `UC-FDBK-rate-product`, `UC-FDBK-flip-card`, `UC-FDBK-open-card-media`, and `UC-FDBK-complete-market`. These are business-level data requirements, not database column definitions.

| Entity | Field | Data type | Rules / Description |
|---|---|---|---|
| Consumer | Consumer reference | Identifier | Identifies a signed-in Consumer or a temporary Public Access Consumer. |
| Market Session | Session reference | Identifier | Uniquely identifies a Consumer's participation in a Market. |
| Market Session | Market reference | Identifier | Identifies the associated Market. |
| Market Session | Session stages | Enumeration / timestamps | Records entered, viewed, started, and completed stages when applicable. |
| Market Session | Completion Time | Duration | Calculated from the applicable start stage to completion; incomplete sessions have zero Completion Time. |
| Market Session | Selected Categories | Collection of identifiers | Records Categories selected during the same Market session, including Categories added later. |
| Feedback | Card / Line Item reference | Identifier | Identifies the rated item. |
| Feedback | Swipe direction | Enumeration | Left or right, as specified in `UC-FDBK-rate-product`. |
| Feedback | Swipe timestamp | Timestamp | Records when the Consumer rates the Card. |
| Feedback | Decision Time | Duration | Refer to the calculation defined in `UC-FDBK-rate-product`. |
| Feedback | Dwell Time | Duration | Refer to `UC-FDBK-rate-product` for the applicable measurement rules. |
| Card Flip | Card reference | Identifier | Identifies the Card flipped by the Consumer. |
| Card Flip | Flip interaction | Event / timestamp | Records the flip activity described in `UC-FDBK-flip-card`. |
| Media Interaction | Media item reference | Identifier | Identifies the specific photo or video, not just its position in the Card. |
| Media Interaction | Media slot | Enumeration | `PHOTO_1`, `PHOTO_2`, `PHOTO_3`, or `VIDEO`. |
| Media Interaction | Clicked at | Timestamp | Records a deliberate media Click. Repeated taps on the same photo count as one Click per Consumer. |
| Media Interaction | Photo View Time | Duration (milliseconds) | Photos only; nonnegative; summed across viewings within a Market session. Video watch time is not captured. |

The exact expiration period for temporary Public Access Consumer identities remains undecided. Demographic data collection and retention must be reconciled with `BR-collect-email-only` and `OI-45`. Vendor access to funnel reporting remains open under `OI-21`.

### 7.3 Reports

_[Any report the system generates: who reads it, what it contains, how often, and in what format. Reports are where clients discover late that a field they need was never captured, so specify them early.]_

#### FDBK - Consumer Feedback Reports

Market Match provides feedback insights to authorized Brands using data captured during Consumer interactions with Markets and Cards. The reports below describe the expected information. Exact metric calculations and access permissions remain subject to the linked use cases and open issues.

| Report | Intended audience | Information included | Frequency / format |
|---|---|---|---|
| Product Feedback Insights | Owning Brand | Swipe counts, product reach, decision time, dwell time, and available demographic breakdowns | On request through the Brand Dashboard; exact refresh frequency not yet specified |
| Card Interaction Insights | Owning Brand | Card flips, front/back interactions, and related engagement measurements | On request through the Brand Dashboard; exact refresh frequency not yet specified |
| Media Engagement Insights | Owning Brand | Clicks for individual photos and videos and Photo View Time for photos | On request through the Brand Dashboard; exact refresh frequency not yet specified |
| Engagement Funnel | Authorized Market stakeholders | Counts for entered, viewed, started, and completed stages, plus Completion Time | On request through a reporting interface; exact refresh frequency not yet specified |

The Engagement Funnel applies to both Standard Markets and Brand Markets. Vendor visibility is unresolved (`OI-21`). The treatment of incomplete sessions in average Completion Time (`OI-33`), the Average Swipes formula (`OI-34`), and demographic collection and retention (`OI-45`) require confirmation. Metrics must follow the definitions in the FDBK use cases and project glossary.

### 7.4 Data acquisition, integrity, retention, and disposal

_[Where the data comes from, how it is kept correct, how long it is kept, and how it is destroyed. If your system holds anything about students or other identifiable people, this section is not optional, and its content is usually a business rule you should cite rather than invent.]_

---

#### FDBK - Data Acquisition, Integrity, Retention, and Disposal

**Data acquisition:** Market Match collects feedback during Consumer participation in Markets. This includes product swipes, Card flips, photo and video clicks, Photo View Time, Decision Time, Dwell Time, and Market session stages. Records are associated with the relevant Market session and product or media item. Signed-in Consumers use their authenticated identity, while Public Access Consumers use a temporary identity.

**Data integrity:** Each interaction must be associated with the correct Consumer, Market session, and item. Repeated clicks on the same photo count once per Consumer, while Photo View Time accumulates across repeat viewings. Retry handling must prevent duplicate feedback submissions. Market session records must remain consistent when Consumers leave, resume, or select additional Categories.

**Privacy and access:** Feedback insights must be available only to authorized users. Brands must not access private feedback belonging to unrelated Brands. Demographic data collection and retention must be reconciled with `BR-collect-email-only`, `SEC-pii-protection`, and `OI-45`.

**Retention and disposal:** Retention periods for feedback, Market sessions, and demographic information have not been finalized. A temporary Public Access Consumer identity expiration of approximately 30 days was discussed but not approved. The team must confirm retention periods, deletion procedures, and responsibility for disposal before implementation.

**Open decisions:** Demographic retention (`OI-12`, `OI-45`), Vendor access to funnel reports (`OI-21`), incomplete session handling (`OI-33`), and Average Swipes calculation (`OI-34`) remain unresolved.

## 8. External Interface Requirements

### 8.1 User interfaces

_[The user-facing surfaces, at requirement level: which views exist, standards they must conform to, accessibility requirements. Link to wireframes or prototypes rather than describing pixel layouts.]_

### 8.2 Hardware interfaces

_[Any hardware the system talks to, or "none".]_

### 8.3 Software interfaces

_[Other software systems yours connects to: what crosses the boundary, in which direction, in what format, and what happens when the other side is unavailable.]_

- **`SI-brand-product-system`:** A Brand's own system, wherever it keeps its products, sends batches of up to 200 products into Market Match's API, authenticated by the Brand's API Key, and receives a result for every product (`UC-BRND-send-products`). The format is the published product contract (`FR-API-published-contract`). If Market Match is unavailable, nothing in a batch is half-applied, and the Brand's system sends the same batch again without creating duplicates (`ROB-import-resend`).

The interfaces that already exist (WorkOS for sign-in, Cloudflare for hosting and storage, and YouTube for video links) are described in the architecture-of-record's context view and are to be added here when this section is completed.

### 8.4 API document

_[Link to your API documentation. It is generated from the code, so link it rather than transcribing endpoints that will be stale within a week.]_

The product import contract (`FR-API-published-contract`) is generated from the code once the product API exists, and is linked here then.

### 8.5 Communications interfaces

_[Email, notifications, messaging, and the protocols involved.]_

---

## 9. Quality Attributes

_[How well the system does what it does. **This is the section that decides whether your client is happy with software that meets every functional requirement**, so do not treat it as a formality.]_

_The rule for every entry: an adjective is not a requirement. "Fast", "easy", "secure", and "user-friendly" are the starting point of a conversation, not the end of one. Each entry needs a number and a way to measure it._

_Write one subsection per attribute your project actually has, and say "not applicable" with a reason for the ones it does not. An explicit "not applicable" is information; silence is not._

### 9.1 Usability

_Example: `USE-wcag-aa`: All user-facing views shall conform to WCAG 2.1 level AA._

### 9.2 Performance

- **`PER-import-results`:** For one sending of 200 products, by spreadsheet or through the API, the system shall return the result for every product within a time the client sets, at the 95th percentile, measured from receiving the sending to returning the last result. *Pending `OI-44`*: the threshold is the client's to give.

### 9.3 Security

- **`SEC-authentication`:** The system shall authenticate every request to a non-public endpoint, by a signed-in session or an API Key, and shall refuse an unauthenticated request without revealing whether the requested resource exists. *Measure:* 100% of non-public endpoints, called without credentials, are refused.
- **`SEC-brand-isolation`:** No request authenticated as one Brand, by session or API Key, shall read or change another Brand's products. *Measure:* 0 cross-Brand reads or writes in a test that calls every product endpoint as Brand A against Brand B's products. Carries out `BR-products-brand-only` and `BR-connect-product-system`.
- **`SEC-api-key-strength`:** Each API Key shall carry at least 256 bits of randomness, shall be shown to its Brand only once, when generated, and shall be stored only as a one-way hash from which the key cannot be recovered. *Measure:* inspecting storage finds no value that is, or can be turned back into, a key. Team decision, 2026-10-25, following common industry practice for API tokens.
- **`SEC-api-key-ending`:** A replaced or revoked API Key, or one whose Brand's access has been removed, shall be refused on 100% of requests from the moment it ends. *Measure:* a request with each kind of ended key is refused, in a test run immediately after the key ends.
- **`SEC-pii-protection`:** Personal data shall be encrypted at rest and in transit and never stored in plaintext (`BR-protect-pii`). How this applies on top of the encryption Cloudflare D1 already provides at rest is decided in the architecture-of-record. Which personal data Market Match may hold at all is open: `BR-collect-email-only` allows only an email address, while the feedback use cases store demographic answers (`OI-45`).

### 9.4 Safety

_[Conditions under which the system could contribute to harm, and what prevents it. For most projects in this course the honest answer is `SAF-not-applicable`, with a sentence saying why.]_

- **`SAF-not-applicable`:** Market Match collects product preferences and shows marketing content; no failure of it can cause physical harm. Its worst failures lose or expose data, which `SEC-*` and `ROB-*` cover.

### 9.5 Availability

_Example: `AVL-uptime`: The system shall be available 99% of the time during the academic term, excluding announced maintenance windows._

### 9.6 Robustness

- **`ROB-import-resend`:** When an import or a sending stops partway and the same spreadsheet or batch is sent again, the system shall create 0 duplicate products, matching each product by its SKU within the Brand. *Measure:* interrupt an import of 200 products partway, send it again, and count products per SKU.

### 9.7 Scalability, interoperability, maintainability

_[Add the ones that apply, with `SCA-`, `INT-`, and `MNT-` identifiers. Maintainability is the one this course cares about most, because someone inherits your code in January.]_

- **`SCA-import-batch-limit`:** One sending, by spreadsheet or through the API, shall carry at most 200 products, matching the largest catalog among the client's Brands today (10 to 200 SKUs); a larger one is refused whole, with the limit, so the Brand sends smaller batches. *Measure:* a 200-product sending is accepted and a 201-product sending is refused with the limit. Team decision, 2026-10-25.

---

## 10. Internationalization and Localization

_[Languages, character sets, time zones, date and currency formats. If the answer is a single locale, say so and say why, because that is a real constraint on who can use the system.]_

---

## 11. Other Requirements

_[Anything real that fits nowhere above: legal, licensing, installation, training, documentation. Delete this section if it is empty rather than leaving it as a placeholder.]_

---

## Working this document with your agent

_[Delegate: converting prose requirements into EARS shapes; checking that every `UC-*`, `BR-*`, and `FEAT-*` cited here exists in the document that owns it; finding functional requirements that appear in several use cases and should be lifted into section 5.2; drafting an oracle for a quality attribute you have stated only as an adjective._

_Keep human: the numbers. Every threshold in section 9 is a commitment somebody has to live with, and an agent will supply a plausible one (99.9% uptime, 200ms response) that nobody asked for and no one can meet. A number in this document either came from your client, from a measurement, or from a decision your team made deliberately and can defend._

_**The specific failure to watch for: invented precision.** A generated specification reads as authoritative at exactly the points where it is guessing. Check every number, every browser version, every retention period against something real, and put the ones you cannot verify in [OPEN-ISSUES.md](OPEN-ISSUES.md) instead of leaving a confident guess in the document your team will build from.]_
