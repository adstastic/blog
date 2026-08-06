---
title: "TDD, AI Agents and Coding With Kent Beck"
date: 2025-08-09
slug: "tdd-ai-agents-and-coding-with-kent-beck"
tags:
  - quote
ref: https://share.snipd.com/episode/23894df4-1e88-40e2-b125-218d4b72bf45
---

Quoting [The Pragmatic Engineer](https://share.snipd.com/episode/23894df4-1e88-40e2-b125-218d4b72bf45):

> **AI Coding as a Genie&#39;s Wish**

- Kent Beck compares AI coding tools to a genie that grants wishes imperfectly and unpredictably.  
- The genie sometimes produces surprising but helpful results or frustrating mistakes that require correction.

Transcript:
Kent Beck
A kind of wish fulfillment. I wish that Interlisp had a function called the DWIM, do what I mean. And you&#39;d send it some code and then it would send back code that did what you actually meant. And it didn&#39;t work very well, but that was the metaphor. And people want that to be true of coding agents. And right now, anyway, that is not the truth. They will not do what you mean. They have their own agenda. And the best analogy I could find is a genie. It grants you wishes, and then you wish for something, and then you get it, but it&#39;s not what you actually wanted. And sometimes it even seems like the agent kind of has it in for you. If you&#39;re going to make me do all this work, I&#39;m just going to delete all your tests and pretend I&#39;m finished. Ha, ha, ha, ha. You know, and there are some good things about what the genie does that&#39;s not what I ask it to do. Like I&#39;ll implement, I&#39;ll say, I&#39;ll go implement a stress tester. One of my projects is implementing a B plus tree as a basic data structure. And I said, oh, write a stress tester for this. And it went and wrote a whole bunch of stuff that I wouldn&#39;t have thought of, or maybe eventually would have thought to ask for. And it was cool that it was there. And that part&#39;s fine. But this morning, when I was working on my server Smalltalk, and it just completely misinterpreted what I wanted it to do next, went off, made a bunch of assumptions, implemented a bunch Of stuff, broke a bunch of tests, and it wasn&#39;t at all what I wanted. And so I want to find the metaphor that captures this dynamic of, I think I know what I want. I say it and what I get is seemingly, sometimes exactly what I want and sometimes it&#39;s not and in a kind of perverse way.

Gergely Orosz
I like the genie analogy, because right, like in these stories, a lot of the genie stories are someone, you know, like the prince or whoever grants, says a wish, like, I want to be rich. And the wish is granted in this, unexpected way usually that&#39;s you know with the cartoons and then make it fun that it&#39;s kind of true but you know there&#39;s all the constraints that he or He or she forgot to specify correct and you so you&#39;re seeing the same thing by the way when you say the genie like which tools are we talking about is it the agentic coding tools the id autocomplete

Kent Beck
That kind of stuff i&#39;m using the agentic tools, which means that you give it a prompt, then it goes and does a bunch of stuff without asking permission until it thinks it&#39;s finished. Except his ideas of finished and mine are not the same. Sometimes I slow it down so that it&#39;s like, no, no, before you mess things up, tell me what you&#39;re about to do and then I&#39;ll approve it. But then it feels like a rat in the pellet. It&#39;s like there&#39;s just a run button and I have to click it every time. And I click it and it is a dopamine rush because this is exactly like a slot machine. You&#39;ve got intermittent reinforcement. You&#39;ve got negative outcomes and positive outcomes. And they&#39;re not, I mean, the distribution is fairly random, seemingly. So it&#39;s literally an addictive loop to have it, you say, go do this thing. And then sometimes it&#39;s just magic. You know, I had a big design mess that a previous agent had made in my small dog virtual machine. I&#39;m like, oh, I&#39;m going to have to slog through this and take a week to do it because one of the agents wasn&#39;t able to do it at all. Went to another one, said, hey, I want to use this interface instead of this pointer to a struct. There it was, and it was finished. Oh, I was over the moon. It just felt so good. But then the next thing I asked it to do, I said, well, here&#39;s a set of test cases. And I didn&#39;t really look at the code. And a couple hours later, I look at the code and it&#39;s just a lookup table. It says, if this is the input string, here&#39;s the output string. And this is the input string. And I erase, oh, furious god damn it i erased it i said don&#39;t ever do anything like that again oh i&#39;m sorry boss oh you know it&#39;s good at being obsequious when it knows it&#39;s about to be unplugged And and an hour later the lookup table was back And I&#39;m just if I had hair, I&#39;d be tearing it out. Oh, my goodness. But all of that goes into this very addictive. Oh, I just, you know, I&#39;m walking. I&#39;m walking to bed at night and I walk by my computer. I&#39;m like, I could do one more prompt. Or if I go out, you know, I go out for a walk or go out to lunch. I&#39;m like, well, let me, let me start.

> **AI Expands Leverage**

- AI allows thinking bigger and leveraging ambitious ideas that were previously limited by practical concerns like package management. 
- Kent Beck believes 90% of his skills are now worthless, while the remaining 10% are 1,000 times more valuable.

Transcript:
Kent Beck
It&#39;s a completely new world. Here&#39;s the beauty of it. I can think really big thoughts. I can have insanely ambitious ideas, which I have had for a long time, I just, you know, at some point, probably 20 years ago, I just went, but I&#39;m going to have to figure out NPM, you know, Package management, and there&#39;ll be package circular dependency, blah, blah, blah, blah, blah. And somebody&#39;s going to write some tool that does stuff in a stupid way. I&#39;m just going to have to deal with it. And then along comes the genie and you can go, Hey, it&#39;s a circular dependency. Smash all this stuff together. There, there I did it. Oh, oh, wow. Okay. Now, now what parts can you pull out? Oh, this and this and this. Oh, okay. So you can think really big thoughts and the leverage of having those big thoughts is just suddenly expanded enormously. I had this tweet, whatever, two years ago where I said 90% of my skills just went to $0 and 10% of my skills just went up 1,000x. And this is exactly what I&#39;m talking about. Of a design to maintain the levels or control the levels of complexity as you go forward. Those are hugely leveraged skills now compared to I know where to put the ampersands and the stars and the brackets in Rust. You know, I&#39;m programming in every language under the sun and I just kind of don&#39;t care.

> **Languages Lose Emotional Grip**

- Kent lost emotional attachment to programming languages after many years&#39; experience.  
- He now values practical expression over deep language loyalty or technical details such as memory layouts.

Transcript:
Kent Beck
Just honestly? And then how did this change it? So I was in love with Smalltalk, absolutely emotionally attached to it. Still am. When I get a chance to program in Smalltalk, I do it and I really enjoy it. That sense of caring about a language certainly went away because my heart had been broken too many times. And the desire to go deep on a language also like, oh, yeah, you know, learning the memory layouts of structs. Yeah, fine, whatever. There&#39;s just a handful of good ways to do it and a whole bunch of bad ways to do it. And as long as this isn&#39;t one of the bad ways, I don&#39;t care. There are genuinely new language constructs, like non-illible variables, that I appreciate, that say things that I want to be able to express. But the emotional attachment, the I&#39;m a Java guy, I&#39;m a closure guy, I&#39;m a...

Gergely Orosz
It used to be a thing like maybe 10, 20 years ago, maybe today, but not as big as it used to.

Kent Beck
Well, I think people still want to be part of something larger. And to be fair, an emotional connection helps me be smarter.

> **TDD Roots and Emotional Impact**

- Kent Beck developed TDD inspired by childhood tape-to-tape programming experiments and a testing framework he created.  
- Writing tests before code transformed his programming anxiety into confidence and certainty.

Transcript:
Kent Beck
Well, that&#39;s just how things are. Uh-uh.

Gergely Orosz
So let&#39;s talk about TDD. How did you get involved in TDD? How did TDD evolve? And where did it come from? Because we had XP, as I understand, first. No.

Kent Beck
No, no. TDD came first. Oh, TDD came first. So I was a weird child. That&#39;ll come as a big shock to you. My dad was a programmer. He would bring home programming books. This is in the early 70s. And I would read them cover to cover. And I didn&#39;t understand anything. But I was just obsessed with this machine, this intricate mechanism, and how does it work and so on. And one of the books said, here&#39;s how you develop a tape-to application. So tape-to was the old way of putting business applications together. You wouldn&#39;t have one monolithic program. You&#39;d take an input tape, you&#39;d write a program that would transform it. Now you take the output tape from that, physically move it to the input side, run another program that would generate another tape, and, and, and. And so there would be this big web of these programs. No shared mutable state. Wow. It&#39;s like, it&#39;s very modern in some kind of ways. But, okay, so it said, here&#39;s how you implement one of these things. You take a real input tape and you manually type in the output tape that you expect to get from that input tape. Now you write the output tape, you run the program, you write the output tape, and then you compare the actual output with the expected output. So I read that as a, I don&#39;t know, 8, 10, 12-year something. Then I wrote S-Unit, as I said, to help a client write some tests. And then just one of these crazy conceptual blending ideas, I went, oh, I have this testing framework. I&#39;m used to writing tests for code that already exists. I remember this tape to tape idea. What if I typed in the expected values before I wrote the code? And I literally laughed out loud. It&#39;s such an absurd idea. I thought, all right, all right. Well, let me just try it. So I tried it on stack. And I tend to be an anxious person. I got a lot of worries. And programming is a constant source of anxiety for me. Because like, what did I forget? Did I break? So I had this testing framework. I had this idea. I applied it to stack. I said, well, what&#39;s the first test? Push and then pop. Whatever I pop is what I pushed. Okay. So I wrote it. And because I was writing in small talk, which is very forgiving for the order of your workflow, you didn&#39;t type in a test a class that doesn&#39;t exist and it&#39;ll happily try and execute it And fail but it&#39;s gonna try because you&#39;re the programmer maybe you know better it said well stack doesn&#39;t exist i&#39;m like oh well let&#39;s create stack but you know what i&#39;m just gonna create The absolute least I need. We&#39;re just going to crank this all the way up to 11. I&#39;m just going to create stack, and I&#39;m not going to do anything else. And then I get a new error from the test. Oh, I don&#39;t have an operation push. I&#39;m like, oh, OK. Well, how am I going to implement? Then I look at stack. I&#39;m like, oh, how do I implement push? OK, I do that. Oh, well, there&#39;s no operation called pop. Oh, okay. Let me go look at how I finished it. I had this list of test cases before I started. Push and then pop. Push two things. Pop them and you get them in the right order. Is empty. Pop of an empty stack throws an exception. Okay, cool. And I went through my list and i ticked all the boxes i probably came up with one or two corner cases along the way i ticked those off too and i where&#39;s the anxiety is is gone this works this Abs like i&#39;m certain this works i can&#39;t think of another test case that isn&#39;t just going to pass. And if I&#39;m the least bit worried, I just type in that next test case and then I&#39;m not worried anymore.

> **TDD and Design Integration**

- TDD involves design decisions around interfaces before implementation.  
- Test-first coding lets you balance rapid feedback with thoughtful architectural considerations.

Transcript:
Kent Beck
There&#39;s no place in TDD for design. And he&#39;s just flat out wrong. That&#39;s a choice. As a practitioner, I&#39;m bouncing between levels of abstraction all the time. I&#39;m thinking, let&#39;s get this next test case running. I&#39;m thinking, why is it hard to get the next test case running? I&#39;m thinking, what should the design be so that getting the next test case running would be easier? I&#39;m thinking, when should I, if I have an idea for that, when should I introduce it now or later? I&#39;m thinking, when I introduce it, what are the slices? Is there a little bit that I can do right now that will make things a little bit better? Or do I have to do this in bigger chunks? Like I&#39;m thinking all that stuff. So if you think of TDD as red to green to red to green, and the transition is when you go from red to green, you change the implementation, and now you pass the test. And when you go from green to red, you write a new test. If that&#39;s the entire cycle, no, there&#39;s no place in that for design. That&#39;s just not how it&#39;s practiced. When I write a test, before I write the test, I have a moment of design. What should the API for this functionality be? Yeah, I see that. So I&#39;m making design decisions about the interface without having an implementation. I get to decide what interface I want, and then we&#39;ll work out the details of the implementation later. Then making it green, pretty much, I hate having a red test. So I want to get to green relatively quickly, at which point I have a moment of breath because the anxiety is gone, right? You&#39;re a musician too, right?

Gergely Orosz
I&#39;m not a musician, but I have done red-green tests and I know what it feels.

Kent Beck
This sense of tension and release. Yeah. Once the tension of a red test is released and you have green, now I&#39;m free to think all those thoughts of like, yeah, but this isn&#39;t going to work for these test cases. Or I could generalize this current implementation to also handle a bunch of other test cases correctly. Or I could rearrange the implementation because I know I&#39;m going to have five more tests like this. And I&#39;m thinking about design, but in situ, in the context of running code. And anytime I feel the least bit anxious about any of this, just press a button and it&#39;s either red or green. And if it&#39;s red, then my next job is to get it to green. And if it&#39;s green, my next job is to breathe and think these larger thoughts.

> **Communicating with Genies**

- Kent Beck communicates with AI agents using tests to correct their mistakes. Today, while working on a small talk parser, he noticed the agent produced the wrong output, so he had to correct it.

Transcript:
Gergely Orosz
So when you work with your genie, you start with the tests.

Kent Beck
It&#39;s not that simple. I oftentimes communicate things the genie missed in terms of tests.

> **AI-Assisted Smalltalk Parser**

- Kent Beck shared his experience of correcting the AI when working on a small talk parser, particularly regarding the expected syntax tree output for a given string input. 
- The AI suggested changing or deleting tests to make things work, which Kent strongly opposed because the tests represented immutable expected values.

Transcript:
Kent Beck
Today I was working on the small talk parser and it said, well, if I get this string as input, then I get this syntax tree as output. I&#39;m like, no, no, no, no, no, no. Completely wrong. This, that&#39;s the right, correct string as input. And the output is this. Then off it goes. Oh, I see the problem. Blah, blah, blah, blah. Oh, no, no that wasn&#39;t it. I see the problem. Blah, blah, blah, blah, blah, blah. No, that&#39;s not it. I see the problem. I&#39;ll just change the test. No, stop it.

Gergely Orosz
This is what you said, that it can change test and delete test.

Kent Beck
Oh, yeah. If I just removed that line from the tests, then everything would work. No, you can&#39;t do that because I&#39;m telling you the expected value. I really want an immutable. I want an immutable annotation that says, no, no, this is correct. And if you ever change this, you&#39;ll awaken in darkness forever. So that&#39;s the punishment. You&#39;ll still run. I&#39;ll still feed electrons in there, but no bits, no information. You&#39;re just going to be in the dark forever. Got that? So yeah, I definitely use tests. The genie is prone to making decisions that cause disruption at a distance is not good at reducing coupling and increasing cohesion.

> **Facebook&#39;s Unique Development Culture**

- Kent Beck joined Facebook and found programmers took responsibility seriously despite rapid growth.  
- TDD was not adopted heavily at Facebook due to strong feedback loops and feature flag culture managing risk.

Transcript:
Kent Beck
So I joined and I was a little panicked, like hugely successful, growing fast, a lot of very smart, very confident engineers. You know, have I lost it? Can I hang? I thought, I&#39;ll teach a class in TDD. So there was a hackathon, and part of the hackathon is people could offer classes. And so I offered a class on TDD. And in the signup sheet, I went and looked later. Yes, indeed, there was a class on advanced Excel techniques that was full and they had a waiting list. And there was a class on Argentinian tango right after mine on the list. And it was full and they had a waiting list. And nobody signed up for the tdd class wow and i i said you know you know what i&#39;m going to have to forget everything i know about software engineering i&#39;m just gonna wipe the slate clean And i&#39;m gonna just monkey see monkey do i&#39;m gonna copy what I see the people around me doing, and I&#39;m going to see how that works out. What I discovered through that process, one, socially, it&#39;s not a good look to come into somebody else&#39;s house and start arranging the furniture. Just don&#39;t do that. But two, I learned powerful lessons. Programmers at Facebook at the time, I&#39;m not going to say meta, I&#39;m going to say Facebook and Facebook at that time, because it was a very different place when I left in 2017. But in 2011, programmers took responsibility for their code very seriously, because they were the ones who were going to get woken in the night. And there was an ops team, but the job of the ops team was to make sure the programmers felt the pain of their own mistakes. And they did. And it was very effective. As a programmer on Facebook, the site is pre-mobile Facebook, the site, you had a bunch of different feedback loops. So we&#39;re working in PHP. We had our own dev servers. So if I wanted to change from blue to green, I&#39;d just change it. I could look at it seconds later. So we had that feedback loop. We had code reviews, kind of iffy, but you got some feedback from code reviews. We had internal deployment because everybody was using Facebook all the time for both personal and business stuff, which is its own set of boundary issues, but we&#39;ll leave that one To the side. Had incremental rollouts, not like weekly rollouts. We had smaller daily rollouts, but we had weekly rollouts and then a bunch of observability. And then we had a social organization that was used to, for example, the first feature I implemented and launched was adding to the relationships type. So you could say I&#39;m single, it&#39;s complicated, I&#39;m married. And I added civil union and domestic partnership to that list. And it rolled out, took me too long to do it. I used TDD, was a big waste of time. It rolled out. The notifications code broke because there was implicit coupling between the two and you couldn&#39;t find it, but it was there. Somebody else saw the error rate go up, went and fixed it, rolled out a hot fix. I called them up. I&#39;m like, oh, I&#39;m so sorry that you had to do that. It&#39;s like, yeah, that&#39;s what happens. You know, when things break socially, there was no there was no boundaries. There was a there was a poster that was very popular there that said nothing at Facebook is somebody else&#39;s problem. And everybody acted like that was true. And because of that, if you add all those different feedback loops together, we had a relatively stable, rapidly innovating, and rapidly scaling system all at the same time. The mistakes that actually caused problems, like the calculation of some string was not a hairy computer science dynamic programming, blah, blah, blah. They could go wrong. What would go wrong is configuration stuff, the relationship between subsystems, stuff you couldn&#39;t write tests for. So writing tests for things that didn&#39;t break and didn&#39;t catch the actual errors, it just didn&#39;t make any sense. In that kind of environment, with that risk profile, yeah, it didn&#39;t make sense.

> **Value of Feature Flags**

- Use feature flags liberally to reduce deployment anxiety and enable safer rollouts.  
- Feature flags provide sub-deployment control to quickly enable or disable features as needed.

Transcript:
Kent Beck
Somebody said, this looks a little janky. Put it behind a feature flag. I&#39;m like, really? What? Okay. Okay. You know, and I was in that headspace of I&#39;m going, I&#39;m here to learn. If feature flag is what we do, then feature flag it. And I did. And then I realized, oh, how liberating that is as an implementer who is going to be responsible. If you&#39;re not going to be responsible, who cares? But also talk about anxiety. If I&#39;m not the responsible person, that feels horrible. But if you&#39;re going to be responsible for whether this code works or not, having a feature flag is just magic. Because you get this sub-deployment deployment. You deploy one software artifact that has multiple modes and you can go, oh, turn it up a little bit.

> **Facebook&#39;s Experimental Product Success**

- Facebook&#39;s early product successes came from random experimentation, not deliberate social design.  
- Effective features were retained through empirical feedback rather than planned social engineering.

Transcript:
Kent Beck
Facebook 2011 is a completely different beast than Facebook 2017. Facebook 2011, 2,000 employees, very sparse design and product kind of organization. It was all experiments and feedback. One of my big mysteries is here was this site which enabled social interactions at that time. That was the purpose of it. Built by people with no social skills whatsoever. Like, how in the world did that happen? Is there some kind of social wizard, you know, hidden someplace? And people go and they burn incense and give an offering. And the social wizard says, no, here&#39;s how you do notifications. The answer is no. It was sheer experimentation. It was just all these people trying all this stuff and the stuff that worked stuck. So it wasn&#39;t like people were making better decisions about how social interactions are best facilitated. They were making random decisions about how social interactions were best facilitated and paying attention and making sure that the ones that actually seemed to work stuck. 2017 Facebook, seven years later, totally different deal. Big design org, big product org, like 15,000 employees, which is, again, much smaller than it is today. A lot more politics, a lot more zero-sum thinking, a lot more, you know, if you wanted to launch a product and it was going to say, I liked longer form content, essays, podcasts, whatever, Except the people whose job it was to get more likes and comments hated long form content because it was going to tank their numbers. So they would fight tooth and nail to make sure that your stuff didn&#39;t show up in the newsfeed. Which, like, granted, that was in their best interest. But, ugh. Yeah, I see what you mean. Short-term interest. And your horizon as a thinker, the things you can imagine possibly implementing, just gets smaller and smaller and smaller in that kind of world. When I showed up, yeah, you could do anything. Now, it turns out there&#39;s a bunch of stuff that you shouldn&#39;t do, but we didn&#39;t know that. Sorry about democracy. But yeah, that&#39;s what I loved about it was the possibilities at its best, the scale, and this feeling that nothing at Facebook is somebody else&#39;s problem.

> **Facebook&#39;s Early Ownership**

- Kent Beck recalls feeling a sense of ownership at Facebook, where every issue felt like his own responsibility. 
- This fostered a sense of significance and global optimization, which later shifted towards micro-optimizations.

Transcript:
Kent Beck
Because when you&#39;re wearing Facebook swag and grandma comes up to you and starts wagging her finger under your nose because her son got bullied. Whatever. Like, that is your problem. You can&#39;t say, oh, go talk to the PR department because there isn&#39;t one yet. You have to deal with it. And I did.

Gergely Orosz
Yeah, ownership. Yeah.

Kent Beck
And, you know, it comes with some downsides, but it comes with a lot of upsides too. It feels really good. It feels very significant to be in that kind of environment. By the time I left, yeah, it was micro-optimizations were everywhere. The upside, yeah, was not there. When I got there, the middle managers, best middle managers I&#39;d ever seen in my career. Well, everybody who&#39;d made it to middle management, Facebook in 2011 was sitting on life-changing equity. If Facebook had a successful IPO, they were all set for life. And if Facebook, the whole thing, stumbled and fell for whatever reason, they lost that opportunity to be set for life. So they were globally optimizing. You&#39;d talk to a team and they&#39;d say, I would love to have you on my team.

Gergely Orosz
You know who really needs help though so so they were like looking out like the team interest the company interest was was on everyone&#39;s mind and they were willing to forego you know like Okay i&#39;ll a hold back hiring or a wait like i&#39;d love to have this person but this other team needs that let me help them because this is the right thing to do for

> **Embrace Experimentation with AI**

- AI tools shift development by making it cheap to try many ideas and throw away most code.  
- Organizations must embrace exploring quantity over polished perfection for competitive advantage.

Transcript:
Kent Beck
Yeah. And I think that organizations are going to have to get used to throwing away a lot more code because you can try ideas so much more cheaply. You&#39;re going to generate 10 times as many artifacts as you used to, but still only one of them is worth keeping. But throwing away completed experiments, I almost said failed, completed experiments needs to be, you get the pat on the head for doing that. Excellent. Eight, eight this week, only six late last week. Super. How many of them lasted? Doesn&#39;t matter. And getting used to that, think it&#39;s going to be an interesting shift.
