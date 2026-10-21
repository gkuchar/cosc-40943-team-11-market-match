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
| 10/16/2026 | 0.2 | Added constraints (2.4), dependencies (2.5), software interfaces (8.3), and quality attributes (9) for Checkpoint 1 feedback | Griffin Kuchar |

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

_The constraint students forget: **who maintains this after you graduate, and what do they already know how to run?** If the answer is one person who knows Python, a Spring Boot service is a constraint violation nobody wrote down._

- `CO-cloudflare-hosting`: The system shall run on the client's existing Cloudflare hosting: two Cloudflare Workers, one serving Production from the main branch and one serving the Preview Link, with Cloudflare storing the platform's image files. **Source:** second client meeting; [Cloudflare](project-glossary.md#cloudflare).
- `CO-workos-identity`: The system shall use WorkOS for users, Organizations, Roles, and sign-in, and shall not implement its own credential store. **Source:** second client meeting; `BR-dashboard-access`; [WorkOS](project-glossary.md#workos).
- `CO-existing-codebase`: Changes shall extend the client's existing Market Match repository and its TypeScript stack (React front end, Node.js-compatible Worker back end) rather than replace it, and shall remain compatible with existing data. **Source:** second client meeting; vision and scope section 4.4; `AS-existing-platform`.
- `CO-client-maintains`: The system shall remain maintainable by the client, who has no technical background and maintains the platform himself by prompting Claude Code. **Source:** first and second client meetings; vision and scope section 4.4.
- `CO-preview-before-production`: No change shall reach Production without first being deployed to and tested on the Preview Link. **Source:** second client meeting; [Preview Link](project-glossary.md#preview-link).

### 2.5 Assumptions and dependencies

_[An assumption is a factor you believe true without proof, which would change these requirements if it turned out false. A dependency is something outside your control that the project relies on: an external API, a third-party library, a change someone else has to make.]_

- `DE-workos`: Sign-in, Organization membership, and Role assignment depend on WorkOS being available. WorkOS has its own production and staging sides, matching Production and the Preview Link. See `SI-workos-auth`.
- `DE-cloudflare`: Hosting, the production database (Cloudflare D1), and image storage depend on Cloudflare. See `SI-d1-storage`, `SI-cloudflare-images`.
- `DE-youtube`: A Card's video is supplied as a YouTube link (`BR-product-media-limit`), so video playback depends on YouTube. See `SI-youtube-video`.

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

_Example: `FR-SAVE-autosave-active`: While a student is editing a weekly activity report during an active week, the system shall persist the draft every 30 seconds._

_**Every requirement here needs an oracle.** If you cannot say how a tester would tell whether it holds, it is not a requirement yet.]_

---

## 6. Business Rules

_[Link only, to [business-rules.md](business-rules.md). Business rules are a rich source of requirements because they dictate properties the system must have in order to conform to them, but the rules themselves are properties of the client's business, not of your software, and they have their own document.]_

---

## 7. Data Requirements

### 7.1 Business domain model

_[The entities in the problem domain and how they relate, as a mermaid class diagram. Model the **business**, not your database schema: this is what the client would recognize, before any decision about tables or persistence.]_

    ```mermaid
    classDiagram
      class Team {
        +String name
      }
      class Student {
        +String email
      }
      Team "1" --> "*" Student : has
    ```

### 7.2 Data dictionary

_[Each entity's fields, with data type, allowed values, defaults, and validation rules. Where a use case already specifies a field's validation in its Associated Information, cite the use case instead of repeating it.]_

### 7.3 Reports

_[Any report the system generates: who reads it, what it contains, how often, and in what format. Reports are where clients discover late that a field they need was never captured, so specify them early.]_

### 7.4 Data acquisition, integrity, retention, and disposal

_[Where the data comes from, how it is kept correct, how long it is kept, and how it is destroyed. If your system holds anything about students or other identifiable people, this section is not optional, and its content is usually a business rule you should cite rather than invent.]_

---

## 8. External Interface Requirements

### 8.1 User interfaces

_[The user-facing surfaces, at requirement level: which views exist, standards they must conform to, accessibility requirements. Link to wireframes or prototypes rather than describing pixel layouts.]_

### 8.2 Hardware interfaces

_[Any hardware the system talks to, or "none".]_

### 8.3 Software interfaces

_[Other software systems yours connects to: what crosses the boundary, in which direction, in what format, and what happens when the other side is unavailable.]_

- `SI-workos-auth`: **WorkOS.** The Application API redirects users to WorkOS sign-in (login.marketmatch.app, One-Time Code or security key) and receives back the user's identity, Organization, and Role over HTTPS. No password passes through Market Match. If WorkOS is unavailable, the system shall refuse sign-in and every authenticated request rather than fall back to any other authentication; Public Access Markets (`BR-public-market`) need no sign-in and are unaffected.
- `SI-d1-storage`: **Cloudflare D1 (Production database).** The Application API reads and writes all Market Match data (Markets, Categories, Inventory, Market sessions, impressions, swipes, Flips, Clicks) through the Worker's D1 binding. If a write fails or its outcome is unknown, the system shall not report success; behavior per use case is in the extensions of `UC-FDBK-rate-product` (4b), `UC-FDBK-complete-market` (2b), and `UC-BRND-create-product` (4c).
- `SI-postgres-local`: **PostgreSQL (local development database).** Developers run the Application API against a local PostgreSQL database holding the same schema as D1. It never holds Production data and is never reachable from Production.
- `SI-cloudflare-images`: **Cloudflare image storage.** The Application API stores Card photos uploaded through `UC-BRND-create-product` and the front end loads them over HTTPS. If an image cannot be loaded, the Card still displays its remaining content.
- `SI-youtube-video`: **YouTube.** A Card's video is a YouTube link stored with the Card (`BR-product-media-limit`); the browser loads it from YouTube directly and Market Match sends YouTube nothing. If the video cannot be loaded, `UC-FDBK-open-card-media` extension 3a applies.

### 8.4 API document

_[Link to your API documentation. It is generated from the code, so link it rather than transcribing endpoints that will be stale within a week.]_

### 8.5 Communications interfaces

_[Email, notifications, messaging, and the protocols involved.]_

---

## 9. Quality Attributes

_[How well the system does what it does. **This is the section that decides whether your client is happy with software that meets every functional requirement**, so do not treat it as a formality.]_

_The rule for every entry: an adjective is not a requirement. "Fast", "easy", "secure", and "user-friendly" are the starting point of a conversation, not the end of one. Each entry needs a number and a way to measure it._

_Write one subsection per attribute your project actually has, and say "not applicable" with a reason for the ones it does not. An explicit "not applicable" is information; silence is not._

_Every number below came from the client or from a business rule. Thresholds the client has not given are left unspecified and tracked in [OPEN-ISSUES.md](OPEN-ISSUES.md), rather than filled with a plausible guess._

### 9.1 Usability

- `USE-not-yet-specified`: No usability or accessibility standard has been confirmed with the client. Tracked as [OI-30](OPEN-ISSUES.md#open).

### 9.2 Performance

- `PER-not-yet-specified`: The client has given no response-time target. Tracked as [OI-28](OPEN-ISSUES.md#open). The load the system must survive is specified in `SCA-qr-event-burst`.

### 9.3 Security

- `SEC-org-data-isolation`: The system shall return a Market, its results, or any data collected in it only to users whose email is assigned to the Organization that Market is assigned to. 100% of requests for another Organization's data shall be refused, and the refusal shall not reveal whether the data exists. **Source:** `BR-access-own-data`, `BR-view-org-markets`, `BR-market-organization`. **Oracle:** an integration test that signs in as a user of one Organization and requests every Market and result endpoint for another Organization's Market.
- `SEC-role-data-scope`: The system shall return to each Role only the data points that Role may see: a Vendor receives no dwell time, decision time, flip rate, or Clicks; the Admin receives no Organization's detailed data points; a Brand receives figures only for its own SKUs. 0 responses to a Vendor or Admin request shall contain a Brand-only field. **Source:** `BR-vendor-feedback-scope`, `BR-brand-feedback-scope`, `BR-admin-feedback-scope`, `BR-assign-role`. **Oracle:** a test per Role that inspects every dashboard response for forbidden fields.
- `SEC-pii-encrypted`: The system shall store personal data (email addresses and Demographic answers) encrypted at rest and transmit it only over TLS. 0 personal-data fields shall be stored or logged in plaintext. **Source:** `BR-protect-pii`, `BR-collect-email-only`. **Oracle:** inspection of the schema, the logs, and every external request.
- `SEC-dashboard-auth`: The system shall authenticate every request to a non-public endpoint through a WorkOS-issued session, and shall reject 100% of unauthenticated requests. Only Public Access Market entry and its swipes (`BR-public-market`) are public. **Source:** `BR-dashboard-access`, `BR-code-requires-sign-in`, `CO-workos-identity`. **Oracle:** an automated sweep of every route the Worker answers, without a session.

### 9.4 Safety

- `SAF-not-applicable`: Market Match records product preferences and controls no physical process, money transfer, or health decision, so no failure of the software can contribute to physical harm. Harm to people through their data is covered by the `SEC-*` attributes.

### 9.5 Availability

- `AVL-not-yet-specified`: The client has given no availability target. Tracked as [OI-29](OPEN-ISSUES.md#open).

### 9.6 Robustness

- `ROB-swipe-exactly-once`: Each swipe shall be stored exactly once, including when the Consumer's device retries a submission whose outcome was unknown: 0 duplicate swipes and 0 swipes reported to the Consumer as saved but not stored. **Source:** `UC-FDBK-rate-product` POST-2 and extension 4b; the repository gaps listed there (no retry detection, swallowed errors). **Oracle:** a test that submits the same swipe twice with one submission key and checks one stored row, and a test that forces a failed write and checks the Consumer is not advanced.

### 9.7 Scalability, interoperability, maintainability

- `SCA-qr-event-burst`: The system shall accept Market sessions and swipes from 10,000 Consumers who scan the same Public Access QR Code at one event without crashing or losing a stored swipe. **Source:** the client's growth scenario, second client meeting ("I get 10,000 people wanting to scan that QR code ... I just want to make sure that it doesn't crash"). The time window in which they arrive is not yet known; tracked as [OI-27](OPEN-ISSUES.md#open). **Oracle:** a load test replaying 10,000 Market sessions against the Preview Link.
- `MNT-client-maintainable`: Every change the team delivers shall be documented well enough for the client to maintain it by prompting Claude Code: every cross-cutting rule is written in section 8.2 of the [architectural design](../design/architectural-design.md), and every changed behavior has an automated test. **Source:** `CO-client-maintains`. **Oracle:** pull request review checks both for every merged change.
- Interoperability: `BR-connect-api` (`FEAT-api-integration`) will introduce `INT-*` attributes once the API's consumers and their needs are confirmed with the client (`AS-enterprise-requirements`).

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
