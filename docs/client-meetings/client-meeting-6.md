# Client Meeting 6 — Transcript

**Project:** Market Match
**Team:** Team 11
**Client:** Demetrie King
**Attendees (speakers in the transcript):** Demetrie King, Matt Stafford, Griffin Kuchar, Vinh Nguyen
**Date:** 2026-11-18 or 2026-11-19 _[the Zoom export is named `zoom-transcript-full-2026-11-19.txt`; confirm against the calendar]_
**Format:** Demo by Matt Stafford of the Admin generating, replacing, and revoking a Brand's API Key (`UC-BRND-generate-api-key`) against a test WorkOS setup, then questions on WorkOS, API Key expiry, pending product updates, and the order of products in a Market (about 21 minutes)

---

_**What this file is.** The unedited automatic Zoom transcript of the sixth client meeting, kept exactly as exported. The export prints most utterances twice, and its speaker labels and timestamps are shifted: a line's trailing `(mm:ss): Name` names the speaker of the **next** line. "Worko Westside" is WorkOS, "Coliseum" is a stray caption, and "written days" is fourteen days. Read it as raw source, not as notes._

_**Why it is in the repository.** It records the client's answers on how long an API Key lasts, on reminding the Admin before a key expires, on keeping provisioning with the Admin, on how a WorkOS Organization counts as a Brand, on offboarding a Brand, and on what a Consumer sees while an update to an approved product waits for Approval._

_**What it covers.** The client approved the API Key demo and kept the Admin alone giving out API Keys, with Brands requesting their own left for later; an Organization is a Brand when a member holds the Brand role with an active membership, and the same institution can also be a separate Vendor; the client offboards a Brand by revoking its WorkOS access and keeps the Organization; an API Key expires, first set at 14 days, then agreed as a duration the Admin picks when generating it (a week, 14, 30, 45, or 90 days were mentioned; the team advised against keys that never expire); the Admin wants a reminder and a days-left countdown next to the Brand, which both go away once the Brand has sent its products through the API; while an update to an approved product waits for Approval, the live product stays unchanged and updates once approved; products in a Market show in the same order every time today; and the team's next work, the product API and the Market data points._

_**Earlier meetings** are in [client-meeting-1.md](client-meeting-1.md) (curated notes), [client-meeting-2.md](client-meeting-2.md), [client-meeting-3.md](client-meeting-3.md), [client-meeting-4.md](client-meeting-4.md), and [client-meeting-5.md](client-meeting-5.md) (transcripts)._

---

## Transcript

00:06

Matt Stafford

Okay.

Can you see this? (00:09): Demetrie King

Yeah, you're good. (00:11): Matt Stafford

Okay, so, since we didn't have access to your, WorkOS, basically what I did is that I kind of tried to mirror your setup as best as possible. (00:20): Demetrie King

So… (00:20): Matt Stafford I just made, like, a WorkOS account. In this, I just made, like, a Market Match Admin, per se, like, that would be your account. And then this would just be a brand organization, that kind of you've made. And kind of how we're… deciding on whether or not, like, a person or a brand, is a brand in WorkOS, is that you have, like, these brand roles here. So, like, a person has to have the brand role, they have to be active. Coliseum… I guess you can't change it there. But yeah, they basically have to be active and a brand user. Basically, what happens… Hey, there's a lot of… stuff on here. Okay. So, kind of on the admin side of it now, what we've basically created is, if you go to your brands here, you can see we have this brand, Tesco.

And then within here, I was testing it earlier, but you can generate them their API key here. (01:23): Demetrie King

Okay. (01:25): Matt Stafford And then, basically, this is a one-time shown, just for security reasons. So, like, how we're kind of storing this in the database, and what industry standard kind of is, is that you can really only get your API key, like, once, just because if it's shared anywhere, then other people will have access to it. So, you'd basically copy this down. This would be what you would send to, the different brands? So then you can copy it, it goes to your clipboard. And then basically, once you say, I've saved the key.

Basically just shows you here that, like, it's active. There's two actions, you can either replace it, let's say they lost what it was, they don't remember it for whatever reason, you can hit… it gives you a little prompt saying they have to switch to the new key. (02:12): Demetrie King

Okay. (02:12): Matt Stafford But then you can replace it again, and then you would copy it, send it over.

And then if you also stop working with the brand, or for whatever reason, you don't really want them to be putting any more products onto the site, you can also revoke their API key, which basically just means on our side, we're no longer gonna accept it, when the API key is routed with their API request. (02:36): Demetrie King

Oh, nice. (02:38): Matt Stafford Basically, like, what this has done is, like, laid the groundwork, for us to actually start building out that whole API, because this is all the authorization, authentication.

To make sure that a brand is really a brand, and it's kind of your security net to make sure that, with other brands you're working with, like, you have full access on who's allowed to use this API and who's not. (03:00): Demetrie King Okay.

I don't do this once, right? (03:05): Matt Stafford

Sorry? (03:06): Demetrie King

I only have to send the API key once, like, unless, like, they lose it, like you said. (03:12): Matt Stafford

Yeah, so this would mostly just be, like, a one-time thing for, like, if you're talking with a new client that you're just onboarding, you just have to generate for them once, unless they lost it. (03:23): Demetrie King

Awesome. (03:25): Matt Stafford So, a question I did kind of have on that… WorkOS. I just wanted to make sure I kind of got your WorkOS, flow kind of right, and, like, this is kind of what you'd be doing, to where, like, you'd have your organizations, like, you could create one.

Kind of this whole thing, like, does that match your current workflow? (03:48):

Demetrie King (03:48): Demetrie King Yeah, it's kind of set up that way. You would do, like, create organization, all you really put is the name, and then after you put in the name, you go add the users. I either manually add the users, or if they've, like, already logged in one time, I'm able to just kind of search it up. Yeah, it's kind of set up that way. You would do, like, create organization, all you really put is the name, and then after you put in the name, you go add the users. I either manually add the users, or if they've, like, already logged in one time, I'm able to just kind of search it up. Down the road, you know, this is something y'all don't really have to worry about, but just to give you a heads up, Down the road, you know, this is something y'all don't really have to worry about, but just to give you a heads up, WorkOS, like, I will have, like, the ability to kind of put, like, an admin over an organization, and then give them the ability to go in and add people if they want to, to their orgs and stuff like that. I will be… that will be something I'll be doing on my end as well, but just to give you a heads up of what I'll be doing as well.

WorkOS, like, I will have, like, the ability to kind of put, like, an admin over an organization, and then give them the ability to go in and add people if they want to, to their orgs and stuff like that. I will be… that will be something I'll be doing on my end as well, but just to give you a heads up of what I'll be doing as well. (04:28):

Matt Stafford (04:28): Matt Stafford Okay, I think that kind of goes… matches our workflow. Okay, I think that kind of goes… matches our workflow. A little bit as well, because if you do have an admin, then the admin for this brand could generate their API key as well. A little bit as well, because if you do have an admin, then the admin for this brand could generate their API key as well. Because I guess that's how you would have it set up, right? Is where, if you're an admin of a brand, you would have this admin OS, or is this only you?

Because I guess that's how you would have it set up, right? Is where, if you're an admin of a brand, you would have this admin OS, or is this only you? (04:48):

Demetrie King (04:48): Demetrie King Yeah, that's only me. The brands have their brand stuff, but they would be able to give, you know, access to people to see multiple, you know, as a vendor, I would say.

Yeah, that's only me. The brands have their brand stuff, but they would be able to give, you know, access to people to see multiple, you know, as a vendor, I would say. (05:00):

Matt Stafford (05:00): Matt Stafford Okay, okay, that makes sense. Okay, okay, that makes sense. I mean, yeah, I mean, yeah, I think for now, like, if this matched, like, kind of what your expectation was, if… I think for now, like, if this matched, like, kind of what your expectation was, if… Because there's kind of two ways you can, like, provision API keys. Usually what happens is that… Because there's kind of two ways you can, like, provision API keys. Usually what happens is that… like, a brand, if they were on here, then they could request their own API key, instead of you giving it out, but kind of how you talked about your flow and how you wanted to run it, I thought this was a better, kind of strategy, like having you create the API key, and then you can give it out to them.

like, a brand, if they were on here, then they could request their own API key, instead of you giving it out, but kind of how you talked about your flow and how you wanted to run it, I thought this was a better, kind of strategy, like having you create the API key, and then you can give it out to them. (05:32):

Demetrie King (05:32): Demetrie King No.

No. (05:33):

Matt Stafford (05:33): Matt Stafford Is there any opinion on your side if you would want, in the future, for a certain brand from their, brand dashboard to be able to, like, request an API key without you, or…

Is there any opinion on your side if you would want, in the future, for a certain brand from their, brand dashboard to be able to, like, request an API key without you, or… (05:46):

Demetrie King (05:46): Demetrie King I would say kind of leave it where it is right now. I think that works best, because I'm trying to… I would say kind of leave it where it is right now. I think that works best, because I'm trying to… keep everything contained, because that is the main goal. You know, I've heard this from other VCs and stuff as well, too, is that's the route they want me to go. But to make sure that I have great quality control and wouldn't put them out there right now, I want to kind of keep it what we have right now.

keep everything contained, because that is the main goal. You know, I've heard this from other VCs and stuff as well, too, is that's the route they want me to go. But to make sure that I have great quality control and wouldn't put them out there right now, I want to kind of keep it what we have right now. (06:08):

Matt Stafford (06:08): Matt Stafford Okay.

Okay. (06:11):

Demetrie King (06:11): Demetrie King But yeah, that works perfect for me, because then I'm, you know, as soon as I have people come in, I have them, you know, I send the API key over to them, they push their stuff over to me when needed, and then I load it in, and I'm able to create the markets as needed.

But yeah, that works perfect for me, because then I'm, you know, as soon as I have people come in, I have them, you know, I send the API key over to them, they push their stuff over to me when needed, and then I load it in, and I'm able to create the markets as needed. (06:33):

Matt Stafford (06:33): Matt Stafford Okay, and then I just wanted to make sure for, the Worko Westside, again, basically. Okay, and then I just wanted to make sure for, the Worko Westside, again, basically. when you're creating a brand, like, they always have that brand role, or at least, like, one person in that does, because that's kind of the way that I'm… when you're creating a brand, like, they always have that brand role, or at least, like, one person in that does, because that's kind of the way that I'm… right now, defining, like, what a brand is from WorkOS. right now, defining, like, what a brand is from WorkOS. Would that make sense?

Would that make sense? (06:56):

Demetrie King (06:56): Demetrie King Yeah, say that one more time.

Yeah, say that one more time. (06:58):

Matt Stafford (06:58): Matt Stafford So, like, on WorkOS, like, with the brand test that I had, basically right now we're deciding if, like, an organization is a brand or not, based off if there's a person within that organization that holds the brand role and has an active membership in it.

So, like, on WorkOS, like, with the brand test that I had, basically right now we're deciding if, like, an organization is a brand or not, based off if there's a person within that organization that holds the brand role and has an active membership in it. (07:17):

Demetrie King (07:17): Demetrie King So… what's crazy about it is, like, I can have… So… what's crazy about it is, like, I can have… I can create a… a brand that would technically be, like, marketing for TCU, right? And they're giving me all their stuff in regards to marketing purposes, but I could also have… I can create a… a brand that would technically be, like, marketing for TCU, right? And they're giving me all their stuff in regards to marketing purposes, but I could also have… a vendor that's just an organization inside TCU, that are two separate roles, but I'm still… like, one… one really cares about marketing, the other one cares about just surveys in general. a vendor that's just an organization inside TCU, that are two separate roles, but I'm still… like, one… one really cares about marketing, the other one cares about just surveys in general. and right now, I guess the brand role would just kind of be that. It would be like a marketing person that I'd be working with, that handles all their type of and right now, I guess the brand role would just kind of be that. It would be like a marketing person that I'd be working with, that handles all their type of Content, or apparel, whatever it is.

Content, or apparel, whatever it is. (08:00):

Matt Stafford (08:00): Matt Stafford Okay. Okay. Okay, so I think that kind of matches, how I was understanding that.

Okay, so I think that kind of matches, how I was understanding that. (08:09):

Demetrie King (08:09): Demetrie King just to give you, like, another example, so I'm working with the Christian Academic Society with TCU, and they're… they're just, like, a vendor, so I'm using a… I created a survey for them, and right now, I just have, like, one person underneath that org, and that's what I'm kind of really doing, because I have different just to give you, like, another example, so I'm working with the Christian Academic Society with TCU, and they're… they're just, like, a vendor, so I'm using a… I created a survey for them, and right now, I just have, like, one person underneath that org, and that's what I'm kind of really doing, because I have different you know, departments within the university, and each one is just, right now, just a vendor, until, like, I get to their marketing person, who's probably gonna be, like, the brand side of it.

you know, departments within the university, and each one is just, right now, just a vendor, until, like, I get to their marketing person, who's probably gonna be, like, the brand side of it. (08:38):

Matt Stafford (08:38): Matt Stafford Okay, okay. Okay, okay. And then kind of similar on the WorkOS flow, like, when you stop working with a brand, like, do you just delete their entire organization in WorkOS? Or, like, what does that process look like?

And then kind of similar on the WorkOS flow, like, when you stop working with a brand, like, do you just delete their entire organization in WorkOS? Or, like, what does that process look like? (08:52):

Demetrie King (08:52):

Demetrie King (08:52): Demetrie King As of right now, I just kinda, I would say, revoke access to it. That's really it, depending on the time.

As of right now, I just kinda, I would say, revoke access to it. That's really it, depending on the time. (08:58):

Matt Stafford (08:58):

Matt Stafford (08:58): Matt Stafford Go ahead.

Go ahead. (08:58):

Demetrie King (08:58):

Demetrie King (08:58): Demetrie King with. with. Like, I could… like, I've deleted some, but it was when I was first testing it out and trying to do that, but really, I'm gonna kind of hold on to everything. Like, I could… like, I've deleted some, but it was when I was first testing it out and trying to do that, but really, I'm gonna kind of hold on to everything.

Like, I could… like, I've deleted some, but it was when I was first testing it out and trying to do that, but really, I'm gonna kind of hold on to everything. (09:08):

Matt Stafford (09:08): Matt Stafford Okay So, like, you would keep them all in WorkOS, Okay So, like, you would keep them all in WorkOS, Okay So, like, you would keep them all in WorkOS, I guess, like, right now, are you just, like, removing their logins, or… I guess, like, right now, are you just, like, removing their logins, or… Okay, so they wouldn't even have access to log into Market Match at all? Okay, so they wouldn't even have access to log into Market Match at all?

Okay, so they wouldn't even have access to log into Market Match at all? (09:22):

Demetrie King (09:22): Demetrie King Right. Right.

Right. (09:23):

Matt Stafford (09:23): Matt Stafford Okay. Okay. Okay. And then kind of on the API keys as well, is there, like, a set time limit that you would want these API keys to last for? And then kind of on the API keys as well, is there, like, a set time limit that you would want these API keys to last for? Since usually, like, in industry, there's… Since usually, like, in industry, there's…

Since usually, like, in industry, there's… (09:37):

Demetrie King (09:37): Demetrie King You're gonna… You're gonna…

You're gonna… (09:38):

Matt Stafford (09:38): Matt Stafford keys that expire after a certain amount of time, so you can kind of set it if you wanted to be, like, a 30-day key, 60-day, or you could have a key that never expires. Is there a certain time frame that you would want to allow, or, like, keep it indefinite? keys that expire after a certain amount of time, so you can kind of set it if you wanted to be, like, a 30-day key, 60-day, or you could have a key that never expires. Is there a certain time frame that you would want to allow, or, like, keep it indefinite?

keys that expire after a certain amount of time, so you can kind of set it if you wanted to be, like, a 30-day key, 60-day, or you could have a key that never expires. Is there a certain time frame that you would want to allow, or, like, keep it indefinite? (09:54):

Demetrie King (09:54): Demetrie King Let's do 2 weeks for now. Okay. That way, it'll kind of give them… because I know it can move slow on some things, and I just want to make sure they have, like, a sense of urgency of, you know, getting their stuff to me as soon as possible. Let's do 2 weeks for now. Okay. That way, it'll kind of give them… because I know it can move slow on some things, and I just want to make sure they have, like, a sense of urgency of, you know, getting their stuff to me as soon as possible.

Let's do 2 weeks for now. Okay. That way, it'll kind of give them… because I know it can move slow on some things, and I just want to make sure they have, like, a sense of urgency of, you know, getting their stuff to me as soon as possible. (10:07):

Matt Stafford (10:07): Matt Stafford Okay. Okay. Okay. And then… so this kind of goes into, like, the approval process. I think we kind of touched on it a little bit. And then… so this kind of goes into, like, the approval process. I think we kind of touched on it a little bit. But, so let's say a brand already has a product that's already in Market Match, but then they wanted to make an update to it. But, so let's say a brand already has a product that's already in Market Match, but then they wanted to make an update to it. But, so let's say a brand already has a product that's already in Market Match, but then they wanted to make an update to it. That update is gonna go through the flow of, like, you have to approve it before it's actually applied. That update is gonna go through the flow of, like, you have to approve it before it's actually applied. Basically during that time, would you like the product that's, like, already on Market Match to stay unchanged? Basically during that time, would you like the product that's, like, already on Market Match to stay unchanged? Basically during that time, would you like the product that's, like, already on Market Match to stay unchanged? Or does that product just kind of, I guess, not go away, but like… Or does that product just kind of, I guess, not go away, but like… Doesn't get shown until you approve changes? Or, like, what's your kind of expected, Route for that. Doesn't get shown until you approve changes? Or, like, what's your kind of expected, Route for that.

Doesn't get shown until you approve changes? Or, like, what's your kind of expected, Route for that. (10:58):

Demetrie King (10:58): Demetrie King Yeah, that's a good question. Yeah, that's a good question. Yeah, that's a good question. I would say let's… let's stay.

I would say let's… let's stay. (11:04):

Matt Stafford (11:04):

Matt Stafford (11:04): Matt Stafford Brilliant.

Brilliant. (11:05):

Demetrie King (11:05):

Demetrie King (11:05): Demetrie King Because what I'll end up doing is just making that… well, I wouldn't make it inactive, because it'd be the same thing. Because what I'll end up doing is just making that… well, I wouldn't make it inactive, because it'd be the same thing. Yeah, let's… let's let it stay until I get approved, like, I approve it, and then once it's approved, just let it update. Yeah, let's… let's let it stay until I get approved, like, I approve it, and then once it's approved, just let it update.

Yeah, let's… let's let it stay until I get approved, like, I approve it, and then once it's approved, just let it update. (11:21):

Matt Stafford (11:21):

Matt Stafford (11:21): Matt Stafford Okay. Okay. Okay. I mean, besides that, I don't have really any other questions for you. I mean, besides that, I don't have really any other questions for you. I mean, besides that, I don't have really any other questions for you. I mean, I guess where we've been moving now is that now that we have, like, the API creation is made, and it seems like you kind of like where it's going. I mean, I guess where we've been moving now is that now that we have, like, the API creation is made, and it seems like you kind of like where it's going. I mean, I guess where we've been moving now is that now that we have, like, the API creation is made, and it seems like you kind of like where it's going. Kind of going out and building that full API out. Kind of going out and building that full API out. Kind of going out and building that full API out. Which is probably gonna take testing some time to do, but I've already started, like, kind of designing it out. Which is probably gonna take testing some time to do, but I've already started, like, kind of designing it out. Which is probably gonna take testing some time to do, but I've already started, like, kind of designing it out. So, kind of going along with that, making the API for it, and then also getting started on some of the work with the data points. So, actually, when you go into a market, just… I think an initial good baseline would just be able to So, kind of going along with that, making the API for it, and then also getting started on some of the work with the data points. So, actually, when you go into a market, just… I think an initial good baseline would just be able to I guess be able to just mark down all the numbers, all the data points that you wanted.

I guess be able to just mark down all the numbers, all the data points that you wanted. (12:25):

Demetrie King (12:25): Demetrie King And then…

And then… (12:26):

Matt Stafford (12:26): Matt Stafford And just making sure that you can kind of see that for one market, and then kind of expanding that out to make sure, for, like, averages over many markets, that that works as well.

And just making sure that you can kind of see that for one market, and then kind of expanding that out to make sure, for, like, averages over many markets, that that works as well. (12:35):

Demetrie King (12:35): Demetrie King Okay.

Okay. (12:37):

Matt Stafford (12:37): Matt Stafford So, I think that's kind of the direction we're going. So, I think that's kind of the direction we're going. Kind of it for me, if anyone else has anything.

Kind of it for me, if anyone else has anything. (12:45):

Vinh Nguyen (12:45): Vinh Nguyen I have a little bit… I have, like, a question about… can you… can you guys repeat about the time limit for API? I kinda didn't hear that well, so…

I have a little bit… I have, like, a question about… can you… can you guys repeat about the time limit for API? I kinda didn't hear that well, so… (12:55):

Demetrie King (12:55): Demetrie King 14 days.

14 days. (12:57):

Vinh Nguyen (12:57): Vinh Nguyen written days, so it's a time limit for the API, right?

written days, so it's a time limit for the API, right? (13:01):

Demetrie King (13:01): Demetrie King Correct. Correct. And if you could, just, And if you could, just, have, like, a reminder set up for me. I get the 14-day pass to come to me, so that way I can, you know, reach out if I need to if they haven't got it to me in enough time.

have, like, a reminder set up for me. I get the 14-day pass to come to me, so that way I can, you know, reach out if I need to if they haven't got it to me in enough time. (13:24):

Matt Stafford (13:24): Matt Stafford Okay, and then kind of… Okay, and then kind of… I guess for that, would you just want something next to, like, the organization which says, like. I guess for that, would you just want something next to, like, the organization which says, like. how many days are left until their key expires? Is that something good?

how many days are left until their key expires? Is that something good? (13:34):

Demetrie King (13:34): Demetrie King Yeah.

Yeah. (13:35):

Matt Stafford (13:35): Matt Stafford D. Okay.

D. Okay. (13:36):

Griffin Kuchar (13:36): Griffin Kuchar Do you want that warning even if they've already submitted their products through the API? Do you want that warning even if they've already submitted their products through the API? Or do you want it all the time?

Or do you want it all the time? (13:46):

Demetrie King (13:46): Demetrie King If they've already, like, submitted, like, you're talking about all of them, or what?

If they've already, like, submitted, like, you're talking about all of them, or what? (13:49):

Griffin Kuchar (13:49): Griffin Kuchar Right, like, so if the API's for them to submit their products, and it's gonna expire before they had submitted their products, then obviously we want to remind them. But if they've already submitted it, should we still send them the reminder, or just, you know, all is good?

Right, like, so if the API's for them to submit their products, and it's gonna expire before they had submitted their products, then obviously we want to remind them. But if they've already submitted it, should we still send them the reminder, or just, you know, all is good? (14:04):

Demetrie King (14:04): Demetrie King Yeah, all's good, you can make it go away, and I guess the, what Matt's talking about, the… Yeah, all's good, you can make it go away, and I guess the, what Matt's talking about, the… The little icon or whatever that's the countdown, that can go away as well, too.

The little icon or whatever that's the countdown, that can go away as well, too. (14:13):

Griffin Kuchar (14:13): Griffin Kuchar Okay, cool.

Okay, cool. (14:16):

Matt Stafford (14:16): Matt Stafford Okay, so, like, if they did… if they've already, like, used the API, then that reminder can go away? Okay, so, like, if they did… if they've already, like, used the API, then that reminder can go away? Okay, that sounds good. Okay, that sounds good. Oh, well… I guess if…

Oh, well… I guess if… (14:32):

Vinh Nguyen (14:32): Vinh Nguyen Yeah, I… so, I'm kind of curious, because, like, cool. Yeah, I… so, I'm kind of curious, because, like, cool. So for the time limit for the API, what do the clients gonna do, like, if they have, like, two-week limit? Because I feel like you guys can correct me if I'm wrong, but I feel like 2 weeks is kinda a little bit… a little bit too long for… So for the time limit for the API, what do the clients gonna do, like, if they have, like, two-week limit? Because I feel like you guys can correct me if I'm wrong, but I feel like 2 weeks is kinda a little bit… a little bit too long for… an API time limit?

an API time limit? (14:56):

Demetrie King (14:56): Demetrie King If that's… is that usually… like, what's the standard, do you know? Is, like, a week, or a couple days, or…

If that's… is that usually… like, what's the standard, do you know? Is, like, a week, or a couple days, or… (15:02):

Vinh Nguyen (15:02): Vinh Nguyen It should be, like, an… an hour, I guess?

It should be, like, an… an hour, I guess? (15:05):

Demetrie King (15:05): Demetrie King Oh, really?

Oh, really? (15:06): Vinh Nguyen Yeah.

Yeah. (15:08): Matt Stafford My only thing of… My only thing of…

for, like, how long the key should be allowed to work for, is that, like, let's say a brand, like, imports all their products, and then let's say a day or two later, they're like, oh, we messed up on one of these, you'd still be using the API key, I guess, to update the products as well. (15:27):

Vinh Nguyen (15:27): Vinh Nguyen Oh, okay. That makes sense.

That makes sense. (15:30): Matt Stafford So I guess… So I guess… I don't know, Demetrie, it's kind of up to you for, like, how long you'd want it. I mean, like, personally, I've seen, like. It go from, like, a week, 2 weeks, to 30 days, 60 days, 90 days. It go from, like, a week, 2 weeks, to 30 days, 60 days, 90 days. Anything over 90 usually just gets turned into a key that never expires, but… I wouldn't… I personally wouldn't recommend a key that never expires, just because it is kind of a security hazard. If that key ever gets out, no matter how long it's been, it's probably gonna work still, so…

I wouldn't… I personally wouldn't recommend a key that never expires, just because it is kind of a security hazard. If that key ever gets out, no matter how long it's been, it's probably gonna work still, so… (15:59): Demetrie King Yeah. Yeah. I want to make sure, that it's utilized, but also I don't want a chance for security, you know, because that could be a big thing. Once I start really kind of moving and getting people on here, I know that's one of the major things that they're going to be asking about is security. A great example is, so I went and pitched at, DFW Airport Two weeks ago, and it went very well. And I think… Two weeks ago, and it went very well. And I think… that'd be a great way to kind of showcase how this could really be in play, is them putting different, you know, brands, different restaurants, all this other stuff on here. But I… I also, from what I've noticed. you know, it could take some time. So I'm trying to walk that, like, I'm trying to walk the line of, like, I don't want it to be out there for a long time, but I also want to give them enough time to actually, you know. you know, it could take some time. So I'm trying to walk that, like, I'm trying to walk the line of, like, I don't want it to be out there for a long time, but I also want to give them enough time to actually, you know.

Do what they want… do what they need to do. (16:53):

Matt Stafford (16:53): Matt Stafford Yeah, no, that totally makes sense. And I think, like, as time goes on further, And I think, like, as time goes on further, I think kind of the need, or I guess, switching over to, like, where a brand can request an API key is probably useful if… They're gonna be updating their products at a certain time. They're gonna be updating their products at a certain time. Because it seems like right now, like, most of the time, the biggest… issue or hump to get over is just importing all the products. And then if we find that's an issue where, like, a lot of brands, like, really want to be updating their products two weeks after, that that can definitely be, like, another thing to revisit and re-look at if that's a need for the product or not.

issue or hump to get over is just importing all the products. And then if we find that's an issue where, like, a lot of brands, like, really want to be updating their products two weeks after, that that can definitely be, like, another thing to revisit and re-look at if that's a need for the product or not. (17:29): Demetrie King Okay. Yeah, it's… I'm sure I'll run across different variations of, like, businesses. Like, I have one that's a clothing company that they do two runs every single year, but it's, like. Okay. Yeah, it's… I'm sure I'll run across different variations of, like, businesses. Like, I have one that's a clothing company that they do two runs every single year, but it's, like. 500 and 600 SKUs. So it's like a springtime, and they do their… they do their springtime run of stuff in the summer, and then… or, yeah, springtime in the, sorry, winter, and then the… summer and the springtime, something like that. But it'll be… summer and the springtime, something like that. But it'll be… I'll have different options as well from different businesses, so it depends. Right now, I guess let's leave it from there, and then I will probably have to go to the… where they request, the API. But let's leave, I mean, is 30 days still long, or is 14 days solid, or… I really want to kind of get what y'all would think, you know, would be the best option in regards to that.

But let's leave, I mean, is 30 days still long, or is 14 days solid, or… I really want to kind of get what y'all would think, you know, would be the best option in regards to that. (18:22): Griffin Kuchar Yeah, I need…

Yeah, I need… (18:23): Matt Stafford I can look.

I can look. (18:23): Griffin Kuchar into it a little bit, but I think either 14 or 30 sounds about right for what you want to do with it.

into it a little bit, but I think either 14 or 30 sounds about right for what you want to do with it. (18:29): Demetrie King Okay.

Okay. (18:29): Griffin Kuchar From what I've, gathered. From what I've, gathered.

So I, I would… I would aim her in that ballpark. (18:35):

Demetrie King (18:35): Demetrie King

Okay. (18:37): Matt Stafford Yeah, and I mean, it could be a thing where… I guess if you wanted, it wouldn't… I don't think it'd be too much of a lift, but you could have a drop-down menu that basically allows you to choose how long you could Set the key to expire. So, like, if you wanted to have it where you could have a 2-week, 30-day, 90 infinite time.

key, I don't personally think that'd be super hard to implement. (19:02): Demetrie King

That might be a great route to do, because while I'm deciphering and going through these different companies, if they tell me, like, they're… like, it's gonna take us, like, 45 days, and that's perfect, okay, let me set it out for 45 days, or this person's like, give us, like, a week. That'd probably be, like, the best fit for that, so that way I can kind of go along with what's coming in to me. (19:22): Matt Stafford Yeah.

I think that would be best as well. It makes you flexible to different types of… and sizes of companies. (19:31): Demetrie King

So yeah, that works for me. (19:34): Matt Stafford Okay, sorry, I did actually have a question, that popped into my mind. So when you're in a market as a consumer, is there any order

That kind of dictates, like, what products are shown to the user, or, like, an order of the SKUs, or is it, like, the same every time, like, randomized? (19:53): Demetrie King It kind of shows up.

Honestly, I don't know specifically how it shows up. It shows up the same every single time. Like, if I have two different markets and the same things are in each market, they're all… they're all starting with whatever and then going down the line. Nothing… nothing randomized or nothing specific as of right now. (20:14): Matt Stafford I'll go. Yeah, I mean, I think that's kind of all I have for today.

Thank you for joining with us, Demetrie, watching my little demo. (20:36): Demetrie King Yeah, appreciate it. Alright. Anybody else got any questions at all?

All good? (20:47): Griffin Kuchar

I'm all, I'm all good. (20:49): Demetrie King

Alright, well, appreciate y'all, and as usual, give me a shout if you need me. If you have any other questions, just let me know. (20:54): Matt Stafford

Alright, sounds awesome. (20:56): Griffin Kuchar

Sorry, thank you, Demetrie. (20:58): Demetrie King

Of course. (20:58): Matt Stafford Right, see ya.
