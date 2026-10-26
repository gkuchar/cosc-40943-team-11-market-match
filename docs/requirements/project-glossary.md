# Project Glossary

**Project:** Market Match
**Team:** \_11
**Client:** Demetrie King
**Version:** 0.4

---

_**How to use this template.** Instructions appear in italic square brackets. Fill in underneath them and leave them in the file until the document is stable._

_**What this document is for.** Every project has words that mean something specific inside the client's organization and something else outside it, or nothing at all. This file fixes one word to one concept, and commits the team, the client, and the AI teammate to using it. That shared vocabulary is called a **ubiquitous language**: the same term in the client conversation, in the vision and scope, in the use cases, in the class names, and in the database columns._

_**Why the glossary is the first artifact you write and the last one you finish.** It is the cheapest document to start, because your client hands you the terms in the first meeting whether you ask or not, and it is the one that keeps paying: every later document cites it instead of redefining things._

## Why this matters when an agent writes your code

_[Read this once, then delete this section when the document goes stable.]_

_If two words in your project mean the same thing and nothing says so, your team will use both. So will your agent. You will end up with a `Team` class and a `Group` table, a `submitReport` endpoint and a `war_entry` record, and every one of those pairs is a bug waiting for the week you try to join them._

_An agent cannot resolve this on its own. Asked to add a feature, it reads what is in the repository and imitates it. If the repository is inconsistent it will faithfully reproduce the inconsistency, and it will invent a plausible synonym for anything the repository never names. A glossary in the repository is the only thing that stops it, because the repository is the whole of the agent's memory of your project._

_The other half is human. When your client says "cycle" in one sentence and "sprint" in the next, that is your signal to ask which one they mean, in the meeting, while they are in front of you. An agent reading the transcript later cannot ask._

## The entries that earn their place

_[The temptation is to define words your teammates already know. Skip those. The entries worth writing are:]_

- _**Terms two stakeholders use differently.** The highest-value entry in any glossary. In airline statistics, the International Civil Aviation Organization says **city-pair** and the International Air Transport Association says **O and D**, for the same thing; the two bodies also say **traffic by flight stage** and **segment traffic** for another. A team that misses this builds a report that silently mixes them._
- _**Terms that sound generic but are not.** "Active", "submitted", "complete", "week". Ask what makes a record active and you often find a business rule nobody had stated._
- _**The client's acronyms**, spelled out, including the ones they use so fluently they have forgotten they are acronyms._
- _**Terms you invented** that the client does not use. Record them, then consider dropping them in favor of the client's word._

_Ask the client directly: "Is there a word your team uses here that I would not guess the meaning of?"_

## Conventions

_[The **term itself is the identifier**. There is no separate numbering scheme, because a glossary entry already has a unique, meaningful name: the word. Cite a term by writing it, and keep the spelling identical everywhere it appears._

_Rules:_

- _One entry per concept. If two words mean the same thing, pick one, define it, and list the other as a synonym under it rather than giving it its own entry._
- _Alphabetical order, so a reader can find a term without searching._
- _Define the concept, not the implementation. "A weekly record of what a student did" is a definition; "a row in the `war` table" is not._
- _Use the client's word when the client has one. You are joining their world, not renaming it._
- _If a term has a meaning outside this project that differs from the one here, say so explicitly.]_

## Revision History

| Date       | Version | Description                                                                                                                                                                                                               | Author           |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| 2026-09-14 | 0.1     | Initial terms from the client brief and first client meeting                                                                                                                                                              | Matthew Stafford |
| 2026-09-21 | 0.2     | Dashboard, metric, and card terms from the brand dashboard walkthrough                                                                                                                                                    | Matthew Stafford |
| 2026-09-23 | 0.3     | Tenancy, role, market assembly, and environment terms from the second client meeting. Renamed Skew to SKU, split Code into One-Time Code and Market Code, merged Survey into Market, and corrected Brand and Demographic. | Matthew Stafford |
| 2026-10-13 | 0.4     | Data point terms from the third client meeting: Brand Market, Standard Market, Clicks, Completion Time, Engagement Funnel, Join Market, Like Rate, Swipe Behavior, Trends. Corrected Average Dwell Time (to the flip) and Average Decision Time (to the swipe), and superseded Brand Card - Market. | Matthew Stafford |
| 2026-10-25 | 0.6     | Product import terms: added API Key; Inventory now fills by import as well as one item at a time. (Version 0.5 is in the data points pull request.) | Matthew Stafford |

---

## Definitions

_[One `###` heading per term, alphabetical. Follow the heading with a definition of one to three sentences. Add **Synonyms**, **Not to be confused with**, or **Source** lines where they help. Where a term only makes sense with an example, give one._

### Admin

_The platform-wide role that can create Organizations and users, assign roles, build Categories and Inventory, create and launch Markets, approve Brand-submitted content, and delete products. The client, Demetrie King, is the only Admin, and every other user logs in as a Consumer until he changes them._

**Synonyms:** administrator, platform admin

**Not to be confused with:** an organization-level admin, which is a WorkOS capability the client has considered delegating so an Organization could invite its own users. That is not in place today.

**Source:** second client meeting with Demetrie King

### Admin Dashboard

_The Admin dashboard allows for the creation of products, market surveys, and uploading of photos/videos so Brands have their SKUs on the application. It is also where the Admin creates Organizations and users, assigns Roles, builds Categories, adds Inventory items, generates Market Codes, sets a Market to Public Access, launches Markets, and deletes products._

**Not to be confused with:** WorkOS, which is the separate third-party console where user, Organization, and Role records actually live.

### Anonymous Consumer

_A Consumer who reached a Public Access Market by QR Code or link without signing in. Market Match gives each one their own temporary identity for that Market, so each person counts once toward the Market's Consumers and their swipes can be analyzed per person. Rescanning on the same device returns to the same Anonymous Consumer. It holds no email and no Demographic answers, and it is removed after a retention period while the Market keeps its Consumer count._

**Synonyms:** temporary user, temporary survey taker, Public Access Consumer, anonymous survey taker, anonymous user

**Not to be confused with:** the single shared `anonymous-public` user the client's app uses today, under which every Public Access scan counts as one Consumer.

**Source:** fourth client meeting with Demetrie King

### API Key

_The secret a Brand generates in Market Match so that its own system, wherever it keeps its products, can send them through Market Match's API without anyone signing in. Each key belongs to one Brand and reaches only that Brand's Inventory. It is shown once, generating a new one ends the old one, and it stops working when the Brand's access is removed. Every product sent with it still waits for Approval._

**Synonyms:** API connection, product connection, integration, credential. Use API Key in code and on screen.

**Not to be confused with:** `FEAT-api-integration`, the wider API for surveys, users, and responses, which is out of the MVP.

**Source:** the client's "API connections" (fourth client meeting with Demetrie King); term chosen by the team for `BR-connect-product-system`

### Approval

_The client's review of Brand-submitted content before it goes live. Approval is required both when a Brand creates an Inventory item and when a Brand updates an existing item's images or details, so nothing reaches a Market without the Admin seeing it._

**Synonyms:** admin approval, review

**Source:** second client meeting with Demetrie King

### Approval Percentage

_On a Market the approval percentage is the number of Likes divided by the Reach._

**Not to be confused with:** the Brand Engagement Score, which measures the same idea across a whole Brand rather than for one SKU on one Market. Also not Approval, which is the Admin reviewing Brand-submitted content.

### Average Decision Time

_The average time Consumers take to swipe a Card left or right, measured from the moment the Card appears to the moment of the swipe. Reported per SKU on the Brand Dashboard._

**Not to be confused with:** Time-to-Swipe, the raw per-swipe measurement this figure averages, and Average Dwell Time, which stops at the flip rather than at the swipe.

**Source:** third client meeting with Demetrie King, which replaced the version 0.2 reading that decision time was time spent near the call to action buttons

### Average Dwell Time

_The average time Consumers take to flip a Card over, measured from the moment the Card appears to the moment of the flip. A Consumer who swipes without ever flipping the Card has a dwell time of zero. Reported per SKU on the Brand Dashboard and compared across all Consumers who saw the same Card._

_**Example.** A Card sits for 3 seconds before the Consumer flips it: dwell time is 3 seconds. A Consumer who swipes left after 1 second without flipping: dwell time 0, decision time 1 second._

**Not to be confused with:** Average Decision Time, which runs to the swipe rather than to the flip. Also not the total time spent on the Card, which is what version 0.2 of this glossary said and the client corrected.

**Source:** third client meeting with Demetrie King

### Brand

_The entity that owns the products on the Cards, such as Celsius. A Brand owns its Inventory of SKUs, its Brand Card, and the Markets its products appear in, and it reads its own product statistics on the Brand Dashboard. A Brand can have its own market surveys; today the Admin builds those Markets on the Brand's behalf, because self-serve Market creation is deferred until the client settles pricing._

**Not to be confused with:** a Vendor, which is the organization that receives a Market and its results rather than the company whose products are being rated. A Brand may also be a Vendor, but the two roles are assigned separately.

**Source:** second client meeting with Demetrie King

### Brand Card - Brand Dashboard

_The Brand's profile within Market Match: its overview, address and location, and social media handles. A Brand fills this in itself when it first logs in, and it is what a Consumer or Vendor sees when they look at the Brand rather than at one of its products._

**Not to be confused with:** Brand Card - Market, the Card type chosen at Market creation. See also Settings - Brand Dashboard, the page where this profile is edited.

**Source:** second client meeting with Demetrie King

### Brand Card - Market

_Superseded in version 0.4: see Brand Market. The "brand card or standard market card" choice the client makes at Market creation is the choice of Market type, Brand Market or Standard Market, not a type of Card._

**Source:** second client meeting with Demetrie King, reinterpreted after the third

### Brand Dashboard

_The brand dashboard shows statistics for each Brand on Market Match. This dashboard includes an overview, analytics, inventory, settings, and replay tour page._

### Brand Engagement Score

_The brand engagement score is the percentage of Consumers that swiped right, or liked a SKU._

**Synonyms:** impact score

**Not to be confused with:** Approval Percentage, which is the same ratio computed for one SKU on one Market. The engagement score is the Brand-level figure.

### Brand Market

_A Market run for a Brand, so the Brand can test its own products with an audience the client hands a Market Code to. On top of the Likes and Passes every Market produces, a Brand Market is where the client wants the Engagement Funnel and Completion Time reported. The client chooses Brand Market or Standard Market when he creates the Market._

**Synonyms:** brand market survey, brand card (the client's label for the choice at Market creation)

**Not to be confused with:** a Standard Market, which is run for a Vendor. Also not Brand Card - Brand Dashboard, which is a Brand's profile.

**Source:** second and third client meetings with Demetrie King

### Card

_A Card has a front side and back side. The front side is a photo of the product and the product name. The back of the Card includes more details in which a Brand can put a description of their product as well as a video showcasing their product. A Card carries up to three photos and one video, and the video is supplied as a YouTube link rather than an uploaded file._

**Not to be confused with:** a Text Card, which is a Card with no product photo or video.

### Category

_A named grouping of Line Items inside a Market. A Category is usually a product type such as energy drinks, sports drinks, or chips, but it can also be a question, in which case the Cards under it are Text Cards holding the answer options. The Admin creates Categories, attaches Inventory items to them, and assembles a Market by selecting which Categories it contains._

_**Example.** "What type of music do y'all want?" is a Category; each music genre under it is a Text Card._

**Not to be confused with:** a Market, which is the whole survey. A Market contains Categories; a Category contains Line Items.

**Source:** second client meeting with Demetrie King

### Clicks

_The number of times Consumers open each individual piece of media on a Card: each of its up to three photos, and its video link. A Brand reads Clicks per photo and per video so it can see which media draws attention and swap out what does not, for example by promoting the most-clicked photo to be the front photo. Clicks are the only measure taken on the video. How long a Consumer watches is left to YouTube, which the Brand can read for itself._

**Not to be confused with:** a Flip, which turns the Card over rather than opening one piece of media on it.

**Source:** third client meeting with Demetrie King

### Cloudflare

_Where Market Match is hosted. The application runs as two Cloudflare Workers, one serving Production from the main branch and one serving the Preview Link, and Cloudflare also stores the platform's image files._

**Source:** second client meeting with Demetrie King

### Completion Time

_How long a Consumer takes to go through a whole Market, start to finish, meaning every Line Item in every Category the Consumer chose to go through. The client wants the average Completion Time across all Consumers who completed a Market, on both Brand Markets and Standard Markets. "It took 100 students, on average, this amount of time to go through this survey." This is an overall figure for the Market, not a product-by-product one._

**Synonyms:** time to complete, market completion time

**Not to be confused with:** Average Decision Time and Average Dwell Time, which are per-Card. Whether a Consumer's time away from a Market they stopped and came back to counts toward Completion Time has not been decided.

**Source:** third client meeting with Demetrie King

### Consumer

_One user from a Market, this is one person from the target population that is being sampled/surveyed. Consumer is the role every user receives automatically on first login, no matter how they arrive; only the Admin can change a user to Brand or Vendor. Most Consumers today never log in at all, because the TCU and UTD Markets are run as Public Access._

**Not to be confused with:** a Vendor, which is the organization receiving the results rather than a person answering.

### CPG

_Consumer Packaged Goods: everyday branded products sold at retail, such as energy drinks, sports drinks, and chips. This is the client's primary market segment, and the fixed category structure he described applies on the CPG side; non-CPG uses, such as a job fair or a music preference survey, get Categories built to order._

**Source:** second client meeting with Demetrie King

### Demographic

_Attributes of the Markets and Consumers, describing who the Consumers are for targeted market experiments._

_**Examples.** College students at TCU; people attending football games; students in the College of Science and Engineering._

**Not to be confused with:** a Market, which is the survey itself rather than the population it is aimed at.

### Engagement Funnel

_The stages a Consumer passes through in one Market, and how many Consumers reach each stage: they enter the Market Code, view the Market, start swiping, and complete it, along with the Completion Time it took. The funnel starts when the Market Code is entered, or when a Public Access link is opened. Sign-in comes before it and is not a stage the Brand sees. The client wants it for Brand Markets first and possibly Standard Markets too._

**Not to be confused with:** the "Engagement Funnel" panel already on the Admin Dashboard, whose Login, View Market, Start Swiping, Complete 10, and Complete All figures are placeholders rather than measured values.

**Source:** third client meeting with Demetrie King

### Feedback

_Two stakeholders use this word for two different things, and both uses are live in this project._

_The client means, first, the consumer preference data a Market collects — "get some great feedback before they buy anything." He also means, second, the comments TCU students give him about the Market Match application itself, which he acts on by making small UI changes on his own side and which he has committed to routing past the team so those changes do not collide with Version 3 work. Incorporating that second kind into Version 3 is a project requirement._

**Synonyms:** user feedback and product feedback, for the second sense only

**Not to be confused with:** Likes, Passes, and Reach, which are the specific measures the first sense produces. When writing requirements, name the measure instead of saying "feedback".

### Flip

_A Card can be flipped from the front side to the back side. This is a metric tracked in which Brands will be able to see, reported on the Brand Dashboard as flip rate percentage._

### Inventory

_The collection of Line Items a Brand or the Admin has loaded into Market Match. Items are added one at a time, imported by spreadsheet, or sent from the Brand's own system through Market Match's API with an API Key; each has up to three photos and one YouTube video link or is a Text Card, waits for the Admin's Approval, and is then attached to a Category so it can appear in a Market._

**Not to be confused with:** Inventory - Brand Dashboard, which is the page that reports statistics on those items rather than the collection itself.

**Source:** second client meeting with Demetrie King

### Inventory - Brand Dashboard

_The inventory page on the brand dashboard includes all the products from Brands. Each SKU includes product name, Reach, Likes, Passes, Approval Percentage, gender, age, ethnicity, and flip rate percentage. It also includes a detailed view that includes all the prior stats plus Average Decision Time, Average Dwell Time, and top performing locations._

**Not to be confused with:** Inventory, which is the collection of Line Items itself rather than this reporting page.

### Join Market

_The section of the Consumer app where a signed-in Consumer types a Market Code to open a Market. In a Brand Market, entering the code here is the first stage of the Engagement Funnel._

**Not to be confused with:** Public Access, where a Consumer reaches a Market by QR Code or link without signing in and without passing through Join Market.

**Source:** third client meeting with Demetrie King

### Launch

_The Admin action that makes a Market live. A Market is created, assigned to an Organization, given its Categories, and those Categories applied, all before launch; launching is what makes its QR Code, link, and Market Code actually reach the survey._

**Source:** second client meeting with Demetrie King

### Like Rate

_The share of all swipes on one SKU that were right swipes, across every Market the SKU has appeared in. It is what the Brand Dashboard shows for each product; that dashboard reports overall figures, not figures per Market._

**Not to be confused with:** Approval Percentage, which is the same ratio for one SKU on one Market, and Brand Engagement Score, which covers a whole Brand.

**Source:** third client meeting with Demetrie King; the Brand Dashboard's "Like Rate" label in the client's repository

### Likes

_On a Market the likes is the number of people that liked the product, also corresponds to swiping right._

### Line Item

_A single entry inside a Category, added to Inventory one at a time. A Line Item is either a product, with up to three photos and one YouTube video link, or a Text Card. The number of Categories and Line Items in a Market is one of the three inputs to Market Pricing._

**Synonyms:** item

**Not to be confused with:** a SKU. Every SKU is a Line Item, but a Line Item can also be a Text Card with no product behind it.

**Source:** second client meeting with Demetrie King

### Market

_A named collection of Cards, grouped into Categories, that Consumers swipe through. A Market has an auto-generated Market Code, is assigned to exactly one Organization, and must be launched before anyone can reach it. This is the main interaction for the users of the product and is used by Brands and Vendors to gather information on their target audience. Some of the statistics shown are the Reach, Likes, Passes, and Approval Percentage._

**Synonyms:** survey, market survey

**Not to be confused with:** the group of people that Vendors and Brands are targeting, which is a Demographic. Also not a Category, which is a grouping of Line Items inside a Market.

### Market Code

_The unique code automatically generated when a Market is created, tied to that Market. A Consumer enters it to pull up that Market's survey. The client hands this code out when he wants a specific audience to reach a specific Market._

**Synonyms:** market ID code, unique code

**Not to be confused with:** the One-Time Code used to sign in, and the QR Code, which is the scannable form of a Public Access link rather than a typed code.

**Source:** second client meeting with Demetrie King

### Market Pricing

_What the client charges a Vendor or Brand for a Market, set case by case on three inputs: how much has to be built (how many Categories and Line Items), how long the Market stays open, and how many people it goes to. Recorded here because unsettled pricing is the client's stated reason that self-serve Market creation is out of scope for this phase._

**Source:** second client meeting with Demetrie King

### MVP

_Minimum Viable Product: the version of Market Match the client built himself and runs in Production today. It is working and taking real traffic, which sets the constraint on this project — the MVP must keep working while Version 3 is built._

**Not to be confused with:** Version 3, the platform the team is building. The team's documents also call the MVP "version 2".

**Source:** `client-meeting-1.md`, `napkin-round-0.md`, and the second client meeting

### One-Time Code

_A single-use code emailed to a user so they can sign in at login.marketmatch.app without a password. The client uses it as the standard sign-in path for Brand, Vendor, and Admin users, and cites it as the security control on the platform._

**Synonyms:** sign-in code, email code

**Not to be confused with:** the Market Code, which is entered after sign-in to open a particular Market. Sign-in answers "who are you"; a Market Code answers "which Market do you want".

**Source:** second client meeting with Demetrie King

### Organization

_The container that a set of user emails and a set of Markets are both assigned to. An Organization decides which Markets and which results a user can see: only users whose emails are attached to an Organization can see the Markets assigned to it. The client creates one Organization per department or company rather than one per institution, because a single TCU Organization would let every department see every TCU Market's results._

_**Example.** TCU is not one Organization. TCU Director of Student Activities is one, TCU food services is another, and each sees only the Markets assigned to it._

**Synonyms:** tenant (the team's word in `napkin-round-0.md` and `initial-questions.md`), org

**Not to be confused with:** Brand and Vendor, which are roles held by users inside an Organization, not containers. Getting this wrong is the multi-tenant data isolation risk named in `napkin-round-0.md`.

**Source:** second client meeting with Demetrie King

### Passes

_On a Market the passes is the number of the people that did not like the product, also corresponds to a user swiping left on a SKU._

### Preview Link

_The Cloudflare preview deployment the client tests a change on before merging to main. It is a separate URL with its own Worker and its own WorkOS side, and the client's workflow is to request a preview link, test the change there, and only then commit and push to main._

**Synonyms:** staging, staging link, preview deploy

**Not to be confused with:** Production, and the TCU Staging Branch, which is the team's own separate deployment of the same kind.

**Source:** second client meeting with Demetrie King

### Production

_The live Market Match at marketmatch.app and login.marketmatch.app, served by the main Cloudflare Worker from the main branch. This is what the client's real users are swiping on today, which is why nothing reaches it without first being tested on the Preview Link._

**Not to be confused with:** the Preview Link, which the client calls his staging.

**Source:** second client meeting with Demetrie King

### Public Access

_A Market setting that lets a Consumer reach the survey with no login, no email, and no Market Code, by scanning a QR Code or clicking a link. The Market is still assigned to an Organization, so its Vendor still sees the results. This is how TCU and UTD run today, deliberately, to get people used to the product before asking them to sign in._

**Synonyms:** public market, open market

**Not to be confused with:** One-Time Code sign-in, which is the opposite path. A Public Access Market collects no identity at all, which is why Market Match currently holds no student emails.

**Source:** second client meeting with Demetrie King

### QR Code

_The scannable code generated for a Public Access Market, and the main way Consumers reach a Market today._

**Not to be confused with:** the Market Code, which is a code a signed-in Consumer types in. A QR Code carries a link; a Market Code is entered by hand.

**Source:** second client meeting with Demetrie King

### Reach

_On a Market the reach is the number of Consumers that saw the SKU._

**Synonyms:** impressions

### Role

_What a user is allowed to do in Market Match: Consumer, Brand, Vendor, or Admin. Every user is a Consumer on first login and only the Admin can grant Brand or Vendor. A user holding more than one role can switch between them from the dashboard; a user holding only Consumer sees no dashboard switcher at all._

**Source:** second client meeting with Demetrie King

### Settings - Brand Dashboard

_The settings page on the brand dashboard allows a Brand to select their banner photo, profile photo, a brand overview, location/address, and social media handles._

**Not to be confused with:** the Brand Card - Brand Dashboard, which is the profile this page edits.

### SKU

_A single product a Brand wants feedback on, and the unit that Reach, Likes, Passes, Approval Percentage, and flip rate are all reported against._

**Synonyms:** skew (the client's spelling and how the team recorded it through version 0.2), product

**Not to be confused with:** its meaning in retail generally, where a SKU is the identifier code for a stockable item rather than the item itself. Here the word means the product. Also not a Line Item, which may be a Text Card with no product behind it.

### Standard Market

_A Market run for a Vendor, such as the TCU and UTD Markets. A Vendor sees each Line Item's Likes and Passes, ranked from most liked to least, narrowed by Category or to the top ten or top five, and the Market's average Completion Time. Unlike a Brand, it does not see per-Card measures such as dwell time or decision time._

**Synonyms:** vendor market

**Not to be confused with:** a Brand Market, which is run for a Brand.

**Source:** second and third client meetings with Demetrie King

### Swipe

_The action the user takes on a Card, which is a swipe left or right. Brands manufacture different Cards that Consumers swipe on._

### Swipe Behavior

_The client's name for everything a Consumer does on a Card besides the swipe itself: how long it takes them to flip the Card, how long it takes them to decide, and which photos and video they open. The client's patent covers using swipe behavior to forecast demand and to guide marketing materials, which is why he treats these measures as the product's core data rather than as extras._

**Not to be confused with:** a Swipe, which is only the left-or-right decision. Swipe behavior is the activity around that decision.

**Source:** third client meeting with Demetrie King

### Swipe Left / Swipe Right

_A user can swipe left on the Card, which indicates that they dislike the product. This is another metric that is tracked that Brands will be able to see for their products. A user can swipe right on the Card, which indicates that they like the product, this is another metric._

**Not to be confused with:** Likes and Passes, which are the counts these two actions accumulate on a Market.

### TCU Staging Branch

_The branch on the client's repository where Team 11's work lives, `tcu-fall-2026-stage`, with its own staging preview so the client can follow the team's changes without them reaching Production. The team works here rather than in a fork so both sides can watch each other's work and compare before anything is merged._

**Synonyms:** `tcu-fall-2026-stage`, TCU branch, TCU staging

**Not to be confused with:** the client's own Preview Link, which is where he tests his small UI changes.

**Source:** second client meeting with Demetrie King

### Text Card

_A Line Item that is text only, with no product photo and no video. Used when the Category is a question rather than a product type, so the Consumer swipes on a written option instead of an image._

**Not to be confused with:** a Card, which by default has a product photo on the front. A Text Card is the exception.

**Source:** second client meeting with Demetrie King

### Time-to-Swipe

_A metric that measures how long it takes a user to swipe left or right on a product._

**Not to be confused with:** Average Decision Time, which is this same measure averaged across Consumers and reported on the Brand Dashboard. Time-to-Swipe is the raw per-swipe measurement.

### Trends

_Patterns the Admin would see across many Markets without seeing any one Organization's specific results. The client's example: if he knows from earlier Markets what Consumers of a given age range, ethnicity, and gender liked, he can put those items into a new Market aimed at the same Demographic. Today the Admin sees swipe counts and users but not Brand or Vendor data points. Trends are deferred to a later phase and are out of scope for Version 3's first phase._

**Source:** third client meeting with Demetrie King

### Vendor

_The organization that receives a Market and its results, such as TCU Director of Student Activities or UTD. A Vendor user signs in and sees the Markets assigned to their Organization on the Vendor Dashboard. The only information Market Match holds about a Vendor user is their email address._

**Not to be confused with:** a Brand, which owns the products being rated. See Brand for the split.

**Source:** second client meeting with Demetrie King

### Vendor Dashboard

_The Vendor dashboard allows for a Vendor to see all of their market surveys they currently have, meaning the Markets assigned to their Organization and the results those Markets have collected._

### Version 3

_The enterprise-grade Market Match the team is building: multi-organization, API-first, secure, scalable, and White-Label, able to survive an event where thousands of people scan a QR Code at once._

**Not to be confused with:** the MVP, which is the live application it will eventually replace.

**Source:** `napkin-round-0.md`

### Vibe-Coded

_Built by prompting an AI coding tool rather than writing the code by hand. The client vibe-coded the current MVP, starting in Google Antigravity and moving to Claude Code. The term is recorded because it names the project's central risk: an application with no design documents, whose architecture nobody has written down._

**Source:** `client-meeting-1.md`, `napkin-round-0.md`, and the second client meeting

### White-Label

_Running Market Match for an enterprise organization under that organization's own branding, so the platform looks like theirs rather than like Market Match. Named by the client as a Version 3 goal alongside API access._

**Source:** `napkin-round-0.md` and the vision and scope

### WorkOS

_The third-party identity platform Market Match uses for users, Organizations, Roles, and sign-in. Creating a user, creating an Organization, attaching an email to it, and assigning a Role all happen in the WorkOS console rather than in Market Match itself. WorkOS has its own production and staging sides, matching Market Match's._

**Not to be confused with:** the Admin Dashboard, which is Market Match's own console for Markets, Categories, and Inventory.

**Source:** second client meeting with Demetrie King

### Wrangler

_Cloudflare's command-line tool, used to deploy Market Match's Workers._

**Source:** second client meeting with Demetrie King
