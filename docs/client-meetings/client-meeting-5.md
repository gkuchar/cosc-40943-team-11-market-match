# Client Meeting 5 — Transcript

**Project:** Market Match
**Team:** Team 11
**Client:** Demetrie King
**Attendees:** Demetrie King, Matt Stafford, Griffin Kuchar, Chris Ramirez, Vinh Nguyen, Kritika Karanjit, Kevin Doan
**Date:** 2026-10-26, evening _[the date [OPEN-ISSUES.md](../requirements/OPEN-ISSUES.md) planned for this meeting; confirm against the calendar]_
**Format:** Q&A led by Matt Stafford on the team's proposed design for Brands sending products through an API and the Admin approving them, then questions on anonymous Consumers and Completion Time (about 41 minutes)

---

_**What this file is.** The unedited automatic transcript of the fifth client meeting, with the timestamps dropped. Each line starts with the speaker's name. The transcription mangles some words — "DMW Airport" is DFW Airport, "Clyde" and "chat" are Claude and ChatGPT, "ski products" is SKU products, "the brain" is the brand, and "Sick New World" is the music festival. Short lines such as "Tomorrow.", "Mill.", "Good morning.", and "Beatlehead" on Matt Stafford's turns are stray captions, not something said. Read it as raw source, not as notes._

_**Why it is in the repository.** It answers, in whole or in part, several questions in [OPEN-ISSUES.md](../requirements/OPEN-ISSUES.md) about bringing in Brands' products: who gives a Brand its API Key (`OI-31`, where the client's answer differs from the team's proposal), how often Brands send products (`OI-32`), approving many products in one decision (`OI-37`), which video links are allowed (`OI-38`), who chooses a product's Category (`OI-39`), whether data points carry over after a change (`OI-41`), whether a Brand can remove its products (`OI-42`), image formats (`OI-24`), and the time baseline and target for onboarding (`OI-29`, `OI-30`). It also settles a cutoff for Completion Time when a Consumer never finishes a Market._

_**What it covers.** The Admin alone provisions each Brand (WorkOS Organization first) and hands out its API Key; Brands only, never Vendors, send products; an Admin approval list per Brand with reject-with-reason and an approve-all option, and an approval email the client will send by hand for now; the fields per SKU, left open until the client sends his list of about 50–60 possible columns; Brands defining their own Categories, scoped to that Brand; updates allowed, with data points reset but the earlier period kept and visible to the Brand; Brands allowed to remove products under a count limit rather than a waiting period, with the removed product's data kept; any video link (YouTube, Vimeo, and others) or an uploaded video file; JPEG and PNG only; the time it takes today (a minute to a minute and a half per product) and the approval target (100 products in 10–15 minutes); linking an anonymous Consumer's data to the account they later create, and not showing a Consumer products they already swiped in an earlier Market; a 15-minute inactivity cutoff for Completion Time; and the client being on the TCU campus on 2026-11-16._

_**Earlier meetings** are in [client-meeting-1.md](client-meeting-1.md) (curated notes), [client-meeting-2.md](client-meeting-2.md), [client-meeting-3.md](client-meeting-3.md), and [client-meeting-4.md](client-meeting-4.md) (transcripts)._

---

## Transcript

Kritika Karanjit: What are you doing?

Demetrie King: I'm doing good, how about yourself, Kritika?

Kritika Karanjit: I'm doing good, too.

Chris Ramirez: Hi, Demetri, how's it going?

Demetrie King: Good, Chris. How about yourself?

Chris Ramirez: Pretty good.

Demetrie King: Everybody have a good, break off?

Kritika Karanjit: Yes.

Vinh Nguyen: Hi, Demetrie, how are you?

Demetrie King: Good, Vinh, how about yourself?

Vinh Nguyen: Pretty good.

Demetrie King: I'm getting busy over here on my end. I went to a great expo this past week. I got to meet a whole bunch of new CPG brands that I could possibly bring on.

Demetrie King: TCU campus, and then, UTD campus as well, too. And then, actually, I'll be pitching for, I'll be pitching to DMW Airport on Wednesday.

Demetrie King: To use Market Match to potentially be, something to help them choose what retailers and

Demetrie King: Products they're gonna have there.

Chris Ramirez: That sounds exciting.

Demetrie King: It is. It's also nerve-wrecking at the same time, but I'm excited.

Demetrie King: Oh, we lost Kritika.

Demetrie King: What's up, Griffin? How are you?

Griffin Kuchar: Hello, hello, I'm doing good, how are you, Demetri?

Demetrie King: Alright. What's up, Matt? How are you?

Matt Stafford: I'm doing good, how are you, Demetri?

Demetrie King: Tonight, tonight.

Matt Stafford: You know what I… I love the hat, dude.

Demetrie King: Appreciate it, my man.

Matt Stafford: That's awesome

Matt Stafford: Yes, I think kind of today, last week we kind of met about dividing up all of our tasks, so… Kevin… okay.

Matt Stafford: Kind of dividing up the tasks, working on our use cases for each of the things that you kind of wanted from the application, so the major points,

Matt Stafford: Yeah, gathering, like, all the data, the data collection, all those data points that we listed earlier, entire meetings, getting all of those up to date in the app.

Matt Stafford: Kind of a smaller thing was, like, the anonymous users. So actually the amount of people, or the reach, per se, is the correct number, not just stuck at one if everyone was anonymous.

Demetrie King: Hmm.

Matt Stafford: And then kind of, like, the major portion of it was, the API that you've been wanting, so that other businesses can connect to it.

Matt Stafford: And import their products through that.

Matt Stafford: And I know we were… I was kind of sending out some text, for some questions earlier this week, but I kind of did just want to confirm, for that API, it's only products, or brands, sorry, that are allowed to import products? Like, a vendor has no ability? Okay.

Demetrie King: Yeah, I might have… that's why I was like, I might have said it wrong incorrectly. So, yeah, just brands are the only ones that are gonna be able to upload something. The vendor's just gonna be able to see, like, when I create a market, and then the data points in regards to just swipe rights and lefts, and, you know, that's… that's about it.

Matt Stafford: Okay, I guess just going straight into it, because I had some kind of questions for you when I was kind of designing this out, in terms of use cases.

Matt Stafford: So, my initial design that I kind of came up with is that you would basically…

Matt Stafford: on your… on the admin side, basically for your API, you could have an API key.

Matt Stafford: And that key would be something that's generated once, and you only share with, like, a brand that you're gonna work with, so only they have access to it.

Matt Stafford: And basically what this key allows them to do is that when they can… they can hit your API endpoint, so upload all their products, and they have to validate who they are through using that API key.

Matt Stafford: So kind of a question I had with that is…

Matt Stafford: Do you want to be the one that's giving out API keys? Like, kind of what's the process of a brand connecting with you?

Matt Stafford: In a way to where they can start to upload their products and be a part of the platform.

Demetrie King: Yeah, so right now, it potentially is just gonna be me giving that key out, because right now I'm having these conversations with, like… I just met with all these different types.

Matt Stafford: Just…

Demetrie King: a few brands recently.

Demetrie King: And, so I'm having meetings, and whenever we get, like, I finally get it closed through, I'll be like, okay, hey, I'm gonna create your dashboard, your brand dashboard in the back end, and whenever I do that, I guess I could give them the key that's needed to upload whatever products they had. Because I have to create the organization on my side, through WorkOS first, so then they'll be able to be

Demetrie King: connected as a brand, on that end.

Matt Stafford: Okay, okay, that makes sense. So basically, you would be the one provisioning all of it. It's not like a thing where a brand can kind of self-serve on the Market Match website through, like, that brand portal.

Demetrie King: Right. That probably will be the plan later on, but honestly, I don't… I don't want to have a whole bunch of people trying to push through stuff, and then I'm just sitting there getting bombarded, and, you know, it could possibly throw off the whole flow. But for right now, it's just…

Demetrie King: I'll be talking to them once I close them, then I'll provide them the API key to connect to their organization, and then they can upload whatever they want to.

Matt Stafford: Hmm.

Matt Stafford: And then I had another question, so kind of the proposed flow that I had right now is that…

Matt Stafford: You talk to a brand, they're a new client, so then you set them up in WorkOS,

Matt Stafford: And they now have their API key, so then they can now upload products. I wanted to get your thoughts on the approval process for it, since I know we talked about that you still want to have full control over whether

Matt Stafford: Like, what products actually are on Market Match?

Matt Stafford: So, my idea for it was kind of have on that admin panel, dashboard, you kind of have a section of brand by brand. It'd basically just be a list of the new products that they want to push, to the application.

Matt Stafford: And it would basically just… you would approve, say yes or no, and if no, then it would get sent back to the brand, for them to fix their cards, or, like, kind of with the reason why on the brand dashboard side.

Demetrie King: Yeah, you started to freeze a little bit, but I think I got majority of what you said. So yeah, that sounds good to me. Also, just to…

Demetrie King: Right now, I… like, if I create a product on the profile, I do have the ability to, once I create a brand, just to connect that product to the brand. That's an ability that I have to do now as well, too.

Demetrie King: But yeah, that's the setup I like. If they load something up, and I say, hey, this doesn't look good, or whatever, then it, you know, pushes back to them and say, hey, you need to upload this and that, and, you know.

Demetrie King: whatever else, because, you know, I don't really want…

Demetrie King: blurry pictures and stuff like that, I want to make sure that everything's uniform and, you know, looking good. So that way… because essentially, this is their first impression as well, too, by putting their brand out there, if they're brand new, so yeah.

Matt Stafford: And then on that same, wavelength, so… would you want, like, an approve all option? So, like, instead of having to go through each one individually.

Matt Stafford: And say, like, oh, I approve of this, approve of this. Let's say, I don't know, you glance over all the stuff a brand has, all the products, and you just say, hey, I want to approve all of it at once. Is that a functionality you would like to have, or…

Matt Stafford: Tomorrow.

Demetrie King: Yeah, that'd be great.

Demetrie King: No, that'd be great. I mean, if it's possible to do both, that's fine, but, you know, if someone has, like, 200 plus SKUs, that's gonna be forever, so I would love to, you know, have a select all option, and then if you could add in there,

Demetrie King: some type of notification that the brand receives saying, hey, you've been approved, then that would be, you know, good as well, too.

Matt Stafford: Okay, and then… I kind of wanted to find notification, like, so… what you mean by that?

Matt Stafford: Mill.

Matt Stafford: A text message. What's your definition of, like, they get a notification?

Demetrie King: Hmm,

Demetrie King: I'm trying to figure out, like, I… I want it to be automated, but I don't want it, like, if it's something that's, you know, extra work for no reason, you know, I could also send them an email myself.

Demetrie King: potentially, I would just like an email sent to them saying, hey, you've been approved. That's really about it.

Matt Stafford: Okay.

Matt Stafford: And then another question, so basically on this API, like, what we would define is contract. So it's basically so the brand should know exactly, like, what they need to send. And kind of, like, the draft that I came up of things that are required would obviously be, like, the product name.

Matt Stafford: Name slash title, like, a product description. There are three… That they were gonna have.

Matt Stafford: And then a link.

Matt Stafford: And then on top of that, like, I also saw there was a price, don't think there's too much else, but, like, what would be the defined things that you would want,

Matt Stafford: per SKU to have stored.

Demetrie King: So that's one thing that I've been trying to really figure out, because, you know.

Demetrie King: these different items could have different types of titles and SKUs, like, there's, like, product name, there's, like, color, there's all this other type of stuff, and when I was…

Demetrie King: putting this together, kind of building it through Clyde, I… I essentially put all those type of opt-ins in there, so it would, like, kind of find what it needed to and connect to it.

Demetrie King: it's… and if you want, I can… I can try to find the original, description of all the different types of titles, or columns, I would say. Is that the right verbiage? Columns for them to connect to? Because, I mean, there's about, I think, about 50 or 60 of them that, you know, is possible.

Matt Stafford: Yeah, I think you're kind of talking about in your database, in your schema for that, like, of what exactly would need to be in there.

Matt Stafford: Okay. Yeah, if you could get back to us on, like, the exact stuff that's, like, required to have in the app, at least for each SKU, because then that lets us kind of define, like, what our API, like, how to design… or how to build it, basically, without those fields, like, we can't really…

Matt Stafford: do that.

Demetrie King: Yeah, cause right now, the only thing I really have is,

Demetrie King: I have the product, and then I add up to the 3 images, I add the link, and then I just connect it to a category that I've created. And that's… and that's really, like, all the parameters I have right now, but I know further along, it's gonna be…

Demetrie King: I'm gonna have all those different type of line items that they want in there that kind of connects to their product line, depending on what it is, like.

Demetrie King: Compared to, like, a t-shirt and an Amazon drink, you know what I mean? It's gonna have a different set of, line items.

Matt Stafford: And then, correct me if I'm wrong, but the scope of this that we're kind of looking at for the categories?

Matt Stafford: Because there's kind of a different… couple different options I could think of. Like, would you want the brand to specify what category it goes into, or do you want that to still be a step that you manually do? That you manually put products into categories?

Matt Stafford: like, on the approval step is one way I could see that, or… In the API itself.

Matt Stafford: what category their SKU belongs to?

Demetrie King: what I think…

Demetrie King: could, you know, it might, you know, alleviate a lot of confusion, is if, especially on the brand side. So, if a brand

Demetrie King: chose whatever category they wanted, then the only… whenever I do the drop-down of the brand organization, only their stuff will pull up. Do you think that would be probably the better way to do that, instead of trying to connect it? Do you get what I'm saying?

Matt Stafford: Can you, can you explain that again?

Demetrie King: So…

Demetrie King: So, like, right now, whenever I put something in, you know, I create a category, then I just connect something to it. Would it be easier for them to create their own category themselves, and then tie it

Demetrie King: to whatever it is, to tie the category to the product that they have, and then whenever I'm, when I have the drop-down of the organization that pulls up all their products, then it would just populate everything that they chose, like, whatever category they said, and then the product connected to that category.

Matt Stafford: I think that works if everything is scoped to a singular brand. So, like, if you're saying…

Matt Stafford: let's say I pull up, I don't know, Monster Energy, they have, what.

Matt Stafford: energy drinks, their juices, or whatever. If it's just scoped to, like, Monster only, where, like, let's say, okay, a vendor wants to see what their students think about Monster, it pulls up only those categories to find on Monster, then I think that works.

Demetrie King: Okay.

Demetrie King: Okay, yeah, that would be great.

Matt Stafford: Okay.

Demetrie King: Cause I'm trying to…

Demetrie King: And I don't know if, like, showing you could kind of make a little bit, better understanding.

Demetrie King: what I want to do is, like, once I start getting these brands on the application, like.

Demetrie King: great examples, like, Monsters, like, alright, Monster wants to do a survey, and it wants to be their… their, energy drinks, and then it also wants to be their,

Demetrie King: well, I guess they're all sugar-free. But, like, energy drinks, and then they have the different types of energy drinks, like, I don't know. So that way I can just…

Demetrie King: tap that category, and then say there's 20 line items in that category, it loads those 20 items into my market survey that I'm creating, and and then that's how I kind of build it on my end.

Matt Stafford: So you would want… I guess to just define it, like, in the API, when, say, Monster is importing all of their… all of their energy drinks, you would want Monster to define exactly what category each SKU item goes into.

Demetrie King: Yeah.

Matt Stafford: Okay.

Matt Stafford: Okay.

Matt Stafford: Good morning.

Matt Stafford: Okay.

Matt Stafford: Beatlehead, so… I guess two things bundled into one. You're allowing brands to update their products, correct?

Matt Stafford: Right, so.

Demetrie King: Right now.

Demetrie King: Right now, they just kind of send me their stuff.

Matt Stafford: Mmm.

Matt Stafford: But I'm saying, like, when we build this API, do you want to allow for the updating of their ski products? So let's say…

Matt Stafford: I don't know, Monster wants to go change one of their photos for one of their energy drinks, like, you want to allow that, right?

Demetrie King: Right, right.

Matt Stafford: Okay, and then kind of building off of that,

Matt Stafford: Since we're keeping all these data points, based off of each product, let's say they change photos, let's say they change…

Matt Stafford: product description, whatever attribute about the SKU itself.

Matt Stafford: Do you want to keep those data points, or do you want them to reset?

Matt Stafford: Because it could be misleading of, let's say, you have photo 1 clicks, but then they change the photo, it's not really…

Matt Stafford: Representative of what it currently is.

Demetrie King: Yeah, that's a… that's a great, point there, because…

Demetrie King: The plan is, is to… say they have 3 photos, and then one of the 3 photos is, like, getting all the clicks, right? So now they need to change the other 2 photos and see if those get more clicks. I would like it to reset, but I do want to keep the data points that were there before, so, like.

Demetrie King: photo, like.

Demetrie King: Photo 2 and 3 that, you know, didn't get a lot of clicks the first time in October, you know, only got this amount of clicks, but when we updated it on November 1st and put two new pictures in, it got this many amount of clicks whenever it was out there.

Matt Stafford: Okay, and then… Another question based off that. How do you kind of want that distinction made, like…

Matt Stafford: Is that just something we're storing in, like, our database, or is that something that, like, you…

Matt Stafford: At least on the admin or the brand side, for them to physically see.

Demetrie King: So, on the brand side, I would like them to be able to see that.

Demetrie King: potentially, I'm not getting, like… like, their data's their data, right? So if they have their SKU items on there, and they make any changes, they're able to see all that. I don't know if there's an easier way, because what I don't want to do is, like, kind of…

Demetrie King: Like, they might be switching stuff in and out just to see, you know, what people say.

Demetrie King: But I don't know what the better route is to make sure that, you know, the data's not skewed, or there's not stuff going in and out.

Matt Stafford: Okay.

Matt Stafford: Okay.

Matt Stafford: So, since we've kind of talked about, like, the creation of products, I kind of wanted to go into, like, deletion.

Matt Stafford: So, as of right now, kind of what's your policy for that? Like, is a brand allowed to delete any of their products at any time? Does deletion require…

Matt Stafford: process? Like, what were you envisioning?

Demetrie King: So, right now, a brand isn't allowed to delete anything, I'm just able to delete it on my end, because right now, whenever something's uploaded into the system, it goes directly into my admin inventory, and then, you know, I'm able to create the market with that. I would like,

Demetrie King: To give them the ability to delete some stuff.

Demetrie King: As well, too.

Demetrie King: I don't think it… I don't know if it really, like, matters on my end if I…

Demetrie King: If they delete it or not.

Demetrie King: But it could, you know… I just don't… what I don't want is, like, a whole bunch of… they add it, delete it, add it, delete it, and then it could skew their numbers. What I want to make sure is that, you know, if they have something locked in place, at least let it sit for a little bit, then they get the numbers they need, and then they can possibly make a change, and then delete if they want to.

Matt Stafford: Okay, so is that… are you kind of saying you would want a hard rule in which, after a brand uploads a product, it gets approved by you, there's a set, like, time until they can delete, or…

Demetrie King: I would say, sorry, you're cutting out on me a little bit, but I think I got what you said.

Matt Stafford: Alright.

Demetrie King: I don't want to put a hard rule,

Demetrie King: I mean, it is something that, you know, could possibly help.

Demetrie King: I don't know, that is something that could help.

Demetrie King: Maybe so. Maybe so. I'm just trying to keep from a whole bunch of deletions and additions, and then, you know, even though I'm approving, like, I'm just getting all these emails or whatever saying, hey, you need to approve this stuff, because, you know, it's…

Demetrie King: It… they're going back and forth.

Demetrie King: Maybe, like, a two-week. A two-week could be something, like a two-week, like, of the items on there. I don't know if that's a solid time frame.

Griffin Kuchar: also, like, I guess, and…

Griffin Kuchar: maybe not in, like, a hard time. Like, limit, it could be account limit. Like, they could do, you know, it doesn't matter how many in a day, but they can only do 3, you know, some sort of rate limiting kind of thing.

Griffin Kuchar: But, I don't know, whatever… what do you think about that?

Demetrie King: I think that probably might be a better, you know, option right there, because that way, they'll understand that, you know, they can only do it a couple times, and then when they're uploading their products for, like, the first or second time, then it'll keep them from doing it over and over again. That might probably be the best route.

Griffin Kuchar: Yeah, and that way, if they, like, make an accidental mistake or something, they don't have to wait the full two weeks, they can just quickly update it on the count, something like that.

Demetrie King: Yeah, that's a good call. Yeah. I just need to get them accustomed to not making… or making as least amount of mistakes as possible, you know, so that way it's better for everyone.

Matt Stafford: Okay, and then one more thing on the deletion part. So, if a brand deletes their product, let's say, I guess what is the procedure for, like, all the data that's associated with that SKU? Is that just deleted? Are we holding onto it, or…

Demetrie King: Yeah, let's hold onto it, and not even specifically for me. Like, they might want to take that data themselves later on. That's gonna be something that I'll probably be charging them for as well, too.

Demetrie King: Because if they want to go back and look and say, hey, well, we had this one on here, we have 10 products on here, but we already deleted it, and now we forgot what we had. I could possibly use that as a charge to say, well, let me go back and find it, and then I can give you that data, and here's a cost for it.

Matt Stafford: Okay.

Matt Stafford: And then I did want to define another thing, so for the links, are you kind of just scoping it only to YouTube links, or are we kind of allowing any sort of link? Like, let's say a website has, like, a video on their home webpage, like, are we allowing that, or is it just strictly…

Matt Stafford: Like, YouTube video source links.

Demetrie King: I believe it actually might be a little bit of everything. I don't think it's just YouTube. I'm really kind of push… I'm… I'm pushing YouTube, because that's a way for them to, you know, of course, make more money. But I think… I think… I think it's, like, Vimeo, YouTube, and a couple other options as well, too.

Demetrie King: And I can, I can upload, I can also upload a, video as well, too, so if they send me a video, I can upload it as well.

Griffin Kuchar: Yeah, that was my question, was gonna be, if…

Griffin Kuchar: you want the option where they can also just send you, you know, the raw, the video file.

Demetrie King: Yep.

Griffin Kuchar: Okay, cool.

Matt Stafford: Okay.

Matt Stafford: So as of right now, like, for the product API, kind of the scope of it was, like, kind of why I asked you earlier, like, how many products is it usually? So it'd be, like, 5 to 200 SKUs at once.

Matt Stafford: And then, I kind of just wanted to get your timeframe on this, like, what would be an acceptable amount of time for, let's say, a product to upload all their stuff, and then… until they can actually see it live on Market Match? Like, until the whole approval process goes through, or it gets to you?

Demetrie King: Hmm… that's a good question, and honestly, I don't know the answer right now.

Demetrie King: Because, like, whenever… so, I had a TCU… well, I'm working with a TCU student who has a,

Demetrie King: a company that has designs for, like, e-scooters, right? And, whenever he sent me his files, he sent me, like, 200, 200 designs.

Demetrie King: And each design has about 2 pictures and a description, right? And whenever I went through his, and that was him just sending me a Google Drive with, you know, the images and stuff in there.

Demetrie King: And it probably took me a little over two hours, 2 and a half hours to get through all that.

Demetrie King: So that's why I'm, like, I'm wanting, like, a bulk upload, but I honestly don't know what that time frame should be. Like, if I'm able… even if it takes, like.

Matt Stafford: I agree.

Demetrie King: 20 or 30 minutes to go through that process, I'm fine with that. It's…

Demetrie King: it's just hard for that first time by uploading, because once I… once I get it uploaded, then it's easy to create a market like… like nothing. So that's… honestly, I don't know what that timeframe would be, or what it… what it usually is. That's what I was kind of hoping you might be able to give a little insight on that.

Matt Stafford: Yeah, I mean, I'm only asking that because I kind of want to have, like, a success metric to be able to measure, like, okay, with this product import.

Matt Stafford: how much time is it really saving you? And I think that's the whole point of having this, is that you don't have to go in there and manually do it yourself. The brands can go put their products in, and then you only have to spend time on accepting or rejecting

Matt Stafford: Yeah.

Matt Stafford: So with, like, you would say, on average, usually, for the amount of SKUs, like, each brand has been sending you, it's about 2 to 2.5 hours?

Demetrie King: Well, it's, like, I would say about, if I'm, like, just chilling and just sitting there at the house, like, it might take me, like, a minute

Demetrie King: to a minute and a half per item, if they handle all three pictures, description, and that's literally just me, click, click, click, copy and paste, and then click, and copy and paste the YouTube link in there.

Demetrie King: It's about a minute to a minute and a half per item.

Matt Stafford: Okay, so, I mean, if you scaled that up, it'd be about…

Matt Stafford: I don't know, 5-ish to 200 minutes, just…

Demetrie King: Yep.

Matt Stafford: Okay.

Matt Stafford: I don't know.

Matt Stafford: And then, is there any other, like, image requirements beyond, like, the 3MB limit that you were saying earlier? Like, is there…

Matt Stafford: a specific format, like PNG, JPEG, or anything that cannot be put in there, like, as a photo?

Demetrie King: It is PNG and JPEG right now. I know I can't put in… what is it, WebP, like, if it's a WebP image.

Demetrie King: I can't do that.

Demetrie King: I told you, and I forgot to do it. I'm gonna go find the, the document that I have that kind of gives the outlay of everything that, when I ask chat what I need, and that way it could give you some insight. So let me… I'll find that, and then I'll send that to y'all.

Matt Stafford: Okay. But, like, is there any restrictions that you would want to be put on that, like, before we build this out, of, like…

Matt Stafford: hey, I want… I don't know, I want all of them to be JPEG or PNG, like, I don't want to use any other type of photo.

Demetrie King: It would… I would say just probably, JPEG or PNG is what I'm really looking for, to keep it easy.

Matt Stafford: Okay.

Demetrie King: Let me write that down, too.

Demetrie King: image requirements.

Matt Stafford: And then, kind of in your experience, and when you've been working with brands, like, how often… are those…

Demetrie King: You're cutting out on me a little bit again.

Matt Stafford: the whole… Oh, sorry.

Matt Stafford: Okay. Like, kind of what is the frequency of, like, when you're working with the brain, of, like, how often they gave you new items to upload? Like, is it usually just, like, when you first talk to them, it's like an all-in-one, like, here's everything we have, or is it kind of…

Matt Stafford: here's 10 items, the next week, oh, here's another 10 SKUs. Like, what's the frequency of it?

Demetrie King: As of right now, it's just been a one-time thing. Like, they have either…

Demetrie King: 10 SKUs, or, like, 200 SKUs, but what my…

Demetrie King: my mindset is gonna be is, like, especially when I start working with clothing brands, is they're gonna be sending me designs before, like, they… they start kind of putting it to market. So, if they have, like, 100 different designs, like… like, Sick New World just came, like, just… just happened, right? And,

Demetrie King: before the concert, if they wanted to give me, like, 500 different SKUs of stuff before the concert happened so they could send it out, that's what I want to be able to…

Demetrie King: attain is like, okay, they gave me 100, okay, we got what we wanted out of those 100, now there's another 100 that they're about to send me of the designs. But as of right now, it's just been a, hey, what do you have? Send it over to me, we get it uploaded, and then, you know.

Demetrie King: the next batch that you have, send that over, and then we'll do the same thing. There's nothing being, put on, like, kind of on my platform, and then, you know, a month or two later, they're pushing, like, another 50 products, but it could possibly be that in the long run.

Matt Stafford: Okay.

Matt Stafford: And then, kind of, last few questions I have.

Matt Stafford: for the photos and the storing of those, as of right now, it's always, since it's been through Google Drive, Docs.

Matt Stafford: It's always, like, they're always stored on your actual app, right? It's never, like, a link to an image to where… okay.

Demetrie King: Right. Yeah, so right now, I just have, like, a… yeah, it's just a Google Drive, and I open it up on my side, and then I just, you know, input the…

Matt Stafford: route.

Demetrie King: Give me.

Matt Stafford: Okay.

Matt Stafford: Okay, well, that's kind of all the questions I had for you today, and, I mean…

Matt Stafford: The floor is for anyone else if…

Griffin Kuchar: I have a question.

Demetrie King: Yeah, what's up?

Griffin Kuchar: So, I was kind of scoping out the use case for the, the anonymous users, kind of having their own, like, becoming their own user into the system.

Griffin Kuchar: I was coming across kind of a question where I was thinking about if somebody was an anonymous user, and then they filled out a survey, and we kind of store their data, and then they come back, and then they create an account, so now they are a signed user. Would you want their data to be linked, or kind of just keep it as this

Griffin Kuchar: the set of data when this guy was anonymous, and then here's the set of data when the guy was signed in. I can see it being helpful in either way.

Demetrie King: Yeah, that's,

Demetrie King: Yeah, that… yeah. I probably want it linked, if… yeah, I probably want it linked. I don't know how… I mean, I'm sure y'all can know how to figure out how to do all that yourself.

Demetrie King: Yeah, that would be great.

Demetrie King: And another thing, too… And I don't know if this,

Demetrie King: So in… say, for instance, say I'm a… let's just say I'm a… I'm a concert attendee, right? And I'm going to an event, and then they,

Demetrie King: swipe through the products. Like, say I'm just swiping through alcohol, right? So I'm going to one concert, I'm swiping through alcohol, or I put in the code, then I swipe through the alcohol. If I'm going to another concert.

Demetrie King: through, if I'm going to another concert the next month.

Demetrie King: and I put in a code, I don't want to have to be able to swipe through everything I've already swiped through before. I want to be able to just… it just showcases things that I haven't seen before. So that way, it's pulling the data… I don't know if this is making sense, it's pulling the data that me as the user have done.

Demetrie King: And just saying, hey, he's already swiped through here, so this is what the data should be on this market, because he's already done it on this market.

Griffin Kuchar: Okay, yeah, I see what you're saying. I haven't super researched it, but I think there's probably a way to tie the device to the user, and then you can kind of check based on the device which products they've seen, and then once they, you know, create an account, we'll know it's that device, and we should be able to link

Griffin Kuchar: The existing data.

Demetrie King: Okay, yeah, that'll work. Yeah, that way we can do… because that way we're not starting all over, and then we can connect whatever anonymous data that they've already done to whatever… whenever they log in, and we get everything else from it as well.

Griffin Kuchar: Awesome. Thanks.

Vinh Nguyen: Wait, so, in that case, like, when the user, they might not see the items that they already, like, swiped before? Like, what if there's a case where, like, if some, for some reason, they just change the taste in, like, the wines or alcohol? Like, if they want to change, like, that taste.

Vinh Nguyen: Are they gonna be, like, have a chance to see the items again, or no?

Demetrie King: Wait, say that one more time?

Vinh Nguyen: Like,

Vinh Nguyen: So, you mentioned that, like, when the user, and they… they're gonna strive for an alcohol, like the wine, in one…

Vinh Nguyen: kind of, like, occasion, and then they're gonna have another survey in, like, another concert or something, and, like, in some case, if the user, they might change their taste in the alcohol, is there a chance they can… they can see the items again, or…

Demetrie King: Oh, no.

Vinh Nguyen: the new ones.

Demetrie King: So, I would say…

Matt Stafford: Good luck.

Demetrie King: longer down the line, they probably… we can circle back to it, but potentially what I'm saying is, like, say they,

Demetrie King: on the first concert they go to, they give, like, they were given 50 wines, right? And they swipe through those 50, and then the second concert they're going to.

Demetrie King: they're given 100 wines, but they're not able to see those 50… the first 50 that they've already swiped through. They're only able to see the 50 that they haven't. And then the… later on, we'll… we will be…

Demetrie King: we will be kind of what you're talking about is, like, because people's tastes can change, and so I would want to circle back. That is something probably, like, later in the future that I want to be able to handle, but maybe… maybe not right now. But I think you are right, you know, people's tastes change. I was drinking something completely different than when I was, like, 5 years ago.

Demetrie King: But we want to get that first, just kind of…

Demetrie King: glance what you think, and then, okay, we don't want to put it back in front of you unless I'm working with a specific, like, brand, and then they're going out and putting out a brand market to figure out what their next thing should be.

Vinh Nguyen: And, I also have another question about, like, the notification. Like, for now, like, when the seller or the vendors, they finish, like, uploading every item on the API, using the API, and after you approve it, then you're gonna, like, write an email manually and send it back to the vendors? Is that what you said?

Demetrie King: Yeah, I'll go ahead and do that. I'll just do an email myself saying, hey, you've been approved.

Demetrie King: Maybe later on, I can tie it in where it's automated, and then after I either hit select all, or I, hit a certain amount, and then say, like, you gave me 50, but 45 of them are approved, and 5 of them aren't approved. So let me just do it manually right now.

Vinh Nguyen: Oh, okay, awesome, yep.

Matt Stafford: I guess if no one else has any other questions, Demetrie, I did have one open thing from our last meeting.

Matt Stafford: And this is kind of on the, more associated with the data points rather than the product API.

Matt Stafford: Thank you.

Matt Stafford: But I know we were kind of talking about for… The average completion time?

Matt Stafford: And within that.

Matt Stafford: kind of how we wanted, or not… or yeah, how we wanted to handle, like, if a user starts a market but never completes it.

Matt Stafford: I don't think we ever pinned down an exact, like, what we should do in that situation, if that should just…

Matt Stafford: Go on for, like, a certain amount of time and then cut off, to be added to the average, or if it should just not be added to it.

Demetrie King: Yeah, let's… let's cut it off after a certain time frame. Maybe if, like, they're… they're going through and then they stop.

Demetrie King: you know, maybe 15 minutes after they stop, we can kind of cut it off there, and then I don't know if there's a way for us to either start the clock when they start it again, that could…

Demetrie King: Bring it in, or, you know, whatever the best route is to get the average decision time on that.

Matt Stafford: Okay.

Matt Stafford: Yeah, we can kind of…

Matt Stafford: Think about what the best decision for design route for that would be.

Demetrie King: hungry.

Matt Stafford: And then I had one last question. This is kind of on the success metrics of, like, how much faster the product API should be.

Matt Stafford: What would be, like, an acceptable, like, threshold for how long it should take you

Matt Stafford: to approve or reject of, like, the SKUs, like, once, a brand.

Matt Stafford: imports it? Like, how much time would you…

Matt Stafford: Say is acceptable for you to be spending on that.

Demetrie King: I mean…

Demetrie King: I don't know if this is, like, just me thinking great, but, like, if, like, say they send over 100 products, and I can approve all of them within, like, 10 to 15 minutes, that would be…

Demetrie King: Very successful on my end.

Matt Stafford: Okay.

Demetrie King: Because the hardest part is essentially, like, not even on my end, because I'm just going to be really kind of viewing, and then after I get the green light, I'm just saying, okay, this is done. As long as they're able to load up their stuff quickly, and then I can approve it as fast as I can, then, you know, we should be good.

Matt Stafford: Okay, that sounds good.

Matt Stafford: I mean, that's kind of all I have for you today, if anyone else has anything, before we wrap it up.

Griffin Kuchar: I'm good.

Demetrie King: And then also… oh, go ahead, Griffin.

Griffin Kuchar: No, I was just gonna say, you answered the main question I had, so I'm all good on my end.

Demetrie King: Okay.

Demetrie King: So I'll be on campus, on November 16th, that's a Monday, and we're set to meet on then, too, so I don't know if you want, I can come and meet with y'all there. I'll be going and speaking at the PRSSA, that evening from 7 to 8, so I can meet y'all before that if you would like.

Demetrie King: I don't know if that'd be a better fit, you know.

Demetrie King: Or if you might not even need to meet, but just wanted to give you a heads up that I will be on campus, next month.

Griffin Kuchar: Sweet. Yeah, that sounds good.

Matt Stafford: Yeah, I think for that meeting time,

Matt Stafford: Well, we can update you and let you know, but I think if we are going to meet with you on that week, that we would obviously want it to be in person. I think that's just a better way overall. But kind of when that time comes, like, we can let you know a week in advance, kind of how we have been, in prior weeks of, like, when we're…

Matt Stafford: work.

Matt Stafford: So…

Demetrie King: Okay, yeah, just let me know, keep me updated. Like I said, we may… y'all might be just doing y'all's thing, and we might not even need to meet, so that's fine with me too, but if you have any questions, we can more than… I'll be more than happy to connect with y'all.

Matt Stafford: Okay.

Matt Stafford: Well, that sounds good. Thank you for coming out and meeting with us again tonight, Demetrie. Answering all my questions, so…

Demetrie King: Cool, appreciate y'all, and if anything, you need anything else, just please let me know, text me. I might be slow to text, because like I said, I'm kind of running around right now, but I appreciate what y'all are doing for me.

Vinh Nguyen: Thank you, Demetrie.

Demetrie King: Alright, that's how you can do.

Matt Stafford: Thank you, have a good rest of your night.
