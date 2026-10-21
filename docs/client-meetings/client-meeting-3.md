# Client Meeting 3 — Transcript

**Project:** Market Match
**Team:** Team 11
**Client:** Demetrie King
**Attendees:** Demetrie King, Matt Stafford, Vinh Nguyen, Kevin Doan, Griffin Kuchar
**Date:** _[unconfirmed — the glossary and use cases were updated from it on 2026-10-13]_
**Format:** Screen-share walkthrough of the Brand, Vendor, and Admin dashboards, followed by Q&A (about 37 minutes)

---

_**What this file is.** The unedited automatic transcript of the third client meeting. Unlike the second meeting's transcript, each turn carries a speaker label (the name appears twice) and a minutes:seconds timestamp. The transcription mangles some words — "IFAS" is I-Fest, and the closing "Get imagery." is a stray caption. Read it as raw source, not as notes._

_**Why it is in the repository.** Every term added to [project-glossary.md](../requirements/project-glossary.md) in version 0.4, the `UC-FDBK-*` use cases in [use-cases.md](../requirements/use-cases.md) version 0.2, and the open issues resolved in [OPEN-ISSUES.md](../requirements/OPEN-ISSUES.md#resolved) cite this meeting. Without the transcript in the repo those citations do not resolve._

_**What it covers.** The data points the client wants on each card (Clicks on images, watch duration on videos, dwell time to the flip, decision time to the swipe); the Engagement Funnel from entering a Market Code through completion; Brand Markets versus Standard Markets; what a Brand, a Vendor, and an Admin each see on their dashboards; and the cross-market Trends the client wants as Admin._

_**Earlier meetings** are in [client-meeting-1.md](client-meeting-1.md) (curated notes) and [client-meeting-2.md](client-meeting-2.md) (transcript)._

---

## Transcript

Demetrie King
Wait on that, right?
So, just want to see… so, on these meetings, I guess we'll just… what are we going to be doing? We'll be doing kind of walkthroughs of what…
Because I know we kind of gave a…
overview of what I want to do, and then, you know, Vin asked, you know, what the product at the end… the end product I want to be, but these meetings are going to be kind of a walkthrough of what y'all are working on right now, and then possible, you know, additions, or…
insights that you might have, because also one thing I'm really leaning on you guys, you know, is you could help me, clean up a few things that I have on here, in regards to something that you might see, like, hey, Demetri missed something right here, this doesn't look safe, he should do this. That's another thing I want you guys to really
You know, help me out with, because, you know, I don't have the technical background. I'm more than happy to listen to what you guys are bringing to the table.
And gals, sorry.
What's up, Matt?
Matt Stafford
Matt Stafford
01:42
Going on Demetri, how are you?
Demetrie King
Demetrie King
01:43
Doing alright. How's your week been?
Matt Stafford
Matt Stafford
01:45
you Oh, it's been pretty good so far. No complaints or anything. How about you?
Demetrie King
Demetrie King
01:51
Been pretty chill. I was telling them we've been rolling out this,
a few surveys, one with a concert venue in Austin, and then at UTD, it's been going pretty well, so…
We'll be on campus at TCU here shortly, too. We're gonna be doing a couple different surveys, one of them for, like, events and stuff, and then also, we're gonna be surveying the students that like Celsius on what flavors they'd love for us to bring on campus, so I'm excited.
Matt Stafford
Matt Stafford
02:19
It's awesome.
Yeah, and I guess I don't know what I missed, but
At least on you. Oh, okay. On your repo now, I know we've got set up, like, we have our own branch and everything.
I don't know if you're looking currently at the repo. Let me pull it up.
Where is my…
Feel like I can just share this right now.
TCU Fall… Yeah, so this is kind of, like, our branch that, we kind of all set up together.
All we have in it right now is just some documentation stuff, so in here, we have, like, requirements, and…
We're gonna have, like, open issues, so this is all stuff, like, when we're working together on the project, like, things that we might have questions about, or just things that need to get done, in order to, like, meet your expectations.
Demetrie King
Demetrie King
03:34
Okay.
Matt Stafford
Matt Stafford
03:35
And then we have, like, our business rules here, which is, like, basically come from you of, like.
Any external rules that, like, we kind of have to follow?
And there's, like, interview guides. Then we have, like, a project glossary, which kind of goes over, like.
Everything that you've told us, like, in your own terms, like, what you define as, like, a market, a vendor.
A brand, those types of things.
Demetrie King
Demetrie King
03:59
Mmm.
Matt Stafford
Matt Stafford
04:00
We have our team contract, and then we have traceability use cases, visions, and scope. Basically, those three documents, traceability is just being able to trace, like, how we are doing everything. So, like, someone else can look back on it, see the history, and be like, okay. This is how they got to this conclusion.
Our use cases is basically breaking down, like, each feature that you kinda want. So, like, I think in our case.
Like, a client being able to onboard their full inventory into the application?
That might be a couple different use cases, but it's basically what that is. And then vision and scope is kind of just like.
overall, like, what the scope of the project is, so, like, kind of how you were saying last week, how there's kind of, like, two phases to this. Like, the first phase is just being able to have, like, a…
vendor or brand be able to import all their products, and then kind of the next phase after that would be going truly white label. So that's kind of what our vision and scope kind of nails down of, like, right now, we're just focusing on that first part, and then the next phase.
Over.
Demetrie King
Demetrie King
05:03
Perfect.
Matt Stafford
Matt Stafford
05:05
Yeah.
Okay.
Yeah, no, another thing that, at least I was up to, I was looking… so I was able to look at the database for the app.
It's pretty complex, but… Trying to get this full diagram in view.
My only question that I kind of had with that is…
When you're doing, like, these, like, in the codebase, there's, like, these different migrations that are trapped.
And I'm assuming that's you, like, making updates to the database? Like, adding new columns, adding a new table, things like that. I kind of just wanted to know your flow with, let's say, like, you have this migration that you want to do, you want to add a new column.
Let's say we wanted to add a migration. For us locally, that's pretty easily to do, but…
I guess, how do you want that flow to go of, like, we have a proposed migration, we run it on our side on our local, like, database?
Demetrie King
Demetrie King
06:18
I.
Matt Stafford
Matt Stafford
06:19
Would you want that flow to go to the database in Cloudflare? Because I don't think we have access to that.
Demetrie King
Demetrie King
06:26
Okay, yeah, because right now, I think whenever… so, like, I just did a… I mean, it wouldn't technically count as a fully update, but I just did, like, a slight update in regards to logging in, like, when you log out now.
You have to, after 15 minutes, you have to enter the email again to get the, you know, the WorkOS push notification to get the code.
vincentnestler: Right now, I do it… I put it in, it puts it on another branch, and then, it puts it on PR.
And then I test everything out.
And then after I test it out, that's when I push it to main. So what are you missing right now? It's like, you can't… you're not able to… you're able to create it, and then what?
Matt Stafford
Matt Stafford
07:09
I guess when you're, like at least from my understanding of what these migrations were, it was, like, changes to your database, which is on your Cloudflare.
And I guess, like, if we're making any migrations to the database.
I'm kind of wondering if you would want those changes to your main production database, or do you want us to just, like, keep track of every migration, so then when it, like, finally merges in with your stuff.
I just feel like it could be a little problematic if we have a bunch of migrations going into, like, your production database.
Demetrie King
Demetrie King
07:42
Yeah, sounds like… so you… I'm thinking it sounds like it's a little bit better to…
Kind of have it off on the side, build, build, build, and then, you know, at the end, put it together. What I don't…
want, and you know, I want this for both of us, because like I said, I don't want y'all to do all this hard work, and then whenever y'all do push it up, there might be a problem.
whatever you think is kind of best on that ends. If it's better for you to kind of do it on your end, and then you show me, hey, this is what we're working on, this is what we have right now on the local, and then once we get ready to push it to Maine, we can do it all at once. That's… that's fine with me, if you think that's the better route.
Matt Stafford
Matt Stafford
08:21
Okay.
I mean, I think I just wanted to see if there was any baseline that you had to go off of.
Like, before, if we started making changes or whatever.
So.
Demetrie King
Demetrie King
08:33
No, like, right now, I'm just kind of writing out what I have built, and then, you know, I'm gonna kind of tell you what… if I might have some changes on another side, but other than that, it's mainly, like.
What y'all are putting together is gonna be ready once we push it up, so I'm cool with that.
Matt Stafford
Matt Stafford
08:51
Okay, that sounds good.
Mmm.
Yeah, I mean, I personally don't have any questions. I know, kind of in our process of this right now, we're kind of… at least in our class, we're going over, like, the whole architecture, so… Kind of like the full design of your project, we're going into that right now, and I know…
We're gonna probably be taking a look over your code base and kind of seeing the architecture that you've built already, kind of mapping… mapping that out, to kind of see where we can improve things, like, especially for the white label side of it.
Scalability is gonna be probably the one factor, like, holding you back, like, how many users can you support, like, how much data you can hold, all of that stuff, and…
I think where we are is just kind of mapping that out so you get a sense of where you're at, and then kind of figuring out what the best direction to go is from there.
Demetrie King
Demetrie King
09:50
Okay.
Yeah, so the only other thing… so, I mean, if you want, I can kind of show you just, on my…
you know, it might be… might not be fully done, like, so I can show you the brand side of the data points that I want, so you can fully get the… what I'm trying to bring to the table. Do you want me to show you that?
Matt Stafford
Matt Stafford
10:12
Yes, sir, that'd be awesome.
Demetrie King
Demetrie King
10:14
I got you. Hold on one second.
Here, I'm gonna go ahead and shut off my screen so I'm not messing with nothing.
Alright, should be able to see my screen?
Matt Stafford
Matt Stafford
10:27
Yes, sir.
Demetrie King
Demetrie King
10:28
Alright, cool.
So… Brand side, like, this is honestly, it's very…
generic, in a sense. I wanna really,
dig down into it, but mainly what I want to dig down into is kind of this right here. So I showed y'all this… these are, like, the data points that I'm bringing for, like, a CPG brand.
So it's the swipes, the like rate, the flip rate. And honestly, I don't know if all this is fully connected yet. I know on the vendor side, all this stuff is connected how it needs to be, but I really need these data points to be shown.
When I originally put this together, what I was going to put — so I have the three pictures here. So I have the main picture, second picture, third, and then I usually have a video.
The data points that I want here is, honestly, like, how many clicks. So, like, on the consumer side.
Whenever you have… you know, so like this right here, I want to see how many clicks this.
Matt Stafford
Matt Stafford
11:34
Hmm.
Demetrie King
Demetrie King
11:34
each one gets. So, if I'm a brand, right, and the brand logs in, and they can see, like, hey, people are really clicking on, you know, let's just use this for an example. They're clicking on this more than they're clicking on this, so maybe that should be the front main picture, or, you know, something like that. That's…
That's what I'm kind of showing on that end, but…
So I want to be able to see… let me go back to it.
I want to be able to see, like, the number of clicks right here, and then on the… on the duration time, like the app, you know, or dwell time, I should say.
There's gonna be the dwell time for the video, so, you know, I'm having them give me YouTube links so they can connect their YouTube links to this, because that could be potentially another form of monetization they could use. So, whenever they click on the video, I want to be able to tell them how long they lasted on the video right here, so…
On the images, it would be how many clicks it has, and then on the video, it'll be what the duration is in regards to,
Them watching the video. Now, on the average dwell time, what I'm looking for on that is whenever I'm,
You know, consumer… And I first go to…
You know, the energy drinks, the average dwell time is how long it takes me to either
Click to flip the card over.
And then I want other data points of showing, okay, how long, how long did it take them to click this? How long did it take them to click that? Because those are, those are huge things, because, you know, also they can, you know, click right here and see
The different, pictures as well, too, and the videos if they want to.
But those are what I'm calling swipe behavior. And that's what my technology is patented on, is using this type of behavior for forecast demand and then also marketing materials.
But also, what I'm really wanting to showcase is, if I was a…
brand, and I put out a… a brand market survey, so instead of just a regular survey that they're putting out the brand market survey, I want to be able to have the analytics, which it's not there now, this is just mainly just how many right swipes, left swipes, and total number reach, you know,
Which is pretty basic, but I want to be able to know, okay,
Kind of similar to what I have for the admin dashboard, but it's… Let me go back.
So, the admin dashboard…
Like, I want to be able to see, like, an engagement funnel for a brand market. So someone…
you know, a brand market I create.
And I want to be… actually, if you have a sense for the vendor market, too, it's possible, but basically, as soon as they… they enter a code for the brand market.
I want to see how long it takes them to go through the engagement funnel, if they completed all of it, if, how long it took
them to do it, as well. I don't know if you're following along on that, like, how long it took them to go through. Like, if I give them, like, 50 options to go through, I want to be able to say, okay, 100 people went through these 50 options, and it took them an average of this amount of time. Does that make sense?
Matt Stafford
Matt Stafford
15:03
Oh, yeah. And then I do have a question on the engagement funnel.
Demetrie King
Demetrie King
15:06
Yeah.
Matt Stafford
Matt Stafford
15:06
Like, I'm assuming…
So, like, first step would be, like, they have the code, they go in, they enter the code, and that's when that starts. Like, that's the first step of the engagement? Okay.
Demetrie King
Demetrie King
15:17
Yep.
Matt Stafford
Matt Stafford
15:18
And then after that.
I'm a little confused on the login part of it, because a person doesn't have to log in, correct, to take a survey, like, if they have that code.
Demetrie King
Demetrie King
15:28
Right. So no. So if you have a code, you will have to log in. And that's right now I'm just using the well code. When I say code, I mean like a unique code instead of QR code. So let me.
The unique code you have to enter in, like, if you're a consumer, you have to log in and enter it here in the join market section. If I'm just… what I'm doing right now is just using a QR code, which is scannable, and you don't have to log in, and it's essentially just giving me, you know, all the numbers, but no information behind it.
But my plan is, you know, because I probably won't be using,
I probably won't be using… when I'm going to the schools, I'm gonna ask students to… to join a newsletter, but they probably won't be using, like, your TCU email address, because that way I don't have to worry about, you know.
them being worried about, you know, something happening at TCU, which I don't think there will be, but…
If I… if I start having companies and CPG brands start,
working with me, I want to be able to, you know, you'll log in with, like, your personal email address, you'll put it in, you'll put whatever code I provide you right here, and then that's whenever it will lock in to the,
to the engagement funnel, as soon as you put that unique code in, then I can be able to see if I'm a brand, if I'm a brand, I can see, okay, let me see the engagement funnel for this brand market survey that I put together. And that way, you can see, okay.
They, they don't have to see the login, they would just be able to see, they view the market, they start swiping, they complete, and then they, if they complete it all, and then the time frame it took them to go through that market on an average.
Matt Stafford
Matt Stafford
17:12
Okay.
I'm… the one thing I'm a little confused about, and I… you…
probably went over it before, but I just want to make sure that, like, when you log in and you get that code for the survey, like, that market has already kind of predefined, like, what
They want you to swipe on. So what do you necessarily mean by viewing the market?
Demetrie King
Demetrie King
17:36
So, I would say, like, the…
That's them putting… them putting the code is starting the market.
Okay. Yeah, so I guess the verbiage might be different, but it's them inputting that code means, okay, they're viewing the market, so…
Usually how it would work is… and I guess it would start, honestly, from, like.
So it wouldn't start, like, right here, right? So it would start right when you click this, and then that's when you go and view the market.
Matt Stafford
Matt Stafford
18:09
So that's considered a view in the market once you get to the cards, but then…
Basically, you're wanting to measure that amount of time from where you put the code in, you…
Hit that little part again.
And yeah, so you go to demo, and then you choose…
Like, is this for every single survey, like, their interest? Or I thought this was something that, like, the market would pre… or be predefined for a user.
Demetrie King
Demetrie King
18:36
So the market is predefined. It's it depends on who I'm working with. I'm if I'm working with a school, it could be a like like like for example.
Yeah.
So, I'm working with UTA about…
plays, right? So they're doing the… they want to see what plays the students want to go see. So what I would like is, after you enter the code, and you click… like, you enter the code, then it's going to pull up
Usually, depending on,
How many, categories are in there? So, if there's 5 categories and they only choose 3, then they would click and then go through those, if that makes sense.
Kind of like this right here, kind of like the, like, the demo version. So, like, these… this has many different categories, just to showcase how Market Match can be used for different industries, but just take… Okay.
Second.
Matt Stafford
Matt Stafford
19:36
I'm just confused on, like, what… so, like, for that other option there, like, it didn't have this page here. Is this just for the demo to show, like, hey, you could use it for this different thing, how you were saying? Or is this something that would explicitly be on, like…
Every market survey.
Demetrie King
Demetrie King
19:52
So, this… the setup that you're looking up… looking at right now is how it'd be set up for each survey. So, if I have, one survey that only has
one category on it for people to swipe through, then it would just be one button for them to choose. If it has three, then it'd be three buttons for them to choose. This is… this right here, kind of what you said, this is just showcasing how you could use it for many different things, not just
Not just food, not just, you know,
Closed, just a little bit of everything.
Matt Stafford
Matt Stafford
20:25
me.
Demetrie King
Demetrie King
20:25
if I build a survey that… kind of what I did with TCU is, like, one survey that I started with had, you know, food options, it had, events on campus, and then it had,
What type of music, right?
Matt Stafford
Matt Stafford
20:39
you.
Demetrie King
Demetrie King
20:40
Three categories on here, so then they would choose the three.
And then once you start here.
Matt Stafford
Matt Stafford
20:48
the.
Demetrie King
Demetrie King
20:48
That's whenever the, the,
the market, like, you start going through the market. And then, like, say, for instance, you only do, like.
You only do, like, 10 things on here, and then stop.
Matt Stafford
Matt Stafford
21:01
intention.
Demetrie King
Demetrie King
21:02
I'll come back to this one to then go through it. You know, I wanna be able to average out how long it took someone to go through the full market. So if it has three categories and 30 line items in each category, I wanna be able to know how long it took someone to go through those three categories with all those line items in the category.
Matt Stafford
Matt Stafford
21:23
So you just want overall time, like, you don't want granular, like, let's say, product to product.
Interest to interest, like…
Do you want it to be on that granular of a scale, or do you just want like the overall how long it took for them to complete all of it?
Demetrie King
Demetrie King
21:38
So the overall, would be the main play for right now because this is just on the brand side. Because if I'm a brand and I have my products on here, you're gonna be able to see all those type of, analytics on this side of it.
So, like, if this… so right now, what I'm talking about is… is… I'm sorry, what I'm talking about is not, like, a, a data point that's on the brand side at all. So it would be, like, another button here, and it would be, like, markets, and then I create a market, you know, with,
You know, create a brand market in the admin page, push it out there to the students, and then they're like, okay.
not only can I, see all the… all the… the data that I need in regards to the individuals, but I want to see how, you know, everything that… everything in regards to what happened when that market was given out to the…
The community, so it took, if I give it to 100 students, I want to know what the average time for those 100 students to go through the full market.
Matt Stafford
Matt Stafford
22:43
And just to clarify, this is on the brand side only that gets to see that, or the vendor gets to see that?
Demetrie King
Demetrie King
22:51
So technically, it could be both. The brand side could do it for a… because I have a…
So…
Like when I'm creating a market, this is me like creating a market, right? So I can do a standard market and then the standard market is just me. You know, I have like, you know.
The UTD students, that's just a vendor, so just an organization, or, if I was a brand, I could do the exact same thing, too. So technically, it could be both.
Matt Stafford
Matt Stafford
23:33
Okay, I guess going off of that then, like, what… what differences and data points would you want the brand… or, like, the standard markets, like a vendor versus a brand to have? Like, I know the brand has, like, the individual.
Of their, like, SKU items?
But the vendor doesn't have that information, they just have overall… Or do they? Like, I…
I'm getting a little confused, sorry.
Demetrie King
Demetrie King
24:03
No, no worries, here, here, here. Alright, so maybe, I think a visual might be able… so…
Like, let's take, alright, so let's take…
the TCU thing, right? So, this is… this is the… just the vendor dashboard.
Now…
only thing they're able to see was everything that was swiped right and swiped left, and it puts it in order from the most swiped right to least. And then the only other, you know, you could add it in here on, like, hey, this is a one individual market by itself, so it looks like you had
100 students, and it took them…
This amount of time, like, you could put that data, like, right in here. It took them this amount of time. It took 100 students, on average, this amount of time to go through this survey.
Matt Stafford
Matt Stafford
24:55
Okay.
Demetrie King
Demetrie King
24:56
Start to finish.
Matt Stafford
Matt Stafford
24:58
and No, it makes more sense now. Like, from the vendor side of it, you just…
you don't have, like, that detailed view like you do on the brand side of where you have the average dwell time, all that stuff. They don't get any of that. They just get, here's the product, here's how many people it reached, here's who liked it, here's who didn't like it, and here's how long it took them to do the survey.
Demetrie King
Demetrie King
25:22
Exactly. And then and then you can narrow it down, like, instead of looking at all, like, you can just narrow it down by the categories and even more, like, the top 10, the top five. That that's the only thing as a vendor they would be able to see.
Matt Stafford
Matt Stafford
25:38
Okay.
And then, can you clarify again?
I have two questions. So, the decision versus the dwell time.
Your decision time, can that be categorized as basically you get to a card?
and how long it takes you to swipe left or right on it. That would be your decision time.
Demetrie King
Demetrie King
26:05
Right, right.
Matt Stafford
Matt Stafford
26:07
And then your dwell time is how long it takes a user to flip over the card.
Or if they don't flip over the card, do you want it to be zero? Or does that just match the decision time?
Demetrie King
Demetrie King
26:21
Yeah, it would be, the dwell time is, like, how long, like.
how long it took them to flip over the card. So if they, as soon as they pull up the card and it sits there for 3 seconds, okay, it took them 3 seconds to flip it over, but then you want to average it out compared to the other students that did the exact same thing.
Matt Stafford
Matt Stafford
26:45
Yeah, but what happens in the case of, let's say, like, an individual student? Like, they don't even flip the card over. They just instantly go, no, I don't like it.
Like, their decision time could be 1 second, but is their dwell time 0 seconds, or is it 1 second as well? Because they never flipped it.
Demetrie King
Demetrie King
27:02
Yeah, that's a good question. I think that would be zero.
Matt Stafford
Matt Stafford
27:05
Okay.
And then, my other question was…
Kind of for… I don't know, this might be something that we have to figure out, but…
If you're having people go to, like, an external link.
I guess…
Because you said you wanted a data point on, like, the video for the brand side to see, like, oh, how long did a user actually spend watching it?
I'm just kind of wondering, like…
how you would want us to implement it, because, like, kind of the definition that I'd go off of, of, like.
You'd see if, like, a user clicked the link, and then you would just wait until the next activity.
on the site.
You.
That's how I would define it, but I don't know if there's another thing you had in mind.
Demetrie King
Demetrie King
28:03
Now that I think about it, it might not need to… We might just need to…
add clicks to that, too, because, you know, they will get that type of data in regards to, like, especially if they're giving me a YouTube link.
Matt Stafford
Matt Stafford
28:19
Yeah.
Demetrie King
Demetrie King
28:20
YouTube should be able to provide them that data. So we might just be able to make all the pictures and then whatever videos added, just like tell me how many clicks it got.
That'd probably be the easier route.
Matt Stafford
Matt Stafford
28:36
You know, that makes sense.
Demetrie King
Demetrie King
28:43
Because all we're really trying to showcase is, you know, they can get that data themselves with YouTube. All we're just trying to do is showcase, okay, they have
It looks like you got all these clicks, and for this video, or for this picture, or whatever, so then they can make changes according to… if they see a picture's not really getting a lot of traction, they can swap it out and say, okay, let's put this picture in there and see if it gets more traction.
There you are.
Matt Stafford
Matt Stafford
29:06
Yeah, can you go to the analytics page again?
Demetrie King
Demetrie King
29:10
Yep.
Matt Stafford
Matt Stafford
29:10
I think… Okay, sorry, I think it's the inventory page.
Demetrie King
Demetrie King
29:17
Alright.
Matt Stafford
Matt Stafford
29:20
Okay, so… In the category, I'm just trying to think of, like.
overall, like, this is for every single market survey that these products have ever been in. There's no scope of, like.
Here's how it did on this exact market.
If you're from the brand side of it.
Like, this is overall.
Demetrie King
Demetrie King
29:44
Right. This is if I… if I… so this is if I connected a, and these are the only ones that I've actually connected to a brand, so, like, me… that brand right now is Market Match. Just… I just did this to kind of test it out and see if it was working. So whenever I'm a,
whenever I'm creating a product.
So, I create the product here, and then what I do is I add it to the organization. So, right now, if I wanted to add… add it to my inventory, I'd add it to Market Match's inventory right here, and then that's what connects that to the brand, you know, that I have…
created the organization inside of WorkOS for them to log in as a brand.
Matt Stafford
Matt Stafford
30:35
Thanks.
So there is no, like, scale of… from the brand side, at least, of per…
Market that this product has been in, this is how it performed in those certain markets. It's just
Out of every market your product's been in, here's the percent that swiped left, here's the percent that swiped right.
Basically.
Demetrie King
Demetrie King
30:59
Correct. Yeah. And then and then it shows you the, you know, the percentage of, you know, the people that actually fill out the demographic information. It'll show that here. But, yeah, it's just an overall thing right now.
Matt Stafford
Matt Stafford
31:12
Okay.
Yeah, I just wanted to confirm, like, the scale on that, if you wanted, like.
per market that that thing's been in, or if it's just overall rate. But, thank you.
I mean, I don't really have any other questions. I don't know if anyone else on the team has anything.
Demetrie King
Demetrie King
31:44
I'll come back. Hold on.
Anybody else?
Griffin Kuchar
Griffin Kuchar
31:59
Nothing on my end.
Kevin Doan
Kevin Doan
32:03
I'm good as well.
Demetrie King
Demetrie King
32:13
Alright, cool. Yeah, so that's… that's kind of what I'm trying to put together, is…
you know, something for those brands, as y'all know, just to load up and be able to put that information in there, and then once I start pushing it out, they're able to see, you know, specifically
what each individual SKU item wants, and then also see an overview of how the market did. And you made a good point, Matt, you know, it should be… I think it is, it's on both sides, on the vendor and the brand side.
Just right now I don't have like a, a brand market built yet, so that's why I'm like really kind of talking towards just the standard market.
Matt Stafford
Matt Stafford
32:54
Anything.
Yeah. No. I think I think this meeting was good. It gave I think it's gonna give our team, like, good good, like, scope in terms of, like, what data points we know we need to start tracking and, like, how we're gonna start implementing the tracking on them.
Because it seems like, to me, like, the scope for Phase 1 has always been…
Bulk import into the app of a brand's inventory.
And then these data points, like being able to have a survey.
And then actually have, like, the or I guess I don't know if the admin does the admin see all the data points or no?
Demetrie King
Demetrie King
33:32
No.
Matt Stafford
Matt Stafford
33:33
Okay.
Demetrie King
Demetrie King
33:34
Yeah, so, as an admin, the only thing I can technically see is,
I can see how many swipes, they have on it, I can see the users, but other than that, like, I can't see their data points. The thing is, though, is what I do want to be able to do without imposing is I want to…
be, like…
if someone makes a market, you know, that's fine, do the market, but I also want to be able to see some trends on my side, not specific data that they're getting. I just want to be able to see trends, if that's a possibility.
Matt Stafford
Matt Stafford
34:13
Could you define what you mean by trends? Like, let's say…
let's say for, like, the TCU IFAS survey, where, like, people were filling out, like, what types of food they wanted, that type of thing, like, what… what would be an example trend you would want from that?
Demetrie King
Demetrie King
34:30
So…
Matt Stafford
Matt Stafford
34:35
Or if there's a better scenario that makes more sense, in your eyes.
Demetrie King
Demetrie King
34:41
Well, honestly, what I'm thinking, it might be… a further phase, okay.
And I just don't want to…
What I'm thinking is, like, so for instance, like, kind of with the TCU thing, like, alright.
I'm seeing that y'all are wanting these things, and then say I have a concert coming up, right? And that concert is… I'm letting them swipe through.
Things at the concert.
and I see that the demographic is gonna be this demographic for this concert, right? Well, I already know people from this age range, this ethnicity, and this gender, from what I've done before at other market surveys, really like this, so it should be on this survey. Does that make sense?
Matt Stafford
Matt Stafford
35:29
Yeah, no, I get what you're saying. It's basically like, it's kind of dynamic in the way where it checks and says, hey.
This concert has a demographic of 20 to 25 year olds, mostly male.
This other survey I've done has the same demographic, so let's take the same items from there and see if this demographic or the same demographic likes it as well.
Demetrie King
Demetrie King
35:52
Right.
Matt Stafford
Matt Stafford
35:53
Okay.
Demetrie King
Demetrie King
35:54
Yeah, exactly.
Matt Stafford
Matt Stafford
35:56
But that's not in scope for us now, for our… Okay.
Demetrie King
Demetrie King
36:01
Yeah.
Matt Stafford
Matt Stafford
36:01
Yeah.
Yeah, at least in my eyes, you can correct me if I'm wrong, but basically the
Scope and vision for right now is…
The bulk import, I just said, and then basically those data points, being able to track all of those.
Okay.
Alright, well, that sounds good to me. Thank you for coming out and meeting with us tonight. Sorry about Monday. We should have given you a heads up a little bit earlier, but…
Demetrie King
Demetrie King
36:33
Thanks, buddy.
Matt Stafford
Matt Stafford
36:33
I did.
Demetrie King
Demetrie King
36:34
I know stuff happens, so no worries.
Matt Stafford
Matt Stafford
36:37
I already will.
And take care. Have a good rest of your week, Demetri.
Demetrie King
Demetrie King
36:43
All right, you too. Y'all take it easy. All right. See you later.
Vinh Nguyen
Vinh Nguyen
36:46
Get imagery.
