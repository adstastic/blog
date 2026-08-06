---
title: "AI-assisted Coding for Teams That Can&#39;t Get Away With Vibes"
date: 2025-06-22
slug: "ai-assisted-coding-for-teams-that-can-t-get-away-with-vibes"
tags:
  - quote
ref: https://blog.nilenso.com/blog/2025/05/29/ai-assisted-coding/
---

Quoting [Nilenso](https://blog.nilenso.com/blog/2025/05/29/ai-assisted-coding/):

> AI tools are tricky to use. Hold it wrong, and you can generate underwhelming results, worse still, slow down your velocity by drowning your project in slop and technical debt.

> To make AI good, get good yourself. AI is a multiplier. If you are a small coefficient, you won’t see much gain. If you are a negative coefficient, expect negative gains.

> the best and most experienced engineers are able to extract a lot more out of AI tools. There are several reasons for this:

•   They are extremely good at communicating technical ideas.
•   They have a keen calibration and feel for what leads to a good system and can steer LLMs accordingly, i.e., they have what I like to call “the mechanic’s touch”.
•   They have strong fundamentals, so they immediately get up to speed with new tools and systems where knowledge, not skill is the bottleneck.
•   AI is still sensitive to language and style and will often mirror the tastes and sensibilities of the prompter. Highly skilled engineers have really sharpened taste and instinct for what works and what doesn’t.

> embody the care of a craftperson. At the end of the day, you should produce artifacts you are proud of, even if the AI assisted in making it. This has translated well into the output I am seeing from these systems.

> A technique that has worked well for us is *metaprompting*. I prompt the model with a simple task and ask it to help surface tradeoffs and edge cases. Then I turn it into a tech spec and hand it off to another LLM agent to execute. Even the “better prompt” I shared above is a result of asking the AI to come up with a good prompt. From my experience, models have become good at prompting themselves.

> The mechanics of what works for these tools are in flux, but one robust principle is to really work on yourself to be a good engineer. Your habits will quickly pass on to the AI systems you work with.

> software engineering is the art and science of maintaining a large body of well-defined mental models that achieve a business or economic need. Much of the work is around crafting and curating these large, complex sociotechnical systems, and code is just one representation of these systems.

Until AI is good enough to engulf this whole sociotechnical system and expel out all the humans cultivating it, it has to participate and benefit from this very system. In simpler words: AI thrives far, far better in an environment in which a human would also thrive. Which means your team’s software fundamentals should be strong.

> A system in which AI thrives is one with markers of a high quality team and codebase. These are:

•   Good test coverage, with *useful* assertions
•   Automated linting, formatting and test checks before code merges
•   Continuous integration and deployment
•   Well documented changes, tech specs, ADRs with good commit messages
•   Consistent styles and patterns, enforced through a formatter
•   Simple, concise, well-organised code
•   Clearly defined features, broken down into multiple small story cards

> the messier codebase was as confusing for the AI as it would be for a human. There were mixed signals about the right way to do things.

> Do not try to save credits and cost by using a worse model. The goodness of a good model compounds.

> The effectiveness of AI-assisted coding is strongly dependent on how skillfully you can provide the right context to the LLM.

> LLMs can get distracted and fall into rabbitholes if given irrelevant or a cluttered context. Focus its attention by only @-mentioning files that are relevant and linking only to documentation that helps the task.

> AI works better the more specific you are. Remember, you can also use the AI to reduce the tedium of making your prompts better written and more specific. Reasoning models are great at this!

> Supply tech specs and relevant documentation about the product and feature. Don’t just ask it to write code without broader context of the product. Also feed it documentation on how to use the libraries you are using.

> break down the feature into “planning” and “execution” stages.

> Do not take AI suggestions for granted. Ask it to justify its choices, present alternatives and think about advantages and drawbacks.

> Use AI to debug errors in its generation. Always paste the error context most relevant for the LLM to help it understand the issue (I prefer to delineate the error logs or output in a separate XML tag).

> Explain what you have tried, and additional observations to help the model generate correct hypotheses and eliminate bad ones. Provide lots of context.

> LLMs are an infinitely patient teacher with massive world knowledge (and more recently, ability to research effectively). Aggressively use them to learn things and demystify any new code or stack. Relentlessly dig. Figure out the best practices. Ensure you are learning correctly by getting the LLM to cite high quality sources.

> Create lots of detailed documentation easily by feeding codebases to the LLM.

> LLMs greatly reduce the cost of creating lubricants for all the minor friction points that teams run into on a daily basis.

> Use LLMs to explain a change that you don’t fully understand as a reviewer. Ask it for clarification, and then ask the implementer after gathering the necessary context.

> It’s less valuable to spend too much time looking for and building sophisticated abstractions. DRY is useful for ensuring patterns in the code don’t go out of sync, but there are costs to implementing and maintaining an abstraction to handle changing requirements. LLMs make some repetition palatable and allow you to wait a bit more and avoid premature abstraction.

Redoing work is now extremely cheap. Code in the small is less important than structural patterns and organisation of the code in the large. You can also build lots of prototypes to test an idea out. For this, vibe-coding is great, as long as the prototype is thrown away and rewritten properly later.

Working with LLMs also lets you take advantage of the generator-verifier gap. Often it’s easier to verify and fix things than it is to produce them from scratch. This reduces activation energy to try new things.

Tests are non-negotiable, and AI removes all excuses to not write them because of how fast they can belt them out. But always review the assertions!
