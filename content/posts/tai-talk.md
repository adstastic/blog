---
title: "The weird intern in your terminal"
date: 2025-07-24T19:46:28+09:00
draft: false
tags: [ai, talk, tokyo]
slug: tai-talk
---

I gave a talk at [Tokyo AI #10](https://lu.ma/1awrd4sx) exploring how you can make Claude Code and other AI tools into coworkers.
Below are the slides and my presenter notes augmented with a transcript from memory. References are at the end.

## Slides

![Title slide](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎001.jpeg)

Thanks Ilya for building this wonderful community, organising these events, and inviting me to speak.  
Hi everyone, I'm Adi, and I'm here to talk to you about the [weird intern](https://simonwillison.net/2024/Sep/10/software-misadventures/#the-weird-intern) in your terminal.

![Claude code](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎003.jpeg)

This talk leans heavily on Claude Code, but the tips, principles, and ideas apply not just to other Terminal agents and LLM tools, but to working with AI in general.  
So even if you’re not a Claude Code power user, I think you’ll get something out of it.

![What's a weird intern?](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎004.jpeg)

'Weird intern' is a wonderful phrase coined by [Simon Willison](https://x.com/simonw) (who runs an [excellent blog](https://simonwillison.net) on AI and Software engineering) to describe the experience of working with an LLM.  
These are some of the traits of your weird intern.

![Examples of shouting at claude code](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎005.jpeg)

Shouting at them can be fun, but doesn’t really help.  

![How to manage your intern](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎006.jpeg)

So how do you manage your intern?

![Context](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎007.jpeg)

Lets talk about context.  
LLMs are next token predictors, but I think the metaphor of storyteller captures the experience much better.  
The context window is fragments of a story being told. The LLM continues the story.  
Everything in the context affects the story, and anything unnecessary to the goal deviates the story from the goal.

![Context engineering diagram](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎008.jpeg)
    
This isn't new. 
RAG, prompt engineering, history, memory, structured outputs, etc - all this [context engineering](https://x.com/dexhorthy/status/1933283008863482067).  
Since the beginning, we've been trying to optimise the context to get the best work out an LLM.

![The anatomy of context](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎009.jpeg)

Let’s look at what’s in a context window

![Claude-trace visualisation page 1](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎010.jpeg)

There's a wonderful tool called [claude-trace](https://github.com/badlogic/lemmy/tree/main/apps/claude-trace), I used it to inspect the raw data of my claude code sessions.  
This is a visualisation of the context window for one of those sessions.  
We're going to walk through this context window for the first message-response pair.  
So we start here with the system prompt, then we have tool definitions, starting with the built-ins from Anthropic.  
As we go through this, pay attention to how much space visually the different blocks are taking up.

![Claude-trace visualisation page 2](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎011.jpeg)

More tool definitions

![Claude-trace visualisation page 3](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎012.jpeg)

Now we get to MCP tools

![Claude-trace visualisation page 4](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎013.jpeg)

More MCPs

![Claude-trace visualisation page 5](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎014.jpeg)

And more

![Claude-trace visualisation page 6](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎015.jpeg)

And more

![Claude-trace visualisation page 7](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎016.jpeg)

And more

![Claude-trace visualisation page 8](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎017.jpeg)

And even more.
Then finally my prompt, in the green in the middle there, followed by Claude’s response in blue.  
This is all just me opening Claude Code, sending the first message, and getting the reply.  

![full context window visualisation](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎018.jpeg)

I built a tool that visualises the context window at the time of compaction.  
Compaction, if you don’t know, is starting a fresh context with the summary of the previous context window.  
<explain the legend>  
As you can see, a huge amount of this conversation happened before my first message was sent, with the purple system prompt, and red and pink tool definitions  
Keeping the context clean is really important to the reliability of your agent.

![Keep the context clean](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎019.jpeg)

Everything else in this talk is about keeping the context clean.  

![MCPs](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎020.jpeg)

MCPs are good, but as we just saw, they can be very verbose.  
Add them at the project level, not globally, so that the context is used only where its relevant.  
Add them sparingly. The previous example had 7 MCPs, I think 2-3 is probably the max.  
Examine them with tools like claude-trace or my thing (which I’ll publish soon).  
A lot of third party MCPs are very documentation and tool heavy - they should be, they're trying to cover an entire API surface.  
If you know the subset of those tools you actually need, write your own leaner version.  
Or...

![CLIs](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎021.jpeg)

CLIs are even better. Both you and Claude can use them.  
Put the docs in the help flag or a manpage, Claude looks up them when needed.  
Models are generally pretty good at CLIs and you can have Claude summarise instructions for frequently used commands into CLAUDE.md for efficiency.

![Example: git & gh](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎022.jpeg)

`git` and `gh` (the Github CLI) are probably the tools that most enable Claude to become a coworker, because they let me work with it the way I work with humans: git and Github.  
Using these CLIs, Claude can interact with issues, PRs, comments, code reviews, and commits the way colleague would.  
A lot of my workflow is around filing issues and getting claude to fix it, or doing code reviews and having it make improvements - like I would with a human intern!  
Another great use way to use Claude is to dig around in git history, it’s a great source of context.  
An underutilised feature of git worktrees - they allow you to have parallel copies of your repo so you can have multiple agents working on different tasks simultaneously.  

![Prompts](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎023.jpeg)

Let’s talk about prompts.  
Prompts are a blank canvas to express yourself.  
I’ve seen essays in CLAUDE.md, elaborate templating frameworks, people selling prompt packs, which feel like the new "internet courses".  
The issue with all these is: we have no evals, no way to measure the effect of these “configuration changes”.  
It’s all vibe based, so it’s very easy to confirmation bias yourself into believing something works when it is non-functional.    
This is a screenshot from a discussion with the maintainer of one such framework where the templating mechanism was entirely hallucinated - I looked at the content being sent to the model and it showed none of the “features” of this framework were being used.  
Be wary of these things.

![Custom commands](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎024.jpeg)

Anthropic has provided plenty of ways to configure claude code. [Custom commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands) are a great one.    
They’re best used for precise instructions for a workflow, and only pulled in at invocation time, which is very context efficient You can use them to codify frequently workflows and iterate on them over time to optimise them.  
It’s the best way to document “how” you want something done.


![Memories](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎025.jpeg)

Memories are very useful to document steering decisions.  
Every time I steer claude in a repeatable way, I add a memory, then ask it to continue.  
They're just a shortcut to add stuff to CLAUDE.md, but I like them because they let you do it emperically.  
You should put effort into writing a good CLAUDE.md, but when doing so a priori, you're trying to document what you think Claude needs.  
By adding memories when you need to steer, you're responding to a witnessed deficiency - its emperical.  
This will make your CLAUDE.md messy, so you should clean it up regularly, and move things to the right level abstraction (user, project, local) to keep the context clean.

![Vibe coding](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎026.jpeg)

We’ve talked about how to be more robust with vibe configuration, lets talk about vibe coding.  
I think of vibe coding as engaging with the work only via chat and outputs, not looking at any code.  
It’s very tempting, but can be very frustrating too.  
There’s a lot of hype around it, and in my experience it requires a much more deliberate approach than people say.  
It can be efficient for quick & dirty tools, or prototyping - I often vibe code the first demo of something to prove to myself it’s worth working on
All the configuration stuff we just discussed can make vibe coding much more reliable.  
But it’s not useful above a level of complexity.

![Workflows](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎027.jpeg)

What’s better? [Workflows](https://docs.anthropic.com/en/docs/claude-code/common-workflows)  
They’re mental models for you and your intern.    
A good resistance to vibe coding, because they define a process to stick to, which also increases agent autonomy - Claude no longer has to guess at “how” to do something.  
There’s nothing fancy involved, we can use the tools we just discussed to define workflows.  
Write a good problem statement, Codify the workflow into custom commands, tune permissions so the Claude has more autonomy, and document your opinions so it knows how you like things done

![Workflow examples](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎028.jpeg)

Here are some [examples](https://www.anthropic.com/engineering/claude-code-best-practices)

![Sub agents](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎029.jpeg)

[Sub agents](https://docs.anthropic.com/en/docs/claude-code/sub-agents) give your intern its own interns!  
They’re a great way to achieve subtasks without polluting the context window with the details.  
Claude now has native support for sub agents so you can build personas.  
One of my most useful sub agents isn’t Claude though, it’s Gemini.  
Gemini has a wonderful 1M token context window, and I get Claude to use to for long context stuff like reading files too big for Claude.  
Much better than Claude jumping around, reading a few lines here and there of it, and claiming to understand the whole thing.  

![Tips](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎030.jpeg)

Some specific tips on using Claude Code

![Principles](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎031.jpeg)

General principles for working with your weird intern

![Not just for coding](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎032.jpeg)

These tools aren’t just for coding! Here are some non-code workflows I’ve found useful

![Demo](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎033.jpeg)

_This demo was me using my mobile Claude Code setup to deploy a web page, which the audience could load on their phones after Claude was finished.
I wrote a [blog about how to remote control Claude Code](https://adim.in/p/remote-control-claude-code/) like this, if you're interested._

![Other terminal agents](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎034.jpeg)

You don’t have to use Claude Code, here are some alternatives.

![Cognitive atrophy](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎035.jpeg)

I want to wrap up with something a bit more philosophical.
We're in this era where things are moving way faster than before. Lots of hype, FOMO, everything feels like a race you can’t participate in unless you're constantly switching to the latest and greatest tools.  
These tools make it very easy to disengage and outsource thinking.  
I don't know what the post AGI/ASI future will be, but for now our core skills as engineers, researchers, humans are creativity and problem solving. Always have been.

We need to use these tools as [tools of leverage, not tools of reliance](/q/tools-leverage-not-reliance/).

I really like Niall Ferguson's [Cloister/Starship](https://uatx.substack.com/p/the-cloister-and-the-starship) metaphor for this, which describes 2 modes of working: the Starship, where you have full access to all tools and can leverage them to amplify your capabilities, and the Cloister, where you're in full analog medieval monk mode. I don't necessairily think this is the right way to break up a work day, but I think it's very important to spend time away from the tools, testing your own capabilities. Keeps you honest and ensures you're training yourself, not outsourcing your thinking.  

![Richard Feynman's problem solving technique](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎036.jpeg)

I find [Richard Feynman's problem solving algorithm](https://wiki.c2.com/?FeynmanAlgorithm) a good reminder.

![Final slide](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎037.jpeg)

Your intern awaits, use wisely.

![Thank you](/assets/the-weird-intern-in-your-terminal/‎the-weird-intern-in-your-terminal.‎038.jpeg)

Thanks for listening!

## References

- [The weird intern](https://simonwillison.net/2024/Sep/10/software-misadventures/#the-weird-intern) - Simon Willison's post coining the "weird intern" metaphor
- [Simon's blog](https://simonwillison.net) - Excellent blog on AI and software engineering
- [Diagram of context engineering](https://x.com/dexhorthy/status/1933283008863482067) - Visualization of context engineering concepts
- [Claude-trace](https://github.com/badlogic/lemmy/tree/main/apps/claude-trace) - Tool for inspecting Claude Code sessions
- [Custom Commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands) - Claude Code custom command documentation
- [Common workflows](https://docs.anthropic.com/en/docs/claude-code/common-workflows) - Claude Code workflow patterns
- [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices) - Workflow examples and best practices
- [Sub-agents](https://docs.anthropic.com/en/docs/claude-code/sub-agents) - Using sub-agents in Claude Code
- [My mobile claude code setup](https://adim.in/p/remote-control-claude-code/) - Remote Claude Code demo setup
- [The Cloister and the Starship](https://uatx.substack.com/p/the-cloister-and-the-starship) - Niall Ferguson's metaphor for working modes
