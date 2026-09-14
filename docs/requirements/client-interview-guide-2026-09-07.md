# Client Interview Guide

**Project:** Market Match
**Team:** 11
**Client:** Demetrie King
**Meeting:** 1: Client introduction

---

## Meeting record

| | |
|---|---|
| **Date** | 2026-09-07 |
| **Time and location** | 6:30 PM CDT, Remote (Zoom) |
| **Client participants** | Demetrie King (Founder & CTO) |
| **Team participants** | Everyone presented |
| **Recording** | N/A |
| **Photos of screens or forms** | N/A |

---

# Opening

## 1. Get to know your client

*Tell me about founding Market Match. What sparked the idea to turn surveys into a swipe-based experience, and how does this platform fit into your long-term vision for the company?*

**What they said:**
"I started Market Match because I was incredibly bored filling out standard university feedback forms. Nobody wants to click bubbles on a 1-to-5 scale. I realized that if we made it feel like a dating app—swipe right for yes, left for no—people would actually engage. I built the MVP incredibly fast using 'vibe coding' and rapid tools just to prove the concept. Now, it's my full-time focus. The long-term vision is that we don't just own an app, we own the infrastructure for interactive market research everywhere."

---

# The business

## 2. Context and domain

*Give us some background on the current Market Match architecture. When you say the MVP was built with "vibe coding," what does that actually mean for the state of the codebase today?*

**What they said:**
"By 'vibe coding', I mean we duct-taped it together to get it to market. We didn't worry about clean architecture, scalable databases, or strict APIs. It's very monolithic right now. We hardcoded a lot of configurations for our early tests at restaurants and food trucks. If an organization wants to use Market Match right now, they basically get our branding, or I have to manually go into the code and change hex codes to match their colors."

**Terms for the glossary, in their words:** 
*   **Vibe Coding:** Rapid, messy, proof-of-concept development prioritized for speed over scalability.
*   **Swipe-based Experience:** The core UI where end-users swipe cards left/right/up/down to register preferences instead of traditional radio buttons.
*   **White-label:** Creating the system so a client (like a university) can slap their own logo and colors on it without knowing Market Match is running the backend.
*   **Multi-tenant:** A single instance of our backend that securely serves multiple different enterprise clients without their data leaking into each other.
*   **API-first:** Building the backend routes before the frontend, so enterprise clients can hook their own custom apps directly into our database.

## 3. Business drivers and objectives

*Why make the jump to Version 3 right now? What is the core bottleneck stopping you from signing larger organizations, and what numbers are we looking at today versus where you want to be?*

**What they said:**
"Expanding to more stability codebase, more functioning, well-built with engineers' scopes and executions"

**Candidate objectives (`BO-<slug>`), with baselines where you got them:** 
*   `BO-API-INTEGRATION`: Enable external organizations to connect their systems directly to Market Match. (Baseline: 0 API partners).
*   `BO-WHITELABEL`: Support 100% customizable branding per organization instance. (Baseline: Hardcoded colors/logos requiring developer intervention).
*   `BO-ANALYTICS`: Capture micro-behaviors (swipe speed, time spent viewing) rather than just the final answer. (Baseline: Currently only capturing the final swipe direction).

---

# The process

## 4. How it works today

*Walk me through exactly what happens right now when a new client, like a restaurant chain, wants to run a Market Match campaign. Show me the steps from onboarding to them seeing their data.*

**What they said:** 
Very manual work, Demetrie has to take care most of it.

**Artifacts they showed us:** 
Demo shown

## 5. What is hard about it

*What is the most frustrating part of that process? Where does it break down if three different companies want to launch campaigns on the same day?*

**What they said:**
"The manual onboarding is a nightmare. I am the bottleneck. Because we don't have a multi-tenant architecture, I have to babysit every single campaign. The most frustrating part is when a client wants to change a question halfway through—I have to push a code update. Also, we have zero isolation. If I mess up a query, I could accidentally send Company A's data to Company B."

**Rules heard (candidate `BR-*` for week 4):** 
*   `BR-TENANT-ISOLATION`: Organization A must never be able to query, access, or view Organization B's data, users, or surveys.
*   `BR-SELF-SERVICE`: Organizations must be able to create and update their own survey items without Market Match developer intervention.

## 6. What already works

*What part of the current MVP must we absolutely keep? What do your users currently love that we shouldn't touch while rebuilding the backend?*

**What they said:**
The form functions well with customers

## 7. Volumes and scale

*How many users currently*

**What they said:**
"500 -> 1000"

## 8. Who the users are

*Who will actually be logging into the new administrative side of this platform? Do we have access to talk to some of these organization admins to see what kind of dashboard they expect?*

**What they said:**
"College students and forms' admin"

---

# The boundaries

## 9. Constraints and rules

*Are there any specific cloud providers, tech stacks, or security compliance standards (like FERPA or GDPR) we are required to use or adhere to for Version 3?*

**What they said:**
"Because we're targeting universities, FERPA compliance is a major plus, meaning we need strict data encryption at rest and in transit. No storing plaintext PII. For the stack, I want to stick to modern JavaScript/TypeScript—Node.js or similar for the backend, React for the frontend, and we need a highly scalable database like PostgreSQL or a robust NoSQL solution. We are hosted on AWS right now, so native AWS architecture is preferred."

## 10. External dependencies

*What systems will this API ultimately need to talk to? Are there specific CRMs or marketing platforms we should research for integration patterns?*

**What they said:**
"We aren't building direct integrations to specific CRMs this semester, but we are building the API *so that* they can. You should look at how Stripe or Twilio structure their APIs. We need standard REST or GraphQL endpoints, webhook support for when a user finishes a survey, and API key generation for our clients."

## 11. Lifetime and who maintains it

*Who takes over this codebase in May when we graduate? What languages or frameworks are they most comfortable maintaining?*

**What they said:**
"I will be maintaining it, and hopefully, I'll be hiring a small engineering team next summer using seed funding. That's why we must move away from the 'vibe code'. I need standard, well-documented, enterprise-grade code (TypeScript/Node) that a mid-level engineer can jump into and understand immediately."

## 12. Other stakeholders

*Besides you and the marketing admins, who else will be scrutinizing this system? Any security IT teams at the universities?*

**What they said:**
"Absolutely. University IT departments are ruthless. If we try to sell them an API integration and we don't have proper rate limiting, audit logging, and role-based access control (RBAC), they will kill the deal instantly. Security is a primary stakeholder here."

---

# The close

## 13. Anything else

*Is there anything I should have asked and did not? What have we not talked about that worries you regarding this two-semester transition?*

**What they said:**
"I'm worried about over-engineering. I want enterprise architecture, but we're still a startup. I don't want us spending six months diagramming microservices if it means we don't have a working API by the end of Semester 1. We need a balance of scalable architecture and actual deliverable code."

## 14. The read-back

*To make sure we are fully aligned: Market Match's problem is that the current monolithic, hardcoded system cannot scale to support enterprise clients who want self-service and API access. Our objective is to rebuild the backend into a multi-tenant, white-labeled, API-first platform. The hardest things right now are manual campaign creation and lack of data isolation. One thing I believe is OUT of scope for this year is building direct, native integrations to specific CRMs like Salesforce—instead, we are just building the API infrastructure so clients can do that themselves.*

**What we read back, and what they corrected:** 
"Spot on regarding the CRMs being out of scope. One correction though: don't completely ignore the frontend. While the swiping mechanic stays exactly the same, the frontend *architecture* needs to be refactored so it can dynamically fetch a client's logo, colors, and fonts via the API. So the frontend is in scope for refactoring, just not for redesigning the UI."

## 15. Before you leave the room

- [x] **Next meeting on the calendar:** Monday, September 14 at 6:00 PM.
- [x] **Cadence agreed:** Weekly on Mondays at 6:00 PM via Zoom, 45 minutes. 
- [x] **Contact channel and how fast they reply:** Imess. Usually replies within 2 hours during business hours.
- [x] **Who to contact between meetings:** Demetrie directly.
- [x] **Say what happens next:** We will review the GitHub repo and bring questions to our meeting next Monday.

---