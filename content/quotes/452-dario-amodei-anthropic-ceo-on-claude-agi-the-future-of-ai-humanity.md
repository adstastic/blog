---
title: "#452 – Dario Amodei: Anthropic CEO on Claude, AGI &amp; the Future of AI &amp; Humanity"
date: 2025-08-09
slug: "452-dario-amodei-anthropic-ceo-on-claude-agi-the-future-of-ai-humanity"
tags:
  - quote
ref: https://share.snipd.com/episode/4e6e3023-e279-4b22-8368-216720a3775a
---

Quoting [Lex Fridman Podcast](https://share.snipd.com/episode/4e6e3023-e279-4b22-8368-216720a3775a):

> **Scaling Laws**  

- Scaling laws suggest linearly scaling network size, training time, and data improves model performance.
- This observation has held true across various AI domains, like speech and language, despite initial skepticism.

Transcript:
Lex Fridman
Start with the big idea of scaling laws and the scaling hypothesis. What is it? What is its history? And where do we stand today?

Dario Amodei
So I can only describe it as it relates to kind of my own experience, but I&#39;ve been in the AI field for about 10 years. And it was something I noticed very early on. So I first joined the AI world when I was working at Baidu with Andrew Ng in late 2014, which is almost exactly 10 years ago now. And the first thing we worked on was speech recognition systems. And in those days, I think deep learning was a new thing. It had made lots of progress, but everyone was always saying, we don&#39;t have the algorithms we need to succeed. We&#39;re only matching a tiny, tiny fraction. There&#39;s so much we need to kind of discover algorithmically. We haven&#39;t found the picture of how to match the human brain. And in some ways, it was fortunate. I was kind of, you can have almost beginner&#39;s luck, right? I was like a newcomer to the field. And I looked at the neural net that we were using for speech, the recurrent neural networks. And I said, I don&#39;t know, what if you make them bigger and give them more layers? And what if you scale up the data along with this, right? I just saw these as like independent dials that you could turn. And I noticed that the model started to do better and better as you gave them more data, as you made the models larger, as you trained them for longer. And I didn&#39;t measure things precisely in those days, but along with colleagues, we very much got the informal sense that the more data and the more compute and the more training you put Into these models, the better they perform. And so initially my thinking was, hey, maybe that is just true for speech recognition systems, right? Maybe that&#39;s just one particular quirk, one particular area. I think it wasn&#39;t until 2017 when I first saw the results from GPT-1 that it clicked for me that language is probably the area in which we can do this. We can get trillions of words of language data. We can train on them. And the models we were trained in those days were tiny. You could train them on one to eight GPUs, whereas now we train jobs on tens of thousands, soon going to hundreds of thousands of GPUs. And so when I saw those two things together, and there were a few people like Ilya Suitskiver, who you&#39;ve interviewed, who had somewhat similar views, right? He might&#39;ve been the first one, although I think a few people came to similar views around the same time, right? There was, you know, Rich Sutton&#39;s Bitter Lesson. There was Gorin wrote about the scaling hypothesis. But I think somewhere between 2014 and 2017 was when it really clicked for me, when I really got conviction that, hey, we&#39;re going to be able to do these incredibly wide cognitive tasks If we just scale up the models. And at every stage of scaling, there are always arguments. And when I first heard them, honestly, I thought probably I&#39;m the one who&#39;s wrong. And all these experts in the field are right. They know the situation better than I do, right? There&#39;s the Chomsky argument about like, you can get syntactics, but you can&#39;t get semantics. There was this idea, oh, you can make a sentence make sense, but you can&#39;t make a paragraph make sense. The latest one we have today is, you know, we&#39;re going to run out of data or the data isn&#39;t high quality enough or models can&#39;t reason. And each time, every time we manage to either find a way around or scaling just is the way around. Sometimes it&#39;s one, sometimes it&#39;s the other. And so I&#39;m now at this point, I still think, you know, it&#39;s always quite uncertain. We have nothing but inductive inference to tell us that the next few years are going to be like the last 10 years. But I&#39;ve seen the movie enough times. I&#39;ve seen the story happen for enough times to really believe that probably the scaling is going to continue and that there&#39;s some magic to it that we haven&#39;t really explained on a theoretical Basis yet.

> **Why Bigger Networks Are Better**  

- Larger networks capture simpler patterns first, then progressively learn more complex ones with increased capacity.
- This is analogous to 1/f noise, where larger scales reveal finer details in a distribution.

Transcript:
Lex Fridman
Of course, the scaling here is bigger networks, bigger data, bigger compute. Yes.

Dario Amodei
In particular, linear scaling up of bigger networks, bigger training times, and more data. So all of these things, almost like a chemical reaction, you know, you have three ingredients in the chemical reaction, and you need to linearly scale up the three ingredients. If you scale up one, not the others, you run out of the other reagents and the reaction stops. But if you scale up everything in series, then the reaction can proceed.

> **Hierarchy of Concepts**

- Larger networks capture simple correlations and a long tail of complex patterns, improving prediction and performance.
- Dario Amodei believes there&#39;s no ceiling below human-level understanding, suggesting continued scaling will reach human capabilities.

Transcript:
Dario Amodei
We have common expressions and less common expressions. We have ideas, cliches that are expressed frequently, and we have novel ideas. And that process has developed, has evolved with humans over millions of years. And so the guess, and this is pure speculation, would be that there&#39;s some kind of long tail distribution of the distribution of these ideas. So there&#39;s the long tail, but also there&#39;s the height of the hierarchy of concepts that you&#39;re building up.

Lex Fridman
So the bigger the network, presumably you have a higher capacity to... Exactly. If you have a small network, you only get the common stuff, right?

Dario Amodei
If I take a tiny neural network, it&#39;s very good at understanding that, you know, a sentence has to have, you know, verb, adjective, noun, right? But it&#39;s terrible at deciding what those verb, adjective, and noun should be and whether they should make sense. If I make it just a little bigger, it gets good at that. Then suddenly it&#39;s good at the sentences, but it&#39;s not good at the paragraphs. And so these rarer and more complex patterns get picked up as I add more capacity to the network.

Lex Fridman
Well, the natural question then is, what&#39;s the ceiling of this? How complicated and complex is the real world? How much of this stuff is there to learn? I don&#39;t think any of us knows the answer to that question.

Dario Amodei
My strong instinct would be that there&#39;s no ceiling below the level of humans, right? We humans are able to understand these various patterns. And so that makes me think that if we continue to, you know, scale up these models to kind of develop new methods for training them and scaling them up, that will

> **Limits of Scaling**  

- AI progress may be limited by data quality and availability, as internet data has limitations.
-  Synthetic data generation or new training methods like chain-of-thought reasoning may overcome this.

Transcript:
Lex Fridman
What do you think would be the reason? Is it compute limited, data limited? Is it something else, idea limited?

Dario Amodei
So a few things. Now we&#39;re talking about hitting the limit before we get to the level of humans and the skill of humans. So I think one that&#39;s popular today, and I think could be a limit that we run into, like most of the limits, I would bet against it, but it&#39;s definitely possible, is we simply run out of data. There&#39;s only so much data on the internet. And there&#39;s issues with the quality of the data, right? You can get hundreds of trillions of words on the internet, but a lot of it is repetitive or it&#39;s search engine, you know, search engine optimization drivel, or maybe in the future it&#39;ll Even be text generated by AIs itself. And so I think there are limits to what can be produced in this way. That said, we, and I would guess other companies are working on ways to make data synthetic where you can, you know, you can use the model to generate more data of the type that you have, That you have already, or even generate data from scratch. If you think about what was done with DeepMind&#39;s AlphaGo Zero, they managed to get a bot all the way from, you know, no ability to play Go whatsoever to above human level just by playing Against itself. There was no example data from humans required in the AlphaGo Zero version of it. The other direction, of course, is these reasoning models that do chain of thought and stop to think and reflect on their own thinking. In a way, that&#39;s another kind of synthetic data coupled with reinforcement learning. So my guess is with one of those methods, we&#39;ll get around the data limitation, or there may be other sources of data that are available. We could just observe that even if there&#39;s no problem with data, as we start to scale models up, they just stop getting better. It seemed to be our reliable observation that they&#39;ve gotten better. That could just stop at some point for a reason we don&#39;t understand. The answer could be that we need to, you know, we need to invent some new architecture. It&#39;s been there have been problems in the past with, say, numerical stability of models where it looked like things were were leveling off. But but actually, you know, when we found the right unblocker, they didn&#39;t end up doing so. So perhaps there&#39;s some new optimization method or some new technique we need to unblock things. I&#39;ve seen no evidence of that so far, but if things were to slow down, that perhaps could

> **Golden Gate Claude**  

- Anthropic released a demo model fixated on the Golden Gate Bridge due to an activated feature.
- This demonstrated how specific activations influence model behavior and create unique personalities.

Transcript:
Lex Fridman
Golden Gate Bridge. Or, you know. It would masterfully change topic to the Golden Gate Bridge and integrate it. There was also a sadness to it, to the focus it had on the Golden Gate Bridge. I think people quickly fell in love with it, I think. So people already miss it because it was taken down, I think, after a day.

Dario Amodei
Somehow these interventions on the model where you kind of adjust its behavior somehow emotionally made it seem more human than any other version of the model would seem. It&#39;s a strong personality, strong identity. It has a strong personality. It has these kind of like obsessive interests. You know, we can all think of someone who&#39;s like obsessed

> **Claude&#39;s Perceived Intelligence**  

- User complaints about Claude getting dumber are likely due to unchanging model weights and psychological effects.
-  Subtle prompt changes or A/B testing might cause perceived differences, but the core model remains static.

Transcript:
Lex Fridman
Know, there&#39;s just this fascinating, to me at least, it&#39;s a psychological social phenomenon where people report that Claude has gotten dumber for them over time. And so the question is, does the user complaint about the dumbing down of Claude 3-5 Sonnet hold any water? So are these anecdotal reports a kind of social phenomena or is there any cases where Claude would get dumber?

Dario Amodei
So this actually doesn&#39;t apply. This isn&#39;t just about Claude. I believe I&#39;ve seen these complaints for every foundation model produced by a major company. People said this about GPT-4. They said it about GPT-4 Turbo. So a couple things. One, the actual weights of the model, right? The actual brain of the model, that does not change unless we introduce a new model. There are just a number of reasons why it would not make sense practically to be randomly substituting in new versions of the model. It&#39;s difficult from an inference perspective, and it&#39;s actually hard to control all the consequences of changing the weights of the model. Let&#39;s say you wanted to fine-tune the model to be like, I don&#39;t know, to say certainly less, which an old version of Sonnet used to do. You actually end up changing a hundred things as well. So we have a whole process for it, and we have a whole process for modifying the model. We do a bunch of testing on it. We do a bunch of user testing in early customers. So we both have never changed the weights of the model without telling anyone. And certainly in the current setup, it would not make sense to do that. Now, there are a couple of things that we do occasionally do. One is sometimes we run A-B tests, but those are typically very close to when a model is being released and for a very small fraction of time. So, you know, like the day before the new Sonnet 3.5, I agree, we should have had a better name. It&#39;s clunky to refer to it. There were some comments from people that like it&#39;s gotten a lot better and that&#39;s because, you know, a fraction were exposed to an A-B test for those one or two days. The other is that occasionally the system prompt will change. The system prompt can have some effects, although it&#39;s unlikely to dumb down models. It&#39;s unlikely to make them dumber. And we&#39;ve seen that while these two things, which I&#39;m listing to be very complete, happen relatively, happen quite infrequently. The complaints about, for us and for other model companies about the model change, the model isn&#39;t good at this, the model got more censored, the model was dumbed down, those complaints Are constant. And so I don&#39;t want to say like people are imagining it or anything, but like the models are for the most part, not changing. Um, if I were to offer a theory, um, I, I think it actually relates to one of the things I said before, which is that models have many are very complex and have many aspects to them. And so often, you know, if I, if I, if I, if I asked the model a question, you know, if I&#39;m like, if I&#39;m like, do X versus can you do Task X, the model might respond in different ways. And so there are all kinds of subtle things that you can change about the way you interact with the model that can give you very different results. To be clear, this itself is like a failing by us and by the other model providers that the models are just often sensitive to like small changes in wording. It&#39;s yet another way in which the science of how these models work is very poorly developed. And so, you know, if I go to sleep one night and I was like talking to the model in a certain way and I like slightly change the phrasing of how I talk to the model, you know, I could get different Results. So that&#39;s one possible way. The other thing is, man, it&#39;s just hard to quantify this stuff. It&#39;s hard to quantify this stuff. I think people are very excited by new models when they come out. And then as time goes on, they become very aware of the limitations. So that may be another effect. But that&#39;s all a very long-winded way of saying, for the most part, with some fairly narrow exceptions, the models are not changing. I think there is a psychological effect.

> **AI and Catastrophic Misuse**

- AI could break the correlation between smart, well-educated people and those who want to do horrific things. 
- Preventing catastrophic misuse should be the number one priority.

Transcript:
Dario Amodei
Like these are the number one priority to prevent. And here, I would just make a simple observation, which is that the models, if I look today at people who have done really bad things in the world, I think actually humanity has been protected By the fact that the overlap between really smart, well-educated people and people who want to do really horrific things has generally been small. Like, you know, let&#39;s say I&#39;m someone who, you know, I have a PhD in this field. I have a well-paying job. There&#39;s so much to lose. Why do I want to like, you know, even assuming I&#39;m completely evil, which most people are not, Why would such a person risk their life, risk their legacy, their reputation to do something Truly, truly evil? If we had a lot more people like that, the world would be a much more dangerous place. And so my worry is that by being a much more intelligent agent, AI could break that correlation. And so I do have serious worries about that. I believe we can prevent those worries.
