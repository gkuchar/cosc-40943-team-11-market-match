# Client Meeting 4 — Transcript

**Project:** Market Match
**Team:** Team 11
**Client:** Demetrie King
**Attendees:** Demetrie King, Matt Stafford, Griffin Kuchar, Kevin Doan, Chris Ramirez, Vinh Nguyen
**Date:** 2026-10-21, evening
**Format:** The team walked the client through its plan for the data points and for bringing in Brands' products, with screen shares of the admin side, followed by Q&A

---

_**What this file is.** The unedited automatic transcript of the fourth client meeting. Each line starts with the speaker's name. The transcription mangles some words — "CVS file" is CSV file, "chat" is ChatGPT, and "Gary Holness@" on one of Matt Stafford's lines is a stray name pasted from the call chat, not something said. Read it as raw source, not as notes._

_**Why it is in the repository.** The version 0.3 changes to [vision-and-scope.md](../requirements/vision-and-scope.md) for `FEAT-bulk-product-import` cite this meeting: how Brands send their products today, why the client needs a connection Brands can push products through, and why the team's first spreadsheet-only proposal fell short. It also answers several data point questions in [OPEN-ISSUES.md](../requirements/OPEN-ISSUES.md)._

_**What it covers.** The data points the team plans to capture, with the client adding average swipes and per-photo viewing time; when Completion Time starts for signed-in and anonymous Consumers; counting each anonymous Consumer separately instead of as one shared user; how Brands send their products today (a Google Doc or Drive of pictures and details, copied in by hand); prospective partners asking for an API connection, with Shopify as the model; Brands bringing their own Categories, and products belonging to more than one Category; and read-only Cloudflare access for the team._

_**Earlier meetings** are in [client-meeting-1.md](client-meeting-1.md) (curated notes), [client-meeting-2.md](client-meeting-2.md), and [client-meeting-3.md](client-meeting-3.md) (transcripts)._

---

## Transcript

Demetrie King: What's up, everyone?

Griffin Kuchar: What's up, what's up?

Matt Stafford: What's up, Demetri? How are you?

Demetrie King: Doing well, how about y'all?

Kevin Doan: Hi Demetri.

Kevin Doan: Like…

Chris Ramirez: Hey Demetri, how's it going?

Demetrie King: That was a break for you guys.

Matt Stafford: It's pretty good, honestly. Had a good time.

Demetrie King: Nice.

Matt Stafford: Sorry.

Matt Stafford: Yeah, we have everyone. I think kind of, like, the purpose of this meeting is, so last week we kind of met as a team.

Matt Stafford: And we kind of went through, like, your requirements, the things that you wanted us to fill out and get done.

Matt Stafford: We kind of met as a team, discussed kind of the strategies that we wanted to do and how we wanted to implement it inside your existing code base.

Matt Stafford: So I think today, just kind of going over what we talked about, our strategies for it, run them by you before we start making, like, any actual code changes, and…

Matt Stafford: Do you still have some questions that we can kind of get into later? But…

Matt Stafford: At least for now, I'll kind of talk about…

Matt Stafford: Like, the data points capturing aspect of it.

Matt Stafford: I think that kind of use case or ask is not super hard to implement. It's basically just looking at your code base right now.

Matt Stafford: Capturing different points of when users are dwelling, when they're swiping, how many swipes they have. Kind of just connecting that to your current database. Just getting those to show.

Matt Stafford: So right now, for the data points,

Demetrie King: Excuse me.

Matt Stafford: Kind of the data points that we'd go over is, like, the likes and passes, which would be your right and left swipes, left swipes on each product.

Matt Stafford: The reach, which is, like, how many people saw a product's card, their decision time, dwell time, the flip rate, so how many people that saw the card actually flipped it over.

Matt Stafford: Photo and video clicks, so, vendors, or I think it's brands. Brands will be able to see, yeah, like, how many times, like, a person clicked on their photo, and how many times people clicked on their link.

Matt Stafford: I think for the video watch time, I think since you kind of said that was going to be a YouTube link, that…

Matt Stafford: I think for that, we might not be able to actually record that. It might just be how many times a person actually clicked on the link.

Demetrie King: Okay.

Matt Stafford: Then completion time, so this would be over, the entirety… entirety of the population that took the market, like, the average time it took for them to finish.

Matt Stafford: And then you have your engagement funnel, which is basically how many people entered, viewed, started, and finished a market.

Matt Stafford: And then other demographics such as gender, age, ethnicity, and location.

Matt Stafford: I think those are the main ones that I picked up on from our prior meetings, but is there…

Matt Stafford: Anything else that comes to mind that I might have missed, that you would want tracked?

Demetrie King: The only thing I would say is, like, the average time someone,

Demetrie King: I guess it kind of goes through in the funnel. Well, the average time someone takes to go through, the thing, that would be a great, like, to go through our actual market, that would be a great thing to do.

Demetrie King: Also average swipes, as well.

Demetrie King: So, yeah, those are… those are probably two, like, the main things that I would like to do… to add on.

Matt Stafford: Okay, so I think…

Matt Stafford: on your average, like, completion time, we do… we do have that plan to be tracked, but we can also add on, like, the average swipes, right? Yeah. Okay.

Matt Stafford: Yeah, I mean, that… it's kind of, if we're already gonna get all the data on who swiped left and right, just getting an average is pretty easy.

Demetrie King: And then the time frame, is that, is that a part of the, what you spoke about as well, too, is, like, how long it goes through?

Matt Stafford: Yeah, so there's…

Matt Stafford: The completion time is a data point that we're going to track that basically is like the average time for all the users that did the market, like how long it took them to start it, go through it, and finish it.

Demetrie King: Okay, yeah.

Matt Stafford: Okay.

Matt Stafford: And…

Matt Stafford: The only thing I did want to ask on it for demographics,

Matt Stafford: Since there's kind of two ways you can enter your market where you have, like, you have your code and you could be, like, signed into it, or you're joining straight through the QR code, which is no sign on.

Matt Stafford: Are you, like, kind of fine with, like… Those statistics of like.

Matt Stafford: How many of those demographic, age, location, that type of thing, like…

Matt Stafford: If the user's not signed in, like, how would you want to get that information? Is that something that you'd want prompted before they take the market, or is it just for signed-in users?

Demetrie King: Yeah, it's… I would say it's mainly for signed-in users. The QR code thing is, like, kind of just… I just want to do it quick, and then once I get, you know, you're used to the software, then I'll have, like, students or whoever log in, and then I'll have them do the code.

Demetrie King: Now, one thing I want to ask, because it's kind of, like, it's working right now, but,

Demetrie King: I'm guessing it's just a roundabout way of making it work. So, if I create a market right now, and I, have someone scan on it, whether it's one person or 100 people scan it and go through the market.

Demetrie King: On the back end side, it only shows one consumer. And I don't know if y'all can see that, but here, I might be able to show it on my — if you want me to share my screen.

Demetrie King: But right now it's like, I'm guessing how it has it set up is it just has like one anonymous like fake email. And then whenever I'm creating the market, you know, there is already a code attached to it as well.

Demetrie King: But right now, it's only… it's only… when someone scans it, it only says one person is doing it, so only that one fake email is doing it. Does that kind of make sense, what I'm saying? I don't know if that's…

Matt Stafford: Yeah, I mean, that was also another question that I was gonna have of, like, let's say someone scans the QR code.

Matt Stafford: And let's say, I don't know, their Wi-Fi goes out, something like that, where they have to rescan it.

Matt Stafford: Like, I guess in that aspect, you would only want that counted as, like, one person, since…

Matt Stafford: Like, in reality, to one person, like, it shouldn't count as, like, oh, two people started the survey.

Demetrie King: Right. And right now, honestly, I think it has it set up like, say, for instance, they they scan a QR code and that QR code has one category and 50 line items in that category, and they swipe through 25 of them.

Demetrie King: and then they come back later and scan that same QR code, it will bring it back to wherever they left off, so the 26th deck card. So it does that correctly. But yeah, as you said, I don't want it to, like, it doesn't start over, but I want to kind of show you what I'm talking about so you can really see.

Demetrie King: Here, hold on one second.

Matt Stafford: I guess.

Matt Stafford: Like, if you're saying that, like,

Matt Stafford: potential use case of, like, a person could scan the QR code.

Matt Stafford: Start a market, go through their category, and go through, like, 25 out of the 50 SKU items. Like, when they come back…

Matt Stafford: How is that?

Matt Stafford: Would you know how that session is saved?

Demetrie King: I don't know that, how it was actually saved. Whenever I was building it, it put it together, it was like…

Demetrie King: This is what it's going to do. And right now, it's working here. But let me show you — sorry, my dog's crying because he wants to go outside. So hold on one second.

Demetrie King: Alright, so… So here I… you can see my screen, right?

Matt Stafford: Yes, sir.

Demetrie King: Alright, cool. So, like, these… like, perfect example, so here's the TCU, you know, survey that I did, right? And as you can see, it shows all the swipes that was done, but right now, it only shows one consumer did it. And it's doing that because, I'm guessing.

Demetrie King: on… The users… where's it at? Hold on.

Demetrie King: You'll be able to see it in a second.

Demetrie King: -Oh, I need to get that checked out.

Demetrie King: Yeah, alright, so you see this one right here? So, it's, it's saying that this is, it's connecting to this, so anytime someone scans it, oops, anytime someone scans it.

Demetrie King: It's just doing this one instead of actually saying, hey, it's, you know.

Demetrie King: If 20 people scan it, it's showing 20 consumers. It's only showing one consumer right now, and it's only this one. So that's why this one has all these markets entered.

Demetrie King: Because when I create a, when I create a market.

Demetrie King: Of course, I have to use a unique code, even if I'm using the public access form.

Demetrie King: Like, that's how… that's how I create it. So I use this code, but whenever I'm creating the actual market, and it's an anonymous market that's just, like, a link where they're not putting in the code and logging in, it's only…

Demetrie King: Showing up as one consumer as that anonymous one right here, instead of being like.

Demetrie King: multiple anonymous… Put in this code, does that make sense?

Matt Stafford: Yeah, no, that makes sense.

Matt Stafford: I guess, like, an initial question or ask from that is…

Matt Stafford: Like, my initial solution is that you just have every time someone logs in anonymously.

Matt Stafford: It just creates, like, a new temporary user. Okay.

Matt Stafford: which would work for just getting the data, but I don't know if it's a thing where you want…

Matt Stafford: all of those temporary users to kind of stay, so you could see all of that, where it's tracked over time. Since you could have one temporary user for each, like, person that signs in, they finish the survey, and then we gather the data, delete them.

Matt Stafford: Kind of like that flow.

Demetrie King: I think that probably would be best, so maybe it expires after, like, 30 days or something like that, whatever is, like, the usual parameter for that. That might be the best route. Because honestly, it's not, like, it's not a huge deal, because I'm still getting the data that I want in regards to the swipes.

Demetrie King: But if I'm using, if I'm giving this to a university or whoever, I want them to be able to see, okay, approximately this many consumers used it. So it'll at least lock in the consumer count and then later on it can just drop off, you know, on my back end side.

Matt Stafford: Yeah, well, I mean, because I was going to say for the data points, we, if you want averages, we're going to need.

Matt Stafford: Like, how many… unless you switch to a different metric, but…

Demetrie King: Yeah.

Matt Stafford: But yeah, I guess if someone else wants to take, kind of the API endpoint, or spreadsheets.

Matt Stafford: Basically, like, we had an idea for how we wanted to implement, like, let's say a product or a brand coming in and putting all their products into your application.

Matt Stafford: Gary Holness@So I guess if someone else wants to spearhead that…

Griffin Kuchar: I can try. But if I'm saying things that don't seem right, please interrupt me.

Griffin Kuchar: Basically, we were saying…

Griffin Kuchar: We're gonna give each of the, the brands who are gonna submit their markets, sort of a standardized way to implement everything, kind of through

Griffin Kuchar: a CVS file, or CSV, sorry. And then, once we have that, then we can kind of write a standardized backend API that will just sort of autonomously implement it into

Griffin Kuchar: the database and the backend and all that. That's kind of where we landed.

Demetrie King: Yeah, that would be… that sounds good. One thing that I'm not worried about, I just want to figure out how it would work. So, like, right now on the admin side.

Demetrie King: You know, I create a category, and then I connect, like, when I do a product, I put the items in the product, and then connect that product to the category. And what I was thinking, and I think that's how I kind of was… what I was building towards, is,

Demetrie King: Here, I might be able to show you, and it'd probably be better if I show you. So,

Demetrie King: So…

Demetrie King: Okay, no breakers.

Demetrie King: So… When I'm creating a market.

Demetrie King: Does it have it on here?

Demetrie King: Okay, so… No, actually, hold on, that's the wrong thing, sorry.

Demetrie King: All right.

Demetrie King: So, when I'm creating a product.

Demetrie King: Like in the background, so on WorkOS, I create an organization, and when I create the organization, it puts it in this area right here.

Demetrie King: And then… What I'm wanting is like say when I create an actual market.

Demetrie King: If I want to… Trying to figure out how I can say this.

Demetrie King: All right, if I'm creating a market, like, just say, like, let's just take Tech Fort Worth as a,

Demetrie King: As, say they were a brand and they had, you know, a product line.

Demetrie King: and say I wanted to click it right here, it should pull up all of their

Demetrie King: Items that they've loaded in here, and then with the categories, but what my question is, is,

Demetrie King: how do I connect the category, like, because, you know, some… like, a brand will come in and they'll have their own category, and I want to be able to make sure that that's connecting properly, whenever I'm, putting stuff or creating a market, so…

Demetrie King: Because right now… let me go down.

Demetrie King: Right now, this is how I'm creating a category, right? So I just go in here, I type whatever the category name is, I save it, and then I go in and I,

Demetrie King: you know, I go to add items, and then I put whatever it is here, and then, you know, I connect it to this category. But what I'm asking is, like, they're gonna have their own categories, and, like, is there a way to… for it to auto-populate the correct category it needs to go to? So, or…

Demetrie King: Would they be able to create a category in their own sense, and then I can load it into here whenever I approve it?

Demetrie King: If that makes sense, what I'm saying at all.

Griffin Kuchar: Yeah, I don't… I don't think that would be an issue. I'm sure they can just sort of submit the category, and then either, like you said, either way wouldn't be an issue. Either it can run through you for approval, or it can automatically create the category and link it. I don't… unless anyone else sees some blocker that I'm not thinking of, I feel like that shouldn't be an issue.

Matt Stafford: you Yeah, I mean, I don't personally see any issues with it,

Matt Stafford: The only thing that, like, might want to change to make this, like, more scalable is… I haven't taken too much of a deep dive of how your database is structured, Demetri, but…

Demetrie King: Mmhm.

Matt Stafford: Maybe reorganizing that…

Matt Stafford: To where you have, like, you have a brand, and a brand connects to a product.

Matt Stafford: And, well, yeah, a brand connects to that product.

Matt Stafford: And then products connect to categories.

Matt Stafford: And that would kind of solve your problem of like, okay, like which products belong to which category. And that's something that.

Matt Stafford: Kind of with what we were, our solution was out or saying is with like the CSV file, Excel spreadsheet, whatever format that's in that we give like a client that wants to work with us, it would kind of predefine like, hey, I have a Celsius category is energy drink.

Matt Stafford: And they would kind of upload that on their little brand side, and then that would auto-populate for that brand, all of their products, what category it goes in, and…

Matt Stafford: I think, like, going through you for approval on it as well.

Demetrie King: Okay. Yeah, that'd probably be the better route. That's what I was just kind of wondering how it would be, because, like.

Demetrie King: One thing that I did want to change, so right now, I can only assign a product to a single category.

Demetrie King: But I'm gonna need it to be able to do, like, probably dual or multiple categories later on. Because that's another thing that I would love to do, because right now, it's just…

Demetrie King: I could have a category, I could have a product for something and it could be like in three different categories. However, if I don't get it set up where I can select, like do a checkbox for each category instead of a dot, then I have to go through and build it every single time. And I don't want to have to do that over and over and over again.

Matt Stafford: Yeah, I think a question we have for you, so with our proposed solution of using some sort of Excel CSV sheets, what's kind of the accepted practice of when you've asked clients for their list of products, all their SKUs?

Matt Stafford: What is that format that they usually send you?

Demetrie King: So, right now, they just send me pictures and details. Everyone else has just been asking, how can we connect to… can we connect to your APIs? Can we connect to your APIs? That's… that's what I…

Demetrie King: That was the main thing. I was like, okay, that's what I really need to do because even if they sent me stuff, it would take me some time to do it. And I just want to make it an easy process for everyone.

Matt Stafford: Can you kind of go in a little more detail of, like, how the photos, information of each, like, SKU was given to you? Because, like…

Matt Stafford: I'm just trying to imagine of, like, if we make a solution, like, we want it to be tailored towards, like, what other clients already give you to make that process, like, as seamless as possible.

Matt Stafford: We don't want to create something where it's like a hassle for another client to be like, oh, now we have to do all this just to get our products in.

Demetrie King: Gotcha.

Matt Stafford: So, like, is it like a Google Doc, or is it literally just…

Matt Stafford: like, email exchange? Like, I'm just kind of curious.

Demetrie King: Yeah, it's kind of a Google Doc drive, and I usually tell them to give me pictures that are less than 3 megabytes.

Demetrie King: Then it's like an overview, and then pricing, and stuff like that. It's literally just a copy and paste right now.

Matt Stafford: Okay.

Matt Stafford: I mean, what are your thoughts of, like, let's say you went to a client to try and work with them.

Matt Stafford: And you're gonna say, hey, here's a Microsoft Excel template.

Matt Stafford: Please fill it out and send it back to us.

Matt Stafford: Do you think that's a reasonable ask for you to say to a client or?

Demetrie King: It depends.

Demetrie King: It could be a reasonable ask, but, you know.

Demetrie King: Honestly, you know, if I'm looking to work with big brands, which that is the plan to do, I want some type of like.

Demetrie King: Like a… like a Shopify client, right?

Demetrie King: there's a lot of people that probably use CSVs for their Shopify, but there's probably a lot of people that don't, that just have a connection put together, and that's what I'm trying to figure out, what's the best way to get that done.

Matt Stafford: Okay.

Matt Stafford: I mean, because I know another thing we talked about was kind of more your API route.

Matt Stafford: Of where we have something public where…

Matt Stafford: I guess my only thing is, like, you would have a public API where, like, a person can import, like, a batch of their products with, like, a photo.

Matt Stafford: Like, photo, category, product type, all the information that they would want for it.

Matt Stafford: I'd have to do more research into this, but just the security aspect of it, of…

Matt Stafford: How that process would work for… trusted clients, I guess.

Matt Stafford: Like, where you only would have it where, like.

Matt Stafford: Only clients you're working with can use it.

Demetrie King: Right, that's what I want, and that's kind of what I'm really kind of leaning on you guys about, is, because that's kind of as far as I go, like, what I built, and then they started hitting me with.

Demetrie King: hey, can you give me these APIs and these connections? Like, we'd be… it'd be so helpful. And I was like, okay, like, I'm… and I, you know, I tried to look into doing it myself, but I was like, I don't want to mess up what I already have on something that's bigger than what…

Demetrie King: Right.

Demetrie King: you know, I can do myself.

Matt Stafford: Okay, so, like, with the API route.

Matt Stafford: I think your desired process is that you still would like to approve of the products and categories that they're putting in, right?

Matt Stafford: Okay.

Griffin Kuchar: if.

Matt Stafford: I guess.

Griffin Kuchar: A quick question for Demetri.

Demetrie King: Yeah.

Griffin Kuchar: If you don't mind, maybe find an example of one of your clients asking for the APIs, and kind of if you're willing to share that with us so we can sort of see the exact phrasing, that they're looking for, and that way we know kind of what they're expecting, rather than kind of us just

Griffin Kuchar: Assuming and coming out with some API that's not exactly what would fit the need, would you be willing to share that?

Demetrie King: To be honest with you, it's my conversations with the people that I've been working with kind of stopped there because I didn't have those API connections. And that's why I was like, okay, this is something that I really need to get on my radar. And it essentially was them saying, hey, we need API connections, and

Demetrie King: Like, I'm gonna try to, like, bullshit and say, like, okay, I know exactly, you know what I mean? So that's why I was like.

Demetrie King: I don't know specifically, what they would be looking for, but, you know, one of the people that I was talking to,

Demetrie King: He's a, like, professional basketball player, and he has a clothing company, and…

Demetrie King: he has a Shopify store that he was like, if we could get the API connection so I could put my whole product line on here, create my own surveys, blah blah blah blah. Yes, that is something I want to do down the line, but I just want someone to be able to,

Demetrie King: Push their products on my platform without taking up, you know.

Demetrie King: Hours of time frame to get it done.

Demetrie King: For what?

Griffin Kuchar: Got it.

Demetrie King: Because I think I have, I was trying to build something myself.

Demetrie King: That was, I don't know if y'all saw that, that was for CSV bulk upload. But, like, honestly, I didn't… I didn't try it out at all. I was just kind of taking what I had built, using it, just getting it out there, showing that it works, and then, you know, seeing how we could add on to it later on.

Demetrie King: Let me see if I can… inventory.

Demetrie King: Yeah.

Demetrie King: So I do here… I'll go back to… I'll share my screen again, just to show you.

Demetrie King: So right here, I have, like, this button for a CSV upload, but, you know, I didn't… I haven't tried it out at all or anything, it's just a…

Demetrie King: area, and then I… all I did was, like, give all the type of columns that could be a part of it, and then it's supposed to…

Demetrie King: When they upload, connect to the correct

Demetrie King: Table that they need to.

Demetrie King: I don't know if that helped at all.

Griffin Kuchar: Yes, thank you.

Matt Stafford: Okay, sorry, I was looking at…

Matt Stafford: I was looking at how Shopify kind of does it, and I mean, their flow kind of describes where…

Matt Stafford: Basically, like, a person or a seller on that app would ask their API for permission to, like, upload their files or products.

Demetrie King: and.

Matt Stafford: And then basically what Shopify does is that they have, they send back a link to a cloud storage.

Matt Stafford: Area, so that would be, like, your Cloudflare, I guess.

Demetrie King: Okay.

Matt Stafford: And then, like, the client uploads all of their files into that storage center, and then through there,

Matt Stafford: It gets uploaded through. So is that kind of what you're wanting?

Demetrie King: Yeah, that is something that I'll probably be okay with.

Demetrie King: Because I think we have all… from what you told me from beforehand, I think you said my… all my images and stuff are all set up in Cloudflare, correct?

Matt Stafford: They should be.

Matt Stafford: I'm assuming that's where they're stored.

Matt Stafford: Because I know you have… you have a database on there, 10, take a look.

Demetrie King: Thank you.

Matt Stafford: You have two databases, because you have one database that holds, like, all the data.

Matt Stafford: like, not photo data, it's, like, all of your, like, your swipes, reach, all that different stuff. Yeah. And then I'm assuming you have another… it's called blob storage, but it's…

Matt Stafford: Basically, where you can just put large objects, like photos, videos, that type of thing.

Matt Stafford: So that's what I'm assuming your setup is, which would work.

Matt Stafford: For… I think it would work for what we're trying to do.

Demetrie King: Okay.

Matt Stafford: I guess with that, is there any good way for us to look at exactly what your Cloudflare setup is? Is there any way you could…

Demetrie King: Okay.

Matt Stafford: I don't know if there's a way for…

Matt Stafford: You to give us, like, an account that just has, like, read-only access or something like that?

Demetrie King: I think so, I'll have to go back through and find it, so let me, let me look tonight. Okay.

Demetrie King: What do you want me… do you know for sure? Is it usually like a… I think it's like I can send you an email and then give you read-only access, right?

Matt Stafford: Yeah, I'm assuming what it would be is that, like, a…

Matt Stafford: I think you'd kind of just add us as a user on there, or like our accounts, and you could just give us read-only access, so like we can't do anything besides just look at it, but I think that'd be very helpful to see.

Matt Stafford: kind of what your cloud situation looks like, because it's handling a lot of your storage, and with the data points, and with the API connection, that's gonna be…

Matt Stafford: Our main focus is on the cloud.

Demetrie King: Okay, I'll get to working on that tonight for you, and do I need to give it to everyone, I'm guessing? Or a specific person, or what?

Matt Stafford: I mean, everyone would be great, so we all have access to it, but if it ends up being too much or too hard,

Matt Stafford: You could just do one person, and I guess you use, like, a shared account, or just share through that.

Demetrie King: Okay. I'll look into it and see. I think I should be able to because so my buddy that that kinda put me on to to doing this, he he set up kinda like the foundational groundwork and was like, hey. This is what you really need. You do all the UI stuff. I'll kinda give you the framework that you need.

Demetrie King: And when we were setting up the images, he did set it up to say, hey, this is where all your photos and stuff are gonna go, because you're gonna have a lot of large images. So…

Demetrie King: I'll set y'all up as users, and then let you take a look, and hopefully get that to you by tomorrow, by the latest.

Matt Stafford: Okay.

Demetrie King: Let me see… actually, let me, let me… I might be able to…

Demetrie King: Give me one second. Might as well do it while I got you on the phone here.

Demetrie King: Or I got you on the call.

Demetrie King: Members… oh, no, yeah, we didn't. Hold on.

Demetrie King: Drop your, drop your… Sheesh, that's a whole bunch.

Demetrie King: Drop emails in the chat, and then I'll add it, and then I'll go through.

Demetrie King: Alright, I'm adding everybody in, but there's a whole bunch of, stuff I gotta go through.

Demetrie King: But I'll get it knocked out for you tonight.

Matt Stafford: Okay, thank you.

Demetrie King: All right, I got everyone. Yeah, I'll go through it tonight, and then give you all the access that you need.

Demetrie King: I might shoot you a text either later this evening… well, it's almost 7. But, maybe, like, early tomorrow, too.

Demetrie King: To let you know, hey… or you'll probably get an email anyway saying you got access.

Matt Stafford: Okay.

Demetrie King: Oh, actually, it might be good…

Demetrie King: Actually, alright, I'll just send it your way.

Demetrie King: It should get read-only. I might… if you need me to make any edits on anything, let me know.

Demetrie King: But you should be just getting the emails.

Matt Stafford: Okay, thank you.

Demetrie King: Yeah, I got you.

Demetrie King: And if you didn't get in, let me know and I'll resend.

Matt Stafford: Yeah, no, I got it, thank you.

Matt Stafford: I do just have some questions, kind of on the data points part of it.

Matt Stafford: So.

Demetrie King: Yep.

Matt Stafford: Like, for the completion time, do you want this to start, like, as soon as someone enters in the code?

Matt Stafford: For the market, and then they start picking their categories, or is it once they've picked all their categories and they start swiping.

Matt Stafford: That's kind of when the timer starts for completion time.

Demetrie King: Starts as soon as I enter the code.

Demetrie King: Okay. And I guess it might be different because you know, there's the one that they have to log in and enter the code, and then you set it up a separate way for if as soon as someone starts tapping on a category and swiping, if it's like just the the anonymous one, is that something we could do?

Matt Stafford: Like, have two different data points?

Demetrie King: Yeah.

Matt Stafford: Like, one for logged in users, and then one for anonymous.

Demetrie King: Right.

Matt Stafford: So, like, in that completion time, then, for a user that's logging in, like, you wanna include that time of them logging in on it, or…

Demetrie King: No, just the as soon as they enter the yeah, the actual unique code. And then on the other side, if they're scanning that, because most people it's either gonna be a scanned QR code or a clickable link. So as soon as they hit the first category and the first card pops up, that's a it should start then for that side.

Matt Stafford: Okay.

Matt Stafford: Makes sense.

Matt Stafford: Another question I had, so, like, let's say how we were talking about earlier, someone stops halfway through swiping, and then they come back later. Like, you do want that included in the completion time?

Demetrie King: Yes.

Matt Stafford: Okay.

Matt Stafford: And I guess, like, is there a timeout of…

Matt Stafford: Let's say someone's swiping on it, and then they never complete the market.

Matt Stafford: Is there, like, a cutoff on the amount of time that you would want to wait?

Matt Stafford: Or is that just a zero?

Demetrie King: That's a good question.

Demetrie King: Yeah, I'd say it could… well…

Demetrie King: I guess, yeah, that would just be a zero.

Demetrie King: Okay.

Demetrie King: Yeah, it would just be a zero.

Demetrie King: Because I do have some, like, I do have it built that if I create a market survey, there is a timer. I haven't done it yet, but it was just something I did set up that, hey, you have 24 hours to use this survey, and then it kind of goes away. But, you know, that's a little bit further down the road.

Matt Stafford: Okay.

Matt Stafford: And then I guess for clicking on photos,

Matt Stafford: Like, let's say a user's clicking on the photos and they end up clicking a certain photo more than once. Do you want to count that as multiple clicks on that photo, or is that just considered a singular click?

Demetrie King: That would just be, considered a singular click. Is there… and, you know, if it's too much, just let me know.

Demetrie King: But is there a way to calculate too late, like…

Demetrie King: If they click on it, how long they looked at it, like, a dwell time on that one picture, so say they have 3 pictures, and then picture number 2, they tap on it.

Demetrie King: but they look at picture number 2, because they like it a lot, so they looked at… they sat on it for, like, 5 seconds compared to the first picture, which was, like, only 2 seconds. Is there something that we can add a calculation on that, too?

Matt Stafford: I think there should be, yeah.

Matt Stafford: Okay. I can add that.

Demetrie King: So just, like, a singular click, and then how long someone… because, like, at some point, people are gonna be, like, zooming in and looking at, like, if it's different designs and stuff like that, they're gonna be looking longer at some of the pictures than others.

Matt Stafford: And then should standard markets, so like the vendor created markets, like should they get the engagement funnel as well or is that only for the brands?

Demetrie King: Engagement funnel, too, yeah.

Matt Stafford: Okay.

Matt Stafford: And then I guess, like…

Matt Stafford: Let's say a person's going through a market, they pick one category, they complete it.

Matt Stafford: And then let's say they want to go back and do another category. Is that…

Matt Stafford: one continuous time? Like, does that time continue, or is it… you picked your category, you went through it all?

Matt Stafford: And then it's the completion times done there, or is it?

Matt Stafford: Kind of one big thing.

Demetrie King: As the, like, if they had 5 categories, the completion time is whenever all 5 categories are done?

Demetrie King: Is that what you're saying?

Matt Stafford: Yeah. Type of thing, or yeah, or if it's like…

Matt Stafford: Let's say, I don't know, a user goes through…

Matt Stafford: They only picked one category, they go through it, and they're like, oh wait, like I wanted to do the other two.

Demetrie King: Like.

Matt Stafford: Are those all individual completion times, like all individual data points for all of that, or is that one continuous?

Demetrie King: So, that would be… I'm gonna say continuous,

Demetrie King: However, like, one thing that I'm having to… that I'm understanding while I'm out, you know, at schools using this is it's a little bit different if I'm out there telling people, like, say I have 5 categories.

Demetrie King: Some people, if they… if I'm telling them, hey, you gotta select these 5 categories before you hit start exploring to get to the next page to start tapping on the category and swipe, they understand it. But if I just have a QR code.

Demetrie King: Like, sitting up on a, you know, a board somewhere, and it has three categories, and they don't select all three, and they only select one and go to that one, and then they wanted to, kind of what you're saying, they wanted to do those other two, but now they can't, because

Demetrie King: They already passed the phase where they could select them. And…

Demetrie King: that's gonna… that's… that's something on my side I'm gonna have to just, you know, spell out to people what they need to do. Let's just keep it continuous as… as for right now. Maybe something that we can change later on, but I'm just trying to get the, you know, people acclimated to using it.

Matt Stafford: Okay.

Matt Stafford: And then… I think my last question is kind of, like, for demographic answers, like age, ethnicity, that type of stuff, like, is that data… is there, like, a time limit on that data, or…

Matt Stafford: like, will it ever expire, or… because, like, I feel like if the products are up for a while, you're gonna end up, like, getting a lot of data, and it might be…

Matt Stafford: I think, since all the data is aggregated, that you'd want to see it for, like, specific locations, or, like, specific, like, vendor markets, brand markets.

Matt Stafford: So I guess, would you want everything aggregated, or is there, like, a time expiry?

Matt Stafford: For the data.

Demetrie King: That makes sense.

Matt Stafford: Explain it better, but…

Demetrie King: Yeah, I… I get what you're saying, so… so, like, right now, My…

Demetrie King: demographic pool is at the, kind of, the very beginning, right? So, if someone logs in, the first thing it asks them is, like, their gender, then it asks, like, an age range, so it's not, like, a specific birth date or anything like that, it just does an age range.

Demetrie King: Then it does ethnicity. They can choose to do an ethnicity if they want to. They don't have to. And then the last is location.

Demetrie King: Now… What I would…

Demetrie King: What I would like is, I mean, I guess over time, is there a way for, like, say they choose 18 to…

Demetrie King: I've seen that, and that's… that may be a problem. Say they say 18 to 24, right?

Demetrie King: I want to be able to, like, if 2 years go by, And it…

Demetrie King: I might have to, you know, then ask them what their actual birth date is to get, like, a direct demographic pool.

Demetrie King: But I'm really trying to figure that out, because right now it's just an age range. I get what you're saying, because it's going to end up being stale, and it might not be accurate data. That's why I kind of just did the ranges right now.

Demetrie King: that might be something that I have to revisit, like.

Demetrie King: After a year or so, like, hey, like.

Demetrie King: Give us your actual birth date, or give us your, you know, this and that, so that way it's not the wrong data that's coming through.

Matt Stafford: Yeah.

Matt Stafford: Okay, that makes sense.

Matt Stafford: I mean, I don't have… .

Matt Stafford: and I guess you kind of already went over over it a little bit. But for, like the Api and everything, when people are sending in photos.

Matt Stafford: Like, kind of what restrictions do you have on that? Like, I know you said 3 megabytes, right? Like, is there any other kind of restrictions on…

Matt Stafford: What exactly someone could send through an API, or just in general, like, for the products and everything?

Demetrie King: I have a document somewhere where I, whenever I was building it, asked what the parameters that were needed to upload stuff to make it not grainy and stuff.

Demetrie King: Let me find that, and I can send you the full list of what… what I was, what I'm asking people, so that way you can see it. I probably will need a couple things on the…

Demetrie King: On the image side to fix, nothing, nothing crazy. Nothing on the product side, it's mainly for, like.

Demetrie King: When I'm building a market, on the backside of the market card, there's… I use, like, the Market Match logo, right? And the… the positioning is kind of off. I just need to get that fixed.

Demetrie King: And I can show you what I'm talking about. But other than that, I can send you the breakdown of what, you know, chat told me, or all the parameters needed to make sure everything's fitting correctly on my side.

Matt Stafford: Okay. Yeah, no, that'd be great.

Demetrie King: And I think,

Demetrie King: whenever I was getting this built with my buddy, he had… and I don't know if y'all are able to see that already, but…

Demetrie King: He had me put something in there to kind of do notes, in a sense, of, like, everything that I was doing.

Demetrie King: So that way you could kind of see, like, this is… this is what we're building, this is what he's been doing so far throughout this whole process. I can see if I can find that as well, too, because it would probably give you a little bit more insight to… to help you.

Matt Stafford: Yeah, no, that'd be great if you can find that and send it over to us.

Demetrie King: Hmm.

Matt Stafford: But besides that, I don't really have any other questions for you. Does anyone else have anything?

Kevin Doan: I don't.

Demetrie King: Everybody get their Cloudflare access?

Griffin Kuchar: Yes.

Matt Stafford: I got the email.

Demetrie King: Cool.

Matt Stafford: I guess if no one else has anything else, I think it was a good meeting. I think we got some more insights for the API of kind of what you want, and I think…

Matt Stafford: As a team, we'll have to regroup again and kind of come up with another proposed solution, for you on that, kind of…

Matt Stafford: Kind of look at, like, how other companies do it, and, like, what's a good example to model off of.

Demetrie King: Let me see if I can find an example on my end as well too. That way it can give you a little bit more, you know, what I'm thinking. Unfortunately, I wish I knew how to explain it on that end, but on the technical side, I'm just, I don't really know. So let me see what I can find and then I'll send it over to you once I get some clarification.

Matt Stafford: Okay, yeah, no, that'd be great, even if you just gave us, like, company that does it in the way that you like it, that would give us a lot to work off of.

Demetrie King: Okay.

Matt Stafford: Okay, well…

Matt Stafford: Besides that, thank you for meeting with us tonight, Demetri. Hope you have a good rest of your night.

Demetrie King: Alright, y'all too, you have a good week, alright? Alright.

Griffin Kuchar: Take care, Demetri.

Vinh Nguyen: See you.

Chris Ramirez: No.
